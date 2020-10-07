import glob

from psychopy import visual
from Window import window

window = window()
win = window.win

class Women_Misalign(object):
    locations = glob.glob('Images/misalign-women/*.*')
    women_misalign_images = []
    for location in locations:
        women_misalign_images.append(visual.ImageStim(win, image=location, pos=[0, 0], units='pix',
                                                        size=[226.768, 272.12]))