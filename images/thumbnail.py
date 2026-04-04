#!/usr/bin/env python3
"""
thumbnail.py — Generate thumbnails for images in a project folder.

Usage:
    python thumbnail.py <image_folder>

For each image (JPEG/PNG/WEBP) found directly in <image_folder>, a thumbnail
is created in <image_folder>/thumbnails/ with the longest edge scaled to
MAX_LONGEST_EDGE pixels while preserving the original aspect ratio.
"""

import sys
import os
from pathlib import Path
from PIL import Image

MAX_LONGEST_EDGE = 500
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def make_thumbnail(src_path: Path, dst_path: Path, max_edge: int = MAX_LONGEST_EDGE) -> None:
    """Resize *src_path* so its longest edge equals *max_edge* and save to *dst_path*."""
    with Image.open(src_path) as img:
        w, h = img.size
        scale = max_edge / max(w, h)
        new_size = (round(w * scale), round(h * scale))
        thumb = img.resize(new_size, Image.LANCZOS)
        thumb.save(dst_path, quality=85, optimize=True)
    print(f"  {src_path.name}  {w}x{h}  →  {new_size[0]}x{new_size[1]}  →  {dst_path}")


def process_folder(folder: Path) -> None:
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    thumbnails_dir = folder / "thumbnails"
    thumbnails_dir.mkdir(exist_ok=True)
    print(f"Output folder: {thumbnails_dir}\n")

    images = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not images:
        print("No supported images found.")
        return

    for src in images:
        dst = thumbnails_dir / src.name
        make_thumbnail(src, dst)

    print(f"\nDone. {len(images)} thumbnail(s) created.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <image_folder>")
        sys.exit(1)

    process_folder(Path(sys.argv[1]))
