from psychopy import gui

class EndMessage(object):
    def displayEndMessage(self):
        Dialog = gui.Dlg(title='Warning', pos=(575, 375))
        Dialog.addText('پایان آزمون')
        Dialog.show()
