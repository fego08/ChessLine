from board import Board

class ChessLine:
    
    def __init__(self):
        '''Init Class for ChessLine'''

        self.player = {
            'color':'white',
            'name':'name',
            'time_left':['hours', 'minutes', 'seconds']
        }
        self.board = Board()
        self.get_board(game_start=True)

    def get_board(self, game_start=False):

        if game_start==True:

            self.board.square()
            self.board.make_board()
            self.board.visualize_board()

        else:
            self.board.visualize_board()








if __name__ == '__main__':
    cl = ChessLine()
    