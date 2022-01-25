from colorthief import ColorThief
from type_aliases import RGB
import config


def primary(image_path: str) -> RGB:
    '''Get the primary color'''
    thief = ColorThief(image_path)
    return thief.get_color(quality=1)


def rgb_to_luma(color: RGB) -> float:
    r, g, b = color
    return 0.299*r + 0.587*g + 0.114*b


def palette(image_path: str, color_count: int = config.COLORS) -> list[RGB]:
    '''Build a color palette'''
    thief = ColorThief(image_path)
    return thief.get_palette(color_count=color_count, quality=9)
