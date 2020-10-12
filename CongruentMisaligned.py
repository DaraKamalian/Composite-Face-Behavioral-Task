import random
import xlsxwriter

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from MenAlign import Men_Align
from WomenAlign import Women_Align
from DifferentTotalLocationsList import DifferentTotalLocationsList
from DialogueBox import dialoguebox

image = MainAssets()
# subjectInfoList = dialoguebox.showDialogBox()
differentLocationsList = DifferentTotalLocationsList()

women_misalign_images = Women_Misalign().women_misalign_images
women_misalign_locations = Women_Misalign().women_misalign_locations
men_misalign_images = Men_Misalign().men_misalign_images
men_misalign_locations = Men_Misalign().men_misalign_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations

fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Congruent_Misaligned(object):
    def CongruentSameMisalignedMale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)
        print('con-same-mis-m')

        rand1 = random.randint(0, 19)
        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        men_misalign_images[rand1].draw()
        print(men_misalign_images[rand1].image)
        win.flip()

        flag = True
        while flag:
            keys = event.getKeys(keyList=['a', 'l'])
            for key in keys:
                if key == 'a':
                    # print('correct')
                    flag = False
                else:
                    # print('wrong')
                    flag = False

    def CongruentSameMisalignedFemale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)
        print('con-same-mis-f')

        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        women_misalign_images[rand1].draw()
        print(women_misalign_images[rand1].image)
        win.flip()

        flag = True
        while flag:
            keys = event.getKeys(keyList=['a', 'l'])
            for key in keys:
                if key == 'a':
                    # write to table
                    # print('correct')
                    flag = False
                else:
                    # write to table
                    flag = False

    def CongruentDifferentMisalignedMale(name):
        print('con-diff-mis-m')
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        rand1 = random.randint(0, 19)
        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = differentLocationsList.different_total_locations_list(
            men_misalign_locations, men_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)

        for item in men_misalign_images:
            if item.image == newLocations[newLocRand]:
                item.draw()
                win.flip()
                print(item.image)
                break

        flag = True
        while flag:
            keys = event.getKeys(keyList=['a', 'l'])
            for key in keys:
                if key == 'a':
                    # write to table
                    # print('a')
                    flag = False
                else:
                    # write to table
                    # print('l')
                    flag = False

    def CongruentDifferentMisalignedFemale(name):
        print('con-dif-mis-f')
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)
        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = differentLocationsList.different_total_locations_list(
            women_misalign_locations, women_align_images[rand1].image)
        print('newlocs length is:' + str(len(newLocations)))

        newLocRand = random.randint(0, len(newLocations) - 1)

        for item in women_misalign_images:
            if item.image == newLocations[newLocRand]:
                item.draw()
                win.flip()
                print(item.image)
                break

        flag = True
        while flag:
            keys = event.getKeys(keyList=['a', 'l'])
            for key in keys:
                if key == 'a':
                    # write to table
                    # print('a')
                    flag = False
                else:
                    # write to table
                    # print('l')
                    flag = False






























