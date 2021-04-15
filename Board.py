class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def setPosition(self, playerSymbol, move):
        if 0 <= move <= 8:
            if self.board[move] == " ":
                self.board[move] = playerSymbol
                return True
            else:
                print("Space is already occupied")
                return False
        else:
            print("Move out of bounds!")
            return False

    def clearBoard(self):
        self.board = [" " for _ in range(9)]

    def drawBoard(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.board[0], self.board[1], self.board[2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.board[3], self.board[4], self.board[5]))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("\t  {}  |  {}  |  {}".format(self.board[6], self.board[7], self.board[8]))
        print("\t     |     |")
        print("\n")