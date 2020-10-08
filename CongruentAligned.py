import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from DifferentTotalLocationsList import DifferentTotalLocationsList

image = MainAssets()
differentLocationsList = DifferentTotalLocationsList()
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Congruent_Aligned(object):

    def CongruentSameAlignedMale(name):

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

    def CongruentSameAlignedFemale(name):
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

    def CongruentDifferentAlignedMale(name):
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

        newLocations = differentLocationsList.DifferentTotalLocationsList(
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
                    # write to table
                    # print('a')
                    flag = False
                else:
                    # write to table
                    # print('l')
                    flag = False

    def CongruentDifferentAlignedFemale(name):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)
        print('con-dif-al-f')
        rand1 = random.randint(0, 19)
        women_align_images[rand1].draw()
        print(women_align_images[rand1].image)
        win.flip()
        core.wait(0.2)

        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        newLocations = differentLocationsList.DifferentTotalLocationsList(
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
                    # print('a')
                    flag = False
                else:
                    # write to table
                    # print('l')
                    flag = False



    # def CongruentSameAligned(name):
    #
    #     fixationPoint.draw()
    #     win.flip()
    #     core.wait(0.2)
    #
    #     fixationPoint.autoDraw = False
    #     win.flip()
    #     core.wait(0.15)
    #
    #     gender_random = random.randint(0, 100) % 2
    #     # 0 -> female, 1 -> male
    #     m_counter = 0
    #     f_counter = 0
    #
    #     if gender_random == 0 and f_counter == 5:
    #         gender_random = 1
    #     if gender_random == 1 and m_counter == 5:
    #         gender_random = 0
    #
    #     if gender_random == 1:
    #         print('con-same-al-m')
    #         m_counter += 1
    #         rand1 = random.randint(0, 19)
    #         men_align_images[rand1].draw()
    #         print(men_align_images[rand1].image)
    #         win.flip()
    #         core.wait(0.2)
    #
    #         men_align_images[rand1].autoDraw = False
    #         win.flip()
    #         core.wait(0.4)
    #
    #         men_align_images[rand1].draw()
    #         print(men_align_images[rand1].image)
    #         win.flip()
    #
    #         flag = True
    #         while flag:
    #             keys = event.getKeys(keyList=['a', 'l'])
    #             for key in keys:
    #                 if key == 'a':
    #                     # print('correct')
    #                     flag = False
    #                 else:
    #                     # print('wrong')
    #                     flag = False
    #
    #     if gender_random == 0:
    #         print('con-same-al-f')
    #         f_counter += 1
    #         rand1 = random.randint(0, 19)
    #         women_align_images[rand1].draw()
    #         print(women_align_images[rand1].image)
    #         win.flip()
    #         core.wait(0.2)
    #
    #         women_align_images[rand1].autoDraw = False
    #         win.flip()
    #         core.wait(0.4)
    #
    #         women_align_images[rand1].draw()
    #         print(women_align_images[rand1].image)
    #         win.flip()
    #
    #         flag = True
    #         while flag:
    #             keys = event.getKeys(keyList=['a', 'l'])
    #             for key in keys:
    #                 if key == 'a':
    #                     #write to table
    #                     # print('correct')
    #                     flag = False
    #                 else:
    #                     #write to table
    #                     flag = False


    # def CongruentDifferentAlign(name):
    #
    #     fixationPoint.draw()
    #     win.flip()
    #     core.wait(0.2)
    #
    #     fixationPoint.autoDraw = False
    #     win.flip()
    #     core.wait(0.15)
    #
    #     gender_random = random.randint(0, 100) % 2
    #
    #     if gender_random == 0:
    #         print('con-dif-al-f')
    #         rand1 = random.randint(0, 19)
    #         women_align_images[rand1].draw()
    #         print(women_align_images[rand1].image)
    #         win.flip()
    #         core.wait(0.2)
    #
    #         women_align_images[rand1].autoDraw = False
    #         win.flip()
    #         core.wait(0.4)
    #
    #         newLocations = differentLocationsList.DifferentTotalLocationsList(
    #             women_align_locations, women_align_images[rand1].image)
    #
    #         newLocRand = random.randint(0, len(newLocations) - 1)
    #
    #         for item in women_align_images:
    #             if item.image == newLocations[newLocRand]:
    #                 item.draw()
    #                 win.flip()
    #                 print(item.image)
    #                 break
    #
    #
    #         flag = True
    #         while flag:
    #             keys = event.getKeys(keyList=['a', 'l'])
    #             for key in keys:
    #                 if key == 'a':
    #                     #write to table
    #                     # print('a')
    #                     flag = False
    #                 else:
    #                     #write to table
    #                     # print('l')
    #                     flag = False
    #
    #     if gender_random == 1:
    #         print('con-dif-al-m')
    #         rand1 = random.randint(0, 19)
    #         men_align_images[rand1].draw()
    #         print(men_align_images[rand1].image)
    #         win.flip()
    #         core.wait(0.2)
    #
    #         men_align_images[rand1].autoDraw = False
    #         win.flip()
    #         core.wait(0.4)
    #
    #         newLocations = differentLocationsList.DifferentTotalLocationsList(
    #             men_align_locations, men_align_images[rand1].image)
    #
    #         newLocRand = random.randint(0, len(newLocations) - 1)
    #
    #         for item in men_align_images:
    #             if item.image == newLocations[newLocRand]:
    #                 item.draw()
    #                 win.flip()
    #                 print(item.image)
    #                 break
    #
    #         flag = True
    #         while flag:
    #             keys = event.getKeys(keyList=['a', 'l'])
    #             for key in keys:
    #                 if key == 'a':
    #                     # write to table
    #                     # print('a')
    #                     flag = False
    #                 else:
    #                     # write to table
    #                     # print('l')
    #                     flag = False





























