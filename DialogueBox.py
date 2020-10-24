from psychopy import gui
import Config
class dialoguebox(object):
    def showDialogBox(self):
        subjectInfo = []
        flag = True
        while flag:
            Dlg = gui.Dlg(title="Composite Face Task", pos=(525, 250))
            Dlg.addField('Subject First Name')
            Dlg.addField('Subject Surname')
            Dlg.addField('Subject Number')
            Dlg.addField('Experiment Day', choices=['1', '2', '3'])
            Dlg.addField('Gender', choices=['Male', 'Female'])
            Dlg.addField('Age')
            Dlg.addField('Stimulation Site', choices=['R-PPC', 'L-PPC', 'CZ'])
            Dlg.addField('Handedness', choices=['Right', 'Left'])
            Dlg.addField('Resp Version ', choices=['Same-A', 'Same-L'])
            Dlg.addField('Task Version', choices=['1', '2'])
            ok_data = Dlg.show()

            if Dlg.OK:
                if Config.validateFields(ok_data):
                    subjectName = ok_data[0]
                    subjectSurname = ok_data[1]
                    subjectNumber = ok_data[2]
                    experimentDay = ok_data[3]
                    subjectGender = ok_data[4]
                    subjectAge = ok_data[5]
                    stimSite = ok_data[6]
                    handedness = ok_data[7]
                    respVersion = ok_data[8]
                    taskVersion = ok_data[9]

                    if respVersion == 'Same-A':
                        Config.respversion = 1
                    elif respVersion == 'Same-L':
                        Config.respversion = 0

                    if taskVersion == '2':
                        Config.taskversion = 1
                    elif taskVersion == '1':
                        Config.taskversion = 0

                    subjectInfo = [subjectName, subjectSurname, subjectNumber, subjectAge, subjectGender, handedness, experimentDay,
                           stimSite, respVersion, taskVersion]
                    flag = False
        return subjectInfo

