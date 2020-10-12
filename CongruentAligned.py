import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from DifferentTotalLocationsList import DifferentTotalLocationsList

image = MainAssets()
correct = image.correct
wrong = image.wrong
differentLocationsList = DifferentTotalLocationsList()
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Congruent_Aligned(object):

    def CongruentSameAlignedMale(self, practice):

        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)
        print('con-same-al-m')

        rand1 = random.randint(0, 19)
        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.5)

        men_align_images[rand1].autoDraw = False
        questionMark.draw()
        win.flip()

        countdown = core.CountdownTimer(1.5)

        flag = True
        while flag:
            keys = event.getKeys(keyList=['a', 'l'])
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
                        else:
                            print('l')
                            # print('wrong')
                        flag = False
            elif countdown.getTime() <= 0:
                #late
                flag = False

    def CongruentSameAlignedFemale(self, practice):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)
        print('con-same-al-f')
        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.5)

        women_align_images[rand1].autoDraw = False
        questionMark.draw()
        win.flip()

        countdown = core.CountdownTimer(1.5)

        flag = True
        while flag:
            keys = event.getKeys(keyList=['a', 'l'])
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

    def CongruentDifferentAlignedMale(self, practice):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('con-dif-al-m')
        rand1 = random.randint(0, 19)
        men_align_images[rand1].draw()
        print(men_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = differentLocationsList.different_total_locations_list(
            men_align_locations, men_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)
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
            keys = event.getKeys(keyList=['a', 'l'])
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

    def CongruentDifferentAlignedFemale(self, practice):

        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        print('con-dif-al-m')
        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = differentLocationsList.different_total_locations_list(
            women_align_locations, women_align_images[rand1].image)

        newLocRand = random.randint(0, len(newLocations) - 1)
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
            keys = event.getKeys(keyList=['a', 'l'])
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
                            # print('a')
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
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

































