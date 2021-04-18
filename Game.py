from Player import Player
from Board import Board

class Game:
    def __init__(self, p1, p2):
        self.p1 = Player(1, p1)
        self.p2 = Player(2, p2)
        self.board = Board()
        self.curr_player = self.p1

    def printPlayerScores(self):
        print("--------------------------------")
        print("       	   SCOREBOARD       ")
        print("--------------------------------")

        print("   Player ", self.p1.getPlayerNum(), "    ", self.p1.getPlayerScore())
        print("   Player ", self.p2.getPlayerNum(), "    ", self.p2.getPlayerScore())

        print("--------------------------------\n")

    def singleRoundGame(self):
        self.board.drawBoard()

        while not self.p1.getPlayerWin() and not self.p2.getPlayerWin():
            try:
                print("Player ", self.curr_player.playerNum, "- Input Box Number: ",  end="")
                move = int(input())
            except ValueError:
                print("Invalid Input")
                continue

            if not self.board.setPosition(self.curr_player.getPlayerSymbol(), move):
                continue

            self.curr_player.setPlayerMove(move)

            self.board.drawBoard()

            if self.curr_player.checkPlayerWin():
                print("Player ", self.curr_player.playerNum, " Wins!\n")
                self.curr_player.incrementScore()
                self.printPlayerScores()

            if self.curr_player == self.p1:
                self.curr_player = self.p2
            else:
                self.curr_player = self.p1

    def playGame(self):
        response = "Y"

        while response == "Y":
            self.singleRoundGame()

            self.p1.playerReset()
            self.p2.playerReset()
            self.board.clearBoard()
            self.curr_player = self.p1

            response = None

            while response == None:
                print("Play again? (Y/N) : ", end="")
                response = input().upper()
                if response == "N":
                    print("Ending Game")
                elif response == "Y":
                    print("Restarting Game")
                else:
                    print("Invalid response. Please try again!")
                    response = None

if __name__ == "__main__":
    options = ["X", "O"]
    player1Symbol = None
    player2Symbol = None

    while not player1Symbol:
        print("Player 1")
        player1Symbol = input("Choose your symbol (X or O): ")
        player1Symbol = player1Symbol.strip().upper()
        if player1Symbol.strip() not in options:
            print("Invalid Symbol")
            player1Symbol = None

    if player1Symbol == "X":
        player2Symbol = "O"
    else:
        player2Symbol = "X"

    print("\nPlayer 2")
    print("Default Symbol To: " + player2Symbol)

    game = Game(player1Symbol, player2Symbol)
    game.playGame()