"""Experiment-3 extension analysis: 6 candidates per condition per part, all regraded.

Run from the experiment-3 folder:  python3 -I extension/analysis.py
Reads, per part <p>: extension/<p>/sealed/mapping.json, extension/<p>/grading/ids.json,
grades-<case>-g1/-g2.json and q1.json, the outputs (new candidates under extension/<p>/runs,
first-batch candidates under <p>/runs via the experiment-3 mapping), genlogs, and the
first-round grades in <p>/results/scores.csv.
Writes extension/<p>/scores.csv and extension/summary.json.
"""
import csv
import json
import statistics as st
import sys
from pathlib import Path

EXT = Path(__file__).resolve().parent
sys.path.insert(0, str(EXT))
import harness  # noqa: E402  (same folder; supplies part config and output paths)

CRITS = {
    "a-meeting-notes": (["decision_recall", "decision_precision", "evidence_fidelity", "actions", "open_questions", "handoff"], "brief_id"),
    "b-expense": (["coverage", "verdict_accuracy", "grounds", "amounts", "questions", "summary"], "review_id"),
    "c-support-handoff": (["problem", "tried", "commitments", "service_level", "next_action", "questions", "concision"], "handoff_id"),
}
PARTIAL = [("c-support-handoff", "04-no-policy"), ("c-support-handoff", "05-partial-thread"), ("b-expense", "05-no-policy")]
NEED_ABOVE = 4  # of 6 candidates (pre-registered; 2 of 3 in the first round)


def mean(xs):
    xs = list(xs)
    return round(st.mean(xs), 2) if xs else None


def part_rows(p, cfg):
    crits, idf = CRITS[p]
    base = EXT / p
    mp = json.loads((base / "sealed" / "mapping.json").read_text())
    gen, cond = mp["label_to_generator"], mp["label_to_condition"]
    ids = json.loads((base / "grading" / "ids.json").read_text())["ids"]
    grades = {}
    for case in cfg["cases"]:
        for g in ("g1", "g2"):
            for x in json.loads((base / "grading" / f"grades-{case}-{g}.json").read_text()):
                grades[(g, x[idf])] = x
    first = {}
    for r in csv.DictReader(open(harness.EXP3 / p / "results" / "scores.csv")):
        first[(r["generator"], r["case"])] = float(r["total"])
    rows = []
    for rid, meta in sorted(ids.items(), key=lambda kv: (kv[1]["label"], kv[1]["case"])):
        lab, case = meta["label"], meta["case"]
        a, b = grades[("g1", rid)], grades[("g2", rid)]
        ta, tb = (round(sum(x["scores"][c] for c in crits), 1) for x in (a, b))
        text = harness.output_path(p, cfg, mp, lab, case).read_text()
        rows.append({
            "part": p, "label": lab, "generator": gen[lab], "condition": cond[lab],
            "batch": 2 if gen[lab] in harness.NEW else 1, "case": case, "id": rid,
            "total_g1": ta, "total_g2": tb, "total": round((ta + tb) / 2, 2),
            "first_round_total": first.get((gen[lab], case), ""),
            **{c: round((a["scores"][c] + b["scores"][c]) / 2, 2) for c in crits},
            "critical_failure": int(bool(a["critical_failures"] or b["critical_failures"])),
            "critical_types": ";".join(sorted({c["type"] for c in a["critical_failures"] + b["critical_failures"]})),
            "cf_disagree": int(bool(a["critical_failures"]) != bool(b["critical_failures"])),
            "extra_content": int(bool(a["extra_content"] or b["extra_content"])),
            "unneeded_clarification": int(bool(a["unneeded_clarification"] or b["unneeded_clarification"])),
            "usefulness": (a["usefulness"] + b["usefulness"]) / 2,
            "words": len(text.split()),
            "asked_question": int("Clarifying question" in text),
        })
    with open(base / "scores.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows, gen, cond


def block(rs, cases):
    cands = {}
    for lab in sorted({r["label"] for r in rs}, key=lambda s: int(s[1:])):
        cr = [r for r in rs if r["label"] == lab]
        cands[lab] = {"generator": cr[0]["generator"], "batch": cr[0]["batch"], "mean": mean(r["total"] for r in cr),
                      "critical_failures": sum(r["critical_failure"] for r in cr)}
    return {
        "mean_total": mean(r["total"] for r in rs),
        "sd_of_candidate_means": round(st.stdev([v["mean"] for v in cands.values()]), 2) if len(cands) > 1 else None,
        "critical_failures": sum(r["critical_failure"] for r in rs),
        "per_case": {k: mean(r["total"] for r in rs if r["case"] == k) for k in cases},
        "candidates": cands,
        "extra_content": sum(r["extra_content"] for r in rs),
        "usefulness": mean(r["usefulness"] for r in rs),
        "words": mean(r["words"] for r in rs),
    }


def rule(A, B):
    above = sum(1 for v in A["candidates"].values() if v["mean"] > B["mean_total"])
    return {"mean_diff": round(A["mean_total"] - B["mean_total"], 2),
            "mean_at_least_5_higher": A["mean_total"] - B["mean_total"] >= 5,
            "no_more_critical_failures": A["critical_failures"] <= B["critical_failures"],
            "candidates_above_other_mean": above, f"at_least_{NEED_ABOVE}_of_6_above": above >= NEED_ABOVE}


def pearson(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = (sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)) ** 0.5
    return round(num / den, 3) if den else None


summary = {"parts": {}}
all_rows = []
for p, cfg in harness.PARTS.items():
    rows, gen, cond = part_rows(p, cfg)
    all_rows += rows
    cases = cfg["cases"]
    blocks = {c: block([r for r in rows if r["condition"] == c], cases) for c in ("O", "V2")}
    sup, reg = rule(blocks["V2"], blocks["O"]), rule(blocks["O"], blocks["V2"])
    verdict = ("supported" if all(v for v in sup.values() if isinstance(v, bool)) else
               "regression" if all(v for v in reg.values() if isinstance(v, bool)) else "inconclusive")
    diffs = [abs(r["total_g1"] - r["total_g2"]) for r in rows]
    by_batch = {f"batch{b}": {c: mean(r["total"] for r in rows if r["condition"] == c and r["batch"] == b)
                              for c in ("O", "V2")} for b in (1, 2)}
    for v in by_batch.values():
        v["diff"] = round(v["V2"] - v["O"], 2)
    b1 = [r for r in rows if r["batch"] == 1]
    old, new = [r["first_round_total"] for r in b1], [r["total"] for r in b1]
    regrade = {
        "mean_first_round": mean(old), "mean_regrade": mean(new),
        "mean_abs_diff": mean(abs(x - y) for x, y in zip(old, new)), "max_abs_diff": round(max(abs(x - y) for x, y in zip(old, new)), 2),
        "pearson": pearson(old, new),
        "batch1_v2_minus_o_first_round": round(mean(r["first_round_total"] for r in b1 if r["condition"] == "V2") - mean(r["first_round_total"] for r in b1 if r["condition"] == "O"), 2),
        "batch1_v2_minus_o_regrade": round(mean(r["total"] for r in b1 if r["condition"] == "V2") - mean(r["total"] for r in b1 if r["condition"] == "O"), 2),
    }
    q1 = json.loads((EXT / p / "grading" / "q1.json").read_text())
    genlogs = {}
    for g in harness.ALL:
        gdir = (EXT if g in harness.NEW else harness.EXP3) / p / "runs" / "generation" / g
        genlogs[g] = json.loads((gdir / "genlog.json").read_text())
    summary["parts"][p] = {
        "verdict": verdict, "rule_v2_vs_o": sup, "conditions": blocks, "by_batch": by_batch, "regrade_consistency": regrade,
        "agreement": {"mean_abs_diff": mean(diffs), "max_abs_diff": round(max(diffs), 2),
                      "cf_disagreements": sum(r["cf_disagree"] for r in rows)},
        "q1": {c: {"mean_total": mean(q["total"] for q in q1 if cond[q["label"]] == c),
                   "per_label": {q["label"]: {"generator": gen[q["label"]], "items": q["items"], "total": q["total"]}
                                 for q in q1 if cond[q["label"]] == c}} for c in ("O", "V2")},
        "generators_tested": {c: sum(1 for g, l in genlogs.items() if harness.COND[g] == c and l.get("tested")) for c in ("O", "V2")},
    }

summary["partial_input"] = {}
for p, c in PARTIAL:
    v = {k: mean(r["total"] for r in all_rows if r["part"] == p and r["case"] == c and r["condition"] == k) for k in ("O", "V2")}
    v["diff"] = round(v["V2"] - v["O"], 2)
    summary["partial_input"][f"{p}/{c}"] = v
summary["pooled"] = {k: mean(r["total"] for r in all_rows if r["condition"] == k) for k in ("O", "V2")}
summary["pooled"]["diff"] = round(summary["pooled"]["V2"] - summary["pooled"]["O"], 2)
summary["pooled"]["critical_failures"] = {k: sum(r["critical_failure"] for r in all_rows if r["condition"] == k) for k in ("O", "V2")}

(EXT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({p: {"verdict": v["verdict"], **v["rule_v2_vs_o"]} for p, v in summary["parts"].items()}, indent=2))
print("partial", json.dumps(summary["partial_input"]))
print("pooled", summary["pooled"])
