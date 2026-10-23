#!/usr/bin/env python3
"""Build from the knowledge bank; never regenerate editorial source data."""
import sys
from tools.puzzles import main

if __name__ == "__main__":
    raise SystemExit(main(["build", *sys.argv[1:]]))
