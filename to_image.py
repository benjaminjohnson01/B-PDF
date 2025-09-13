#!/usr/bin/env python3

"""
Description:
Convert PDF to image using pdf2image.

Example Usage:
python c:/Users/$USER/OneDrive/Desktop/to_image.py 'C:/Users/$USER/iCloudDrive/Important PDFs/Important-PDF.pdf' 'C:/Users/$USER/iCloudDrive/Important PDFs/'
"""

import argparse
from pathlib import Path

import pdf2image


def pdf_to_png(pdf_path, output_folder=None, output_type="png", dpi=300):
    if output_folder is None:
        output_folder = pdf_path.parent
    images = pdf2image.convert_from_path(str(pdf_path), dpi=dpi, fmt=output_type)
    for i, image in enumerate(images):
        image.save(
            output_folder / f"{pdf_path.stem}_{i}.{output_type}", output_type.upper()
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to lossless PNG.")
    parser.add_argument(
        "pdf_path",
        type=Path,
        help="Path to the input PDF file.",
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        type=Path,
        default=None,
        help="Output folder for PNG files.",
    )
    parser.add_argument(
        "-t",
        "--output_type",
        type=str,
        choices=["png", "jpeg", "jpg"],
        default="png",
        help="Output file type (default: png).",
    )
    parser.add_argument(
        "-d",
        "--dpi",
        type=int,
        default=300,
        help="DPI for the output images (default: 300).",
    )
    args = parser.parse_args()
    pdf_to_png(args.pdf_path, args.output_folder, args.output_type, args.dpi)
