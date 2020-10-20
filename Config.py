from csv import DictWriter
import csv, os, glob
from xlsxwriter.workbook import Workbook

time = 0
filename = ''


def append_dict_as_row(file_name, dict_of_elem, headers):
    with open(file_name, 'a+', newline='') as write_obj:
        dict_writer = DictWriter(write_obj, fieldnames=headers)
        dict_writer.writerow(dict_of_elem)


def createFile(filename):
    with open(filename, 'w', newline='') as file:
        Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                   'Type', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

        writer = csv.DictWriter(file, fieldnames=Headers)
        writer.writeheader()


def convertToExcel():
    for csvfile in glob.glob(os.path.join('.', '*.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()
