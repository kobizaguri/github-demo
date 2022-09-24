from Exceptions import FullBoardException, EmptyBoardException, InvalidNumberException
from Collection import Collection


class Board(Collection):  # inheritance from collection
    def __init__(self, max_capacity, array=[]):  # define all the fields in board
        super().__init__(array)
        self.array = []
        self.max_capacity = max_capacity
        if not 1 <= self.max_capacity <= 28:  # check if the max capacity value is valid
            raise InvalidNumberException("This variable can get values between 1 to 28")

    def in_left(self):  # returning the left value of the leftest domino in the board
        if not self.array:
            raise EmptyBoardException("The board is empty")
        else:
            first_domino = self.array[0]
            return first_domino.left

    def in_right(self):  # returning the right value of the rightest domino in the board
        if not self.array:
            raise EmptyBoardException("The board is empty")
        else:
            last_domino = self.array[-1]
            return last_domino.right

    def add(self, domino, add_to_right=True):  # add the domino to the board. to the right if add_to_right= True else to the left
        if self.max_capacity == len(self.array):
            raise FullBoardException("The board is full")
        elif add_to_right:
            if self.add_right(domino):
                return True

        elif add_to_right is not True:

            if self.add_left(domino):
                return True

        else:
            return False

    def add_left(self, domino):   # add the domino to the left side
        if not self.array:
            self.array.insert(0, domino)
            return True
        flipped_domino = domino.flip()
        if domino.right == self.array[0].left:
            self.array.insert(0, domino)
            return True
        elif flipped_domino.right == self.array[0].left:  # try to add the domino after flipping it.
            self.array.insert(0, flipped_domino)
            return True
        else:
            return False

    def add_right(self, domino): # try to add the domino to the right
        if not self.array:
            self.array.insert(len(self.array), domino)
            return True
        flipped_domino = domino.flip()
        if domino.left == self.array[-1].right:
            self.array.insert(len(self.array), domino)
            return True
        elif flipped_domino.left == self.array[-1].right:  # try to add the domino after flipping it.
            self.array.insert(len(self.array), flipped_domino)
            return True
        else:
            return False

    def get_item(self, i):  # returning the domino in the place we asked
        if i > len(self.array) - 1 or i < -(len(self.array)):
            return None
        else:
            return self.array[i]

    def __contains__(self, key):  # check if the board contain specific domino
        for domino in self.array:
            if domino == key:
                return True
        return False

    def __eq__(self, other):  # checking if to boards are equal
        counter = 0
        if not isinstance(other, Board):  # check that both sides are from board type
            return False
        if len(self.array) != len(other.array):  # check the length of the boards
            return False
        for i in range(0, len(self.array)):
            if self.array[i].left == other.array[i].left and self.array[i].right == other.array[i].right:
                counter += 1
        if self.max_capacity == other.max_capacity and counter == len(self.array):   # make sure that each domino in self equal to each domino in the other board
            return True
        else:
            return False

    def __ne__(self, other):  # check if 2 boards are not equal by using eq method
        if self == other:
            return False
        else:
            return True

    def __str__(self):  # print all the dominos in the board without blank space
        text_to_print = ''
        for i in self.array:
            text_to_print += str(i)
        return text_to_print
