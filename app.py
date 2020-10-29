from CongruentAligned import Congruent_Aligned
from CongruentMisaligned import Congruent_Misaligned
from IncongruentAligned import Incongruent_Aligned
from IncongruentMisaligned import Incongruent_Misaligned
from PracticeTrials import PracticeTrials
from MainAssets import MainAssets
from psychopy import event, core
from EndMessage import EndMessage

from DialogueBox import dialoguebox
import os, csv, glob, datetime, Config
import pandas as pd

from Window import window
import random

win = window().win
images = MainAssets()
firstversion_SameA_firstInstruction = images.firstversion_SameA_firstInstructionImage
firstversion_SameL_firstInstruction = images.firstversion_SameL_firstInstructionImage

secondversion_SameA_firstInstruction = images.secondversion_SameA_firstInstructionImage
secondversion_SameL_firstInstruction = images.secondversion_SameL_firstInstructionImage

secondInstruction_SameL = images.secondInstruction_SameL_Image
secondInstruction_SameA = images.secondInstruction_SameA_Image

betweenblockinstruction = images.between_block_instruction
practiceInstruction = images.practiceSecondInstructionImage

subjectInfoList = dialoguebox().showDialogBox()

event.globalKeys.clear()
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

for filename in glob.glob('./*.csv'):
    os.remove(filename)

drawlist = []
timer1 = core.getTime()
if Config.taskversion and Config.respversion:
    secondversion_SameA_firstInstruction.draw()
    drawlist.append(secondversion_SameA_firstInstruction)

if Config.taskversion and not Config.respversion:
    secondversion_SameL_firstInstruction.draw()
    drawlist.append(secondversion_SameL_firstInstruction)

if not Config.taskversion and Config.respversion:
    firstversion_SameA_firstInstruction.draw()
    drawlist.append(firstversion_SameA_firstInstruction)

if not Config.taskversion and not Config.respversion:
    firstversion_SameL_firstInstruction.draw()
    drawlist.append(firstversion_SameL_firstInstruction)
win.flip()
flag = True
while flag:
    keys = event.getKeys(keyList=['m'])
    for key in keys:
        if key[0] == 'm':
            drawlist[0].autoDraw = False
            practiceInstruction.draw()
            win.flip()
            flag = False

flag = True
while flag:
    keys = event.getKeys(keyList=['m'])
    for key in keys:
        if key[0] == 'm':
            practiceInstruction.autoDraw = False
            win.flip()
            flag = False

PracticeTrials().Practice_Trials()
seconddrawlist = []
if Config.respversion:
    secondInstruction_SameA.draw()
    seconddrawlist.append(secondInstruction_SameA)
if not Config.respversion:
    secondInstruction_SameL.draw()
    seconddrawlist.append(secondInstruction_SameL)
win.flip()
flag = True
while flag:
    keys = event.getKeys(keyList=['m'])
    for key in keys:
        if key[0] == 'm':
            seconddrawlist[0].autoDraw = False
            win.flip()
            flag = False

timer2 = core.getTime()
Config.practiceFinished = timer2

Config.practiceDuration = (timer2 - timer1)
# Config.practiceDuration = 100
if Config.taskversion:
    Config.filename = subjectInfoList[0] + '.' + subjectInfoList[1] + subjectInfoList[2] + '.' + 'D' + \
                      subjectInfoList[6] + '.T2.csv'
else:
    Config.filename = subjectInfoList[0] + '.' + subjectInfoList[1] + subjectInfoList[2] + '.' + 'D' + subjectInfoList[
        6] \
                      + '.T1.csv'
Config.createFile(Config.filename)

# Block counter
for index in range(1, 5):

    type1counter = 0
    type2counter = 0
    type3counter = 0
    type4counter = 0
    type5counter = 0
    type6counter = 0
    type7counter = 0
    type8counter = 0



    onemale = 0
    onefemale = 0
    twomale = 0
    twofemale = 0
    threemale = 0
    threefemale = 0
    fourmale = 0
    fourfemale = 0
    fivemale = 0
    fivefemale = 0
    sixmale = 0
    sixfemale = 0
    sevenmale = 0
    sevenfemale = 0
    eightmale = 0
    eightfemale = 0

    for i in range(1, 41):
        i += 40 * (index - 1)
        mainrandom = random.randint(1, 8)
        print('main random: ' + str(mainrandom))

        if mainrandom == 1 and type1counter == 5:
            mainrandom = 2
        if mainrandom == 2 and type2counter == 5:
            mainrandom = 3
        if mainrandom == 3 and type3counter == 5:
            mainrandom = 4
        if mainrandom == 4 and type4counter == 5:
            mainrandom = 5
        if mainrandom == 5 and type5counter == 5:
            mainrandom = 6
        if mainrandom == 6 and type6counter == 5:
            mainrandom = 7
        if mainrandom == 7 and type7counter == 5:
            mainrandom = 8
        if mainrandom == 8 and type8counter == 5:

            if type7counter < 5:
                mainrandom = 7
            elif type6counter < 5:
                mainrandom = 6
            elif type5counter < 5:
                mainrandom = 5
            if type4counter < 5:
                mainrandom = 4
            if type3counter < 5:
                mainrandom = 3
            elif type2counter < 5:
                mainrandom = 2
            elif type1counter < 5:
                mainrandom = 1

        same_counter = 0
        diff_counter = 0

        samerandom = random.randint(0, 100) % 2

        if not samerandom and diff_counter == 20:
            samerandom = 1
            same_counter += 1
        if samerandom and same_counter == 20:
            samerandom = 0
            diff_counter += 1

        # Congruent Aligned
        if mainrandom == 1:

            gender_random = random.randint(0, 100) % 2

            if gender_random == 1 and onemale == 3:
                gender_random = 0
            elif gender_random == 0 and onefemale == 2:
                gender_random = 1

            if gender_random:
                onemale += 1
            else:
                onefemale += 1

            Congruent_Aligned().CongruentAligned(practice=0, same=1, gender=gender_random, index=i,
                                                 block=index)
            type1counter += 1

        if mainrandom == 2:

            gender_random = random.randint(0, 100) % 2

            if gender_random == 1 and twomale == 2:
                gender_random = 0
            elif gender_random == 0 and twofemale == 3:
                gender_random = 1

            if gender_random:
                twomale += 1
            else:
                twofemale += 1

            Congruent_Aligned().CongruentAligned(practice=0, same=0, gender=gender_random, index=i,
                                                 block=index)
            type2counter += 1

        # Congruent Misaligned
        if mainrandom == 3:

            gender_random = random.randint(0, 100) % 2

            if gender_random == 1 and threemale == 3:
                gender_random = 0
            elif gender_random == 0 and threefemale == 2:
                gender_random = 1

            if gender_random:
                threemale += 1
            else:
                threefemale += 1

            Congruent_Misaligned().CongruentMisaligned(practice=0, same=1, gender=gender_random, index=i,
                                                 block=index)
            type3counter += 1

        # Incongruent Misaligned
        if mainrandom == 4:

            gender_random = random.randint(0, 100) % 2

            if gender_random == 1 and fourmale == 2:
                gender_random = 0
            elif gender_random == 0 and fourfemale == 3:
                gender_random = 1

            if gender_random:
                fourmale += 1
            else:
                fourfemale += 1

            Congruent_Misaligned().CongruentMisaligned(practice=0, same=0, gender=gender_random, index=i,
                                                       block=index)

            type4counter += 1

        # Incongruent Aligned
        if mainrandom == 5:

            gender_random = random.randint(0, 100) % 2

            if gender_random == 1 and fivemale == 3:
                gender_random = 0
            elif gender_random == 0 and fivefemale == 2:
                gender_random = 1

            if gender_random:
                fivemale += 1
            else:
                fivefemale += 1

            Incongruent_Aligned().IncongruentAligned(practice=0, same=1, gender=gender_random, index=i,
                                                       block=index)
            type5counter += 1

        # Incongruent Aligned
        if mainrandom == 6:

            gender_random = random.randint(0, 100) % 2

            if gender_random == 1 and sixmale == 2:
                gender_random = 0
            elif gender_random == 0 and sixfemale == 3:
                gender_random = 1

            if gender_random:
                sixmale += 1
            else:
                sixfemale += 1

            Incongruent_Aligned().IncongruentAligned(practice=0, same=0, gender=gender_random, index=i,
                                                     block=index)
            type6counter += 1

        # Incongruent Aligned
        if mainrandom == 7:

            gender_random = random.randint(0, 100) % 2

            if gender_random == 1 and sevenmale == 3:
                gender_random = 0
            elif gender_random == 0 and sevenfemale == 2:
                gender_random = 1

            if gender_random:
                sevenmale += 1
            else:
                sevenfemale += 1
            Incongruent_Misaligned().IncongruentMisaligned(practice=0, same=1, gender=gender_random, index=i,
                                                     block=index)
            type7counter += 1

        # Incongruent Aligned
        if mainrandom == 8:

            gender_random = random.randint(0, 100) % 2

            if gender_random == 1 and eightmale == 2:
                gender_random = 0
            elif gender_random == 0 and eightfemale == 3:
                gender_random = 1

            if gender_random:
                eightmale += 1
            else:
                eightfemale += 1
            Incongruent_Misaligned().IncongruentMisaligned(practice=0, same=0, gender=gender_random, index=i,
                                                           block=index)
            type8counter += 1

    if index < 4:
        betweenblockinstruction.draw()
        win.flip()
        t1 = core.getTime()
        flag = True
        while flag:
            keys = event.waitKeys(keyList=['m'])
            for key in keys:
                if key[0] == 'm':
                    betweenblockinstruction.autoDraw = False
                    win.flip()
                    t2 = core.getTime()
                    Config.practiceDuration += t2 - t1
                    flag = False

respversion = 'Same-A' if Config.respversion else 'Same-L'
taskversion = '2' if Config.taskversion else '1'
Config.append_list_as_row(Config.filename, ['Subject Name: ' + str(subjectInfoList[0]) + ' ' + str(subjectInfoList[1]),
                                            'Subject Number: ' + str(subjectInfoList[2]),
                                            'Age: ' + str(subjectInfoList[3]), 'Gender: ' + str(subjectInfoList[4]),
                                            'Handedness: ' + str(subjectInfoList[5]),
                                            'Stimulation Site: ' + str(subjectInfoList[7]),
                                            'Resp-Version: ' + respversion,
                                            'Task Version: ' + taskversion,
                                            'Experiment Day: ' + subjectInfoList[6],
                                            'Datetime: ' + str(datetime.datetime.today())])

for filename in glob.glob('./Congruent*.csv'):
    os.remove(filename)
for filename in glob.glob('./Incongruent*.csv'):
    os.remove(filename)

Config.convertToExcel()
for filename in glob.glob('./*.csv'):
    os.remove(filename)
EndMessage().displayEndMessage()
core.quit()
