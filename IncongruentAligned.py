import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from SameUpperLocationsList import SameUpperLocationsList
from SameLowerLocationsList import SameLowerLocationsList

image = MainAssets()
correct = image.correct
wrong = image.wrong
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
women_misalign_images = Women_Misalign().women_misalign_images
women_misalign_locations = Women_Misalign().women_misalign_locations
men_misalign_images = Men_Misalign().men_misalign_images
men_misalign_locations = Men_Misalign().men_misalign_locations

fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Incongruent_Aligned(object):
    def IncongruentSameAlignedMale(self, practice):
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
        obj = SameUpperLocationsList()
        newLocations = SameUpperLocationsList.SameUpperLocationsList(obj,
            men_align_locations, men_align_images[rand1].image)

        newLocRand = random.randint(0, (len(newLocations) - 1))

        list = []
        for item in men_align_images:
            if item.image == newLocations[newLocRand]:
                item.draw()
                win.flip()
                list.append(item)
                print(item.image)
                break
        core.wait(0.5)
        list[0].autoDraw = False
        questionMark.draw()
        win.flip()

        countdown = core.CountdownTimer(1.5)

        flag = True
        while flag:
            # keys = event.getKeys(keyList=['a', 'l'])
            keys = event.waitKeys(keyList=['a', 'l'], maxWait=1.5)
            if keys:
                for key in keys:
                    if key == 'a':
                        if practice:
                            correct.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('a')
                            # write to table
                            # print('correct')
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('l')
                            # write to table
                        flag = False
            elif countdown.getTime() <= 0:
                #late
                flag = False

    def IncongruentSameAlignedFemale(self, practice):
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

        obj = SameUpperLocationsList()
        newLocations = SameUpperLocationsList.SameUpperLocationsList(obj,
            women_align_locations, women_align_images[rand1].image)

        newLocRand = random.randint(0, (len(newLocations) - 1))
        list = []
        for item in women_align_images:
            if item.image == newLocations[newLocRand]:
                item.draw()
                win.flip()
                list.append(item)
                print(item.image)
                break
        core.wait(0.5)
        list[0].autoDraw = False
        questionMark.draw()
        win.flip()

        countdown = core.CountdownTimer(1.5)

        flag = True
        while flag:
            # keys = event.getKeys(keyList=['a', 'l'])
            keys = event.waitKeys(keyList=['a', 'l'], maxWait=1.5)
            if keys:
                for key in keys:
                    if key == 'a':
                        if practice:
                            correct.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('a')
                            # write to table
                            # print('correct')
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('l')
                            # write to table
                        flag = False
            elif countdown.getTime() <= 0:
                #late
                flag = False

    def IncongruentDifferentAlignedMale(self, practice):
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

        obj = SameLowerLocationsList()
        newLocations = SameLowerLocationsList.SameLowerLocationsList(obj,
            men_align_locations, men_align_images[rand1].image)

        newLocRand = random.randint(0, (len(newLocations) - 1))
        list = []
        for item in men_align_images:
            if item.image == newLocations[newLocRand]:
                item.draw()
                win.flip()
                list.append(item)
                print(item.image)
                break
        core.wait(0.5)
        list[0].autoDraw = False
        questionMark.draw()
        win.flip()

        countdown = core.CountdownTimer(1.5)

        flag = True
        while flag:
            # keys = event.getKeys(keyList=['a', 'l'])
            keys = event.waitKeys(keyList=['a', 'l'], maxWait=1.5)
            if keys:
                for key in keys:
                    if key == 'a':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('a')
                            # write to table
                            # print('a')
                        flag = False
                    elif key == 'l':
                        if practice:
                            correct.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('l')
                            # write to table
                            # print('l')
                        flag = False
            elif countdown.getTime() <= 0:
                #late
                flag = False

    def IncongruentDifferentAlignedFemale(self, practice):
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

        obj = SameLowerLocationsList()
        newLocations = SameLowerLocationsList.SameLowerLocationsList(obj,
            women_align_locations, women_align_images[rand1].image)

        newLocRand = random.randint(0, (len(newLocations) - 1))

        list = []
        for item in women_align_images:
            if item.image == newLocations[newLocRand]:
                item.draw()
                win.flip()
                list.append(item)
                print(item.image)
                break
        core.wait(0.5)
        list[0].autoDraw = False
        questionMark.draw()
        win.flip()
        countdown = core.CountdownTimer(1.5)
        flag = True
        while flag:
            # keys = event.getKeys(keyList=['a', 'l'])
            keys = event.waitKeys(keyList=['a', 'l'], maxWait=1.5)
            if keys:
                for key in keys:
                    if key == 'a':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('a')
                            # write to table
                            # print('a')
                        flag = False
                    elif key == 'l':
                        if practice:
                            correct.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('l')
                            # write to table
                            # print('l')
                        flag = False
            elif countdown.getTime() <= 0:
                #late
                flag = False


