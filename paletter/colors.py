from colorthief import ColorThief
from type_aliases import RGB
import config
from sty import bg, fg, rs


def print_palette(pal: list[RGB]) -> None:
    for color in pal:
        r, g, b = color
        r_, g_, b_ = max(pal, key=lambda c: contrast(color, c))
        hex_color = rgb_to_hex(color)
        output = fg(r_, g_, b_) + bg(r, g, b) + f' {hex_color} ' + rs.all
        print(output, end='')
    print()


def rgb_to_hex(color: RGB) -> str:
    r, g, b = color
    return f'#{r:02x}{g:02x}{b:02x}'.upper()


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

    r, g, b = map(f, color)
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
