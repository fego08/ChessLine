class Board:
    '''Makes a Chessboard'''

    def __init__(self, player):

        self.player = player

    def square(self, coordinates):
        '''Defines a square and its coordinates'''
        self.coordinates = coordinates
        pass

    def draw_board(self):
        '''Draws the 64 Squares'''
        pass
