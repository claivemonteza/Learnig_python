# install 
# pip install pillow

from PIL import Image

im = Image.open("feliz-aniversario.jpg")
im.rotate(45).show()

new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")