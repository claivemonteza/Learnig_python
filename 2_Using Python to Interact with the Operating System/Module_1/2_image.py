# INSTALL PILL MODULE
# pip install Pillow

import PIL.Image

image = PIL.Image.open("law-book.png")
print(image.size)
print(image.format) 


