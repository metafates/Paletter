# Paletter

Generates images with color palette from provided picture

## Examples

![Example 1](examples/example1.png)
![Example 2](examples/example2.png)
![Example 3](examples/example3.png)

## Dependencies

-   Python 3.9+
-   colorthief

## Usage

```
usage: main.py [-h] [--out OUT] [--colors COLORS] [--contrast CONTRAST] [--no-squares] [--no-border] image

Generates color palette from image

positional arguments:
  image                Image to work with

options:
  -h, --help           show this help message and exit
  --out OUT            Generated image path (without extension)
  --colors COLORS      Number of colors in the palette
  --contrast CONTRAST  Minimum contrast ratio between primary color and colors in palette
  --no-squares         Do not draw squares on the color blocks
  --no-border          Do not add border to the image
```
