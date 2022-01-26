from type_aliases import Size, ShapeSize, Shape
from cli import args

_MULTIPLIER = args.scale
_W, _H = map(int, args.resolution.lower().split('x'))

# Generated image dimensions in px
SIZE: Size = (int(_W * _MULTIPLIER), int(_H * _MULTIPLIER))

BORDER: bool = args.no_border
BORDER_WIDTH = int(args.border_width * _MULTIPLIER)  # px

COLORS: int = args.colors  # color count
CONTRAST_RATIO: float = args.contrast

GAP = int(args.blocks_gap * _MULTIPLIER)  # px

SHAPES_GAP = int(args.shapes_gap * _MULTIPLIER)  # px
SHAPES: bool = args.no_shapes
SHAPES_SIZE: ShapeSize = args.shape_size
SHAPE: Shape = args.shape
SHAPES_PER_ROW: int = args.shapes_per_row
