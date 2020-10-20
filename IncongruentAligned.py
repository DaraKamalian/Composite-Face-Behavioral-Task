import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from SameUpperLocationsList import SameUpperLocationsList
from SameLowerLocationsList import SameLowerLocationsList
import Config


image = MainAssets()
correct = image.correct
wrong = image.wrong
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
women_misalign_images = Women_Misalign().women_misalign_images
women_misalign_locations = Women_Misalign().women_misalign_locations
men_misalign_images = Men_Misalign().men_misalign_images
men_misalign_locations = Men_Misalign().men_misalign_locations

fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Incongruent_Aligned(object):
    def IncongruentAligned(self, practice, same, gender, index, block):
        generaltimer = core.getTime()
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)


        if same:
            if gender:
                print('inc-same-al-m')
            else:
                print('inc-same-al-f')
        else:
            if gender:
                print('inc-diff-al-m')
            else:
                print('inc-diff-al-f')


        rand1 = random.randint(0, 19)
        localtimer = core.getTime()
        Config.practiceDuration += localtimer - generaltimer
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
            images = men_align_images
            locations = men_align_locations
        else:
            images = women_align_images
            locations = women_align_locations

        secondsamefacelist = []
        seconddifffacelist = []
        if same:
            obj = SameUpperLocationsList()
            newLocations = SameUpperLocationsList.SameUpperLocationsList(obj,
                locations, images[rand1].image)
            print('newlocations length is :' + str(len(newLocations)))

            if len(newLocations) == 1:
                newLocRand = 0
            else:
                newLocRand = random.randint(0, (len(newLocations) - 1))

                print('new loc rand is :' + str(newLocRand))
            # for item in newLocations:
            #     print(item)


            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    win.flip()
                    secondsamefacelist.append(item)
                    # print(item.image)
                    break
            core.wait(0.5)
            secondsamefacelist[0].autoDraw = False
            questionMark.draw()
            win.flip()

        else:
            obj = SameLowerLocationsList()
            newLocations = SameLowerLocationsList.SameLowerLocationsList(obj,
                                                                         locations,
                                                                         images[rand1].image)
            print('newlocations length is :' + str(len(newLocations)))
            if len(newLocations) == 1:
                newLocRand = 0
            else:
                newLocRand = random.randint(0, (len(newLocations) - 1))
                print('new loc rand is :' + str(newLocRand))
            # for item in newLocations:
            #     print(item)

            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    win.flip()
                    seconddifffacelist.append(item)
                    # print(item.image)
                    break
            core.wait(0.5)
            seconddifffacelist[0].autoDraw = False
            questionMark.draw()
            win.flip()

        countdown = core.CountdownTimer(1.5)
        anslist = []
        timerlist = []
        isCorrectAns = False
        flag = True
        while flag:

            keys = event.waitKeys(keyList=['a', 'l'], maxWait=1.5)
            if keys:
                for key in keys:
                    keytimer = core.getTime()
                    timerlist.append(keytimer)
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
                if practice:
                    wrong.draw()
                    win.flip()
                    core.wait(2)
                flag = False

        questionMark.autoDraw = False
        win.flip()
        core.wait(1.5)


        if not practice:
            if anslist:
                accuracy = '1' if isCorrectAns else '0'
            else:
                accuracy = 'None'
            ans = anslist[0].upper() if anslist else 'None'
            rtime = str(1.5 - countdown.getTime()) if anslist else 'None'
            genders = 'Male' if gender else 'Female'
            condition = '2' if same else '3'
            keyrespstart = Config.practiceDuration + timerlist[0] - localtimer if anslist else 'None'
            trialstart = Config.practiceDuration
            cor_ans = 'A' if same else 'L'
            face1 = men_align_images[rand1].image[-13:-4] if gender else women_align_images[rand1].image[-13:-4]

            if same:
                face2 = secondsamefacelist[0].image[-13:-4]
            else:
                face2 = seconddifffacelist[0].image[-13:-4]

            Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                           'Type', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

            toWrite = {'Alignment': '1', 'Condition': condition, 'Cor-Ans': cor_ans,
                       'Key-Resp': ans, 'R-time': rtime, 'Block': block,
                       'Face_Gender': genders, 'Face_1': face1,
                       'Face_2': face2,'Trial': index,
                       'Trial-Start': str(trialstart), 'Congruency': '0',
                       'Type': 'Aligned Incongruent', 'Accuracy': accuracy, 'Key-Resp-Start': keyrespstart}

            Config.append_dict_as_row(Config.filename, dict_of_elem=toWrite, headers=Headers)
            Config.practiceDuration += timerlist[0] - localtimer
