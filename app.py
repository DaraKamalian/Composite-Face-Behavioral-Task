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

typeonecounter = 0
typetwocounter = 0
typethreecounter = 0
typefourcounter = 0

for filename in glob.glob('./*.csv'):
    os.remove(filename)

drawlist = []
timer1 = core.getTime()
if Config.appversion and Config.respversion:
    secondversion_SameA_firstInstruction.draw()
    drawlist.append(secondversion_SameA_firstInstruction)
if Config.appversion and not Config.respversion:
    secondversion_SameL_firstInstruction.draw()
    drawlist.append(secondversion_SameL_firstInstruction)
if not Config.appversion and Config.respversion:
    firstversion_SameA_firstInstruction.draw()
    drawlist.append(firstversion_SameA_firstInstruction)
if not Config.appversion and not Config.respversion:
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

Config.practiceDuration = (timer2 - timer1)
# Config.practiceDuration = 60
if Config.appversion:
    Config.filename = subjectInfoList[0] + subjectInfoList[1] + '.' + 'D' + subjectInfoList[5] + '.T2.csv'
else:
    Config.filename = subjectInfoList[0] + subjectInfoList[1] + '.' + 'D' + subjectInfoList[5] + '.T1.csv'
Config.createFile(Config.filename)

# Block counter
for index in range(1, 5):

    typeonecounter = 0
    typetwocounter = 0
    typethreecounter = 0
    typefourcounter = 0

    typeOneDone = False
    typeTwoDone = False
    typeThreeDone = False
    typeFourDone = False

    m_counter = 0
    f_counter = 0

    for i in range(1, 41):
        i += 40 * (index - 1)
        mainrandom = random.randint(1, 4)
        # mainrandom = 1
        print('main random: ' + str(mainrandom))

        if typeonecounter == 10:
            typeOneDone = True

        if typetwocounter == 10:
            typeTwoDone = True

        if typethreecounter == 10:
            typeThreeDone = True

        if typefourcounter == 10:
            typeFourDone = True

        if mainrandom == 1 and typeOneDone:
            mainrandom = 2
        if mainrandom == 2 and typeTwoDone:
            mainrandom = 3
        if mainrandom == 3 and typeThreeDone:
            mainrandom = 4
        if mainrandom == 4 and typeFourDone:

            if not typeOneDone:
                mainrandom = 1
            elif not typeTwoDone:
                mainrandom = 2
            elif not typeThreeDone:
                mainrandom = 3
            else:
                break

        respversion = subjectInfoList[7]
        taskversion = subjectInfoList[8]

        # Congruent Aligned
        if mainrandom == 1:

            same_counter = 0
            diff_counter = 0
            typeonecounter += 1

            globalcounter = 0

            gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            samerandom = random.randint(0, 100) % 2
            # samerandom = 1

            if not samerandom and diff_counter == 5:
                samerandom = 1
                same_counter += 1
            if samerandom and same_counter == 5:
                samerandom = 0
                diff_counter += 1

            if gender_random and m_counter == 5:
                gender_random = 0
            elif not gender_random and f_counter == 5:
                gender_random = 1

            if gender_random:
                m_counter += 1
            else:
                f_counter += 1

            Congruent_Aligned().CongruentAligned(practice=0, same=samerandom, gender=gender_random, index=i,
                                                 block=index,
                                                 appversion=taskversion, respversion=respversion)

        # Congruent Misaligned
        if mainrandom == 2:
            same_counter = 0
            diff_counter = 0
            typetwocounter += 1

            # for i in range(1, 11):
            gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            samerandom = random.randint(0, 100) % 2

            if not samerandom and diff_counter == 5:
                samerandom = 1
                same_counter += 1
            if samerandom and same_counter == 5:
                samerandom = 0
                diff_counter += 1

            if gender_random and m_counter == 5:
                gender_random = 0
            elif not gender_random and f_counter == 5:
                gender_random = 1

            if gender_random:
                m_counter += 1
            else:
                f_counter += 1

            Congruent_Misaligned().CongruentMisaligned(practice=0, same=samerandom, gender=gender_random, index=i,
                                                       block=index, appversion=taskversion, respversion=respversion)

        # Incongruent Aligned
        if mainrandom == 3:
            same_counter = 0
            diff_counter = 0
            typethreecounter += 1

            gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            samerandom = random.randint(0, 100) % 2
            if not samerandom and diff_counter == 5:
                samerandom = 1
                same_counter += 1
            if samerandom and same_counter == 5:
                samerandom = 0
                diff_counter += 1

            if gender_random and m_counter == 5:
                gender_random = 0
            elif not gender_random and f_counter == 5:
                gender_random = 1

            if gender_random:
                m_counter += 1
            else:
                f_counter += 1

            Incongruent_Aligned().IncongruentAligned(practice=0, same=samerandom, gender=gender_random, index=i,
                                                     block=index, appversion=taskversion, respversion=respversion)

        # Incongruent Misaligned
        if mainrandom == 4:
            same_counter = 0
            diff_counter = 0
            typefourcounter += 1

            # for i in range(1, 11):
            gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            samerandom = random.randint(0, 100) % 2
            if not samerandom and diff_counter == 5:
                samerandom = 1
                same_counter += 1
            if samerandom and same_counter == 5:
                samerandom = 0
                diff_counter += 1

            if gender_random and m_counter == 5:
                gender_random = 0
            elif not gender_random and f_counter == 5:
                gender_random = 1

            if gender_random:
                m_counter += 1
            else:
                f_counter += 1

            Incongruent_Misaligned().IncongruentMisaligned(practice=0, same=samerandom, gender=gender_random, index=i,
                                                           block=index, appversion=taskversion, respversion=respversion)

    if index < 4:
        betweenblockinstruction.draw()
        win.flip()
        flag = True
        while flag:
            keys = event.waitKeys(keyList=['m'])
            for key in keys:
                if key[0] == 'm':
                    betweenblockinstruction.autoDraw = False
                    win.flip()
                    flag = False

respversion = 'Same-A' if subjectInfoList[7] else 'Same-L'
appversion = 'Second Face Remains' if subjectInfoList[8] else 'Second Face Disappears'
Config.append_list_as_row(Config.filename, ['Subject Name: ' + str(subjectInfoList[0]),
                                            'Subject Number: ' + str(subjectInfoList[1]),
                                            'Age: ' + str(subjectInfoList[2]), 'Gender: ' + str(subjectInfoList[3]),
                                            'Handedness: ' + str(subjectInfoList[4]),
                                            'Stimulation Site: ' + str(subjectInfoList[6]),
                                            'Resp-Version: ' + respversion,
                                            'Task Version: ' + appversion,
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
