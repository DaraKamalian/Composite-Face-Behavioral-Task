import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from DifferentTotalLocationsList import DifferentTotalLocationsList

image = MainAssets()
differentLocationsList = DifferentTotalLocationsList()
women_misalign_images = Women_Misalign().women_misalign_images
women_misalign_locations = Women_Misalign().women_misalign_locations
men_misalign_images = Men_Misalign().men_misalign_images
men_misalign_locations = Men_Misalign().men_misalign_locations
fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Congruent_Misaligned(object):

    def CongruentSameMisaligned(name):

        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)



        # 0 -> different, 1 -> same

        # if same_rand == 1 and same_counter == 5:
        #     same_rand = 0
        # if same_rand == 0 and different_counter == 5:
        #     same_rand = 1

        gender_random = random.randint(0, 100) % 2
        # 0 -> female, 1 -> male

        if gender_random == 1:
            print('same')

            rand1 = random.randint(0, 19)
            men_misalign_images[rand1].draw()
            print(men_misalign_images[rand1].image)
            win.flip()
            core.wait(0.2)

            men_misalign_images[rand1].autoDraw = False
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

        if gender_random == 0:
            print('same')

            rand1 = random.randint(0, 19)
            women_misalign_images[rand1].draw()
            print(women_misalign_images[rand1].image)
            win.flip()
            core.wait(0.2)

            women_misalign_images[rand1].autoDraw = False
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
                        #write to table
                        # print('correct')
                        flag = False
                    else:
                        #write to table
                        flag = False

        # if same_rand == 0 and gender_random == 0:
        #     print('different')
        #     different_counter += 1
        #
        #     rand1 = random.randint(0, 19)
        #     women_misalign_images[rand1].draw()
        #     print(women_misalign_images[rand1].image)
        #     win.flip()
        #     core.wait(0.2)
        #
        #     women_misalign_images[rand1].autoDraw = False
        #     win.flip()
        #     core.wait(0.4)
        #
        #     newLocations = differentLocationsList.DifferentTotalLocationsList(
        #         women_misalign_locations, women_misalign_images[rand1].image)
        #
        #     newLocRand = random.randint(0, len(newLocations) - 1)
        #
        #     for item in women_misalign_images:
        #         if item.image == newLocations[newLocRand]:
        #             item.draw()
        #             win.flip()
        #             print(item.image)
        #             break
        #
        #
        #     flag = True
        #     while flag:
        #         keys = event.getKeys(keyList=['a', 'l'])
        #         for key in keys:
        #             if key == 'a':
        #                 #write to table
        #                 # print('a')
        #                 flag = False
        #             else:
        #                 #write to table
        #                 # print('l')
        #                 flag = False
        #
        # if same_rand == 0 and gender_random == 1:
        #     print('different')
        #     different_counter += 1
        #     rand1 = random.randint(0, 19)
        #     men_misalign_images[rand1].draw()
        #     print(men_misalign_images[rand1].image)
        #     win.flip()
        #     core.wait(0.2)
        #
        #     men_misalign_images[rand1].autoDraw = False
        #     win.flip()
        #     core.wait(0.4)
        #
        #     newLocations = differentLocationsList.DifferentTotalLocationsList(
        #         men_misalign_locations, men_misalign_images[rand1].image)
        #
        #     newLocRand = random.randint(0, len(newLocations) - 1)
        #
        #     for item in men_misalign_images:
        #         if item.image == newLocations[newLocRand]:
        #             item.draw()
        #             win.flip()
        #             print(item.image)
        #             break
        #
        #     flag = True
        #     while flag:
        #         keys = event.getKeys(keyList=['a', 'l'])
        #         for key in keys:
        #             if key == 'a':
        #                 # write to table
        #                 # print('a')
        #                 flag = False
        #             else:
        #                 # write to table
        #                 # print('l')
        #                 flag = False

    def CongruentDifferentMisaligned(name):

        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        same_rand = random.randint(0, 100) % 2

        # 0 -> different, 1 -> same

        # if same_rand == 1 and same_counter == 5:
        #     same_rand = 0
        # if same_rand == 0 and different_counter == 5:
        #     same_rand = 1

        gender_random = random.randint(0, 100) % 2
        # 0 -> female, 1 -> male

        # if gender_random == 1:
        #     print('same')
        #
        #     rand1 = random.randint(0, 19)
        #     men_misalign_images[rand1].draw()
        #     print(men_misalign_images[rand1].image)
        #     win.flip()
        #     core.wait(0.2)
        #
        #     men_misalign_images[rand1].autoDraw = False
        #     win.flip()
        #     core.wait(0.4)
        #
        #     men_misalign_images[rand1].draw()
        #     print(men_misalign_images[rand1].image)
        #     win.flip()
        #
        #     flag = True
        #     while flag:
        #         keys = event.getKeys(keyList=['a', 'l'])
        #         for key in keys:
        #             if key == 'a':
        #                 # print('correct')
        #                 flag = False
        #             else:
        #                 # print('wrong')
        #                 flag = False
        #
        # if gender_random == 0:
        #     print('same')
        #
        #     rand1 = random.randint(0, 19)
        #     women_misalign_images[rand1].draw()
        #     print(women_misalign_images[rand1].image)
        #     win.flip()
        #     core.wait(0.2)
        #
        #     women_misalign_images[rand1].autoDraw = False
        #     win.flip()
        #     core.wait(0.4)
        #
        #     women_misalign_images[rand1].draw()
        #     print(women_misalign_images[rand1].image)
        #     win.flip()
        #
        #     flag = True
        #     while flag:
        #         keys = event.getKeys(keyList=['a', 'l'])
        #         for key in keys:
        #             if key == 'a':
        #                 #write to table
        #                 # print('correct')
        #                 flag = False
        #             else:
        #                 #write to table
        #                 flag = False

        if gender_random == 0:

            rand1 = random.randint(0, 19)
            women_misalign_images[rand1].draw()
            print(women_misalign_images[rand1].image)
            win.flip()
            core.wait(0.2)

            women_misalign_images[rand1].autoDraw = False
            win.flip()
            core.wait(0.4)

            newLocations = differentLocationsList.DifferentTotalLocationsList(
                women_misalign_locations, women_misalign_images[rand1].image)

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
                        #write to table
                        # print('a')
                        flag = False
                    else:
                        #write to table
                        # print('l')
                        flag = False

        if gender_random == 1:

            rand1 = random.randint(0, 19)
            men_misalign_images[rand1].draw()
            print(men_misalign_images[rand1].image)
            win.flip()
            core.wait(0.2)

            men_misalign_images[rand1].autoDraw = False
            win.flip()
            core.wait(0.4)

            newLocations = differentLocationsList.DifferentTotalLocationsList(
                men_misalign_locations, men_misalign_images[rand1].image)

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



























