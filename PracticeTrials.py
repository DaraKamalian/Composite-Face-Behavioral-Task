import random
import Config
from psychopy import core
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
        m_counter = 0
        f_counter = 0

        diff_counter = 0
        same_counter = 0
        for index in range(1, 17):

            somenumber = 2

            same_random = random.randint(0, 100) % 2
            gender_random = random.randint(0, 100) % 2
            mainrandom = random.randint(1, 4)

            if not same_random and diff_counter == 8:
                same_random = 1

            if same_random and same_counter == 8:
                same_random = 0

            if same_random:
                same_counter += 1
            else:
                diff_counter += 1

            if not gender_random and f_counter == 8:
                gender_random = 1
            if gender_random and m_counter == 8:
                gender_random = 0

            if gender_random:
                m_counter += 1

            else:
                f_counter += 1

            respversion = Config.respversion
            taskversion = Config.appversion

            # Congruent Aligned
            if mainrandom == 1:
                Congruent_Aligned().CongruentAligned(practice=1, same=same_random, gender=gender_random,
                                                     index=somenumber, block=index,
                                                     respversion=respversion, appversion=taskversion)
            # Congruent Misaligned
            if mainrandom == 2:
                Congruent_Misaligned().CongruentMisaligned(practice=1, same=same_random, gender=gender_random,
                                                           index=somenumber,
                                                           block=index,
                                                           respversion=1, appversion=1)

            # Incongruent Misaligned
            if mainrandom == 3:
                Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=same_random, gender=gender_random,
                                                               index=somenumber,
                                                               block=index,
                                                               respversion=1, appversion=1)
            # Incongruent Aligned
            if mainrandom == 4:
                Incongruent_Aligned().IncongruentAligned(practice=1, same=same_random, gender=gender_random,
                                                         index=somenumber,
                                                         block=index,
                                                         respversion=respversion, appversion=taskversion)
