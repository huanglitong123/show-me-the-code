# -*- coding: utf-8 -*-
#!/usr/bin/env python
import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter


class create_Verifi_Image:

    def __init__(self):
        self.size = (120, 30)
        self.width = 120
        self.height = 30
        self.chars = string.ascii_uppercase
        self.img_type = 'PNG'
        self.mode = 'RGB'
        self.bg_color = (
            random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
        self.fg_color = (
            random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))
        self.font_size = 18
        self.font_type = 'arial.ttf'
        self.length = 4

        self.draw_lines = True
        self.n_line = (1, 2)

        self.draw_points = True
        self.point_chance = 2
        self.img = Image.new(self.mode, self.size, self.bg_color)
        self.draw = ImageDraw.Draw(self.img)

    def create_strs(self):
        c_chars = ''.join([random.choice(self.chars)
                           for i in range(self.length)])
        font = ImageFont.truetype(self.font_type, self.font_size)
        x0 = 9
        for c in c_chars:
            xt = random.randint(0, self.font_size / 3)
            yt = random.randint(2, 6)
            self.draw.text((x0 + xt, yt), c, font=font, fill=self.fg_color)
            x0 = x0 + xt + self.font_size
        return c_chars

    def create_lines(self):
        line_num = random.randint(self.n_line[0], self.n_line[1])
        for i in range(line_num):
            begin = (
                random.randint(0, self.width), random.randint(0, self.height))
            end = (
                random.randint(0, self.width), random.randint(0, self.height))
            self.draw.line([begin, end], fill=(0, 0, 0))

    def create_points(self):
        chance = min(100, max(0, int(self.point_chance)))
        for w in range(self.width):
            for h in range(self.height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    self.draw.point((w, h), fill=(0, 0, 0))

    def main(self):
        params = [
            1 - float(random.randint(1, 2) / 100),
            0,
            0,
            0,
            1 - float(random.randint(1, 10) / 100),
            float(random.randint(1, 2) / 500),
            0.001,
            float(random.randint(1, 2) / 500)]

        self.img = self.img.transform(self.size, Image.PERSPECTIVE, params)
        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)

        return self.img

CVI = create_Verifi_Image()
CVI.create_lines()
CVI.create_points()
strs = CVI.create_strs()
code_img = CVI.main()
code_img.show()
code_img.save("validate.png", "GIF")
print(strs)
