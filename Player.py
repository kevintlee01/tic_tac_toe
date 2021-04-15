class Player:
    def __init__(self, playerNum, playerSymbol):
        self.playerNum = playerNum
        self.playerSymbol = playerSymbol
        self.playerMoves = []
        self.playerWin = False

    def setPlayerMove(self, move):
        if move not in self.playerMoves:
            if 0 <= move <= 8:
                self.playerMoves.append(move)
            else:
                print("Move out of bounds!")
        else:
            print("Move already exists!")

    def getPlayerNum(self):
        return self.playerNum

    def getPlayerMoves(self, player):
        return self.playerMoves

    def setPlayerSymbol(self, playerSymbol):
        self.playerSymbol = playerSymbol

    def getPlayerSymbol(self):
        return self.playerSymbol

    def resetPlayerWin(self):
        self.playerWin = False

    def getPlayerWin(self):
        return self.playerWin

    def checkPlayerWin(self):
        winPositions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        for pos in winPositions:
            if all(y in self.playerMoves for y in pos):
                self.playerWin = True
                return True

        return False

