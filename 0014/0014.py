# coding=utf-8

import json
import xlsxwriter


def load_json_file(file_name):
    f = file(file_name)
    json_data = json.load(f)
    return json_data


def save_as_xls(file_name, data):
    workbook = xlsxwriter.Workbook(file_name)
    # 利用add_worksheet新建的工作表Sheet1
    table = workbook.add_worksheet('student')

    row = 0

    for k, v in data.items():
        table.write(row, 0, k)
        table.write(row, 1, v[0])
        table.write(row, 2, v[1])
        table.write(row, 3, v[2])
        table.write(row, 4, v[3])

        row += 1
    workbook.close()


if __name__ == '__main__':
    data = load_json_file("student.txt")
    if data:
        save_as_xls('student.xlsx', data)
