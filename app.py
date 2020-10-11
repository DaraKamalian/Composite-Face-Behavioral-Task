from CongruentAligned import Congruent_Aligned
from CongruentMisaligned import Congruent_Misaligned
from IncongruentAligned import Incongruent_Aligned
from IncongruentMisaligned import Incongruent_Misaligned
from psychopy import event, monitors
from DialogueBox import dialoguebox
import os

from Window import window
import random

win = window().win


# subjectInfo = dialoguebox().showDialogBox()

# mainrandom = random.randint(0, 3)

event.globalKeys.clear()
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

m_counter = 0
f_counter = 0

typeOneDone = False
typeTwoDone = False
typeThreeDone = False
typeFourDone = False

while True:
    mainrandom = random.randint(1, 4)
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
                Congruent_Aligned().CongruentSameAlignedMale()

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Congruent_Aligned().CongruentSameAlignedFemale()

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Congruent_Aligned().CongruentDifferentAlignedMale()

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Congruent_Aligned().CongruentDifferentAlignedFemale()
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
                Congruent_Misaligned().CongruentSameMisalignedMale()

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Congruent_Misaligned().CongruentSameMisalignedFemale()

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Congruent_Misaligned().CongruentDifferentMisalignedMale()

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Congruent_Misaligned().CongruentDifferentMisalignedFemale()
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
                Incongruent_Aligned().IncongruentSameAlignedMale()

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Incongruent_Aligned().IncongruentSameAlignedFemale()

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Incongruent_Aligned().IncongruentDifferentAlignedMale()

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Incongruent_Aligned().IncongruentDifferentAlignedFemale()
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
                Incongruent_Misaligned().IncongruentSameMisalignedMale()

            if samerandom == 1 and gender_random == 0:
                same_counter += 1
                f_counter += 1
                Incongruent_Misaligned().IncongruentSameMisalignedFemale()

            if samerandom == 0 and gender_random == 1:
                diff_counter += 1
                m_counter += 1
                Incongruent_Misaligned().IncongruentDifferentMisalignedMale()

            if samerandom == 0 and gender_random == 0:
                diff_counter += 1
                f_counter += 1
                Incongruent_Misaligned().IncongruentDifferentMisalignedFemale()
        typeFourDone = True




