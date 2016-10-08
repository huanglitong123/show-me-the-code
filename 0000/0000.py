# coding: utf-8
imagePath = "E:/work/python_practice/0000/image.png"
fontPath = "E:/work/python_practice/0000/ahronbd.ttf"
outputFile = "output.jpg"
from PIL import Image, ImageDraw, ImageFont
# use PIL to draw the photo
# get an image
im = Image.open(imagePath)
draw = ImageDraw.Draw(im)
# get a font
fnt = ImageFont.truetype(fontPath, 40)
# draw text, half opacity
draw.text((im.size[0]-40, 0), "6", font=fnt, fill=(255, 0, 0, 255))
im.show()
im.save(outputFile)


# from PIL import Image, ImageDraw, ImageFont


# class Image_unread_message:

#     def open(self, path):
#         self.im = Image.open(path)
#         return self.im.size

#     def __init__(self):
#         self.fnt = None
#         self.im = None

#     def setFont(self, font_path, size):
#         self.fnt = ImageFont.truetype(font_path, size)
#         return True

#     def draw_text(self, position, str, colour):
#         draw = ImageDraw.Draw(self.im)
#         draw.text(position, str, fill=colour, font=self.fnt)
#         self.im.show()
#         self.im.save(str+'num'+'.jpg')
#         return True


# test = Image_unread_message()
# size = test.open('E:/work/python_practice/0000/image.png')
# print size
# test.setFont('E:/work/python_practice/0000/ahronbd.ttf', 80)
# test.draw_text((size[0]-40, 0), '4', (255, 0, 0))
