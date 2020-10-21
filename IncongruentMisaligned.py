import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from MenAlign import Men_Align
from WomenAlign import Women_Align
import Config
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
    def IncongruentMisaligned(self, practice, same, gender, index, block):
        generalTimer = core.getTime()

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
        localtimer = core.getTime()
        Config.practiceDuration += localtimer - generalTimer
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
        core.wait(0.5)

        if gender:
            images = men_misalign_images
            locations = men_misalign_locations
        else:
            images = women_misalign_images
            locations = women_misalign_locations
        secondfacedifflist = []
        secondfacesamelist = []
        timerlist = []
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

            core.wait(0.2)
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

            core.wait(0.2)
            secondfacedifflist[0].autoDraw = False
            questionMark.draw()
            win.flip()

        # countdown = core.CountdownTimer(1.5)
        time = core.Clock()
        isCorrectAns = False
        anslist = []
        keytimerlist = []
        flag = True
        while flag:
            keys = event.waitKeys(keyList=['a', 'l'], timeStamped=time)
            if keys:
                print(keys[0][1])
                keytimerlist.append(keys[0][1] + 0.2)
                if keys[0][0] == 'l':
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
                        anslist.append('L')
                    isCorrectAns = True if same else False
                    flag = False
                elif keys[0][0] == 'a':
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
                        anslist.append('A')
                    isCorrectAns = False if same else True
                    flag = False
        #     elif countdown.getTime() <= 0:
        #         if practice:
        #             wrong.draw()
        #             win.flip()
        #             core.wait(2)
        #         isLate = True
        #         flag = False
        #
        questionMark.autoDraw = False
        win.flip()
        core.wait(1)

        if not practice:
            if anslist:
                accuracy = '1' if isCorrectAns else '0'
            else:
                accuracy = 'None'
            ans = anslist[0].upper() if anslist else 'None'
            rtime = keytimerlist[0]
            genders = 'Male' if gender else 'Female'
            condition = '2' if same else '3'
            trialstart = Config.practiceDuration
            cor_ans = 'L' if same else 'A'
            keyrespstart = Config.practiceDuration + keytimerlist[0]  if anslist else 'None'
            face1 = men_align_images[rand1].image[-13:-4] if gender else women_align_images[rand1].image[-13:-4]

            if same:
                face2 = secondfacesamelist[0].image[-13:-4]
            else:
                face2 = secondfacedifflist[0].image[-13:-4]

            Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                       'Type', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

            toWrite = {'Alignment': '0', 'Condition': condition, 'Cor-Ans': cor_ans,
                       'Key-Resp': ans, 'R-time': rtime, 'Block': block,
                       'Face_Gender': genders, 'Face_1': face1,
                       'Face_2': face2,'Trial': index,
                       'Trial-Start': str(trialstart), 'Congruency': '0',
                       'Type': 'Misaligned Incongruent', 'Accuracy': accuracy, 'Key-Resp-Start': keyrespstart}

            Config.append_dict_as_row(Config.filename, dict_of_elem=toWrite, headers=Headers)
            if anslist:
                Config.practiceDuration += keytimerlist[0]