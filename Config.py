from csv import DictWriter
import csv

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
