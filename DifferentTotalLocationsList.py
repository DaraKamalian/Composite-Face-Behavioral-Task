class DifferentTotalLocationsList(object):
    def different_total_locations_list(self, list, string):

        leftIndex = string[-11:-9]
        rightIndex = string[-8:-6]

        for item in list:
            if item[-11:-9] == leftIndex:
                list.remove(item)

        for item in list:
            if item[-8:-6] == rightIndex:
                list.remove(item)

        return list
