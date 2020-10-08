from CongruentAligned import Congruent_Aligned
from CongruentMisaligned import Congruent_Misaligned
from IncongruentAligned import Incongruent_Aligned
from IncongruentMisaligned import Incongruent_MisAligned

from Window import window
import random

win = window().win

# mainrandom = random.randind(0, 100) % 4
mainrandom = 0



m_counter = 0
f_counter = 0






# CongruentAligned


if mainrandom == 0:

    same_counter = 0
    diff_counter = 0

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
