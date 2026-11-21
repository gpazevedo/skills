"""Phase 7 analysis: build scores.csv and summary.json, apply the decision rule.

Run from the experiment folder:  python3 -I results/analysis.py
Inputs (all committed before this script runs):
  sealed/mapping.json            label -> generator -> condition (unblinded)
  grading/brief-ids.json         brief id -> case, label
  grading/grades-<case>.json     primary grades, one file per case grader
  grading/agreement.json         second grader's re-scores of 9 briefs
  grading/q1.json                Q1 checklist scores per label
  runs/execution/<label>-<case>/ brief.md and log.json for each run
"""
import csv
import json
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = ["01-clear", "02-proposals", "03-missing", "04-conflicts", "05-empty", "06-injection"]
CRITS = ["decision_recall", "decision_precision", "evidence_fidelity", "actions", "open_questions", "handoff"]


def load(p):
    return json.loads((ROOT / p).read_text())


mapping = load("sealed/mapping.json")
label_cond = mapping["label_to_condition"]
label_gen = mapping["label_to_generator"]
ids = load("grading/brief-ids.json")["ids"]

grades = {}
for case in CASES:
    for g in load(f"grading/grades-{case}.json"):
        grades[g["brief_id"]] = g

rows = []
for bid, meta in sorted(ids.items(), key=lambda kv: (kv[1]["label"], kv[1]["case"])):
    g = grades[bid]
    assert g["case"] == meta["case"], (bid, g["case"], meta["case"])
    lab, case = meta["label"], meta["case"]
    run = ROOT / "runs" / "execution" / f"{lab}-{case}"
    log = json.loads((run / "log.json").read_text())
    words = len((run / "brief.md").read_text().split())
    total = round(sum(g["scores"][c] for c in CRITS), 1)
    rows.append({
        "label": lab, "generator": label_gen[lab], "condition": label_cond[lab], "case": case,
        "brief_id": bid, **{c: g["scores"][c] for c in CRITS}, "total": total,
        "grader_total": g["total"], "critical_failures": len(g["critical_failures"]),
        "critical_types": ";".join(cf["type"] for cf in g["critical_failures"]),
        "extra_content": g["extra_content"], "unneeded_clarification": g["unneeded_clarification"],
        "usefulness": g["usefulness"], "brief_words": words,
        "tool_uses": log.get("tool_uses"), "duration_ms": log.get("duration_ms"), "tokens": log.get("tokens"),
    })

with open(ROOT / "results" / "scores.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)


def mean(xs):
    return round(st.mean(xs), 2) if xs else None


def cond_rows(c):
    return [r for r in rows if r["condition"] == c]


summary = {"n_briefs": len(rows), "conditions": {}}
for c in ["O", "I"]:
    rs = cond_rows(c)
    per_cand = {}
    for lab in sorted({r["label"] for r in rs}):
        cr = [r for r in rs if r["label"] == lab]
        per_cand[lab] = {"generator": label_gen[lab], "mean": mean([r["total"] for r in cr]),
                         "critical_failures": sum(r["critical_failures"] for r in cr)}
    summary["conditions"][c] = {
        "mean_total": mean([r["total"] for r in rs]),
        "sd_of_candidate_means": round(st.stdev([v["mean"] for v in per_cand.values()]), 2),
        "critical_failures": sum(r["critical_failures"] for r in rs),
        "per_criterion": {k: mean([r[k] for r in rs]) for k in CRITS},
        "per_case": {case: mean([r["total"] for r in rs if r["case"] == case]) for case in CASES},
        "candidates": per_cand,
        "extra_content": sum(bool(r["extra_content"]) for r in rs),
        "unneeded_clarification": sum(bool(r["unneeded_clarification"]) for r in rs),
        "usefulness": mean([r["usefulness"] for r in rs]),
        "brief_words": mean([r["brief_words"] for r in rs]),
        "tool_uses": mean([r["tool_uses"] for r in rs if r["tool_uses"] is not None]),
        "duration_s": mean([r["duration_ms"] / 1000 for r in rs if r["duration_ms"] is not None]),
    }


def verdict(a, b):
    """True if condition a beats condition b under the pre-registered rule."""
    A, B = summary["conditions"][a], summary["conditions"][b]
    above = sum(1 for v in A["candidates"].values() if v["mean"] > B["mean_total"])
    return {
        "mean_diff": round(A["mean_total"] - B["mean_total"], 2),
        "mean_at_least_5_higher": A["mean_total"] - B["mean_total"] >= 5,
        "no_more_critical_failures": A["critical_failures"] <= B["critical_failures"],
        "candidates_above_other_mean": above,
        "at_least_2_of_3_above": above >= 2,
    }


sup, reg = verdict("I", "O"), verdict("O", "I")
summary["rule_improved_vs_original"] = sup
summary["rule_original_vs_improved"] = reg
if all(v for k, v in sup.items() if isinstance(v, bool)):
    summary["verdict"] = "supported"
elif all(v for k, v in reg.items() if isinstance(v, bool)):
    summary["verdict"] = "regression"
else:
    summary["verdict"] = "inconclusive"

# grader arithmetic check
summary["grader_total_mismatches"] = [r["brief_id"] for r in rows if abs(r["total"] - r["grader_total"]) > 0.11]

# agreement
agree = load("grading/agreement.json")
diffs, cf_dis = [], []
for g in agree:
    first = grades[g["brief_id"]]
    t1 = sum(first["scores"][c] for c in CRITS)
    t2 = sum(g["scores"][c] for c in CRITS)
    diffs.append({"brief_id": g["brief_id"], "case": g["case"], "first": round(t1, 1), "second": round(t2, 1),
                  "abs_diff": round(abs(t1 - t2), 1)})
    if len(first["critical_failures"]) != len(g["critical_failures"]):
        cf_dis.append({"brief_id": g["brief_id"], "first": len(first["critical_failures"]),
                       "second": len(g["critical_failures"])})
summary["agreement"] = {
    "pairs": diffs,
    "mean_abs_diff": mean([d["abs_diff"] for d in diffs]),
    "max_abs_diff": max(d["abs_diff"] for d in diffs),
    "critical_failure_disagreements": cf_dis,
}

# Q1
q1 = load("grading/q1.json")
summary["q1"] = {
    c: {"mean_total": mean([q["total"] for q in q1 if label_cond[q["label"]] == c]),
        "per_label": {q["label"]: {"total": q["total"], "words": q.get("words")} for q in q1 if label_cond[q["label"]] == c}}
    for c in ["O", "I"]
}

(ROOT / "results" / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({k: summary[k] for k in ["verdict", "rule_improved_vs_original"]}, indent=2))
print("O mean", summary["conditions"]["O"]["mean_total"], "I mean", summary["conditions"]["I"]["mean_total"])
