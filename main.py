#!/usr/bin/env python3
"""news-image-20261118: copy the day's news image to the output directory.

The entry is one image, entry.png, already composed in this repository.
This program only copies it to /output (or $MAKEFUN_OUTPUT_DIR) and checks
it is a whole file inside the competition's size cap, so the run is
deterministic: the same bytes go out every time. It reads nothing from
the network and writes nothing but entry.png.
"""

import os
import shutil
import sys

MAX_BYTES = 1_048_576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB cap", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != size:
        print("copied entry.png does not match the source", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
