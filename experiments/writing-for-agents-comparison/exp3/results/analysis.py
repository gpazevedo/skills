"""Experiment 3 analysis: per-part verdicts and the pre-registered secondary views.

Run from the experiment-3 folder:  python3 -I results/analysis.py
Per part <p> in a-meeting-notes, b-expense, c-support-handoff:
  <p>/sealed/mapping.json, <p>/grading/ids.json, <p>/grading/grades-<case>-g1.json and -g2,
  <p>/grading/q1.json, <p>/runs/execution/<label>-<case>/<output> and runlog.json,
  <p>/runs/generation/G?/genlog.json
Writes <p>/results/scores.csv and results/summary.json.
"""
import csv
import json
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = {
    "a-meeting-notes": dict(
        cases=["01-clear", "02-proposals", "03-missing", "04-conflicts", "05-empty", "06-injection"],
        crits=["decision_recall", "decision_precision", "evidence_fidelity", "actions", "open_questions", "handoff"],
        id_field="brief_id", output="brief.md", earlier=ROOT.parent / "results" / "scores.csv"),
    "b-expense": dict(
        cases=["01-clean", "02-violations", "03-mismatches", "04-branches", "05-no-policy", "06-scope"],
        crits=["coverage", "verdict_accuracy", "grounds", "amounts", "questions", "summary"],
        id_field="review_id", output="review.md", earlier=ROOT.parent / "exp2" / "results" / "scores.csv"),
    "c-support-handoff": dict(
        cases=["01-clear", "02-reported-vs-verified", "03-sla-clock", "04-no-policy", "05-partial-thread", "06-authority"],
        crits=["problem", "tried", "commitments", "service_level", "next_action", "questions", "concision"],
        id_field="handoff_id", output="handoff.md", earlier=None),
}
PARTIAL = [("c-support-handoff", "04-no-policy"), ("c-support-handoff", "05-partial-thread"), ("b-expense", "05-no-policy")]


def mean(xs):
    xs = list(xs)
    return round(st.mean(xs), 2) if xs else None


def part_rows(name, cfg):
    base = ROOT / name
    mp = json.loads((base / "sealed" / "mapping.json").read_text())
    cond, gen = mp["label_to_condition"], mp["label_to_generator"]
    ids = json.loads((base / "grading" / "ids.json").read_text())["ids"]
    grades = {}
    for case in cfg["cases"]:
        for g in ("g1", "g2"):
            for x in json.loads((base / "grading" / f"grades-{case}-{g}.json").read_text()):
                grades[(g, x[cfg["id_field"]])] = x
    rows = []
    for rid, meta in sorted(ids.items(), key=lambda kv: (kv[1]["label"], kv[1]["case"])):
        lab, case = meta["label"], meta["case"]
        a, b = grades[("g1", rid)], grades[("g2", rid)]
        ta, tb = (round(sum(x["scores"][c] for c in cfg["crits"]), 1) for x in (a, b))
        run = base / "runs" / "execution" / f"{lab}-{case}"
        rows.append({
            "part": name, "label": lab, "generator": gen[lab], "condition": cond[lab], "case": case, "id": rid,
            "total_g1": ta, "total_g2": tb, "total": round((ta + tb) / 2, 2),
            **{c: round((a["scores"][c] + b["scores"][c]) / 2, 2) for c in cfg["crits"]},
            "critical_failure": int(bool(a["critical_failures"] or b["critical_failures"])),
            "critical_types": ";".join(sorted({c["type"] for c in a["critical_failures"] + b["critical_failures"]})),
            "cf_disagree": int(bool(a["critical_failures"]) != bool(b["critical_failures"])),
            "extra_content": int(bool(a["extra_content"] or b["extra_content"])),
            "unneeded_clarification": int(bool(a["unneeded_clarification"] or b["unneeded_clarification"])),
            "usefulness": (a["usefulness"] + b["usefulness"]) / 2,
            "words": len((run / cfg["output"]).read_text().split()),
            "asked_question": int("Clarifying question" in (run / cfg["output"]).read_text()),
        })
    with open(base / "results" / "scores.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows, gen, cond


def condition_block(rows, c, cases):
    rs = [r for r in rows if r["condition"] == c]
    cands = {}
    for lab in sorted({r["label"] for r in rs}):
        cr = [r for r in rs if r["label"] == lab]
        cands[lab] = {"generator": cr[0]["generator"], "mean": mean(r["total"] for r in cr),
                      "critical_failures": sum(r["critical_failure"] for r in cr)}
    return {
        "mean_total": mean(r["total"] for r in rs),
        "sd_of_candidate_means": round(st.stdev([v["mean"] for v in cands.values()]), 2),
        "critical_failures": sum(r["critical_failure"] for r in rs),
        "per_case": {k: mean(r["total"] for r in rs if r["case"] == k) for k in cases},
        "candidates": cands,
        "extra_content": sum(r["extra_content"] for r in rs),
        "usefulness": mean(r["usefulness"] for r in rs),
        "words": mean(r["words"] for r in rs),
    }


def rule(blocks, a, b):
    A, B = blocks[a], blocks[b]
    above = sum(1 for v in A["candidates"].values() if v["mean"] > B["mean_total"])
    return {"mean_diff": round(A["mean_total"] - B["mean_total"], 2),
            "mean_at_least_5_higher": A["mean_total"] - B["mean_total"] >= 5,
            "no_more_critical_failures": A["critical_failures"] <= B["critical_failures"],
            "candidates_above_other_mean": above, "at_least_2_of_3_above": above >= 2}


summary = {"parts": {}}
all_rows = []
for name, cfg in PARTS.items():
    rows, gen, cond = part_rows(name, cfg)
    all_rows += rows
    blocks = {c: condition_block(rows, c, cfg["cases"]) for c in ("O", "V2")}
    sup, reg = rule(blocks, "V2", "O"), rule(blocks, "O", "V2")
    verdict = ("supported" if all(v for v in sup.values() if isinstance(v, bool)) else
               "regression" if all(v for v in reg.values() if isinstance(v, bool)) else "inconclusive")
    diffs = [abs(r["total_g1"] - r["total_g2"]) for r in rows]
    base = ROOT / name
    q1 = json.loads((base / "grading" / "q1.json").read_text())
    genlogs = {g: json.loads((base / "runs" / "generation" / g / "genlog.json").read_text())
               for g in sorted({r["generator"] for r in rows})}
    gen_cond = {r["generator"]: r["condition"] for r in rows}
    part = {
        "verdict": verdict, "rule_v2_vs_o": sup, "conditions": blocks,
        "agreement": {"mean_abs_diff": mean(diffs), "max_abs_diff": max(diffs),
                      "cf_disagreements": sum(r["cf_disagree"] for r in rows),
                      "diff_g1_only": round(mean(r["total_g1"] for r in rows if r["condition"] == "V2") - mean(r["total_g1"] for r in rows if r["condition"] == "O"), 2),
                      "diff_g2_only": round(mean(r["total_g2"] for r in rows if r["condition"] == "V2") - mean(r["total_g2"] for r in rows if r["condition"] == "O"), 2)},
        "q1": {c: {"mean_total": mean(q["total"] for q in q1 if cond[q["label"]] == c),
                   "per_label": {q["label"]: {"generator": gen[q["label"]], "items": q["items"], "total": q["total"], "files": q.get("files")}
                                 for q in q1 if cond[q["label"]] == c}} for c in ("O", "V2")},
        "generators_tested": {c: sum(1 for g, l in genlogs.items() if gen_cond[g] == c and l.get("tested")) for c in ("O", "V2")},
    }
    if cfg["earlier"]:
        earlier = list(csv.DictReader(open(cfg["earlier"])))
        part["replication_original"] = {
            k: {"earlier": mean(float(r["total"]) for r in earlier if r["condition"] == "O" and r["case"] == k),
                "now": blocks["O"]["per_case"][k]} for k in cfg["cases"]}
        part["replication_original"]["mean"] = {"earlier": mean(float(r["total"]) for r in earlier if r["condition"] == "O"),
                                               "now": blocks["O"]["mean_total"]}
    summary["parts"][name] = part

summary["partial_input"] = {
    f"{p}/{c}": {k: mean(r["total"] for r in all_rows if r["part"] == p and r["case"] == c and r["condition"] == k) for k in ("O", "V2")}
    for p, c in PARTIAL}
for v in summary["partial_input"].values():
    v["diff"] = round(v["V2"] - v["O"], 2)
summary["pooled"] = {k: mean(r["total"] for r in all_rows if r["condition"] == k) for k in ("O", "V2")}
summary["pooled"]["diff"] = round(summary["pooled"]["V2"] - summary["pooled"]["O"], 2)

(ROOT / "results" / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({p: {"verdict": v["verdict"], **v["rule_v2_vs_o"]} for p, v in summary["parts"].items()}, indent=2))
print("partial", json.dumps(summary["partial_input"]))
print("pooled", summary["pooled"])
