import glob
import numpy as np


from psychopy import visual
from Window import window

window = window()
win = window.win

class Target_Men_Align(object):
    locations = glob.glob('Images/target-face-align/target-men-align/*.*')
    target_men_align_images = []
    for location in locations:
        target_men_align_images.append(visual.ImageStim(win, image=location, pos=[0, 0], units='pix',
                                                        size=[226.768, 272.12]))
