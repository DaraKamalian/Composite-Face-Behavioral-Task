import random
import Config
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
    duration = 0
    def CongruentAligned(self, practice, gender, same):

        generalTimer = core.getTime()
        fixationPoint.draw()
        win.flip()

        core.wait(0.2)
        fixationPoint.autoDraw = False
        win.flip()
        localtimer = core.getTime()
        Config.time += localtimer - generalTimer
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

                win.flip()
                core.wait(0.5)
                men_align_images[rand1].autoDraw = False
                questionMark.draw()
                win.flip()
            else:
                women_align_images[rand1].draw()
                print(women_align_images[rand1].image)


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
                    break
            core.wait(0.5)
            secondfacelist[0].autoDraw = False
            questionMark.draw()
            win.flip()

        countdown = core.CountdownTimer(1.5)

        anslist = []
        isCorrectAns = False
        flag = True
        while flag:

            keys = event.waitKeys(keyList=['a', 'l'], maxWait=1.5)
            if keys:
                for key in keys:
                    if key == 'a':
                        if practice:
                            if same:
                                correct.draw()
                                win.flip()
                                core.wait(2)
                            else:
                                wrong.draw()
                                win.flip()
                                core.wait(2)
                        else:
                            anslist.append('A')
                        isCorrectAns = True if same else False
                        flag = False
                    elif key == 'l':
                        if practice:
                            if same:
                                wrong.draw()
                                win.flip()
                                core.wait(2)
                            else:
                                correct.draw()
                                win.flip()
                                core.wait(2)
                        else:
                            anslist.append('L')
                        isCorrectAns = False if same else True
                        flag = False
            elif countdown.getTime() <= 0:
                isLate = True
                flag = False

        accuracy = '1' if isCorrectAns else '0'
        ans = anslist[0].upper() if anslist else 'None'
        genders = 'Male' if gender else 'Female'
        condition = 'Top Same + Bottom Same' if same else 'Top Different + Bottom Different'
        images = men_align_images if gender else women_align_images
        cor_ans = 'A' if same else 'L'

        ran = random.randint(1, 10)
        with open('CongruentAligned' + str(ran) + '.csv', 'w', newline='') as file:
            Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                       'Type', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']


            writer = csv.DictWriter(file, fieldnames=Headers)
            writer.writeheader()

            writer.writerow({'Alignment': '1', 'Condition': condition, 'Cor-Ans': cor_ans,
                             'Key-Resp': ans, 'R-time': str(1.5 - countdown.getTime()),
                             'Face_Gender': genders, 'Face_1': images[rand1].image[-13:-4],
                             'Face_2': images[rand1].image[-13:-4],
                             'Trial-Start': Config.time, 'Congruency': '1',
                             'Type': 'Aligned Congruent', 'Accuracy': accuracy})












































