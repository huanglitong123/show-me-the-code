# coding=utf-8
import xlrd
import re


def cal_time():
    # start
    # 利用xlrd的open_workbook方法打开已经存在的文件
    wr = xlrd.open_workbook('E:/work/python_practice/0020/phone_test.xlsx')
    # 利用xlrd的open_workbook方法打开已经存在工作表Sheet1
    table = wr.sheet_by_name('Sheet1')
    # 建立3个列表，存储读取的数据
    li_1 = []  # 给每个数建立一个list表
    minute = 0
    second = 0
    # 获取表的行数和列数
    nrows = table.nrows

    # 取出数据
    for row_num in xrange(1, nrows):  # 表示遍历的行数
        m = re.findall(r'(\w*[0-9]+)\w*', table.cell(row_num, 1).value)
        if len(m) == 2:
            minute += int(m[0])
            second += int(m[1])
        else:
            second += int(m[0])

        li_1.append(table.cell(row_num, 1).value)
    minute += second/60
    second = second % 60
    print "%d minute, %d second" % (minute, second)


cal_time()
