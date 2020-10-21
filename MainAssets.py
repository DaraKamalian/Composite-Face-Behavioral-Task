from psychopy import visual
from Window import window

window = window()
win = window.win

class MainAssets(object):
    questionMark = visual.ImageStim(win, image='Images/questionMark.png', pos=[-10, 80], units='pix', size=[140, 210])
    correct = visual.ImageStim(win, image='Images/correct.png', pos=[-10, 80], units='pix', size=[80, 80])
    wrong = visual.ImageStim(win, image='Images/wrong.png', pos=[-10, 80], units='pix', size=[80, 80])
    fixationPoint = visual.ImageStim(win, image='images/fixationPoint.png', pos=[-10, 120], units='pix', size=[300, 400])
    firstversion_SameA_firstInstructionImage = visual.ImageStim(win, image='images/instruction-same-A-1.jpg', pos=[-40, 45],
                                                   units='pix',
                                                   size=[1200, 720])
    firstversion_SameL_firstInstructionImage = visual.ImageStim(win, image='images/instruction-same-L-1.jpg',
                                                                pos=[-40, 45],
                                                                units='pix',
                                                                size=[1200, 720])
    secondInstruction_SameL_Image = visual.ImageStim(win, image='images/instruction-same-L-3.jpg', pos=[-40, 45],
                                             units='pix',
                                             size=[1200, 720])

    secondInstruction_SameA_Image = visual.ImageStim(win, image='images/instruction-same-A-3.jpg', pos=[-40, 45],
                                             units='pix',
                                             size=[1200, 720])

    practiceSecondInstructionImage = visual.ImageStim(win, image='images/practice-instruction-2.jpg', pos=[-75, 75],
                                             units='pix',
                                             size=[1200, 720])

    secondversion_SameL_firstInstructionImage = visual.ImageStim(win, image='images/instruction-same L-1-second-version.jpg',
                                                          pos=[-55, 75], units='pix', size=[1200, 720])

    secondversion_SameA_firstInstructionImage = visual.ImageStim(win, image='images/instruction-same A-1-second-version.jpg',
                                                          pos=[-55, 75], units='pix', size=[1200, 720])