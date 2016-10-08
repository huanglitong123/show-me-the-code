#-*-coding: utf-8-*-
import uuid


class generate_N_keys:

    def __init__(self):
        self.Num = 0
        self.list = []

    def generate(self, Num):
        for i in range(Num):
            self.list.append(str(uuid.uuid1()).replace('-', ''))

    def return_list(self):
        return self.list


test = generate_N_keys()
test.generate(200)
keys = test.return_list()
print(keys)
print(len(keys))
# 转换为字典看keys 是否也是200，表明其中是否有重
print(len({}.fromkeys(keys).keys()))
