class InvalidNumberException(Exception):

    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)

    def __str__(self):
        return f'ERROR {self.msg}'


class EmptyBoardException(Exception):

    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)

    def __str__(self):
        return f'ERROR {self.msg}'


class FullBoardException(Exception):

    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)

    def __str__(self):
        return f'ERROR {self.msg}'


class NoSuchDominoException(Exception):

    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)

    def __str__(self):
        return f'ERROR {self.msg}'

# all the exception throw an error with the message ERROR + the messge we dicided to raise in each case.
# each case have is own type of exception
