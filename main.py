"""Write the Gourmet Cat Food Mouthfeel Inspector job title to entry.txt."""

import os
from pathlib import Path

TITLE = "Gourmet Cat Food Mouthfeel Inspector"


def main() -> None:
    """Validate and write the job title to $MAKEFUN_OUTPUT_DIR/entry.txt."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out_path = out_dir / "entry.txt"
    content = f"{TITLE}\n"

    # Gate: entry.txt is 1-60 chars, UTF-8, not only whitespace (judge reads it pairwise).
    if not (1 <= len(content) <= 60 and content.strip()):
        raise ValueError("Invalid content for entry.txt")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    print(f"Wrote {out_path} ({len(content)} chars)")


if __name__ == "__main__":
    main()
