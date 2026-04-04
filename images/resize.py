#!/usr/bin/env python3
"""
resize.py — Resize images in a project folder in-place.

Usage:
    python resize.py <image_folder>

For each image (JPEG/PNG/WEBP) found directly in <image_folder>, the image is
resized so its longest edge equals MAX_LONGEST_EDGE pixels while preserving the
original aspect ratio. The original file is overwritten.
"""

import sys
from pathlib import Path
from PIL import Image

MAX_LONGEST_EDGE = 3000
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def resize_image(path: Path, max_edge: int = MAX_LONGEST_EDGE) -> None:
    """Resize *path* in-place so its longest edge equals *max_edge*."""
    with Image.open(path) as img:
        w, h = img.size
        if max(w, h) <= max_edge:
            print(f"  {path.name}  {w}x{h}  →  skipped (already within limit)")
            return
        scale = max_edge / max(w, h)
        new_size = (round(w * scale), round(h * scale))
        resized = img.resize(new_size, Image.LANCZOS)
        resized.save(path, quality=90, optimize=True)
    print(f"  {path.name}  {w}x{h}  →  {new_size[0]}x{new_size[1]}")


def process_folder(folder: Path) -> None:
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    images = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not images:
        print("No supported images found.")
        return

    print(f"Resizing {len(images)} image(s) in '{folder}' (longest edge → {MAX_LONGEST_EDGE}px)\n")
    for src in images:
        resize_image(src)

    print(f"\nDone. {len(images)} image(s) processed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <image_folder>")
        sys.exit(1)

    process_folder(Path(sys.argv[1]))
