import random

import csv
from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from DifferentTotalLocationsList import DifferentTotalLocationsList




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
    def CongruentAligned(self, practice, index, gender, same, practiceDuration):

        generalTimer = core.getTime()






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
        localtimer = core.getTime()
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

                win.flip()
                core.wait(0.5)
                men_align_images[rand1].autoDraw = False
                questionMark.draw()
                win.flip()
            else:
                women_align_images[rand1].draw()
                print(women_align_images[rand1].image)
                # worksheet.write('B' + str(index), women_align_images[rand1].image[-13:-4])

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
                            anslist.append('A')

                            # worksheet.write('J' + str(index), 'A')

                            # worksheet.write('L' + str(index), '=IF(K' + str(index) + '= J' +
                            #                 str(index) + ',1,0)')

                            # worksheet.write('M' + str(index), str(1.5 - countdown.getTime()))
                            # data["M"] = str(1.5 - countdown.getTime())
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            anslist.append('L')
                            # worksheet.write('J' + str(index), 'L')

                            # worksheet.write('L' + str(index), '=IF(K' + str(index) + '= J' +
                            #                 str(index) + ',1,0)')

                            # worksheet.write('M' + str(index), str(1.5 - countdown.getTime()))

                        flag = False
            elif countdown.getTime() <= 0:
                lateflag = True
                # worksheet.write('J' + str(index), 'None')
                # worksheet.write('L' + str(index), 'None')
                # worksheet.write('M' + str(index), 'None')
                # worksheet.write('O' + str(index), 'None')

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


        with open('CongruentAligned' + str(index) + '.csv', 'w', newline='') as file:
            Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                       'Type', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

            writer = csv.DictWriter(file, fieldnames=Headers)
            writer.writeheader()

            if same and gender:
                writer.writerow({'Alignment': '1', 'Condition': 'Top Same + Bottom Same', 'Cor-Ans': 'A',
                                  'Key-Resp': str(anslist[0]).upper(), 'R-time': str(1.5 - countdown.getTime()),
                                 'Face_Gender': 'Male', 'Face_1': men_align_images[rand1].image[-13:-4],
                                        'Face_2': men_align_images[rand1].image[-13:-4], 'Trial': str(index),
                                 'Trial-Start': str(localtimer - generalTimer + practiceDuration)})

            if same and not gender:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Same + Bottom Same', 'Cor-Ans': 'A',
                                  'Key-Resp': str(anslist[0]).upper(), 'R-time': str(1.5 - countdown.getTime()),
                                     'Face_Gender': 'Female', 'Face_1': women_align_images[rand1].image[-13:-4],
                                      'Face_2': women_align_images[rand1].image[-13:-4], 'Trial': str(index),
                                     'Trial-Start': str(localtimer - generalTimer + practiceDuration)})
            if not same and gender:
                writer.writerow({'Alignment': '1', 'Condition': 'Top Different + Bottom Different', 'Cor-Ans': 'L',
                                  'Key-Resp': str(anslist[0]).upper(), 'R-time': str(1.5 - countdown.getTime()),'Face_Gender': 'Male', 'Face_1': men_align_images[rand1].image[-13:-4],
                                      'Face_2': secondfacelist[0].image[-13:-4], 'Trial': str(index),
                                 'Trial-Start': str(localtimer - generalTimer + practiceDuration)})

            if not same and not gender:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Different + Bottom Different', 'Cor-Ans': 'L',
                                  'Key-Resp': str(anslist[0]).upper(), 'R-time': str(1.5 - countdown.getTime()),'Face_Gender': 'Female', 'Face_1': women_align_images[rand1].image[-13:-4],
                                      'Face_2': secondfacelist[0].image[-13:-4], 'Trial': str(index),
                                     'Trial-Start': str(localtimer - generalTimer + practiceDuration)})










































