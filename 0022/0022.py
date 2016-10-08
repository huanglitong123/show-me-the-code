#-*-coding: utf-8-*-
class change_DPI:

    def __init__(self):
        self.path = None

    def setPath(self, path):
        self.path = path

    def change_DPI(self):
        import os
        files = os.listdir(self.path)
        is_exist = False
        for f in files:
            if f.lower().endswith(('.jpg', '.png')):
                is_exist = True
                path_name = os.path.join(self.path, f)
                # 更改f对应文件的分辨率
                from PIL import Image
                im = Image.open(path_name)
                x_iphone5 = 1920
                y_iphone5 = 1080
                (x, y) = im.size
                i = 0
                if x < y:
                    x, y = y, x
                    i = 1
                print('origin img size:')
                print(im.size)
                if x > x_iphone5 or y > y_iphone5:
                    if x > x_iphone5:
                        x_resize = x_iphone5
                        y_resize = int(y * (x_resize * 1.0 / x))
                        if not i:
                            f_resize = im.resize((x_resize, y_resize))
                        else:
                            f_resize = im.resize((y_resize, x_resize))
                        f_resize.save(f)
                        continue
                    if y > y_iphone5:
                        y_resize = y_iphone5
                        x_resize = int(x * (y_resize * 1.0 / y))
                        if not i:
                            f_resize = im.resize(
                                (x_resize, y_resize), Image.ANTIALIAS)
                        else:
                            f_resize = im.resize(
                                (y_resize, x_resize), Image.ANTIALIAS)
                        f_resize.save(f)
                        continue

        if is_exist == False:
            print('no photo')


if __name__ == '__main__':
    test = change_DPI()
    test.setPath('E:/work/python_practice/0022')
    test.change_DPI()
