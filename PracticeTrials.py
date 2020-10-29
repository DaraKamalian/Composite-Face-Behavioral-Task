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

        for index in range(1, 17):

            mainrandom = random.randint(1, 8)
            print('main random: ' + str(mainrandom))

            if mainrandom == 1 and type1counter == 2:
                mainrandom = 2
            if mainrandom == 2 and type2counter == 2:
                mainrandom = 3
            if mainrandom == 3 and type3counter == 2:
                mainrandom = 4
            if mainrandom == 4 and type4counter == 2:
                mainrandom = 5
            if mainrandom == 5 and type5counter == 2:
                mainrandom = 6
            if mainrandom == 6 and type6counter == 2:
                mainrandom = 7
            if mainrandom == 7 and type7counter == 2:
                mainrandom = 8
            if mainrandom == 8 and type8counter == 2:

                if type7counter < 2:
                    mainrandom = 7
                elif type6counter < 2:
                    mainrandom = 6
                elif type5counter < 2:
                    mainrandom = 5
                if type4counter < 2:
                    mainrandom = 4
                if type3counter < 2:
                    mainrandom = 3
                elif type2counter < 2:
                    mainrandom = 2
                elif type1counter < 2:
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
                print(str(index) + ' type1')
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and onemale == 1:
                    gender_random = 0
                elif gender_random == 0 and onefemale == 1:
                    gender_random = 1

                if gender_random:
                    onemale += 1
                else:
                    onefemale += 1

                Congruent_Aligned().CongruentAligned(practice=1, same=1, gender=gender_random, index=2,
                                                     block=index)

                type1counter += 1

            if mainrandom == 2:
                print(str(index) + ' type2')
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and twomale == 1:
                    gender_random = 0
                elif gender_random == 0 and twofemale == 1:
                    gender_random = 1

                if gender_random:
                    twomale += 1
                else:
                    twofemale += 1

                Congruent_Aligned().CongruentAligned(practice=1, same=0, gender=gender_random, index=2,
                                                       block=index)

                type2counter += 1

            # Congruent Misaligned
            if mainrandom == 3:
                print(str(index) + ' type3')
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and threemale == 1:
                    gender_random = 0
                elif gender_random == 0 and threefemale == 1:
                    gender_random = 1

                if gender_random:
                    threemale += 1
                else:
                    threefemale += 1

                Congruent_Misaligned().CongruentMisaligned(practice=1, same=1, gender=gender_random, index=2,
                                                           block=index)

                type3counter += 1


            if mainrandom == 4:
                print(str(index) + ' type4')
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and fourmale == 1:
                    gender_random = 0
                elif gender_random == 0 and fourfemale == 1:
                    gender_random = 1

                if gender_random:
                    fourmale += 1
                else:
                    fourfemale += 1

                Congruent_Misaligned().CongruentMisaligned(practice=1, same=0, gender=gender_random, index=2,
                                                           block=index)

                type4counter += 1

            # Incongruent Aligned
            if mainrandom == 5:
                print(str(index) + ' type5')
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and fivemale == 1:
                    gender_random = 0
                elif gender_random == 0 and fivefemale == 1:
                    gender_random = 1

                if gender_random:
                    fivemale += 1
                else:
                    fivefemale += 1

                Incongruent_Aligned().IncongruentAligned(practice=1, same=1, gender=gender_random, index=2,
                                                         block=index)

                type5counter += 1

            if mainrandom == 6:
                print(str(index) + ' type6')
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and sixmale == 1:
                    gender_random = 0
                elif gender_random == 0 and sixfemale == 1:
                    gender_random = 1

                if gender_random:
                    sixmale += 1
                else:
                    sixfemale += 1

                Incongruent_Aligned().IncongruentAligned(practice=1, same=0, gender=gender_random, index=2,
                                                         block=index)

                type6counter += 1

            # Incongruent Misaligned
            if mainrandom == 7:
                print(str(index) + ' type7')
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and sevenmale == 1:
                    gender_random = 0
                elif gender_random == 0 and sevenfemale == 1:
                    gender_random = 1

                if gender_random:
                    sevenmale += 1
                else:
                    sevenfemale += 1
                Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=1, gender=gender_random, index=2,
                                                               block=index)

                type7counter += 1

            if mainrandom == 8:
                print(str(index) + ' type8')
                gender_random = random.randint(0, 100) % 2

                if gender_random == 1 and eightmale == 1:
                    gender_random = 0
                elif gender_random == 0 and eightfemale == 1:
                    gender_random = 1

                if gender_random:
                    eightmale += 1
                else:
                    eightfemale += 1
                Incongruent_Misaligned().IncongruentMisaligned(practice=1, same=0, gender=gender_random, index=2,
                                                               block=index)

                type8counter += 1
