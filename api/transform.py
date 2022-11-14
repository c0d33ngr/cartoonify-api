from cartooner import cartoonize
import cv2, os, time
from cartoonify import settings


base_dir = settings.MEDIA_ROOT

def transform(image_path):

    true_image_path = os.path.join(base_dir, image_path.split("/media/")[1])
    image = cv2.imread(true_image_path)    #load image to read
    output = cartoonize(image)    #cartoonize image

    file_name = "cartoonize-" + image_path.split("/original-images/")[1]    #get name to use for output

    cv2.imwrite(file_name, output)    #write cartoonized image with variable "file_name" as file name

    cartoon_image_path = image_path.split("/original-images/")[0] + file_name
    return cartoon_image_path
