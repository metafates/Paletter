import argparse

parser = argparse.ArgumentParser(
    prog='paletter.py',
    description="Generates color palette from image"
)

parser.add_argument(
    'image',
    help='Image to work with',
    type=str
)

parser.add_argument(
    '--out',
    help='Generated image path (without extension)',
    type=str,
    default='out'
)

parser.add_argument(
    '--colors',
    help='Number of colors in the palette',
    type=int,
    default=7
)

parser.add_argument(
    '--contrast',
    help='Minimum contrast ratio between primary color and colors in palette',
    type=float,
    default=1.5
)

parser.add_argument(
    '--no-squares',
    help='Do not draw squares on the color blocks',
    action='store_false'
)

parser.add_argument(
    '--no-border',
    help='Do not add border to the image',
    action='store_false'
)

parser.add_argument(
    '--squares-size',
    help='Squares size. Valid options are small, medium and large. Default is small',
    type=str,
    default='small'
)

args = parser.parse_args()
