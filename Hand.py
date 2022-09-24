from Collection import Collection
from Exceptions import NoSuchDominoException


class Hand(Collection):  # inheritance domino

    def __init__(self, dominoes):  # define all the fields in hand by using inheritance of domino
        super().__init__(dominoes)

    def add(self, domino, index=None):  # add a domino to the hand
        if index is None:
            self.array.append(domino)
        else:
            self.array.insert(index, domino)

    def remove_domino(self, domino):  # remove domino from a hand and returning the index it's was in the hand
        counter = 0
        if domino not in self.array:
            raise NoSuchDominoException("This domino is not in your hand")
        for i in self.array:
            if i == domino:
                self.array.remove(i)
                return counter
            counter += 1

    def __eq__(self, other):  # check if 2 hands are equal by checking if 2 hands have the same dominoes in the same order

        counter = 0
        if not isinstance(other, Hand):
            return False
        if len(self.array) != len(other.array):
            return False
        for i in range(0, len(self.array)):
            if self.array[i] == other.array[i]:
                counter += 1
        if counter == len(self.array):
            return True
        else:
            return False

    def __ne__(self, other):  # check if 2 dominoes are different by using the eq method

        if self.array == other.array:
            return False
        else:
            return True

    def __str__(self):  # print all the dominoes in the hand without black spaces

        if not self.array:
            return '[]'
        text_to_print = ''
        for i in self.array:
            text_to_print += str(i)
        return text_to_print
