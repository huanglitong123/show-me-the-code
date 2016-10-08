# coding=utf-8

import os
import re

"""
0007：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""


class get_Code_Situation():

    def __init__(self):
        self.full_path = []

    def source_statistic(self):
        total = 0
        blank = 0
        comment = 0
        content = 0
        for file in self.full_path:
            with open(file) as f:
                lines = f.readlines()
                total += len(lines)

                pattern1 = re.compile(r'^\s*$')
                pattern2 = re.compile(r'^\s*\#+')

                for line in lines:
                    if pattern1.match(line):
                        blank += 1
                    elif pattern2.match(line):
                        comment += 1
        content = total - blank - comment
        print 'Total Lines: %d, Content: %d, Blank Lines: %d, Comment Lines: %d' % (total, content, blank, comment)

    def walk_dir(self, image_path):
        for root, dirs, files in os.walk(image_path):
            for f in files:
                if f.lower().endswith('.py'):
                    self.full_path.append(os.path.join(root, f))

                    # resize_image(full_path)
        print self.full_path
get_code_situation = get_Code_Situation()
get_code_situation.walk_dir("source")
get_code_situation.source_statistic()
