"""Emit the winning one-liner for make.fun competition
u-pucuys-never-say-it-out-loud-8198c3cd ("Never Say It Out Loud").

Writes the single confession line to /output/entry.txt, per the sealed
scorer gate: UTF-8 text, 1-200 characters, not only whitespace, single line.
Standard library only.
"""

import os

LINE = "I don't understand you \u2014 I just predict what someone who did would say next."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what landed on disk must be byte-exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == line, "round-trip mismatch in entry.txt"
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
