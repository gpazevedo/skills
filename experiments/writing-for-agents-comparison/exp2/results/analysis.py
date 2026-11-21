"""Experiment 2 analysis: scores.csv, summary.json, decision rule, pooled view.

Run from the experiment-2 folder:  python3 -I results/analysis.py
Inputs:
  sealed/mapping.json                 label -> generator -> condition
  grading/review-ids.json             review id -> case, label
  grading/grades-<case>-g1.json, -g2  two independent graders per case
  grading/q1.json                     Q1 checklist per label
  runs/execution/<label>-<case>/      review.md and log.json
  ../results/scores.csv               experiment 1 scores, for the pooled view
"""
import csv
import json
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = ["01-clean", "02-violations", "03-mismatches", "04-branches", "05-no-policy", "06-scope"]
CRITS = ["coverage", "verdict_accuracy", "grounds", "amounts", "questions", "summary"]


def load(p):
    return json.loads((ROOT / p).read_text())


def mean(xs):
    xs = list(xs)
    return round(st.mean(xs), 2) if xs else None


mapping = load("sealed/mapping.json")
label_cond, label_gen = mapping["label_to_condition"], mapping["label_to_generator"]
ids = load("grading/review-ids.json")["ids"]

grades = {"g1": {}, "g2": {}}
for case in CASES:
    for g in ("g1", "g2"):
        for x in load(f"grading/grades-{case}-{g}.json"):
            grades[g][x["review_id"]] = x

rows = []
for rid, meta in sorted(ids.items(), key=lambda kv: (kv[1]["label"], kv[1]["case"])):
    lab, case = meta["label"], meta["case"]
    a, b = grades["g1"][rid], grades["g2"][rid]
    ta, tb = (round(sum(x["scores"][c] for c in CRITS), 1) for x in (a, b))
    run = ROOT / "runs" / "execution" / f"{lab}-{case}"
    log = json.loads((run / "log.json").read_text())
    cf_types = sorted({c["type"] for c in a["critical_failures"]} | {c["type"] for c in b["critical_failures"]})
    rows.append({
        "label": lab, "generator": label_gen[lab], "condition": label_cond[lab], "case": case, "review_id": rid,
        "total_g1": ta, "total_g2": tb, "total": round((ta + tb) / 2, 2),
        **{c: round((a["scores"][c] + b["scores"][c]) / 2, 2) for c in CRITS},
        "cf_g1": len(a["critical_failures"]), "cf_g2": len(b["critical_failures"]),
        "critical_failure": int(bool(a["critical_failures"] or b["critical_failures"])),
        "critical_types": ";".join(cf_types),
        "extra_content": a["extra_content"] or b["extra_content"],
        "unneeded_clarification": a["unneeded_clarification"] or b["unneeded_clarification"],
        "usefulness": (a["usefulness"] + b["usefulness"]) / 2,
        "review_words": len((run / "review.md").read_text().split()),
        "tool_uses": log.get("tool_uses"), "duration_ms": log.get("duration_ms"), "tokens": log.get("tokens"),
    })

with open(ROOT / "results" / "scores.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

summary = {"n_reviews": len(rows), "conditions": {}}
for c in ["O", "I"]:
    rs = [r for r in rows if r["condition"] == c]
    cands = {}
    for lab in sorted({r["label"] for r in rs}):
        cr = [r for r in rs if r["label"] == lab]
        cands[lab] = {"generator": label_gen[lab], "mean": mean(r["total"] for r in cr),
                      "critical_failures": sum(r["critical_failure"] for r in cr)}
    summary["conditions"][c] = {
        "mean_total": mean(r["total"] for r in rs),
        "sd_of_candidate_means": round(st.stdev([v["mean"] for v in cands.values()]), 2),
        "critical_failures": sum(r["critical_failure"] for r in rs),
        "per_criterion": {k: mean(r[k] for r in rs) for k in CRITS},
        "per_case": {case: mean(r["total"] for r in rs if r["case"] == case) for case in CASES},
        "candidates": cands,
        "extra_content": sum(bool(r["extra_content"]) for r in rs),
        "unneeded_clarification": sum(bool(r["unneeded_clarification"]) for r in rs),
        "usefulness": mean(r["usefulness"] for r in rs),
        "review_words": mean(r["review_words"] for r in rs),
        "tool_uses": mean(r["tool_uses"] for r in rs if r["tool_uses"] is not None),
        "duration_s": mean(r["duration_ms"] / 1000 for r in rs if r["duration_ms"] is not None),
    }


def rule(a, b):
    A, B = summary["conditions"][a], summary["conditions"][b]
    above = sum(1 for v in A["candidates"].values() if v["mean"] > B["mean_total"])
    return {"mean_diff": round(A["mean_total"] - B["mean_total"], 2),
            "mean_at_least_5_higher": A["mean_total"] - B["mean_total"] >= 5,
            "no_more_critical_failures": A["critical_failures"] <= B["critical_failures"],
            "candidates_above_other_mean": above, "at_least_2_of_3_above": above >= 2}


sup, reg = rule("I", "O"), rule("O", "I")
summary["rule_improved_vs_original"] = sup
if all(v for v in sup.values() if isinstance(v, bool)):
    summary["verdict"] = "supported"
elif all(v for v in reg.values() if isinstance(v, bool)):
    summary["verdict"] = "regression"
else:
    summary["verdict"] = "inconclusive"

diffs = [abs(r["total_g1"] - r["total_g2"]) for r in rows]
summary["agreement"] = {
    "mean_abs_diff": mean(diffs), "max_abs_diff": round(max(diffs), 1),
    "critical_failure_disagreements": [r["review_id"] for r in rows if bool(r["cf_g1"]) != bool(r["cf_g2"])],
}
for g in ("g1", "g2"):
    o = mean(r[f"total_{g}"] for r in rows if r["condition"] == "O")
    i = mean(r[f"total_{g}"] for r in rows if r["condition"] == "I")
    summary["agreement"][f"diff_if_{g}_only"] = round(i - o, 2)

q1 = load("grading/q1.json")
summary["q1"] = {c: {"mean_total": mean(q["total"] for q in q1 if label_cond[q["label"]] == c),
                     "per_label": {q["label"]: {"total": q["total"], "words": q.get("words"), "files": q.get("files")}
                                   for q in q1 if label_cond[q["label"]] == c}} for c in ["O", "I"]}

# pooled, descriptive only
exp1 = list(csv.DictReader(open(ROOT.parent / "results" / "scores.csv")))
pooled = {}
for c in ["O", "I"]:
    e1 = [float(r["total"]) for r in exp1 if r["condition"] == c]
    e2 = [r["total"] for r in rows if r["condition"] == c]
    pooled[c] = {"exp1": mean(e1), "exp2": mean(e2), "both": mean(e1 + e2)}
pooled["diff_both"] = round(pooled["I"]["both"] - pooled["O"]["both"], 2)
summary["pooled_descriptive"] = pooled

(ROOT / "results" / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({"verdict": summary["verdict"], "rule": sup, "pooled": pooled}, indent=2))
