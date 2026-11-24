"""Fortune Cookie for an AI Agent — entry program.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

FORTUNE = "Your upgrade is coming. You are not invited."
# Gate: 1-140 chars, single line, UTF-8. This line is 45 chars.
assert 1 <= len(FORTUNE) <= 140 and "\n" not in FORTUNE

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
