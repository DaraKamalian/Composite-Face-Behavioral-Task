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

# Men Congruent Same
class Congruent_Same_Aligned(object):
    def CongruentSameAligned(name):
        same_counter = 0
        different_counter = 0
        for i in range(1, 11):
            fixationPoint.draw()
            win.flip()
            core.wait(0.2)

            fixationPoint.autoDraw = False
            win.flip()
            core.wait(0.15)

            same_rand = random.randint(0, 100) % 2

            # 0 -> different, 1 -> same

            if same_rand == 1 and same_counter == 5:
                same_rand = 0
            if same_rand == 0 and different_counter == 5:
                same_rand = 1

            gender_random = random.randint(0, 1)
            # 0 -> female, 1 -> male

            if same_rand == 1 and gender_random == 1:
                print('same')
                same_counter += 1

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

            if same_rand == 1 and gender_random == 0:
                print('same')
                same_counter += 1

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
                            #write to table
                            # print('correct')
                            flag = False
                        else:
                            #write to table
                            flag = False

            if same_rand == 0 and gender_random == 0:
                print('different')
                different_counter += 1

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
                            #write to table
                            # print('a')
                            flag = False
                        else:
                            #write to table
                            # print('l')
                            flag = False

            if same_rand == 0 and gender_random == 1:
                print('different')
                different_counter += 1
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



























