import random
import xlsxwriter

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from CongruentAligned import Congruent_Aligned
from CongruentMisaligned import Congruent_Misaligned
from IncongruentAligned import Incongruent_Aligned
from IncongruentMisaligned import Incongruent_Misaligned

from MenAlign import Men_Align
from WomenAlign import Women_Align
from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign

women_misalign_images = Women_Misalign().women_misalign_images
women_misalign_locations = Women_Misalign().women_misalign_locations
men_misalign_images = Men_Misalign().men_misalign_images
men_misalign_locations = Men_Misalign().men_misalign_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations

correct = MainAssets().correct
wrong = MainAssets().wrong

win = window.win

class PracticeTrials(object):
    def Practice_Trials(self):
        for index in range(1, 9):
            diff_counter = 0
            same_counter = 0
            m_counter = 0
            f_counter = 0

            same_random = random.randint(0, 100) % 2
            gender_random = random.randint(0, 100) % 2
            typerandom = random.randint(1, 4)


            if not same_random and diff_counter == 8:
                same_random = 1
            if same_random and same_counter == 8:
                same_random = 0

            if not gender_random and f_counter == 8:
                gender_random = 1
            if gender_random and m_counter == 8:
                gender_random = 0

            #Congruent Aligned
            if typerandom == 1:
                if not same_random and not gender_random:
                    f_counter += 1
                    diff_counter += 1
                    for i in range(0, 2):
                        Congruent_Aligned().CongruentDifferentAlignedFemale(practice=1)

                if not same_random and gender_random:
                    m_counter += 1
                    diff_counter += 1
                    for i in range(0, 2):
                        Congruent_Aligned().CongruentDifferentAlignedFemale(practice=1)

                if same_random and not gender_random:
                    f_counter += 1
                    same_counter += 1
                    for i in range(0, 2):
                        Congruent_Aligned().CongruentSameAlignedFemale(practice=1)

                if same_random and gender_random:
                    m_counter += 1
                    same_counter += 1
                    for i in range(0, 2):
                        Congruent_Aligned().CongruentSameAlignedMale(practice=1)

            #Congruent Misaligned
            if typerandom == 2:
                if not same_random and not gender_random:
                    f_counter += 1
                    diff_counter += 1
                    for i in range(0, 2):
                        Congruent_Misaligned().CongruentDifferentMisalignedFemale(practice=1)

                if not same_random and gender_random:
                    m_counter += 1
                    diff_counter += 1
                    for i in range(0, 2):
                        Congruent_Misaligned().CongruentDifferentMisalignedMale(practice=1)

                if same_random and not gender_random:
                    f_counter += 1
                    same_counter += 1
                    for i in range(0, 2):
                        Congruent_Misaligned().CongruentSameMisalignedFemale(practice=1)

                if same_random and gender_random:
                    m_counter += 1
                    same_counter += 1
                    for i in range(0, 2):
                        Congruent_Misaligned().CongruentSameMisalignedMale(practice=1)

            #Incongruent Misaligned
            if typerandom == 3:
                if not same_random and not gender_random:
                    f_counter += 1
                    diff_counter += 1
                    for i in range(0, 2):
                        Incongruent_Misaligned().IncongruentDifferentMisalignedFemale(practice=1)

                if not same_random and gender_random:
                    m_counter += 1
                    diff_counter += 1
                    for i in range(0, 2):
                        Incongruent_Misaligned().IncongruentDifferentMisalignedMale(practice=1)

                if same_random and not gender_random:
                    f_counter += 1
                    same_counter += 1
                    for i in range(0, 2):
                        Incongruent_Misaligned().IncongruentSameMisalignedFemale(practice=1)

                if same_random and gender_random:
                    m_counter += 1
                    same_counter += 1
                    for i in range(0, 2):
                        Incongruent_Misaligned().IncongruentSameMisalignedMale(practice=1)

            #Incongruent Aligned
            if typerandom == 4:
                if not same_random and not gender_random:
                    f_counter += 1
                    diff_counter += 1
                    for i in range(0, 2):
                        Incongruent_Aligned().IncongruentDifferentAlignedFemale(practice=1)

                if not same_random and gender_random:
                    m_counter += 1
                    diff_counter += 1
                    for i in range(0, 2):
                        Incongruent_Aligned().IncongruentDifferentAlignedMale(practice=1)

                if same_random and not gender_random:
                    f_counter += 1
                    same_counter += 1
                    for i in range(0, 2):
                        Incongruent_Aligned().IncongruentSameAlignedFemale(practice=1)

                if same_random and gender_random:
                    m_counter += 1
                    same_counter += 1
                    for i in range(0, 2):
                        Incongruent_Aligned().IncongruentSameAlignedMale(practice=1)












