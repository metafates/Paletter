from colorthief import ColorThief
from type_aliases import RGB
import config


def primary(image_path: str) -> RGB:
    '''Get the primary color'''
    thief = ColorThief(image_path)
    return thief.get_color(quality=1)


def luminance(color: RGB) -> float:
    '''Calculates the luminance of the color'''
    def f(c: int) -> float:
        c_ = c / 255
        if c_ <= 0.03928:
            return c_ / 12.92
        return ((c_ + 0.055) / 1.055) ** 2.4

    color_ = map(f, color)
    r, g, b = color_
    return r * 0.2126 + g * 0.7152 + b * 0.0722


def contrast(a: RGB, b: RGB) -> float:
    '''Calculates contrast ration between 2 colors'''
    lum_a = luminance(a)
    lum_b = luminance(b)
    brightest, darkest = max(lum_a, lum_b), min(lum_a, lum_b)
    return (brightest + 0.05) / (darkest + 0.05)


def palette(image_path: str, color_count: int = config.COLORS) -> list[RGB]:
    '''Build a color palette'''
    thief = ColorThief(image_path)
    primary = thief.get_color(quality=1)
    palette = thief.get_palette(50)
    # throw out colors similar to the primary color
    return list(filter(lambda c: contrast(primary, c) > config.CONTRAST_RATIO, palette))[:color_count]
