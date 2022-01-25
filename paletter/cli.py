import argparse

parser = argparse.ArgumentParser(
    prog='Paletter',
    description="Generates color palette from image"
)

parser.add_argument(
    'image',
    help='Image to work with',
    type=str
)

parser.add_argument(
    '--out',
    help='Generated image name (without extension)',
    type=str,
    default='out'
)

parser.add_argument(
    '--colors',
    help='Number of colors in the palette',
    type=int,
    default=8
)

parser.add_argument(
    '--shift',
    help='How many colors to shift the palette by',
    type=int,
    default=0
)

args = parser.parse_args()
