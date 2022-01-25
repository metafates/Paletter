import colors
import image
import cli
import config
import os


def generate(image_path: str, out_path: str) -> None:
    try:
        print('Getting color palette (this may take a while)')
        primary = colors.primary(image_path)
        palette = colors.palette(image_path)
        most_contrasting = max(
            palette, key=lambda c: colors.contrast(primary, c))

        print('Generating image')
        blank = image.blank(config.SIZE, primary)
        out = image.add_color_blocks(blank, palette)
        out = image.apply_borders(out, config.BORDER, most_contrasting)

        print('Saving')
        out.save(out_path)

        print(f'Done! Saved at {out_path}')
    except Exception:
        print(Exception)


def main():
    cwd = os.getcwd()
    image_path = os.path.join(cwd, cli.args.image)
    image_extension = image_path.split('.')[-1]
    out_name = cli.args.out
    generate(image_path, os.path.join(cwd, f'{out_name}.{image_extension}'))


if __name__ == "__main__":
    main()
