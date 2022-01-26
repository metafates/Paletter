# 🎨 **Paletter**

Generate images with a color palette from the provided picture. You can use them as wallpapers or some fancy backgrounds 🧑‍🎨

## 🌄 Examples

![Example 1](examples/example1.png)
![Example 2](examples/example2.png)
![Example 3](examples/example3.png)

## 📦 Requirements

-   Python 3.9+
-   Poetry

## 🛠 Install

Clone this repo and install dependencies

```bash
git clone https://github.com/metafates/Paletter.git
cd Paletter
poetry install
```

Then you can run the script by running

```bash
poetry run python paletter/paletter.py
```

Or you can build an executable with

```bash
poetry run pyinstaller --onefile --paths paletter paletter/paletter.py
```

This will create an executable at `dist/paletter`

## 📝 Usage

```
usage: paletter.py [-h] [--out OUT] [--colors COLORS] [--contrast CONTRAST] [--no-shapes] [--no-border]
                   [--shape-size SHAPE_SIZE] [--shape SHAPE] [--border-width BORDER_WIDTH] [--blocks-gap BLOCKS_GAP]
                   [--shapes-gap SHAPES_GAP] [--shapes-per-row SHAPES_PER_ROW] [--resolution RESOLUTION] [--scale SCALE]
                   image

Generates color palette from image

positional arguments:
  image                 Image to work with

options:
  -h, --help            show this help message and exit
  --out OUT             Generated image path (without extension)
  --colors COLORS       Number of colors in the palette
  --contrast CONTRAST   Minimum contrast ratio between primary color and colors in palette
  --no-shapes           Do not draw shapes on the color blocks
  --no-border           Do not add border to the image
  --shape-size SHAPE_SIZE
                        Shapes size. Valid options are small, medium and large. Default is small
  --shape SHAPE         Decoration shape on the color block. Valid options are square and circle. Default is square
  --border-width BORDER_WIDTH
                        Border width in pixels. Default 15
  --blocks-gap BLOCKS_GAP
                        Gap between color blocks in pixels. Default is 90
  --shapes-gap SHAPES_GAP
                        Gap between shapes inside color blocks. Default is 15
  --shapes-per-row SHAPES_PER_ROW
                        Shapes per row. Default is 3
  --resolution RESOLUTION
                        Image resolution. Default is 1920x1080
  --scale SCALE         Image scaling. Default is 1
```
