import random

from psychopy import visual, core, event
from Window import window
from MainAssets import MainAssets
from Target_Men_Align import Target_Men_Align
from Probe_Men_Align import Probe_Men_Align
from Target_Women_Align import Target_Women_Align
from Probe_Women_Align import Probe_Women_Align

image = MainAssets()
fixationPoint = image.fixationPoint
questionMark = image.questionMark

targetMenAlign = Target_Men_Align()
probeMenAlign = Probe_Men_Align()
targetWomenAlign = Target_Women_Align()
probeWomenAlign = Probe_Women_Align()

window = window()
win = window.win

class SameAligned(object):
    def SameAligned(self):
        for i in range(1, 6):
            #Men
            fixationPoint.draw()
            win.flip()
            core.wait(0.2)

            fixationPoint.autoDraw = False
            win.flip()
            core.wait(0.15)

            targetRand = random.randint(0, 4)
            print(targetRand)

            targetMenAlign.target_men_align_images[targetRand].draw()
            win.flip()
            core.wait(0.2)

            targetMenAlign.target_men_align_images[targetRand].autoDraw = False
            win.flip()
            core.wait(0.4)

            probeRand = random.randint(0, 24)

            print(probeRand)
            probeMenAlign.probe_men_align_images[probeRand].draw()
            win.flip()
            timer = core.CountdownTimer(2)

            flag = True
            while flag:
                keys = event.getKeys(keyList=['a', 'l'])
                for key in keys:
                    if keys:
                        # write to table
                        print(key)
                        flag = False

                    elif timer.getTime() <= 0:
                        # write to table
                        print('late')
                        flag = False

            probeMenAlign.probe_men_align_images[probeRand].autoDraw = False
            win.flip()

            #Women
            fixationPoint.draw()
            win.flip()
            core.wait(0.2)

            fixationPoint.autoDraw = False
            win.flip()
            core.wait(0.15)



            targetWomenAlign.target_women_align_images[probeRand].draw()
            win.flip()
            core.wait(0.2)

            targetWomenAlign.target_women_align_images[probeRand].autoDraw = False
            win.flip()
            core.wait(0.4)

            probeWomenAlign.probe_women_align_images[probeRand].draw()
            win.flip()
            timer = core.CountdownTimer(2)

            flag = True
            while flag:
                keys = event.getKeys(keyList=['a', 'l'])
                for key in keys:
                    if keys:
                        # write to table
                        print(key)
                        flag = False

                    elif timer.getTime() <= 0:
                        # write to table
                        print('late')
                        flag = False

            probeWomenAlign.probe_women_align_images[probeRand].autoDraw = False
            win.flip()

