import random
import os

from psychopy import core, event
from Window import window
from MainAssets import MainAssets
from Target_Men_Misalign import Target_Men_Misalign
from Probe_Men_Misalign import Probe_Men_Misalign
from Target_Women_Misalign import Target_Women_Misalign
from Probe_Women_Misalign import Probe_Women_Misalign

image = MainAssets()
fixationPoint = image.fixationPoint
questionMark = image.questionMark

window = window()
win = window.win

event.globalKeys.clear()
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

class SameMisaligned(object):
    def SameMisaligned(self):
        for i in range(1, 6):
            #Men
            fixationPoint.draw()
            win.flip()
            core.wait(0.2)

            fixationPoint.autoDraw = False
            win.flip()
            core.wait(0.15)

            targetRand = random.randint(0, 4)
            # print('target is ' + str(targetRand))

            Target_Men_Misalign().target_men_misalign_images[targetRand].draw()
            win.flip()
            core.wait(0.2)

            Target_Men_Misalign().target_men_misalign_images[targetRand].autoDraw = False
            win.flip()
            core.wait(0.4)

            probeRand = random.randint(0, 24)
            # print('probe is ' + str(probeRand))

            Probe_Women_Misalign().probe_women_misalign_images[probeRand].draw()
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

            Probe_Men_Misalign().probe_men_misalign_images[probeRand].autoDraw = False
            win.flip()

            # Women
            fixationPoint.draw()
            win.flip()
            core.wait(0.2)

            fixationPoint.autoDraw = False
            win.flip()
            core.wait(0.15)


            Target_Women_Misalign().target_women_misalign_images[targetRand].draw()
            win.flip()
            core.wait(0.2)

            Target_Women_Misalign().target_women_misalign_images[targetRand].autoDraw = False
            win.flip()
            core.wait(0.4)

            Probe_Women_Misalign().probe_women_misalign_images[probeRand].draw()
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

            Probe_Women_Misalign().probe_women_misalign_images[probeRand].autoDraw = False
            win.flip()

