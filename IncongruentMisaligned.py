import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from MenAlign import Men_Align
from WomenAlign import Women_Align

image = MainAssets()

from SameUpperLocationsList import SameUpperLocationsList
from SameLowerLocationsList import SameLowerLocationsList

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


class Incongruent_Misaligned(object):
    def IncongruentSameMisalignedMale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('inc-same-mis-m')

        rand1 = random.randint(0, 19)
        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = SameUpperLocationsList.SameUpperLocationsList(
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
                    # print('correct')
                    flag = False
                else:
                    # print('wrong')
                    flag = False

    def IncongruentSameMisalignedFemale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('inc-same-mis-f')

        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = SameUpperLocationsList.SameUpperLocationsList(
            women_misalign_locations, women_align_images[rand1].image)

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
                    # print('correct')
                    flag = False
                else:
                    # write to table
                    flag = False

    def IncongruentDifferentMisalignedMale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('inc-dif-mis-m')

        rand1 = random.randint(0, 19)
        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = SameLowerLocationsList.SameLowerLocationsList(
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
                    # print('correct')
                    flag = False
                else:
                    # print('wrong')
                    flag = False

    def IncongruentDifferentMisalignedFemale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('inc-dif-mis-f')

        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = SameLowerLocationsList.SameLowerLocationsList(
            women_misalign_locations, women_align_images[rand1].image)

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
                    # print('correct')
                    flag = False
                else:
                    # write to table
                    flag = False



