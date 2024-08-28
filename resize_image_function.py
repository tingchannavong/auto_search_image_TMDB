"""A function that takes in image path and target aspect ratio, and you specify save folder. This function will return the resized image path in that folder. """
from PIL import Image
import os

def resize_image(image_path, target_size,save_folder):
    # Open image path
    img = Image.open(image_path)

    # Resize the image
    resized_img = img.resize(target_size)

    # Get base name of movie via file path
    img_path_base_name = os.path.basename(image_path)

    # Specify save folder and new file name + path
    resized_image_path = f"{save_folder}/resized_{img_path_base_name}"

    # Save image
    resized_img.save(resized_image_path)

    return resized_image_path

# Type of Instagram Post  Aspect Ratio    Instagram Post Size    Target Size (Tuple)

# Square Photo             1:1             1080 x 1080px        (1080,1080)
# Landscape Photo          1.91:1          1080 x 608px
# Portrait Photo           4:5             1080 x 1350px        (1080,3250)
# Instagram Stories        9:16            1080 x 1920px
# IGTV Cover Photo         1:1.55          420 x 654px
# Instagram Square Video   1:1             1080 x 1080px
# Instagram Landscape Video 1.91:1         1080 x 608px
# Instagram Portrait Video 4:5             1080 x 1350px