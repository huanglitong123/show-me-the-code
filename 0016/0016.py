# coding=utf-8

import json
import xlsxwriter


def load_json_file(file_name):
    f = file(file_name)
    json_data = json.load(f)
    print json_data
    return json_data


def save_as_xls(file_name, data):
    workbook = xlsxwriter.Workbook(file_name)
    # 利用add_worksheet新建的工作表Sheet1
    table = workbook.add_worksheet('numbers')

    row = 0

    # for v in range(1, len(data)+1):
    #     table.write(row, 0, v)
    #     table.write(row, 1, data[str(v)])
    for v in data:
        table.write(row, 0, v[0])
        table.write(row, 1, v[1])
        table.write(row, 2, v[2])

        row += 1
    workbook.close()


if __name__ == '__main__':
    data = load_json_file("numbers.txt")
    if data:
        save_as_xls('numbers.xlsx', data)
