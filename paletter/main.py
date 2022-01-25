import colors
import image
import cli
import config
import os


def generate(image_path: str, out_path: str) -> None:
    print('Getting color palette (this may take a while)')
    primary = colors.primary(image_path)
    palette = colors.palette(image_path)
    brightest_color = max(palette, key=colors.rgb_to_luma)

    print('Generating image')
    blank = image.blank(config.SIZE, primary)
    out = image.add_color_blocks(blank, palette)
    out = image.apply_borders(out, config.BORDER, brightest_color)

    print('Saving')
    out.save(out_path)

    print(f'Done! Saved at {out_path}')


def main():
    cwd = os.getcwd()
    image_path = os.path.join(cwd, cli.args.image)
    image_extension = image_path.split('.')[-1]
    generate(image_path, os.path.join(cwd, f'out.{image_extension}'))


if __name__ == "__main__":
    main()
