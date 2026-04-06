#!/usr/bin/env python3
"""
resize_mobile.py — Resize images to a target width for mobile delivery.

Usage:
    python resize_mobile.py <image_folder> [--width W] [--output <output_folder>]

For each image (JPEG/PNG/WEBP) found directly in <image_folder>, the image is
resized so its width equals WIDTH pixels while preserving the original aspect
ratio. If --output is omitted or equals <image_folder>, the original file is
overwritten in-place; otherwise the resized copy is written to <output_folder>.
"""

import sys
import argparse
from pathlib import Path
from PIL import Image

DEFAULT_WIDTH = 1400
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def resize_image(src: Path, dest: Path, target_width: int) -> None:
    """Resize *src* to *target_width* pixels wide and save to *dest*."""
    with Image.open(src) as img:
        w, h = img.size
        if w == target_width:
            print(f"  {src.name}  {w}x{h}  →  skipped (already target width)")
            if dest != src:
                import shutil
                shutil.copy2(src, dest)
            return
        scale = target_width / w
        new_size = (target_width, round(h * scale))
        resized = img.resize(new_size, Image.LANCZOS)
        resized.save(dest, quality=90, optimize=True)
    print(f"  {src.name}  {w}x{h}  →  {new_size[0]}x{new_size[1]}  →  {dest}")


def process_folder(folder: Path, output: Path, target_width: int) -> None:
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    output.mkdir(parents=True, exist_ok=True)

    images = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not images:
        print("No supported images found.")
        return

    overwrite = output.resolve() == folder.resolve()
    mode = "in-place" if overwrite else f"→ {output}"
    print(f"Resizing {len(images)} image(s) in '{folder}' (width → {target_width}px, {mode})\n")

    for src in images:
        dest = output / src.name
        resize_image(src, dest, target_width)

    print(f"\nDone. {len(images)} image(s) processed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Resize images to a target width for mobile delivery."
    )
    parser.add_argument("image_folder", help="Folder containing source images")
    parser.add_argument(
        "--width", type=int, default=DEFAULT_WIDTH,
        metavar="W",
        help=f"Target width in pixels (default: {DEFAULT_WIDTH})"
    )
    parser.add_argument(
        "--output", default=None,
        metavar="OUTPUT_FOLDER",
        help="Output folder (default: same as image_folder, overwrites originals)"
    )
    args = parser.parse_args()

    folder = Path(args.image_folder)
    output = Path(args.output) if args.output else folder
    process_folder(folder, output, args.width)
