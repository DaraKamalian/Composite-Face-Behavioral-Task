import random
import xlsxwriter
import datetime
import csv

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from DifferentTotalLocationsList import DifferentTotalLocationsList
from Data import ExcelFile



image = MainAssets()
correct = image.correct
wrong = image.wrong
differentLocationsList = DifferentTotalLocationsList()
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Congruent_Aligned(object):
    def CongruentAligned(self, practice, index, gender, same, subjectInfoList):


        print('index is : ' + str(index))
        # Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition', 'Type',
        #            'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

        # Cells = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        #
        # workbook = xlsxwriter.Workbook(
        #     str(subjectInfoList[0] + subjectInfoList[1]) + '-' + 'D' + str(subjectInfoList[2]) + '.xlsx')
        #
        # worksheet = workbook.add_worksheet()
        #
        # HeaderFormat = workbook.add_format({
        #     'bold': True,
        #     'text_wrap': False,
        #     'valign': 'top',
        #     'fg_color': '#D7E4BC',
        #     'border': 1})

        mydict = {
            "0": "Name",
            "1": "Number",
            "2": "Age",
            "3": "Gender",
            "4": "Handedness",
            "5": "Experiment Day",
            "6": "Stimulation Site",
            "7": "Resp Version",
            "8": "Datetime"
        }

        data = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
            "H": None,
            "I": None,
            "J": None,
            "K": None,
            "L": None,
            "M": None,
            "N": None,
            "O": None
        }

        # for i in range(0, 6):
        #     worksheet.write('A' + str(i + 1), 'Subject ' + mydict[str(i)], HeaderFormat)
        #     worksheet.write('B' + str(i + 1), subjectInfoList[i])
        #
        # for i in range(6, 8):
        #     worksheet.write('A' + str(i + 1), mydict[str(i)], HeaderFormat)
        #     worksheet.write('B' + str(i + 1), subjectInfoList[i])
        #
        # worksheet.write('A8', 'Datetime', HeaderFormat)
        # worksheet.write('B8', str(datetime.datetime.today()))
        #
        # for i in range(0, len(Cells)):
        #     worksheet.write(Cells[i] + '9', Headers[i], HeaderFormat)

        # if gender:
        #     worksheet.write('C' + str(index), 'Male')
        #     data["C"] = 'Male'
        # else:
        #     worksheet.write('C' + str(index), 'Female')
        #     data["C"] = 'Female'
        # worksheet.write('G' + str(index), '1')
        # data["G"] = '1'
        # worksheet.write('H' + str(index), 'Top Same + Bottom Same')
        # data["H"] = 'Top Same + Bottom Same'
        # worksheet.write('K' + str(index), 'A')
        # data["K"] = 'A'

        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)
        if same:
            if gender:
                print('con-same-al-m')
            else:
                print('con-same-al-f')
        else:
            if gender:
                print('con-diff-al-m')
            else:
                print('con-diff-al-f')
        rand1 = random.randint(0, 19)
        if gender:
            men_align_images[rand1].draw()
            win.flip()
            core.wait(0.2)
            print(men_align_images[rand1].image)
        else:
            women_align_images[rand1].draw()
            win.flip()
            core.wait(0.2)
            print(women_align_images[rand1].image)

        # if gender:
        #     worksheet.write('A' + str(index), men_align_images[rand1].image[-13:-4])
        #     data["A"] = men_align_images[rand1].image[-13:-4]
        # else:
        #     data["A"] = women_align_images[rand1].image[-13:-4]
        #     worksheet.write('A' + str(index), women_align_images[rand1].image[-13:-4])

        men_align_images[rand1].autoDraw = False
        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        if gender:
            images = men_align_images
            locations = men_align_locations
        else:
            images = women_align_images
            locations = women_align_locations

        if same:
            if gender:
                men_align_images[rand1].draw()
                print(men_align_images[rand1].image)
                # worksheet.write('B' + str(index), men_align_images[rand1].image[-13:-4])
                data["B"] = men_align_images[rand1].image[-13:-4]
                win.flip()
                core.wait(0.5)
                men_align_images[rand1].autoDraw = False
                questionMark.draw()
                win.flip()
            else:
                women_align_images[rand1].draw()
                print(women_align_images[rand1].image)
                # worksheet.write('B' + str(index), women_align_images[rand1].image[-13:-4])
                data["B"] = women_align_images[rand1].image[-13:-4]
                win.flip()
                core.wait(0.5)
                women_align_images[rand1].autoDraw = False
                questionMark.draw()
                win.flip()
        else:
            newLocations = differentLocationsList.different_total_locations_list(
                locations, images[rand1].image)

            newLocRand = random.randint(0, len(newLocations) - 1)
            secondfacelist = []
            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    win.flip()
                    secondfacelist.append(item)
                    print(item.image)
                    # worksheet.write('B' + str(index), item.image[-13:-4])
                    data["B"] = item.image[-13:-4]
                    break
            core.wait(0.5)
            secondfacelist[0].autoDraw = False
            questionMark.draw()
            win.flip()

        countdown = core.CountdownTimer(1.5)

        anslist = []
        lateflag = False
        flag = True
        while flag:
            # keys = event.getKeys(keyList=['a', 'l'])
            keys = event.waitKeys(keyList=['a', 'l'], maxWait=1.5)
            if keys:
                for key in keys:
                    if key == 'a':
                        if practice:
                            correct.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            anslist.append(key)

                            # worksheet.write('J' + str(index), 'A')
                            data["J"] = 'A'
                            # worksheet.write('L' + str(index), '=IF(K' + str(index) + '= J' +
                            #                 str(index) + ',1,0)')
                            data["L"] = 'accuracy'
                            # worksheet.write('M' + str(index), str(1.5 - countdown.getTime()))
                            # data["M"] = str(1.5 - countdown.getTime())
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            anslist.append(key)
                            # worksheet.write('J' + str(index), 'L')
                            data["J"] = 'L'
                            # worksheet.write('L' + str(index), '=IF(K' + str(index) + '= J' +
                            #                 str(index) + ',1,0)')
                            data["L"] = 'accuracy'
                            # worksheet.write('M' + str(index), str(1.5 - countdown.getTime()))
                            data["M"] = str(1.5 - countdown.getTime())
                        flag = False
            elif countdown.getTime() <= 0:
                lateflag = True
                # worksheet.write('J' + str(index), 'None')
                # worksheet.write('L' + str(index), 'None')
                # worksheet.write('M' + str(index), 'None')
                # worksheet.write('O' + str(index), 'None')
                data["J"] = 'None'
                data["L"] = 'None'
                data["M"] = 'None'
                flag = False

        datadict = {
            "Alignment": '1',
            "Condition": None,
            "Cor-Ans": None,
            "Key-Resp": str(anslist[0]),
            "R-time": str(1.5 - countdown.getTime()),
            "Face_Gender": None,
            "Face_1": None,
            "Face_2": None,
        }
        #
        # if same:
        #     datadict["Condition"] = "Top Same + Bottom Same"
        #     datadict["Cor-Ans"] = "A"
        #     if gender:
        #         datadict["Face_Gender"] = 'Male'
        #         datadict["Face_1"] = men_align_images[rand1].image[-13:-4]
        #         datadict["Face_2"] = men_align_images[rand1].image[-13:-4]
        #     else:
        #         datadict["Face_Gender"] = 'Female'
        #         datadict["Face_1"] = women_align_images[rand1].image[-13:-4]
        #         datadict["Face_2"] = women_align_images[rand1].image[-13:-4]
        # else:
        #     datadict["Condition"] = "Top Different + Bottom Different"
        #     datadict["Cor-Ans"] = "L"
        #     if gender:
        #         datadict["Face_Gender"] = 'Male'
        #         datadict["Face_1"] = men_align_images[rand1].image[-13:-4]
        #         datadict["Face_2"] = secondfacelist[0].image[-13:-4]
        #     else:
        #         datadict["Face_Gender"] = 'Female'
        #         datadict["Face_1"] = women_align_images[rand1].image[-13:-4]
        #         datadict["Face_2"] = secondfacelist[0].image[-13:-4]


        with open(str(1) + '.csv', 'w', newline='') as file:
            Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                       'Type','Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

            writer = csv.DictWriter(file, fieldnames=Headers)
            writer.writeheader()

            if same:
                writer.writerow({'Alignment': '1', 'Condition': 'Top Same + Bottom Same', 'Cor-Ans': 'A',
                                  'Key-Resp': str(anslist[0]), 'R-time': str(1.5 - countdown.getTime())})

                if gender:
                    writer.writerow({'Face_Gender': 'Male', 'Face_1': men_align_images[rand1].image[-13:-4],
                                        'Face_2': men_align_images[rand1].image[-13:-4]} )

                else:
                    writer.writerow({'Face_Gender': 'Female', 'Face_1': women_align_images[rand1].image[-13:-4],
                                      'Face_2': women_align_images[rand1].image[-13:-4]})
            else:
                writer.writerow({'Alignment': '1', 'Condition': 'Top Different + Bottom Different', 'Cor-Ans': 'L',
                                  'Key-Resp': str(anslist[0]), 'R-time': str(1.5 - countdown.getTime())})

                if gender:
                    writer.writerow({'Face_Gender': 'Male', 'Face_1': men_align_images[rand1].image[-13:-4],
                                      'Face_2': secondfacelist[0].image[-13:-4]})

                else:
                    writer.writerow({'Face_Gender': 'Female', 'Face_1': women_align_images[rand1].image[-13:-4],
                                      'Face_2': secondfacelist[0].image[-13:-4]})

        datalist = []
        datalist.append(writer)

        return datalist




































