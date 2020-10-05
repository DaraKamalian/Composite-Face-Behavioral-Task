import glob

from psychopy import visual
from Window import window

window = window()
win = window.win

class Probe_Men_Misalign(object):
    locations = glob.glob('Images/probe-face-misalign/probe-men-misalign/*.*')
    probe_men_misalign_images = []
    for location in locations:
        probe_men_misalign_images.append(visual.ImageStim(win, image=location, pos=[0, 0], units='pix',
                                                        size=[226.768, 272.12]))



