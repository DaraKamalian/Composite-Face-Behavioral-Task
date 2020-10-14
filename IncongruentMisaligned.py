import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from MenAlign import Men_Align
from WomenAlign import Women_Align

image = MainAssets()
correct = image.correct
wrong = image.wrong

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
    def IncongruentSameMisalignedMale(self, practice):
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

        obj = SameUpperLocationsList()

        newLocations = SameUpperLocationsList.SameUpperLocationsList(obj,
            men_misalign_locations, men_align_images[rand1].image)
        # print('newlocs length is:' + str(len(newLocations)))

        newLocRand = random.randint(0, len(newLocations) - 1)
        list = []
        for item in men_misalign_images:
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
                            # print('correct')
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                            # print('wrong')
                        else:
                            print('l')
                        flag = False
            elif countdown.getTime() <= 0:
                #late
                flag = False

    def IncongruentSameMisalignedFemale(self, practice):
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

        obj = SameUpperLocationsList()
        newLocations = SameUpperLocationsList.SameUpperLocationsList(obj,
            women_misalign_locations, women_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)

        list = []
        for item in women_misalign_images:
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

    def IncongruentDifferentMisalignedMale(self, practice):
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
        obj = SameLowerLocationsList()
        newLocations = SameLowerLocationsList.SameLowerLocationsList(obj,
            men_misalign_locations, men_align_images[rand1].image)

        newLocRand = random.randint(0, (len(newLocations) - 1))

        list = []
        for item in men_misalign_images:
            if item.image == newLocations[newLocRand]:
                item.draw()
                list.append(item)
                win.flip()
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
                            print('correct')

                        flag = False
                    elif key == 'l':
                        if practice:
                            correct.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('wrong')

                        flag = False
            elif countdown.getTime() <= 0:
                #late
                flag = False

    def IncongruentDifferentMisalignedFemale(self, practice):
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
        obj = SameLowerLocationsList()
        newLocations = SameLowerLocationsList.SameLowerLocationsList(obj,
            women_misalign_locations, women_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)

        list = []
        for item in women_misalign_images:
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
                            print('wrong')
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('wrong')

                        flag = False
                    elif key == 'l':
                        if practice:
                            print('correct')
                            correct.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            print('correct')
                        # write to table
                        flag = False
            elif countdown.getTime() <= 0:
                #late
                flag = False


