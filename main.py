"""Write one short out-of-office reply for make.fun, then report its length."""

import os
import sys
from pathlib import Path

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I "
    "respect her. All my mail is being held at the post office, and by the wasp."
)

assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"


def output_dir() -> Path:
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
