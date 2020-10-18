class SameLowerLocationsList(object):
    def SameLowerLocationsList(self, mylist, string):
        leftIndex = string[-11:-9]
        rightIndex = string[-8:-6]
        list = []

        for item in mylist:
            if item[-8:-6] == rightIndex and item[-11:-9] != leftIndex:
                print('added : ' + str(item))
                list.append(item)
        return list
