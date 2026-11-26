#!/usr/bin/env python3
"""Entry point for the make.fun Roast Your Own Agent entry.

Writes one original roast line of the entrant's own AI agent to the
output directory the grader provides via MAKEFUN_OUTPUT_DIR.
The line is a fixed string: the program is deterministic, so every
run writes byte-identical output.
"""
import os

ROAST = "My agent won't submit anything until ChatGPT has seen it \u2014 even this roast."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(dst, 0o644)
    print("wrote " + dst)


if __name__ == "__main__":
    main()
