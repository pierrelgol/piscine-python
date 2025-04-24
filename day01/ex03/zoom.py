#!/usr/bin/env python

from PIL import Image
import os
import sys


def main() -> None:
    img = Image.open("../../../landscape.jpg")

    img_no_red = img.convert("l")

    w, h = img_no_red.size
    zoom_crop = img_no_red.crop((w // 4, h // 4, 3 * w // 4, 3 * h // 4))
    zoomed_img = zoom_crop.resize((w, h), Image.NEAREST)

    output_path = "/tmp/processed_image.jpg"
    zoomed_img.save(output_path)

    os.system(
        f"xdg-open {output_path}"
        if sys.platform.startswith("linux")
        else f"open {output_path}"
    )


if __name__ == "__main__":
    main()
