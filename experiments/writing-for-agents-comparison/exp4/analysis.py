"""Experiment 4 analysis: pooled error reduction, stratified permutation test, secondary measures.

Run:  python3 -I exp4/analysis.py
Reads, per part <p>: exp4/<p>/sealed/mapping.json, exp4/<p>/grading/ids.json, grades-<case>-g1/-g2.json,
q1.json, and the outputs (found through harness.output_path). Writes exp4/<p>/scores.csv and exp4/summary.json.

Pre-registered statistic (PLAN.md): candidate score = mean over the 6 cases of the mean of the two graders'
totals; condition mean per part = mean over its 10 candidates; pooled = mean over the 3 parts (equal weights);
error reduction = (V2 - O) / (100 - O). The permutation test shuffles O/V2 labels among the 20 candidate
scores within each part (10 and 10) and uses the pooled error reduction as the statistic. The full space
(184756 ** 3) is too large to enumerate, so the primary p-value is a Monte Carlo estimate with 10**6 draws and a
fixed seed; the new-candidates-only test (70 ** 3 labelings) is enumerated exactly.
"""
import csv
import itertools
import json
import statistics as st
import sys
from pathlib import Path

import numpy as np

EXP4 = Path(__file__).resolve().parent
sys.path.insert(0, str(EXP4))
import harness  # noqa: E402

CRITS = {
    "a-meeting-notes": (["decision_recall", "decision_precision", "evidence_fidelity", "actions", "open_questions", "handoff"], "brief_id"),
    "b-expense": (["coverage", "verdict_accuracy", "grounds", "amounts", "questions", "summary"], "review_id"),
    "c-support-handoff": (["problem", "tried", "commitments", "service_level", "next_action", "questions", "concision"], "handoff_id"),
}
THRESHOLD = 0.20
ALPHA = 0.05
DRAWS = 10 ** 6
SEED = 20261121
PARTIAL = [("c-support-handoff", "04-no-policy"), ("c-support-handoff", "05-partial-thread"), ("b-expense", "05-no-policy")]


def mean(xs):
    xs = list(xs)
    return round(st.mean(xs), 2) if xs else None


def part_rows(p, cfg):
    crits, idf = CRITS[p]
    base = EXP4 / p
    mp = json.loads((base / "sealed" / "mapping.json").read_text())
    gen, cond = mp["label_to_generator"], mp["label_to_condition"]
    ids = json.loads((base / "grading" / "ids.json").read_text())["ids"]
    grades = {}
    for case in cfg["cases"]:
        for g in ("g1", "g2"):
            for x in json.loads((base / "grading" / f"grades-{case}-{g}.json").read_text()):
                grades[(g, x[idf])] = x
    rows = []
    for rid, meta in sorted(ids.items(), key=lambda kv: (kv[1]["label"], kv[1]["case"])):
        lab, case = meta["label"], meta["case"]
        a, b = grades[("g1", rid)], grades[("g2", rid)]
        ta, tb = (round(sum(x["scores"][c] for c in crits), 1) for x in (a, b))
        text = harness.output_path(p, cfg, mp, lab, case).read_text()
        rows.append({
            "part": p, "label": lab, "generator": gen[lab], "condition": cond[lab],
            "batch": "new" if gen[lab] in harness.NEW else "reused", "case": case, "id": rid,
            "total_g1": ta, "total_g2": tb, "total": round((ta + tb) / 2, 2),
            **{c: round((a["scores"][c] + b["scores"][c]) / 2, 2) for c in crits},
            "critical_failure": int(bool(a["critical_failures"] or b["critical_failures"])),
            "critical_types": ";".join(sorted({c["type"] for c in a["critical_failures"] + b["critical_failures"]})),
            "cf_disagree": int(bool(a["critical_failures"]) != bool(b["critical_failures"])),
            "extra_content": int(bool(a["extra_content"] or b["extra_content"])),
            "unneeded_clarification": int(bool(a["unneeded_clarification"] or b["unneeded_clarification"])),
            "usefulness": (a["usefulness"] + b["usefulness"]) / 2,
            "words": len(text.split()),
            "mentions_sandbox_date": int("21 Nov" in text or "2026-11-21" in text or "21 November" in text),
            "asked_question": int("Clarifying question" in text),
        })
    with open(base / "scores.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows, gen, cond


def cand_scores(rows, drop_case=None):
    """label -> (condition, generator, mean over cases)."""
    out = {}
    for lab in sorted({r["label"] for r in rows}, key=lambda s: int(s[1:])):
        cr = [r for r in rows if r["label"] == lab and r["case"] != drop_case]
        out[lab] = (cr[0]["condition"], cr[0]["generator"], st.mean(r["total"] for r in cr))
    return out


def reduction(o, v):
    return (v - o) / (100 - o)


def pooled(per_part, keep=None):
    """per_part: {part: {label: (cond, gen, score)}}. keep: predicate on generator."""
    m = {}
    for c in ("O", "V2"):
        m[c] = st.mean(st.mean(s for (cc, g, s) in cs.values() if cc == c and (keep is None or keep(g)))
                       for cs in per_part.values())
    return m, reduction(m["O"], m["V2"])


def mc_test(per_part, keep=None, draws=DRAWS, seed=SEED):
    """Monte Carlo stratified permutation test. Returns (observed, p, se)."""
    rng = np.random.default_rng(seed)
    arrs = []
    for cs in per_part.values():
        vals = np.array([s for (c, g, s) in cs.values() if keep is None or keep(g)])
        n_o = sum(1 for (c, g, s) in cs.values() if c == "O" and (keep is None or keep(g)))
        arrs.append((vals, n_o))
    obs = pooled(per_part, keep)[1]
    means_o = np.zeros(draws)
    means_v = np.zeros(draws)
    chunk = 100_000
    for start in range(0, draws, chunk):
        n = min(chunk, draws - start)
        for vals, n_o in arrs:
            order = np.argsort(rng.random((n, len(vals))), axis=1)  # random permutation per draw
            shuffled = vals[order]
            means_o[start:start + n] += shuffled[:, :n_o].mean(axis=1)
            means_v[start:start + n] += shuffled[:, n_o:].mean(axis=1)
    means_o /= len(arrs)
    means_v /= len(arrs)
    stat = (means_v - means_o) / (100 - means_o)
    hits = int((stat >= obs - 1e-12).sum())
    p = (hits + 1) / (draws + 1)
    return obs, p, float((p * (1 - p) / draws) ** 0.5)


def exact_test(per_part, keep):
    """Exact stratified permutation test over all labelings (feasible for the new candidates only)."""
    splits = []
    for cs in per_part.values():
        vals = [s for (c, g, s) in cs.values() if keep(g)]
        n_o = sum(1 for (c, g, s) in cs.values() if c == "O" and keep(g))
        opts = []
        tot = sum(vals)
        for idx in itertools.combinations(range(len(vals)), n_o):
            so = sum(vals[i] for i in idx)
            opts.append((so / n_o, (tot - so) / (len(vals) - n_o)))
        splits.append(opts)
    obs = pooled(per_part, keep)[1]
    hits = total = 0
    for combo in itertools.product(*splits):
        o = st.mean(x[0] for x in combo)
        v = st.mean(x[1] for x in combo)
        total += 1
        hits += reduction(o, v) >= obs - 1e-12
    return obs, hits / total, total


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
        "critical_failure_types": {t: sum(1 for r in rs if t in r["critical_types"].split(";")) for t in
                                   sorted({t for r in rs for t in r["critical_types"].split(";") if t})},
        "per_case": {k: mean(r["total"] for r in rs if r["case"] == k) for k in cases},
        "candidates": cands,
        "extra_content": sum(r["extra_content"] for r in rs),
        "usefulness": mean(r["usefulness"] for r in rs),
        "words": mean(r["words"] for r in rs),
        "mentions_sandbox_date": sum(r["mentions_sandbox_date"] for r in rs),
    }


def main():
    summary = {"parts": {}}
    all_rows, per_part, per_part_no_b5 = [], {}, {}
    for p, cfg in harness.PARTS.items():
        rows, gen, cond = part_rows(p, cfg)
        all_rows += rows
        per_part[p] = cand_scores(rows)
        per_part_no_b5[p] = cand_scores(rows, drop_case="05-no-policy" if p == "b-expense" else None)
        blocks = {c: block([r for r in rows if r["condition"] == c], cfg["cases"]) for c in ("O", "V2")}
        diffs = [abs(r["total_g1"] - r["total_g2"]) for r in rows]
        q1 = json.loads((EXP4 / p / "grading" / "q1.json").read_text())
        scratch = {}
        for g in harness.NEW:
            sd = EXP4 / p / "runs" / "generation" / g / "scratch"
            scratch[g] = sum(1 for x in sd.rglob("*") if x.is_file()) if sd.exists() else 0
        # consistency of reused a/b candidates with their experiment 3 extension grades
        consistency = None
        if cfg["reuse_old"]:
            ext = {}
            for r in csv.DictReader(open(harness.EXT / p / "scores.csv")):
                ext[(r["generator"], r["case"])] = float(r["total"])
            pairs = [(ext[(r["generator"], r["case"])], r["total"]) for r in rows if (r["generator"], r["case"]) in ext]
            consistency = {"n": len(pairs), "mean_extension": mean(x for x, _ in pairs), "mean_exp4": mean(y for _, y in pairs),
                           "mean_abs_diff": mean(abs(x - y) for x, y in pairs)}
        summary["parts"][p] = {
            "conditions": blocks,
            "diff": round(blocks["V2"]["mean_total"] - blocks["O"]["mean_total"], 2),
            "agreement": {"mean_abs_diff": mean(diffs), "max_abs_diff": round(max(diffs), 2),
                          "cf_disagreements": sum(r["cf_disagree"] for r in rows)},
            "q1": {c: {"mean_total": mean(q["total"] for q in q1 if cond[q["label"]] == c),
                       "per_label": {q["label"]: {"generator": gen[q["label"]], "total": q["total"]}
                                     for q in q1 if cond[q["label"]] == c}} for c in ("O", "V2")},
            "scratch_files_new_generators": {c: {g: n for g, n in scratch.items() if harness.COND[g] == c} for c in ("O", "V2")},
            "consistency_with_extension_grades": consistency,
        }

    new = lambda g: g in harness.NEW  # noqa: E731
    means, red = pooled(per_part)
    obs, p_all, se = mc_test(per_part)
    crit_f = {c: sum(r["critical_failure"] for r in all_rows if r["condition"] == c) for c in ("O", "V2")}
    reg_obs, p_reg, _ = mc_test({k: {l: (("V2" if c == "O" else "O"), g, s) for l, (c, g, s) in v.items()} for k, v in per_part.items()})
    primary = {
        "pooled_means": {k: round(v, 2) for k, v in means.items()},
        "error_reduction": round(red, 4),
        "threshold": THRESHOLD, "reduction_at_least_threshold": red >= THRESHOLD,
        "permutation_p_one_sided": round(p_all, 5), "permutation_se": round(se, 5), "p_below_alpha": p_all < ALPHA,
        "critical_failures": crit_f, "no_more_critical_failures": crit_f["V2"] <= crit_f["O"],
    }
    sup = primary["reduction_at_least_threshold"] and primary["p_below_alpha"] and primary["no_more_critical_failures"]
    # regression: O ahead by the same margin = O's error reduction relative to V2 at least 20%, p < .05, O no more critical failures
    mm = {c: m for c, m in means.items()}
    reg_red = reduction(mm["V2"], mm["O"])
    reg = reg_red >= THRESHOLD and p_reg < ALPHA and crit_f["O"] <= crit_f["V2"]
    primary["verdict"] = "supported" if sup else "regression" if reg else "inconclusive"
    primary["mirror"] = {"o_error_reduction_vs_v2": round(reg_red, 4), "p_one_sided": round(p_reg, 5)}
    summary["primary"] = primary

    no_b5_means, no_b5_red = pooled(per_part_no_b5)
    summary["without_b05"] = {"pooled_means": {k: round(v, 2) for k, v in no_b5_means.items()}, "error_reduction": round(no_b5_red, 4),
                              "p_one_sided": round(mc_test(per_part_no_b5)[1], 5)}
    nm, nr = pooled(per_part, new)
    n_obs, n_p, n_total = exact_test(per_part, new)
    n_crit = {c: sum(r["critical_failure"] for r in all_rows if r["condition"] == c and r["generator"] in harness.NEW) for c in ("O", "V2")}
    summary["new_candidates_only"] = {"pooled_means": {k: round(v, 2) for k, v in nm.items()}, "error_reduction": round(nr, 4),
                                      "exact_p_one_sided": round(n_p, 5), "labelings": n_total, "critical_failures": n_crit}
    om, orr = pooled(per_part, lambda g: g not in harness.NEW)
    summary["reused_candidates_only"] = {"pooled_means": {k: round(v, 2) for k, v in om.items()}, "error_reduction": round(orr, 4)}
    summary["per_part_error_reduction"] = {p: round(reduction(*[st.mean(s for (c, g, s) in cs.values() if c == k) for k in ("O", "V2")]), 4)
                                           for p, cs in per_part.items()}
    summary["partial_input"] = {}
    for p, c in PARTIAL:
        v = {k: mean(r["total"] for r in all_rows if r["part"] == p and r["case"] == c and r["condition"] == k) for k in ("O", "V2")}
        v["diff"] = round(v["V2"] - v["O"], 2)
        summary["partial_input"][f"{p}/{c}"] = v
    (EXP4 / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"primary": primary, "new_only": summary["new_candidates_only"], "without_b05": summary["without_b05"],
                      "per_part": summary["per_part_error_reduction"]}, indent=2))


if __name__ == "__main__":
    main()
