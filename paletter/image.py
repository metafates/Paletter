from typing import Literal
from type_aliases import RGB, RGBA, Size
from PIL import Image, ImageOps, ImageDraw
import config


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
    block = blank(size, color)
    if config.SHAPES:
        match config.SHAPES_SIZE:
            case "small":
                multiplier = 0.1
            case "medium":
                multiplier = 0.15
            case "big":
                multiplier = 0.2

        shapes = decoration_shapes(
            int(size[0] * multiplier), palette, bgFIX=color)
        block.paste(shapes, (
            (block.width - shapes.width) // 2,
            (block.height - shapes.height) // 2
        ))
    return block


def add_color_blocks(
    image: Image.Image,
    palette: list[RGB]
) -> Image.Image:
    w, h = image.size
    block_size = (int(w / (config.COLORS * 1.7)), int(h * 0.85))
    blocks_combined_width = block_size[0] * len(palette)
    combined_width_with_gaps = blocks_combined_width + \
        config.GAP * (len(palette) - 1)

    for i, color in enumerate(palette):
        block = color_block(block_size, color, palette)
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


# ? For some reason PIL does not create a transparent image. Use bgFIX to hide wrapper
def decoration_shapes(
    side: int,
    palette: list[RGB],
    bgFIX: RGB,
    count: int = 3
) -> Image.Image:
    '''Generates shapes'''
    gapX = config.SHAPES_GAP
    gapY = gapX * 2
    colors = len(palette) * 2
    overall_width = side * count + gapX * (count - 1)
    overall_height = side * colors + gapY * (colors - 1)

    wrapper = blank((overall_width, overall_height), bgFIX)

    doubled_palette: list[RGB] = []
    for color in palette:
        doubled_palette.extend([color, color])

    draw = ImageDraw.Draw(wrapper)

    for i, color in enumerate(doubled_palette):
        for j in range(count):
            x = (side + gapX) * j
            y = (side + gapY) * i
            if config.SHAPE == 'circle':
                draw.ellipse((x, y, x+side, y+side), color)
            else:
                square = blank((side, side), color)
                wrapper.paste(square, (x, y))

    return wrapper
