from psychopy import gui
import Config
class dialoguebox(object):
    def showDialogBox(self):
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
        Dlg.addField('Task Version', choices=['Second Face Remaining', 'Second Face Disappearing'])


        ok_data = Dlg.show()

        subjectName = ok_data[0]
        subjectSurname = ok_data[1]
        subjectNumber = ok_data[2]
        experimentDay = ok_data[3]
        subjectGender = ok_data[4]
        subjectAge = ok_data[5]
        stimSite = ok_data[6]
        handedness = ok_data[7]
        respVersion = ok_data[8]
        appVersion = ok_data[9]

        if respVersion == 'Same-A':
            respVersion = 1
        else:
            respVersion = 0

        if appVersion == 'Second Face Remaining':
            appVersion = 1
        else:
            appVersion = 0

        Config.appversion = appVersion
        Config.respversion = respVersion

        subjectInfo = [subjectName, subjectSurname, subjectNumber, subjectAge, subjectGender, handedness, experimentDay,
                       stimSite, respVersion, appVersion]
        return subjectInfo

