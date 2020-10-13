import glob

from psychopy import visual
from Window import window

window = window()
win = window.win

class Women_Align(object):
    locations = glob.glob('Images/align-women/*.*')
    women_align_images = []
    women_align_locations = []
    for location in locations:
        women_align_locations.append(location)
        women_align_images.append(visual.ImageStim(win, image=location, units='pix',pos=[-40, 80], size=(256, 256)))
