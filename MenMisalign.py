import glob

from psychopy import visual
from Window import window

window = window()
win = window.win

class Men_Misalign(object):
    locations = glob.glob('Images/misalign-men/*.*')
    men_misalign_images = []
    men_misalign_locations = []
    for location in locations:
        men_misalign_locations.append(location)
        men_misalign_images.append(visual.ImageStim(win, image=location, units='pix'
                                                    , pos=[-40, 80], size=(320, 256)))