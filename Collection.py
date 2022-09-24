class Collection:

    def __init__(self, array): # define the fields in collection
        self.array = array

    def get_collection(self):  # returning the array
        return self.array

    def add(self, item, option):  # throwing error because this method dont implement in this class
        raise NotImplementedError("To add use the right method")

    def __getitem__(self, i): # get the item in index i of the array
        try:
            return self.array[i]
        except Exception:
            return None

    def __eq__(self, other):  # check if the 2 arrays are equal (of self and other)
        if self.array == other.array:
            return True
        else:
            return False

    def __ne__(self, other): # check if the 2 arrays are not equal (of self and other)
        if self.array != other.array:
            return True
        else:
            return False

    def __len__(self):  # check the length of the array
        counter = 0
        for i in self.array:
            counter += 1
        return counter

    def __contains__(self, item):  # check if the array contain this specific item
        for i in self.array:
            if i == item:
                return True
        return False

    def __str__(self):  # print all the variables in the array as string without blank space
        string_to_return = ''
        for i in self.array:
            string_to_return += str(i)
        return string_to_return

    def __repr__(self):
        return self.__str__()

