from type_aliases import Size, ShapeSize, Shape
from cli import args

SIZE: Size = (1920, 1080)  # Generated image dimensions in px

BORDER: bool = args.no_border
BORDER_WIDTH = 15  # px

COLORS: int = args.colors  # color count
CONTRAST_RATIO: float = args.contrast

GAP = 90  # px

SHAPES_GAP = 15  # px
SHAPES: bool = args.no_shapes
SHAPES_SIZE: ShapeSize = args.shape_size
SHAPE: Shape = args.shape
