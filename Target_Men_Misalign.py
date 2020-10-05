from psychopy import visual
from Window import window

window = window()
win = window.win

class Target_Men_Misalign(object):
    Target_Men_Mis_01 = visual.ImageStim(win, image='Images/target-face-misalign/target-men-misalign/R_09_09_M.bmp',
                                          pos=[0, 0],
                                          units='pix', size=[226.768, 272.12])
    Target_Men_Mis_02 = visual.ImageStim(win, image='Images/target-face-misalign/target-men-misalign/R_10_10_M.bmp',
                                         pos=[0, 0],
                                         units='pix', size=[226.768, 272.12])
    Target_Men_Mis_03 = visual.ImageStim(win, image='Images/target-face-misalign/target-men-misalign/R_11_11_M.bmp',
                                         pos=[0, 0],
                                         units='pix', size=[226.768, 272.12])
    Target_Men_Mis_04 = visual.ImageStim(win, image='Images/target-face-misalign/target-men-misalign/R_12_12_M.bmp',
                                         pos=[0, 0],
                                         units='pix', size=[226.768, 272.12])
    Target_Men_Mis_05 = visual.ImageStim(win, image='Images/target-face-misalign/target-men-misalign/R_14_14_M.bmp',
                                         pos=[0, 0],
                                         units='pix', size=[226.768, 272.12])
