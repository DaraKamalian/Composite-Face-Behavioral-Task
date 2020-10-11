class DifferentTotalLocationsList(object):
    def different_total_locations_list(self, mylist, string):

        leftIndex = string[-11:-9]
        rightIndex = string[-8:-6]
        list = []

        for item in mylist:
            if item[-11:-9] == leftIndex:
                list.append(item)

            if item[-8:-6] == rightIndex:
                list.append(item)

        for member in list:
            if member in mylist:
                mylist.remove(member)
        return mylist
