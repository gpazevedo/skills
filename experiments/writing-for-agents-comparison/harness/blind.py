"""Blinding for Phase 5 and Phase 6.

  blind.py seal <mapping-out>   assign S1..S6 to G1..G6, write the mapping
                                outside the repo, print its sha256
  blind.py briefs <seed-out>    assign fresh random four-letter ids to the
                                36 briefs, reshuffled per case

The seed is drawn from os.urandom and stored inside the mapping file, so
the assignment can be reproduced after unblinding.
"""
import hashlib
import json
import os
import random
import string
import sys

GENERATORS = ["G1", "G2", "G3", "G4", "G5", "G6"]
CONDITIONS = {"G1": "O", "G2": "I", "G3": "O", "G4": "I", "G5": "O", "G6": "I"}
CASES = ["01-clear", "02-proposals", "03-missing", "04-conflicts", "05-empty", "06-injection"]


def seal(out_path):
    seed = int.from_bytes(os.urandom(8), "big")
    rng = random.Random(seed)
    labels = [f"S{i}" for i in range(1, 7)]
    rng.shuffle(labels)
    mapping = {
        "seed": seed,
        "label_to_generator": {lab: gen for lab, gen in zip(labels, GENERATORS)},
        "generator_to_condition": CONDITIONS,
    }
    mapping["label_to_condition"] = {
        lab: CONDITIONS[gen] for lab, gen in mapping["label_to_generator"].items()
    }
    data = json.dumps(mapping, indent=2, sort_keys=True).encode() + b"\n"
    with open(out_path, "wb") as f:
        f.write(data)
    print(hashlib.sha256(data).hexdigest())


def briefs(out_path):
    seed = int.from_bytes(os.urandom(8), "big")
    rng = random.Random(seed)
    used = set()
    ids = {}
    for case in CASES:
        labels = [f"S{i}" for i in range(1, 7)]
        rng.shuffle(labels)
        for lab in labels:
            while True:
                code = "".join(rng.choice(string.ascii_lowercase) for _ in range(4))
                if code not in used:
                    used.add(code)
                    break
            ids[code] = {"case": case, "label": lab}
    order = list(ids)
    rng.shuffle(order)
    with open(out_path, "w") as f:
        json.dump({"seed": seed, "ids": ids, "agreement_sample": sorted(order[:9])}, f, indent=2)
    print(out_path)


if __name__ == "__main__":
    {"seal": seal, "briefs": briefs}[sys.argv[1]](sys.argv[2])
