from PIL import Image

QUALITY = 80
IMAGE_EXTENSION = "JPEG"


def convert(input_file_path, output_file_path, color_code):
    png = Image.open(input_file_path)
    png.load() # required for png.split()
    background = Image.new("RGB", png.size, color_code)
    background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
    background.save(output_file_path, IMAGE_EXTENSION, quality=QUALITY)

convert("background.png", "background.jpg", "#ffffff")
convert("kanye.png", "kanye.jpg", "#ffffff")