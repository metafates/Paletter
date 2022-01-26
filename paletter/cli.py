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
    '--no-shapes',
    help='Do not draw shapes on the color blocks',
    action='store_false'
)

parser.add_argument(
    '--no-border',
    help='Do not add border to the image',
    action='store_false'
)

parser.add_argument(
    '--shape-size',
    help='Shapes size. Valid options are small, medium and large. Default is small',
    type=str,
    default='small'
)

parser.add_argument(
    '--shape',
    help='Decoration shape on the color block. Valid options are square and circle. Default is square',
    type=str,
    default='square'
)

parser.add_argument(
    '--border-width',
    help='Border width in pixels. Default 15',
    type=int,
    default=15
)

parser.add_argument(
    '--blocks-gap',
    help='Gap between color blocks in pixels. Default is 90',
    type=int,
    default=90
)

parser.add_argument(
    '--shapes-gap',
    help='Gap between shapes inside color blocks. Default is 15',
    type=int,
    default=15
)

parser.add_argument(
    '--resolution',
    help='Image resolution. Default is 1920x1080',
    type=str,
    default='1920x1080'
)

parser.add_argument(
    '--scale',
    help='Image scaling. Default is 1',
    type=float,
    default=1
)

args = parser.parse_args()
