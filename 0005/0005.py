#-*-coding: utf-8-*-
class change_DPI:

    def __init__(self):
        self.path = None
        self.outPath = 'E:/work/python_practice/0005/out_'
        self.imgtype = 'jpeg'

    def setPath(self, path):
        self.path = path

    def changeDPI(self):
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
                print('origin img size:')
                print(im.size)
                rate = max(im.size[0]/640.0 if im.size[0] > 640 else 0,
                           im.size[1]/1136.0 if im.size[1] > 1136 else 0)
                if rate:
                    im.thumbnail((im.size[0]/rate, im.size[1]/rate))
                im.save(self.outPath + f, self.imgtype)

        if is_exist == False:
            print('no photo')


if __name__ == '__main__':
    test = change_DPI()
    test.setPath('E:/work/python_practice/0005')
    test.changeDPI()
