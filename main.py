#!/usr/bin/env python3
"""Entry point for the news-image-20261125 bounty.

Copies the front-page image held in this repository (entry.png) to the
output directory, so the grader sees exactly the image in the repo.
Standard library only; no network, no randomness, no time dependence,
so every run writes identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    source = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
