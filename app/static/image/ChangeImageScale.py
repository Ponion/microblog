from PIL import Image
import sys

def scale(load_path, width, height, save_path):
    image = Image.open(load_path)
    new_image = image.resize((int(width),int( height)))
    new_image.save(save_path)

if __name__ == '__main__':
    scale(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

