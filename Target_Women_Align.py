import glob

from psychopy import visual
from Window import window

window = window()
win = window.win

class Target_Women_Align(object):
    locations = glob.glob('Images/target-face-align/target-women-align/*.*')
    target_women_align_images = []
    for location in locations:
        target_women_align_images.append(visual.ImageStim(win, image=location, pos=[0, 0], units='pix',
                                                        size=[226.768, 272.12]))