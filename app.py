from CongruentAligned import Congruent_Aligned
from CongruentMisaligned import Congruent_Misaligned
from IncongruentAligned import Incongruent_Aligned
from IncongruentMisaligned import Incongruent_Misaligned
from PracticeTrials import PracticeTrials
from MainAssets import MainAssets
from psychopy import event
from DialogueBox import dialoguebox
import os

from Window import window
import random

win = window().win
images = MainAssets()
firstInstruction = images.firstInstructionImage
secondInstruction = images.secondInstructionImage
practiceInstruction = images.practiceSecondInstructionImage

event.globalKeys.clear()
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

m_counter = 0
f_counter = 0

typeOneDone = False
typeTwoDone = False
typeThreeDone = False
typeFourDone = False

# firstInstruction.draw()
# win.flip()
# flag = True
# while flag:
#     keys = event.getKeys(keyList=['m'])
#     for key in keys:
#         if key[0] == 'm':
#             firstInstruction.autoDraw = False
#             practiceInstruction.draw()
#             win.flip()
#             flag = False
#
# flag = True
# while flag:
#     keys = event.getKeys(keyList=['m'])
#     for key in keys:
#         if key[0] == 'm':
#             practiceInstruction.autoDraw = False
#             win.flip()
#             flag = False
#
# PracticeTrials().Practice_Trials()
#
# secondInstruction.draw()
# win.flip()
# flag = True
# while flag:
#     keys = event.getKeys(keyList=['m'])
#     for key in keys:
#         if key[0] == 'm':
#             secondInstruction.autoDraw = False
#             win.flip()
#             flag = False

while True:
    # mainrandom = random.randint(1, 4)
    mainrandom = 2
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

        for i in range(1, 11):
            gender_random = 0
            # gender_random = random.randint(0, 100) % 2
            # 0 -> female, 1 -> male
            # samerandom = random.randint(0, 100) % 2
            samerandom = 0
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
                Congruent_Aligned().CongruentSameAlignedMale(practice=0)

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Congruent_Aligned().CongruentSameAlignedFemale(practice=0)

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Congruent_Aligned().CongruentDifferentAlignedMale(practice=0)

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Congruent_Aligned().CongruentDifferentAlignedFemale(practice=0)
        typeOneDone = True

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
                Congruent_Misaligned().CongruentSameMisalignedMale(practice=0)

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Congruent_Misaligned().CongruentSameMisalignedFemale(practice=0)

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Congruent_Misaligned().CongruentDifferentMisalignedMale(practice=0)

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Congruent_Misaligned().CongruentDifferentMisalignedFemale(practice=0)
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
                Incongruent_Aligned().IncongruentSameAlignedMale(practice=0)

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Incongruent_Aligned().IncongruentSameAlignedFemale(practice=0)

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Incongruent_Aligned().IncongruentDifferentAlignedMale(practice=0)

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Incongruent_Aligned().IncongruentDifferentAlignedFemale(practice=0)
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
                Incongruent_Misaligned().IncongruentSameMisalignedMale(practice=0)

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Incongruent_Misaligned().IncongruentSameMisalignedFemale(practice=0)

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Incongruent_Misaligned().IncongruentDifferentMisalignedMale(practice=0)

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Incongruent_Misaligned().IncongruentDifferentMisalignedFemale(practice=0)
        typeFourDone = True




