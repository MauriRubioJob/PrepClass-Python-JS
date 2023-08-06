import arcade
from arcade.arcade_types import PointList
from typing import List

import PIL.Image
import PIL.ImageOps
import PIL.ImageDraw

def load_textures(file_name: str,
                  image_location_list: PointList,
                  mirrored: bool = False,
                  flipped: bool = False,
                  scale: float = 1) -> List['Texture']:
    """
    Load a set of textures off of a single image file.
    Note, if the code is to load only part of the image, the given x, y
    coordinates will start with the origin (0, 0) in the upper left of the
    image. When drawing, Arcade uses (0, 0)
    in the lower left corner when drawing. Be careful about this reversal.
    For a longer explanation of why computers sometimes start in the upper
    left, see:
    http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5
    :param str file_name: Name of the file.
    :param PointList image_location_list: List of image locations. Each location should be
           a list of four floats. ``[x, y, width, height]``.
    :param bool mirrored: If set to true, the image is mirrored left to right.
    :param bool flipped: If set to true, the image is flipped upside down.
    :param float scale: Scale factor to apply on each new texture.
    :Returns: List of textures loaded.
    :Raises: ValueError
    """
    # See if we already loaded this texture file, and we can just use a cached version.
    cache_file_name = "{}".format(file_name)
    if cache_file_name in arcade.load_texture.texture_cache:
        texture = arcade.load_texture.texture_cache[cache_file_name]
        source_image = texture.image
    else:
        source_image = PIL.Image.open(file_name)
        result = arcade.Texture(cache_file_name, source_image)
        arcade.load_texture.texture_cache[cache_file_name] = result

    source_image_width, source_image_height = source_image.size
    texture_info_list = []
    for image_location in image_location_list:
        x, y, width, height = image_location

        if width <= 0:
            raise ValueError("Texture has a width of {}, must be > 0."
                             .format(width))
        if x > source_image_width:
            raise ValueError("Can't load texture starting at an x of {} "
                             "when the image is only {} across."
                             .format(x, source_image_width))
        if y > source_image_height:
            raise ValueError("Can't load texture starting at an y of {} "
                             "when the image is only {} high."
                             .format(y, source_image_height))
        if x + width > source_image_width:
            raise ValueError("Can't load texture ending at an x of {} "
                             "when the image is only {} wide."
                             .format(x + width, source_image_width))
        if y + height > source_image_height:
            raise ValueError("Can't load texture ending at an y of {} "
                             "when the image is only {} high."
                             .format(y + height, source_image_height))

        # See if we already loaded this texture, and we can just use a cached version.
        cache_name = "{}{}{}{}{}{}{}{}".format(file_name, x, y, width, height, scale, flipped, mirrored)
        if cache_name in arcade.load_texture.texture_cache:
            result = load_texture.texture_cache[cache_name]
        else:
            image = source_image.crop((x, y, x + width, y + height))
            # image = _trim_image(image)

            if mirrored:
                image = PIL.ImageOps.mirror(image)

            if flipped:
                image = PIL.ImageOps.flip(image)
            result = arcade.Texture(cache_name, image)
            arcade.load_texture.texture_cache[cache_name] = result
            result.scale = scale
        texture_info_list.append(result)

    return texture_info_list

arcade.load_textures = load_textures
