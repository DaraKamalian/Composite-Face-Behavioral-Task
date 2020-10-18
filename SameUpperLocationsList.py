class SameUpperLocationsList(object):
    def SameUpperLocationsList(self, mylist, string):

        rightIndex = string[-8:-6]
        leftIndex = string[-11:-9]
        list = []

        for item in mylist:
            if item[-11:-9] == leftIndex and item[-8:-6] != rightIndex :
                print('added : ' + str(item))
                list.append(item)

        return list
