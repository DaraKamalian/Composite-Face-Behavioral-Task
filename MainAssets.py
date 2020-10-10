from psychopy import visual
from Window import window

window = window()
win = window.win

class MainAssets(object):
    questionMark = visual.ImageStim(win, image='Images/questionMark.png', pos=[-60, 75], units='pix', size=[140, 210])
    correct = visual.ImageStim(win, image='Images/correct.png', pos=[-60, 75], units='pix', size=[80, 80])
    wrong = visual.ImageStim(win, image='Images/wrong.png', pos=[-60, 75], units='pix', size=[80, 80])
    fixationPoint = visual.ImageStim(win, image='images/fixationPoint.png', pos=[-90, 75], units='pix', size=[300, 400])
