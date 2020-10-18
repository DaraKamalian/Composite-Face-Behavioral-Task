class DifferentTotalLocationsList(object):
    def different_total_locations_list(self, mylist, string):

        leftIndex = string[-11:-9]
        rightIndex = string[-8:-6]
        list = []

        for item in mylist:
            if item[-11:-9] != leftIndex and item[-8:-6] != rightIndex:
                print('added : ' + str(item))
                list.append(item)
        return list
