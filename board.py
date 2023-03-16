import pieces
import json

class Board:
    '''Makes a Chessboard'''

    def __init__(self):

        self.pawn = pieces.Pawn()
        self.rook = pieces.Rook()
        self.knight = pieces.Knight()
        self.bishop = pieces.Bishop()
        self.queen = pieces.Queen()
        self.king = pieces.King()

    def square(self, coordinates=(chr,int), piece=None):
        '''Defines a square and its coordinates'''
        
        self.coordinates = coordinates
        self.piece = piece
        
        return {
            'coordinates':self.coordinates,
            'piece':self.piece,
        }

    def make_board(self):
        '''Makes the board from squares'''

        self.coord_chars = [chr(97+x) for x in range(8)]
        self.board = []
        for i in range(64):
            
            number = int((i/8)+1)
            char = self.coord_chars[i%len(self.coord_chars)]
            self.board.append(self.square((char,number), piece=None))
        
        # print(self.board[0])
        # print(self.board[1])
        # print(self.board[2])
        # print(self.board[3])
        # print(self.board[4])
        # print(self.board[5])
        # print(self.board[6])
        # print(self.board[7])

    def fill_board(self):
        '''fills the board with a position'''

        self.filled_board = []
        filename = 'start_position.json'
        with open(filename) as f:
            self.filled_board = json.load(f)
        print(self.filled_board[:7])

    def visualize_board(self):
        '''takes data from make_board() and makes it readable'''

        self.make_board()
        self.fill_board()
        self.board_vis = []

        for square in self.board:
            if square['piece'] == None:
                self.board_vis.append(square['coordinates'])
            else:
                self.board_vis.append(square['piece'])
        
        # print(self.board_vis[:8])
        # print(self.board_vis[8:16])
        # print(self.board_vis[16:24])
        # print(self.board_vis[24:32])
        # print(self.board_vis[32:40])
        # print(self.board_vis[40:48])
        # print(self.board_vis[48:56])
        # print(self.board_vis[56:64])
