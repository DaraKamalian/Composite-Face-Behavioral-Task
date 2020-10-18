import random, csv

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from MenAlign import Men_Align
from WomenAlign import Women_Align

image = MainAssets()
correct = image.correct
wrong = image.wrong

from SameUpperLocationsList import SameUpperLocationsList
from SameLowerLocationsList import SameLowerLocationsList

women_misalign_images = Women_Misalign().women_misalign_images
women_misalign_locations = Women_Misalign().women_misalign_locations
men_misalign_images = Men_Misalign().men_misalign_images
men_misalign_locations = Men_Misalign().men_misalign_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations

fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win


class Incongruent_Misaligned(object):
    def IncongruentMisaligned(self, practice, same, gender, index):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        if same:
            if gender:
                print('inc-same-mis-m')
            else:
                print('inc-same-mis-f')
        else:
            if gender:
                print('inc-diff-mis-m')
            else:
                print('inc-diff-mis-f')

        rand1 = random.randint(0, 19)
        if gender:
            men_align_images[rand1].draw()
            print(men_align_images[rand1].image)
            win.flip()
            core.wait(0.2)
        else:
            women_align_images[rand1].draw()
            print(women_align_images[rand1].image)
            win.flip()
            core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        if gender:
            images = men_misalign_images
            locations = men_misalign_locations
        else:
            images = women_misalign_images
            locations = women_misalign_locations
        secondfacedifflist = []
        secondfacesamelist = []
        if same:
            obj = SameUpperLocationsList()
            newLocations = SameUpperLocationsList.SameUpperLocationsList(obj,
                locations, images[rand1].image)

            if len(newLocations) == 1:
                newLocRand = 0
            else:
                newLocRand = random.randint(0, (len(newLocations) - 1))

            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    win.flip()
                    secondfacesamelist.append(item)
                    # print(item.image)
                    break

            core.wait(0.5)
            secondfacesamelist[0].autoDraw = False
            questionMark.draw()
            win.flip()

        else:
            obj = SameLowerLocationsList()
            newLocations = SameLowerLocationsList.SameLowerLocationsList(obj,
                                                                         locations,
                                                                         images[rand1].image)
            if len(newLocations) == 1:
                newLocRand = 0
            else:
                newLocRand = random.randint(0, (len(newLocations) - 1))


            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    secondfacedifflist.append(item)
                    win.flip()
                    print(item.image)
                    break

            core.wait(0.5)
            secondfacedifflist[0].autoDraw = False
            questionMark.draw()
            win.flip()


        countdown = core.CountdownTimer(1.5)
        isCorrectAns = False
        anslist = []
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
                        isCorrectAns = True if same else False
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
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
        condition = 'Top Same + Bottom Different' if same else 'Top Different + Bottom Same'
        cor_ans = 'A' if same else 'L'

        face1 = men_align_images[rand1].image[-13:-4] if gender else women_align_images[rand1].image[-13:-4]

        if same:
            face2 = secondfacesamelist[0].image[-13:-4]
        else:
            face2 = secondfacedifflist[0].image[-13:-4]

        with open('CongruentAligned' + str(index) + '.csv', 'w', newline='') as file:
            Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                       'Type', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

            writer = csv.DictWriter(file, fieldnames=Headers)
            writer.writeheader()

            writer.writerow({'Alignment': '0', 'Condition': condition, 'Cor-Ans': cor_ans,
                             'Key-Resp': ans, 'R-time': str(1.5 - countdown.getTime()),
                             'Face_Gender': genders, 'Face_1': face1,
                             'Face_2': face2, 'Trial-Start': "", 'Congruency': '0',
                             'Type': 'Misaligned Incongruent', 'Accuracy': accuracy})
