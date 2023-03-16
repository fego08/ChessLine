class Piece:
    '''Class that defines the different pieces'''

    def __init__(self, is_alive=bool, can_promote=bool, in_check=bool, can_castle=bool, position=tuple):

        self.is_alive = is_alive
        self.can_promote = can_promote
        self.in_check = in_check
        self.can_castle = can_castle
        self.position = position

class Pawn(Piece):
    '''A Pawn'''

    def __init__(self):
           super().__init__(self, is_alive=bool, can_promote=True, position=tuple)
           self.symbol = 'p'

class Rook(Piece):
    '''A Rook'''

    def __init__(self):
           super().__init__(self, is_alive=bool, can_castle=bool, position=tuple)
           self.symbol = 'R'

class Knight(Piece):
    '''A Knight, but how does it move?'''

    def __init__(self):
           super().__init__(self, is_alive=bool, position=tuple)
           self.symbol = 'N'

class Bishop(Piece):
    '''A Bishop'''

    def __init__(self):
           super().__init__(self, is_alive=bool, position=tuple)
           self.symbol = 'B'

class Queen(Piece):
    '''A Queen'''

    def __init__(self):
           super().__init__(self, is_alive=bool, position=tuple)
           self.symbol = 'Q'

class King(Piece):
    '''The King'''

    def __init__(self):
           super().__init__(self, is_alive=bool, in_check=bool, can_castle=bool, position=tuple)
           self.symbol = 'K'


