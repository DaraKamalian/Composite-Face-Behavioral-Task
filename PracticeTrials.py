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

            if Config.respversion and Config.appversion:
                # Congruent Aligned
                if typerandom == 1:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=0, index=i, block=index,
                                                                 respversion=1, appversion=1)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=1, index=i, block=index,
                                                                 respversion=1, appversion=1)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=0, index=i, block=index,
                                                                 respversion=1, appversion=1)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=1, index=i, block=index,
                                                                 respversion=1, appversion=1)

                # Congruent Misaligned
                if typerandom == 2:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=0, index=i,
                                                                       block=index,
                                                                       respversion=1, appversion=1)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=1, index=i,
                                                                       block=index,
                                                                       respversion=1, appversion=1)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=0, index=i,
                                                                       block=index,
                                                                       respversion=1, appversion=1)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=1, index=i,
                                                                       block=index,
                                                                       respversion=1, appversion=1)

                # Incongruent Misaligned
                if typerandom == 3:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=0, index=i,
                                                                           block=index,
                                                                           respversion=1, appversion=1)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=1, index=i,
                                                                           block=index,
                                                                           respversion=1, appversion=1)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=0, index=i,
                                                                           block=index,
                                                                           respversion=1, appversion=1)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=1, index=i,
                                                                           block=index,
                                                                           respversion=1, appversion=1)

                # Incongruent Aligned
                if typerandom == 4:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=0, index=i,
                                                                     block=index,
                                                                     respversion=1, appversion=1)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=1, index=i,
                                                                     block=index,
                                                                     respversion=1, appversion=1)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=0, index=i,
                                                                     block=index,
                                                                     respversion=1, appversion=1)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=1, index=i,
                                                                     block=index,
                                                                     respversion=1, appversion=1)

            if Config.respversion and not Config.appversion:
                # Congruent Aligned
                if typerandom == 1:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=0, index=i,
                                                                 block=index, respversion=1, appversion=0)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=1, index=i,
                                                                 block=index, respversion=1, appversion=0)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=0, index=i,
                                                                 block=index, respversion=1, appversion=0)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=1, index=i,
                                                                 block=index, respversion=1, appversion=0)

                # Congruent Misaligned
                if typerandom == 2:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=0, index=i,
                                                                       block=index, respversion=1, appversion=0)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=1, index=i,
                                                                       block=index, respversion=1, appversion=0)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=0, index=i,
                                                                       block=index, respversion=1, appversion=0)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=1, index=i,
                                                                       block=index, respversion=1, appversion=0)

                # Incongruent Misaligned
                if typerandom == 3:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=0, index=i,
                                                                           block=index, respversion=1, appversion=0)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=1, index=i,
                                                                           block=index, respversion=1, appversion=0)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=0, index=i,
                                                                           block=index, respversion=1, appversion=0)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=1, index=i,
                                                                           block=index, respversion=1, appversion=0)

                # Incongruent Aligned
                if typerandom == 4:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=0, index=i,
                                                                     block=index, respversion=1, appversion=0)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=1, index=i,
                                                                     block=index, respversion=1, appversion=0)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=0, index=i,
                                                                     block=index, respversion=1, appversion=0)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=1, index=i,
                                                                     block=index, respversion=1, appversion=0)

            if not Config.respversion and Config.appversion:
                # Congruent Aligned
                if typerandom == 1:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=0, index=i,
                                                                 block=index, respversion=0, appversion=1)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=1, index=i,
                                                                 block=index, respversion=0, appversion=1)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=0, index=i,
                                                                 block=index, respversion=0, appversion=1)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=1, index=i,
                                                                 block=index, respversion=0, appversion=1)

                # Congruent Misaligned
                if typerandom == 2:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=0, index=i,
                                                                       block=index, respversion=0, appversion=1)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=1, index=i,
                                                                       block=index, respversion=0, appversion=1)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=0, index=i,
                                                                       block=index, respversion=0, appversion=1)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=1, index=i,
                                                                       block=index, respversion=0, appversion=1)

                # Incongruent Misaligned
                if typerandom == 3:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=0, index=i,
                                                                           block=index, respversion=0, appversion=1)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=1, index=i,
                                                                           block=index, respversion=0, appversion=1)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=0, index=i,
                                                                           block=index, respversion=0, appversion=1)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=1, index=i,
                                                                           block=index, respversion=0, appversion=1)

                # Incongruent Aligned
                if typerandom == 4:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=0, index=i,
                                                                     block=index, respversion=0, appversion=1)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=1, index=i,
                                                                     block=index, respversion=0, appversion=1)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=0, index=i,
                                                                     block=index, respversion=0, appversion=1)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=1, index=i,
                                                                     block=index, respversion=0, appversion=1)

            if not Config.respversion and not Config.appversion:
                # Congruent Aligned
                if typerandom == 1:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=0, index=i,
                                                                 block=index, respversion=0, appversion=0)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=1, index=i,
                                                                 block=index, respversion=0, appversion=0)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=0, index=i,
                                                                 block=index, respversion=0, appversion=0)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=1, index=i,
                                                                 block=index, respversion=0, appversion=0)

                # Congruent Misaligned
                if typerandom == 2:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=0,
                                                                       index=i, block=index, respversion=0,
                                                                       appversion=0)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=1,
                                                                       index=i, block=index, respversion=0,
                                                                       appversion=0)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=0,
                                                                       index=i, block=index, respversion=0,
                                                                       appversion=0)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=1,
                                                                       index=i, block=index, respversion=0,
                                                                       appversion=0)

                # Incongruent Misaligned
                if typerandom == 3:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=0,
                                                                           index=i, block=index, respversion=0,
                                                                           appversion=0)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=1,
                                                                           index=i, block=index, respversion=0,
                                                                           appversion=0)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=0,
                                                                           index=i, block=index, respversion=0,
                                                                           appversion=0)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=1,
                                                                           index=i, block=index, respversion=0,
                                                                           appversion=0)

                # Incongruent Aligned
                if typerandom == 4:
                    if not same_random and not gender_random:
                        f_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=0,
                                                                     index=i, block=index, respversion=0, appversion=0)

                    if not same_random and gender_random:
                        m_counter += 1
                        diff_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=1,
                                                                     index=i, block=index, respversion=0, appversion=0)

                    if same_random and not gender_random:
                        f_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=0,
                                                                     index=i, block=index, respversion=0, appversion=0)

                    if same_random and gender_random:
                        m_counter += 1
                        same_counter += 1
                        for i in range(0, 2):
                            Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=1,
                                                                     index=i, block=index, respversion=0, appversion=0)
