import colors
import image
import cli
import config


def generate(image_path: str, out_name: str) -> None:
    print('Getting color palette')
    primary = colors.primary(image_path)
    palette = colors.palette(image_path)
    brightest = max(palette, key=colors.rgb_to_luma)
    print('Generating image')
    blank = image.blank(config.SIZE, primary)
    out = image.add_color_blocks(blank, palette)
    out = image.apply_borders(out, config.BORDER, brightest)
    print('Saving')
    out.save(out_name)
    print(f'Done! Saved as {out_name}')


def main():
    image_path: str = cli.args.image
    image_extension = image_path.split('.')[-1]
    generate(image_path, f'out.{image_extension}')


if __name__ == "__main__":
    main()
