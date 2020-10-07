import random

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align

image = MainAssets()
fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

#Men Congruent Same
class Congruent_Same_Aligned(object):
    def CongruentSameAligned(name):
        for i in range(1, 11):
            fixationPoint.draw()
            win.flip()
            core.wait(0.2)

            fixationPoint.autoDraw = False
            win.flip()
            core.wait(0.15)

            rand1 = random.randint(0, 19)
            Men_Align().men_align_images[rand1].draw()
            win.flip()
            core.wait(0.2)

            Men_Align().men_align_images[rand1].autoDraw = False
            win.flip()
            core.wait(0.4)

            for location in Men_Align().men_align_locations:
                temp = location[-11:-6]
                for i in range(0, 19):
                    if temp == Men_Align().men_align_images[i].image:
                        Men_Align().men_align_images[i].draw()
                        win.flip()
                        print('here')
                        break


            flag = True
            while flag:
                keys = event.getKeys(keyList=['a', 'l'])
                for key in keys:
                    if key == 'a':
                        print('correct')
                        flag = False
                    else:
                        flag = False








