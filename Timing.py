class Timing(object):
    generaltime = 0

    def addTime(self, time):
        self.generaltime += time
        return self.generaltime

    def setTime(self, time):
        self.generaltime = time

