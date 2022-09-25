from Exceptions import InvalidNumberException


class Domino:

    def __init__(self, left, right):  # define all the fields in domino
        left_copy = left  # make sure that the user cant change the domino
        right_copy = right
        self.left = left_copy
        self.right = right_copy
        if 6 < self.left or self.left < 0:  # check if the number on each side of the domino is valid
            raise InvalidNumberException("This variable can get values between 0 to 6")
        if self.right < 0 or self.right > 6:
            raise InvalidNumberException("This variable can get values between 0 to 6")

    def get_left(self):   # get the left value of a domino
        return self.left

    def get_right(self):  # get the right value of a domino
        return self.right

    def __str__(self):  # print the domino as presented here:
        return f'[{self.left}|{self.right}]'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):  # check if 2 dominoes are equal by check if its contain the same values
        if self.right == other.right:
            if self.left == other.left:
                return True
        elif self.right == other.left:
            if self.left == other.right:
                return True
        else:
            return False

    def __ne__(self, other):  # check if 2 dominoes are not equal by using the eq method
        if not self.__eq__(other):
            return True
        else:
            return False

    def __gt__(self, other):  # check which domino of the 2 are bigger (domino value determined by sum the right side with the left side
        self_sum = self.right + self.left
        other_sum = other.right + other.left
        if self_sum > other_sum:
            return True
        elif self_sum < other_sum:
            return False
        else:
            return False

    def __contains__(self, key):  # check if the domino contain the key in one of his sides
        if key == self.left or key == self.right:
            return True
        else:
            return False

    def flip(self):  # flipping the domino
        flipped_dom = Domino(self.right, self.left)
        return flipped_dom
 ## i am working hrad to get the results!