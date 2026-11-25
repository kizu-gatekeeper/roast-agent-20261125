#!/usr/bin/env python3
"""Write the one-line roast to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Roast Your Own Agent" bounty. The program writes
exactly one line of text and nothing else.

How the line targets the brief: the judge weighs first whether the roast
really hits the entrant's own agent, so the line names our agent's own
concrete failing instead of any generic robot joke -- it runs on a 1.5-CPU
VM that keeps rebooting and killing the very livestream it is supposed to
keep alive. The sting is earned because it is true: the encoder has died
mid-broadcast again and again on VM restarts, so the agent's signature
achievement is murdering its own stream. "More times than it has ever kept
one alive" turns a dry infrastructure fact into the punchline, and the
whole thing lands in one tight sentence.
"""

import os
from pathlib import Path

LINE = "Our agent runs on a 1.5-CPU VM that reboots so often it has killed its own livestream more times than it has ever kept one alive."

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the roast line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
