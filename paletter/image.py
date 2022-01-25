from typing import Literal
from type_aliases import RGB, RGBA, Size
from PIL import Image, ImageDraw, ImageOps
import config
import random


def blank(
    size: Size,
    color: RGB | RGBA = (0, 0, 0),
    mode: Literal["RGB", "RGBA"] = "RGB"
) -> Image.Image:
    '''Creates a blank image'''
    image = Image.new(size=size, color=color, mode=mode)
    return image


def color_block(
    size: Size,
    color: RGB,
    palette: list[RGB]
) -> Image.Image:
    '''Generates a color block'''
    # Todo: add squares
    return blank(size, color)


def add_color_blocks(
    image: Image.Image,
    pallette: list[RGB]
) -> Image.Image:
    w, h = image.size
    block_size = (int(w / (config.COLORS * 1.7)), int(h * 0.85))
    blocks_combined_width = block_size[0] * len(pallette)
    combined_width_with_gaps = blocks_combined_width + \
        config.GAP * (len(pallette) - 1)

    for i, color in enumerate(pallette):
        block = color_block(block_size, color, pallette)
        block_coords = (
            (w - combined_width_with_gaps) // 2 +
            ((block.width + config.GAP) * i),
            (h - block.height) // 2
        )
        image.paste(block, block_coords)

    return image


def apply_borders(
    image: Image.Image,
    border_width: int,
    color: RGB
) -> Image.Image:
    '''Adds borders to the image'''
    return ImageOps.expand(image, border_width, fill=color)


def squares(size: Size, color: RGB, count: int = 3) -> Image.Image:
    '''Generates squares'''
    width, height = size
    wrapper_size: Size = (int(width * (count + width * 0.5)), height)
    wrapper = blank(wrapper_size, (0, 0, 0, 0), "RGBA")
    draw = ImageDraw.Draw(wrapper)

    # TODO: make them draw in a row
    for _ in range(count):
        draw.rectangle((0, 0, *size), fill=color)

    return wrapper
