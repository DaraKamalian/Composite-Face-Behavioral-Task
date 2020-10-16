import random
import xlsxwriter
import datetime

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from DifferentTotalLocationsList import DifferentTotalLocationsList
from Data import Data
from DialogueBox import dialoguebox


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
    def CongruentAligned(self, practice, index, subjectInfoList, gender, same):

        Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition', 'Type',
                   'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

        Cells = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

        workbook = xlsxwriter.Workbook(
            str(subjectInfoList[0] + subjectInfoList[1]) + '-' + 'D' + str(subjectInfoList[2]) + '.xlsx')

        worksheet = workbook.add_worksheet()

        HeaderFormat = workbook.add_format({
            'bold': True,
            'text_wrap': False,
            'valign': 'top',
            'fg_color': '#D7E4BC',
            'border': 1})

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

        for i in range(0, 6):
            worksheet.write('A' + str(i + 1), 'Subject ' + mydict[str(i)], HeaderFormat)
            worksheet.write('B' + str(i + 1), subjectInfoList[i])

        for i in range(6, 8):
            worksheet.write('A' + str(i + 1), mydict[str(i)], HeaderFormat)
            worksheet.write('B' + str(i + 1), subjectInfoList[i])

        worksheet.write('A8', 'Datetime', HeaderFormat)
        worksheet.write('B8', str(datetime.datetime.today()))

        for i in range(0, len(Cells)):
            worksheet.write(Cells[i] + '9', Headers[i], HeaderFormat)

        if gender:
            worksheet.write('C' + str(index), 'Male')
        else:
            worksheet.write('C' + str(index), 'Female')
        worksheet.write('G' + str(index), '1')
        worksheet.write('H' + str(index), 'Top Same + Bottom Same')
        worksheet.write('K' + str(index), 'A')

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

        if gender:
            worksheet.write('A' + str(index), men_align_images[rand1].image)
        else:
            worksheet.write('A' + str(index), women_align_images[rand1].image)

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
                worksheet.write('B' + str(index), men_align_images[rand1].image)
                win.flip()
                core.wait(0.5)
                men_align_images[rand1].autoDraw = False
                questionMark.draw()
                win.flip()
            else:
                women_align_images[rand1].draw()
                print(women_align_images[rand1].image)
                worksheet.write('B' + str(index), women_align_images[rand1].image)
                win.flip()
                core.wait(0.5)
                women_align_images[rand1].autoDraw = False
                questionMark.draw()
                win.flip()
        else:
            newLocations = differentLocationsList.different_total_locations_list(
                locations, images[rand1].image)

            newLocRand = random.randint(0, len(newLocations) - 1)
            list = []
            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    win.flip()
                    list.append(item)
                    print(item.image)
                    worksheet.write('B' + str(index), item.image)
                    break
            core.wait(0.5)
            list[0].autoDraw = False
            questionMark.draw()
            win.flip()

        countdown = core.CountdownTimer(1.5)

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
                            worksheet.write('J' + str(index), 'A')
                            worksheet.write('L' + str(index + 1), '=IF(K' + str(index + 1) + '= J' +
                                            str(index + 1) + ',1,0)')
                            worksheet.write('M' + str(index), str(1.5 - countdown.getTime()))
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            worksheet.write('J' + str(index), 'L')
                            worksheet.write('L' + str(index + 1), '=IF(K' + str(index + 1) + '= J' +
                                            str(index + 1) + ',1,0)')
                            worksheet.write('M' + str(index), str(1.5 - countdown.getTime()))
                        flag = False
            elif countdown.getTime() <= 0:
                worksheet.write('J' + str(index), 'None')
                worksheet.write('L' + str(index), 'None')
                worksheet.write('M' + str(index), 'None')
                worksheet.write('O' + str(index), 'None')
                flag = False
        workbook.close()





































