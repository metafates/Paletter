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

args = parser.parse_args()
