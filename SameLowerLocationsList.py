class SameLowerLocationsList(object):
    def SameLowerLocationsList(list, string):
        leftIndex = string[-11:-9]

        for item in list:
            if item[-11:-9] == leftIndex:
                list.remove(item)
        return list
