import random
import Config

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
    def CongruentAligned(self, practice, gender, same, index, block):


        generalTimer = core.getTime()
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
        localtimer = core.getTime()
        Config.practiceDuration += localtimer - generalTimer

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
        core.wait(0.5)

        if gender:
            images = men_align_images
            locations = men_align_locations
        else:
            images = women_align_images
            locations = women_align_locations

        secondfacelist = []
        timerlist = []
        if same:
            if gender:
                men_align_images[rand1].draw()
                win.flip()
                print(men_align_images[rand1].image)
                secondfacelist.append(women_align_images[rand1])
                thistimer = core.getTime()
                timerlist.append(thistimer)
                if not Config.taskversion:
                    core.wait(0.2)
                    men_align_images[rand1].autoDraw = False
                    questionMark.draw()
                    win.flip()
            else:
                women_align_images[rand1].draw()
                win.flip()
                print(women_align_images[rand1].image)
                secondfacelist.append(women_align_images[rand1])
                thistimer = core.getTime()
                timerlist.append(thistimer)
                if not Config.taskversion:
                    core.wait(0.2)
                    women_align_images[rand1].autoDraw = False
                    questionMark.draw()
                    win.flip()
        else:
            newLocations = differentLocationsList.different_total_locations_list(
                locations, images[rand1].image)

            newLocRand = random.randint(0, len(newLocations) - 1)

            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    win.flip()
                    secondfacelist.append(item)
                    print(item.image)
                    break
            thistimer = core.getTime()

            timerlist.append(thistimer)
            if not Config.taskversion:
                core.wait(0.2)
                secondfacelist[0].autoDraw = False
                questionMark.draw()
                win.flip()

        countdown = core.CountdownTimer(1.5)
        time = core.getTime()
        timerlist.append(time)
        anstime = 0

        anslist = []
        keytimerlist = []
        isCorrectAns = False
        flag = True
        while flag:
            if Config.taskversion:
                keys = event.waitKeys(keyList=['a', 'l'], maxWait=2)
            else:
                keys = event.waitKeys(keyList=['a', 'l'], timeStamped=time)
            if keys:
                if Config.taskversion:
                    anstime = 1.5 - countdown.getTime()
                else:
                    now = core.getTime()
                    anstime = keys[0][1] + 0.2
                keytimerlist.append(anstime)
                if keys[0][0] == 'a' and practice:

                    if Config.respversion and same:
                        correct.draw()
                        win.flip()
                        core.wait(2)

                    if Config.respversion and not same:
                        wrong.draw()
                        win.flip()
                        core.wait(2)

                    if not Config.respversion and same:
                        wrong.draw()
                        win.flip()
                        core.wait(2)

                    if not Config.respversion and not same:
                        correct.draw()
                        win.flip()
                        core.wait(2)
                    flag = False

                elif keys[0][0] == 'a' and not practice:
                    anslist.append('A')
                    if same:
                        if Config.respversion:
                            isCorrectAns = True
                        else:
                            isCorrectAns = False
                    elif not same:
                        if Config.respversion:
                            isCorrectAns = False
                        else:
                            isCorrectAns = True

                    flag = False

                if keys[0][0] == 'l' and practice:
                    if Config.respversion and same:
                        wrong.draw()
                        win.flip()
                        core.wait(2)

                    if Config.respversion and not same:
                        correct.draw()
                        win.flip()
                        core.wait(2)

                    if not Config.respversion and same:
                        correct.draw()
                        win.flip()
                        core.wait(2)

                    if not Config.respversion and not same:
                        wrong.draw()
                        win.flip()
                        core.wait(2)
                    flag = False
                elif keys[0][0] == 'l' and not practice:
                    anslist.append('L')
                    if same:
                        if Config.respversion:
                            isCorrectAns = False
                        else:
                            isCorrectAns = True
                    elif not same:
                        if Config.respversion:
                            isCorrectAns = True
                        else:
                            isCorrectAns = False

                    flag = False
            else:
                if practice:
                    print('practice')
                    wrong.draw()
                    win.flip()
                    core.wait(2)
                flag = False

        if Config.taskversion:
            secondfacelist[0].autoDraw = False
            win.flip()
        elif not Config.taskversion:
            questionMark.autoDraw = False
            win.flip()
        core.wait(1)

        if not practice:
            if anslist:
                accuracy = '1' if isCorrectAns else '0'
            else:
                accuracy = 'None'

            ans = anslist[0] if anslist else 'None'
            rtime = anstime if anslist else 'None'
            genders = 'Male' if gender else 'Female'
            condition = '1' if same else '4'
            cor_ans = ''
            if same and Config.respversion:
                cor_ans = 'A'
            if same and not Config.respversion:
                cor_ans = 'L'
            if not same and Config.respversion:
                cor_ans = 'L'
            if not same and not Config.respversion:
                cor_ans = 'A'

            # if index == 1:
            trialstart = Config.practiceDuration
            keyrespstart = Config.practiceDuration
            # else:
            #     trialstart = Config.practiceDuration + 1
            #     keyrespstart = Config.practiceDuration

            if anslist:
                if Config.taskversion:
                    keyrespstart += anstime + 1.050
                else:
                    keyrespstart += anstime + 1.250
            else:
                keyrespstart = 'None'
            face1 = men_align_images[rand1].image[-13:-4] if gender else women_align_images[rand1].image[-13:-4]

            if same:
                face2 = men_align_images[rand1].image[-13:-4] if gender else women_align_images[rand1].image[-13:-4]
            else:
                face2 = secondfacelist[0].image[-13:-4]

            Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                       'Type', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

            toWrite = {'Alignment': '1', 'Condition': condition, 'Cor-Ans': cor_ans,
                       'Key-Resp': ans, 'R-time': rtime, 'Block': block,
                       'Face_Gender': genders, 'Face_1': face1,
                       'Face_2': face2, 'Trial': index,
                       'Trial-Start': str(trialstart), 'Congruency': '1',
                       'Type': 'Aligned Congruent', 'Accuracy': accuracy, 'Key-Resp-Start': keyrespstart}

            Config.append_dict_as_row(Config.filename, dict_of_elem=toWrite, headers=Headers)
            if anslist:
                Config.practiceDuration += anstime + 1
