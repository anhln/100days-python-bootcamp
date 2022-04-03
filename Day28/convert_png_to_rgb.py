from PIL import Image

png = Image.open("tomato.png")
png.load() # required for png.split()

background = Image.new("RGB", png.size, "#f7f5dd")
background.paste(png, mask=png.split()[3]) # 3 is the alpha channel

background.save('tomato.jpg', 'JPEG', quality=80)