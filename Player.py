class Player:
    def __init__(self, playerNum, playerSymbol):
        self.playerNum = playerNum
        self.playerSymbol = playerSymbol
        self.playerMoves = []
        self.playerWin = False
        self.playerScore = 0

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

    def getPlayerMoves(self):
        return self.playerMoves

    def setPlayerSymbol(self, playerSymbol):
        self.playerSymbol = playerSymbol

    def getPlayerSymbol(self):
        return self.playerSymbol

    def getPlayerWin(self):
        return self.playerWin

    def incrementScore(self):
        self.playerScore += 1

    def getPlayerScore(self):
        return self.playerScore

    def playerReset(self):
        self.playerMoves = []
        self.playerWin = False

    def checkPlayerWin(self):
        winPositions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for pos in winPositions:
            if all(y in self.playerMoves for y in pos):
                self.playerWin = True
                return True

        return False

