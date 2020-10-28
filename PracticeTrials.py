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
        type1counter = 0
        type2counter = 0
        type3counter = 0
        type4counter = 0

        onemale = 0
        onefemale = 0
        twomale = 0
        twofemale = 0
        threemale = 0
        threefemale = 0
        fourmale = 0
        fourfemale = 0

        for index in range(1, 17):

            mainrandom = random.randint(1, 4)
            print('main random: ' + str(mainrandom))

            if mainrandom == 1 and type1counter == 4:
                mainrandom = 2
            if mainrandom == 2 and type2counter == 4:
                mainrandom = 3
            if mainrandom == 3 and type3counter == 4:
                mainrandom = 4
            if mainrandom == 4 and type4counter == 4:

                if type3counter < 4:
                    mainrandom = 3
                elif type2counter < 4:
                    mainrandom = 2
                elif type1counter < 4:
                    mainrandom = 1

            same_counter = 0
            diff_counter = 0

            samerandom = random.randint(0, 100) % 2

            if not samerandom and diff_counter == 8:
                samerandom = 1
                same_counter += 1
            if samerandom and same_counter == 8:
                samerandom = 0
                diff_counter += 1

            # Congruent Aligned
            if mainrandom == 1:
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and onemale == 2:
                    gender_random = 0
                elif gender_random == 0 and onefemale == 2:
                    gender_random = 1

                if gender_random:
                    onemale += 1
                else:
                    onefemale += 1

                Congruent_Aligned().CongruentAligned(practice=1, same=samerandom, gender=gender_random, index=None,
                                                     block=index)
                type1counter += 1

            # Congruent Misaligned
            if mainrandom == 2:

                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and twomale == 2:
                    gender_random = 0
                elif gender_random == 0 and twofemale == 2:
                    gender_random = 1

                if gender_random:
                    twomale += 1
                else:
                    twofemale += 1

                Congruent_Misaligned().CongruentMisaligned(practice=1, same=samerandom, gender=gender_random, index=None,
                                                           block=index)
                type2counter += 1

            # Incongruent Misaligned
            if mainrandom == 3:

                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and threemale == 2:
                    gender_random = 0
                elif gender_random == 0 and threefemale == 2:
                    gender_random = 1

                if gender_random:
                    threemale += 1
                else:
                    threefemale += 1

                Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=samerandom, gender=gender_random,
                                                               index=None,
                                                               block=index)

                type3counter += 1

            # Incongruent Aligned
            if mainrandom == 4:

                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and fourmale == 2:
                    gender_random = 0
                elif gender_random == 0 and fourfemale == 2:
                    gender_random = 1

                if gender_random:
                    fourmale += 1
                else:
                    fourfemale += 1

                Incongruent_Aligned().IncongruentAligned(practice=1, same=samerandom, gender=gender_random, index=None,
                                                         block=index)
                type4counter += 1
