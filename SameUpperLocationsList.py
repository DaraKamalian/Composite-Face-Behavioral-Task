class SameUpperLocationsList(object):
    def SameUpperLocationsList(self, list, string):

        rightIndex = string[-8:-6]

        for item in list:
            if item[-8:-6] == rightIndex:
                list.remove(item)

        return list
