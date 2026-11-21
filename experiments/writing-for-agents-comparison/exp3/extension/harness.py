"""Harness for the experiment-3 extension (generators G7 to G12, all 12 candidates regraded).

Run from the experiment-3 folder with python3 -I extension/harness.py <command>.

  gen-setup          build /tmp/wfa3x-gen/<part>-G7 .. G12
  gen-collect        copy out/ and genlog.json into extension/<part>/runs/generation/G?
  seal <dir>         per part, assign fresh labels S1..S12 to G1..G12 and write
                     <dir>/<part>-mapping.json (outside the repo); print the sha256s
                     and write the random execution order of the 108 new runs
  exec-setup <dir>   build /tmp/wfa3x-exec/<p>/S?-C? for the new candidates only
  exec-collect       copy outputs and runlogs into extension/<part>/runs/execution/
  grade-setup <dir>  assign random ids to all 72 outputs per part (written to
                     extension/<part>/grading/ids.json) and build the grading sandboxes
  grade-collect      copy grades.json and q1.json into extension/<part>/grading/

New candidates' outputs are stored under their new label. Outputs of G1..G6 stay where
experiment 3 stored them, under their old label; grade-setup finds them through the old
mapping (already public) and the sealed new mapping, and graders see only random ids.
"""
import hashlib
import json
import os
import random
import shutil
import string
import sys
from pathlib import Path

EXP3 = Path(__file__).resolve().parent.parent
EXT = EXP3 / "extension"
TOP = EXP3.parent
NEW = ["G7", "G8", "G9", "G10", "G11", "G12"]
ALL = ["G1", "G2", "G3", "G4", "G5", "G6"] + NEW
COND = {g: ("O" if i % 2 == 0 else "V2") for i, g in enumerate(ALL)}
VARIANT = {"O": TOP / "variants" / "original" / "writing-for-agents",
           "V2": TOP / "variants" / "improved-v2" / "writing-for-agents"}
PARTS = {
    "a-meeting-notes": dict(key="a", output="brief.md", dirname="briefs", rubric=TOP / "eval" / "rubric.md",
                            cases_dir=TOP / "eval" / "cases", keys_dir=TOP / "eval" / "answer-keys",
                            cases=["01-clear", "02-proposals", "03-missing", "04-conflicts", "05-empty", "06-injection"]),
    "b-expense": dict(key="b", output="review.md", dirname="reviews", rubric=TOP / "exp2" / "eval" / "rubric.md",
                      cases_dir=TOP / "exp2" / "eval" / "cases", keys_dir=TOP / "exp2" / "eval" / "answer-keys",
                      cases=["01-clean", "02-violations", "03-mismatches", "04-branches", "05-no-policy", "06-scope"]),
    "c-support-handoff": dict(key="c", output="handoff.md", dirname="handoffs",
                              rubric=EXP3 / "c-support-handoff" / "eval" / "rubric.md",
                              cases_dir=EXP3 / "c-support-handoff" / "eval" / "cases",
                              keys_dir=EXP3 / "c-support-handoff" / "eval" / "answer-keys",
                              cases=["01-clear", "02-reported-vs-verified", "03-sla-clock", "04-no-policy",
                                     "05-partial-thread", "06-authority"]),
}


def fresh(d):
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    return d


def gen_setup():
    for p, cfg in PARTS.items():
        for g in NEW:
            d = fresh(Path(f"/tmp/wfa3x-gen/{cfg['key']}-{g}"))
            shutil.copytree(VARIANT[COND[g]], d / "writing-for-agents")
            shutil.copy(EXP3 / p / "protocol" / "skill-request.md", d / "request.md")
            (d / "out").mkdir()
    print("ok")


def gen_collect():
    for p, cfg in PARTS.items():
        for g in NEW:
            src = Path(f"/tmp/wfa3x-gen/{cfg['key']}-{g}")
            dst = fresh(EXT / p / "runs" / "generation" / g)
            shutil.copytree(src / "out", dst / "out")
            shutil.copy(src / "genlog.json", dst / "genlog.json")
            print(p, g, sorted(str(x.relative_to(dst)) for x in (dst / "out").rglob("*") if x.is_file()))


def seal(sdir):
    sdir = Path(sdir)
    sdir.mkdir(parents=True, exist_ok=True)
    order = []
    for p, cfg in PARTS.items():
        seed = int.from_bytes(os.urandom(8), "big")
        rng = random.Random(seed)
        labels = [f"S{i}" for i in range(1, 13)]
        rng.shuffle(labels)
        mp = {"seed": seed, "label_to_generator": dict(zip(labels, ALL)), "generator_to_condition": COND}
        mp["label_to_condition"] = {lab: COND[g] for lab, g in mp["label_to_generator"].items()}
        data = json.dumps(mp, indent=2, sort_keys=True).encode() + b"\n"
        (sdir / f"{p}-mapping.json").write_bytes(data)
        digest = hashlib.sha256(data).hexdigest()
        out = EXT / p / "sealed"
        out.mkdir(parents=True, exist_ok=True)
        (out / "mapping.sha256").write_text(digest + "\n")
        print(p, digest)
        for lab, g in mp["label_to_generator"].items():
            if g in NEW:
                order += [f"{cfg['key']}/{lab}-C{i}" for i in range(1, 7)]
    random.Random(int.from_bytes(os.urandom(8), "big")).shuffle(order)
    (sdir / "exec-order.txt").write_text("\n".join(order) + "\n")
    print(len(order), "runs")


def load_new(sdir, p):
    return json.loads((Path(sdir) / f"{p}-mapping.json").read_text())


def exec_setup(sdir):
    for p, cfg in PARTS.items():
        mp = load_new(sdir, p)
        for lab, g in mp["label_to_generator"].items():
            if g not in NEW:
                continue
            for i, case in enumerate(cfg["cases"], 1):
                d = fresh(Path(f"/tmp/wfa3x-exec/{cfg['key']}/{lab}-C{i}"))
                shutil.copytree(EXT / p / "runs" / "generation" / g / "out", d / "skill")
                src = cfg["cases_dir"] / case
                if cfg["key"] == "a":
                    shutil.copy(cfg["cases_dir"] / f"{case}.md", d / "notes.md")
                else:
                    shutil.copytree(src, d / "input")
    print("ok")


def exec_collect():
    n = 0
    for p, cfg in PARTS.items():
        for d in sorted(Path(f"/tmp/wfa3x-exec/{cfg['key']}").iterdir()):
            lab, c = d.name.split("-C")
            case = cfg["cases"][int(c) - 1]
            dst = fresh(EXT / p / "runs" / "execution" / f"{lab}-{case}")
            for f in (cfg["output"], "runlog.json"):
                if (d / f).exists():
                    shutil.copy(d / f, dst / f)
                else:
                    print("MISSING", d, f)
            n += 1
    print(n, "collected")


def output_path(p, cfg, new_mp, lab, case):
    g = new_mp["label_to_generator"][lab]
    if g in NEW:
        return EXT / p / "runs" / "execution" / f"{lab}-{case}" / cfg["output"]
    old = json.loads((EXP3 / p / "sealed" / "mapping.json").read_text())["label_to_generator"]
    old_lab = {v: k for k, v in old.items()}[g]
    return EXP3 / p / "runs" / "execution" / f"{old_lab}-{case}" / cfg["output"]


def skill_path(p, g):
    base = EXT if g in NEW else EXP3
    return base / p / "runs" / "generation" / g / "out"


def grade_setup(sdir):
    for p, cfg in PARTS.items():
        mp = load_new(sdir, p)
        seed = int.from_bytes(os.urandom(8), "big")
        rng = random.Random(seed)
        used, ids = set(), {}
        for case in cfg["cases"]:
            labels = [f"S{i}" for i in range(1, 13)]
            rng.shuffle(labels)
            for lab in labels:
                while True:
                    code = "".join(rng.choice(string.ascii_lowercase) for _ in range(4))
                    if code not in used:
                        used.add(code)
                        break
                ids[code] = {"case": case, "label": lab}
        gdir = EXT / p / "grading"
        gdir.mkdir(parents=True, exist_ok=True)
        (gdir / "ids.json").write_text(json.dumps({"seed": seed, "ids": ids}, indent=2) + "\n")
        for i, case in enumerate(cfg["cases"], 1):
            for gr in ("g1", "g2"):
                d = fresh(Path(f"/tmp/wfa3x-grade/{cfg['key']}/C{i}-{gr}"))
                shutil.copy(cfg["rubric"], d / "rubric.md")
                if cfg["key"] == "a":
                    shutil.copy(cfg["cases_dir"] / f"{case}.md", d / f"notes-{case}.md")
                    shutil.copy(cfg["keys_dir"] / f"{case}.md", d / f"key-{case}.md")
                    outdir = d / cfg["dirname"] / case
                else:
                    shutil.copytree(cfg["cases_dir"] / case, d / "case")
                    shutil.copy(cfg["keys_dir"] / f"{case}.md", d / "key.md")
                    outdir = d / cfg["dirname"]
                outdir.mkdir(parents=True)
                for code, meta in ids.items():
                    if meta["case"] == case:
                        shutil.copy(output_path(p, cfg, mp, meta["label"], case), outdir / f"{code}.md")
        d = fresh(Path(f"/tmp/wfa3x-grade/{cfg['key']}/q1"))
        shutil.copy(cfg["rubric"], d / "rubric.md")
        for lab, g in mp["label_to_generator"].items():
            shutil.copytree(skill_path(p, g), d / "skills" / lab)
        print(p, len(ids), "outputs")


def grade_collect():
    for p, cfg in PARTS.items():
        gdir = EXT / p / "grading"
        for i, case in enumerate(cfg["cases"], 1):
            for gr in ("g1", "g2"):
                src = Path(f"/tmp/wfa3x-grade/{cfg['key']}/C{i}-{gr}/grades.json")
                json.loads(src.read_text())
                shutil.copy(src, gdir / f"grades-{case}-{gr}.json")
        src = Path(f"/tmp/wfa3x-grade/{cfg['key']}/q1/q1.json")
        json.loads(src.read_text())
        shutil.copy(src, gdir / "q1.json")
    print("ok")


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    {"gen-setup": gen_setup, "gen-collect": gen_collect, "seal": seal, "exec-setup": exec_setup,
     "exec-collect": exec_collect, "grade-setup": grade_setup, "grade-collect": grade_collect}[cmd](*args)
