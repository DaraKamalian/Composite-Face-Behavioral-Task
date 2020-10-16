from CongruentAligned import Congruent_Aligned
from CongruentMisaligned import Congruent_Misaligned
from IncongruentAligned import Incongruent_Aligned
from IncongruentMisaligned import Incongruent_Misaligned
from PracticeTrials import PracticeTrials
from MainAssets import MainAssets
from psychopy import event
from Data import Data
from DialogueBox import dialoguebox
import os

from Window import window
import random

win = window().win
images = MainAssets()
firstInstruction = images.firstInstructionImage
secondInstruction = images.secondInstructionImage
practiceInstruction = images.practiceSecondInstructionImage


obj2 = Data()
subjectInfoList = dialoguebox().showDialogBox()


workbook = Data.setupExcelFile(obj2, subjectInfoList)[0]
worksheet = Data.setupExcelFile(obj2, subjectInfoList)[1]

event.globalKeys.clear()
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

m_counter = 0
f_counter = 0

typeOneDone = False
typeTwoDone = False
typeThreeDone = False
typeFourDone = False

firstInstruction.draw()
win.flip()
flag = True
while flag:
    keys = event.getKeys(keyList=['m'])
    for key in keys:
        if key[0] == 'm':
            firstInstruction.autoDraw = False
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

secondInstruction.draw()
win.flip()
flag = True
while flag:
    keys = event.getKeys(keyList=['m'])
    for key in keys:
        if key[0] == 'm':
            secondInstruction.autoDraw = False
            win.flip()
            flag = False

while True:
    mainrandom = random.randint(1, 4)
    # mainrandom = 1
    print('main random: ' + str(mainrandom))

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


    # Congruent Aligned
    if mainrandom == 1:

        same_counter = 0
        diff_counter = 0

        m_counter = 0
        f_counter = 0
        globalcounter = 0

        for i in range(1, 11):

            gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            # samerandom = random.randint(0, 100) % 2
            samerandom = 1

            # if samerandom == 0 and diff_counter == 5:
            #     samerandom = 1
            # if samerandom == 1 and same_counter == 5:
            #     samerandom = 0
            #
            # if gender_random == 0 and f_counter == 5:
            #     gender_random = 1
            # if gender_random == 1 and m_counter == 5:
            #     gender_random = 0

            if samerandom == 1 and gender_random == 1:
                same_counter += 1
                m_counter += 1
                globalcounter += 1
                Congruent_Aligned().CongruentAligned(practice=0, index=i+9+globalcounter,
                                                             subjectInfoList=subjectInfoList, same=1, gender=1)

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                globalcounter += 1
                Congruent_Aligned().CongruentAligned(practice=0, index=i+9+globalcounter,
                                                               subjectInfoList=subjectInfoList,same=1, gender=0)

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                globalcounter += 1
                Congruent_Aligned().CongruentAligned(practice=0, index=i+9+globalcounter,
                                                     subjectInfoList=subjectInfoList, same=0, gender=1)

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                globalcounter += 1
                Congruent_Aligned().CongruentAligned(practice=0, index=i+9+globalcounter,
                                                    subjectInfoList=subjectInfoList, same=0, gender=0)
        typeOneDone = True
    workbook.close()



    # Congruent Misaligned
    if mainrandom == 2:
        same_counter = 0
        diff_counter = 0

        m_counter = 0
        f_counter = 0

        for i in range(1, 11):
            gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            samerandom = random.randint(0, 100) % 2
            if samerandom == 0 and diff_counter == 5:
                samerandom = 1
            if samerandom == 1 and same_counter == 5:
                samerandom = 0

            if gender_random == 0 and f_counter == 5:
                gender_random = 1
            if gender_random == 1 and m_counter == 5:
                gender_random = 0

            if samerandom == 1 and gender_random == 1:
                same_counter += 1
                m_counter += 1
                Congruent_Misaligned().CongruentMisaligned(practice=0, same=1, gender=1)

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Congruent_Misaligned().CongruentMisaligned(practice=0, same=1, gender=0)

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Congruent_Misaligned().CongruentMisaligned(practice=0, same=0, gender=1)

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Congruent_Misaligned().CongruentMisaligned(practice=0, same=0, gender=0)
        typeTwoDone = True

    # Incongruent Aligned
    if mainrandom == 3:
        same_counter = 0
        diff_counter = 0

        m_counter = 0
        f_counter = 0

        for i in range(1, 11):
            gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            samerandom = random.randint(0, 100) % 2
            if samerandom == 0 and diff_counter == 5:
                samerandom = 1
            if samerandom == 1 and same_counter == 5:
                samerandom = 0

            if gender_random == 0 and f_counter == 5:
                gender_random = 1
            if gender_random == 1 and m_counter == 5:
                gender_random = 0

            if samerandom == 1 and gender_random == 1:
                same_counter += 1
                m_counter += 1
                Incongruent_Aligned().IncongruentAligned(practice=0, same=1, gender=1)

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Incongruent_Aligned().IncongruentAligned(practice=0, same=1, gender=0)

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Incongruent_Aligned().IncongruentAligned(practice=0, same=0, gender=1)

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Incongruent_Aligned().IncongruentAligned(practice=0, same=0, gender=0)
        typeThreeDone = True

    #Incongruent Misaligned
    if mainrandom == 4:
        same_counter = 0
        diff_counter = 0

        m_counter = 0
        f_counter = 0

        for i in range(1, 11):
            gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            samerandom = random.randint(0, 100) % 2
            if samerandom == 0 and diff_counter == 5:
                samerandom = 1
            if samerandom == 1 and same_counter == 5:
                samerandom = 0

            if gender_random == 0 and f_counter == 5:
                gender_random = 1
            if gender_random == 1 and m_counter == 5:
                gender_random = 0

            if samerandom == 1 and gender_random == 1:
                same_counter += 1
                m_counter += 1
                Incongruent_Misaligned().IncongruentMisaligned(practice=0, same=1, gender=1)

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Incongruent_Misaligned().IncongruentMisaligned(practice=0, same=1, gender=0)

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Incongruent_Misaligned().IncongruentMisaligned(practice=0, same=0, gender=1)

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Incongruent_Misaligned().IncongruentMisaligned(practice=0, same=0, gender=0)
        typeFourDone = True



