


ROWS = boardsize
SHIP = "░"
HITSHIP = "█"



class GameBoard:
    def __init__(self, board):
        self.board = board



def get_letter-to-numbers():
    letters_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7. "I":8, "J":9, "K":10} 
    return letters_to_numbers

  
def print_board(self):
    print(" A B C D E F G H I J K")
    print(" +-+-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in self.board
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1  


class Battleship
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5)
            self.x_row, self-y_column = random.randint(0, 9), random.randint(0, 9)
                while self.board[self.x_row][self.y_cloumn] == "░":
                    self.x_row, self.y_cloumn = random.randint(0, 9), random.randint(0, 9)
                self.board[self.x_row][self.y_column] ="░"
        return self.board













class boardSIX:
    def __init__(self, SHIP, name = ""):
        self.board = [[SHIP] * COLUMNS for _ in range(ROWS)]
        self.name = name
        self.symbol = SHIP
        self.hits = 0


def buildboard(str, boardsize):
    """
    Function for setting up users board
    at game start
    """
    
    
