import glob

from psychopy import visual
from Window import window

window = window()
win = window.win

class Men_Align(object):
    locations = glob.glob('Images/align-men/*.*')
    men_align_images = []
    men_align_locations = []
    for location in locations:
        men_align_locations.append(location)
        men_align_images.append(visual.ImageStim(win, image=location, units='pix', pos=[-40, 80], size=(256, 256)))



