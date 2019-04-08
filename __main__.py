import json
import os
import sys
from zipfile import ZipFile, ZIP_DEFLATED

import click
from PIL import Image

from processor import process


@click.command()
@click.argument('folder', required=True)
def main(folder):
    meta_path = os.path.join(folder, 'meta.json')
    with open(meta_path, 'r') as f:
        meta = json.load(f)

    image_path = os.path.join(folder, meta['image'])
    image = Image.open(image_path)

    output = os.path.join(folder, 'output')
    os.mkdir(output)

    result = process(image, meta, output)

    zip_path = os.path.join(folder, 'output.zip')
    thumbnail_path = os.path.join(folder, 'thumbnail.png')
    output_info = os.path.join(folder, 'output.json')

    with ZipFile(zip_path, 'w', ZIP_DEFLATED) as archive:
        for filename, description in result.items():
            path = os.path.join(output, filename)
            if description.get('thumbnail', False):
                Image.open(path).save(thumbnail_path, 'PNG')
            archive.write(path, os.path.join('output', filename))

    with open(output_info, 'w') as f:
        json.dump(process(image, meta, output), f)


if __name__ == '__main__':
    sys.exit(main())
