import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from SameUpperLocationsList import SameUpperLocationsList
from SameLowerLocationsList import SameLowerLocationsList

image = MainAssets()
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Incongruent_Aligned(object):
    def IncongruentSameAlignedMale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('inc-same-al-m')

        rand1 = random.randint(0, 19)
        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = SameUpperLocationsList.SameUpperLocationsList(
            men_align_locations, men_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)

        for item in men_align_images:
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

    def IncongruentSameAlignedFemale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('inc-same-al-f')

        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = SameUpperLocationsList.SameUpperLocationsList(
            women_align_locations, women_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)

        for item in women_align_images:
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

    def IncongruentDifferentAlignedMale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('inc-dif-al-m')

        rand1 = random.randint(0, 19)
        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = SameLowerLocationsList.SameLowerLocationsList(
            men_align_locations, men_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)

        for item in men_align_images:
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

    def IncongruentDifferentAlignedFemale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('inc-dif-al-f')

        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = SameLowerLocationsList.SameLowerLocationsList(
            women_align_locations, women_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)

        for item in women_align_images:
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


