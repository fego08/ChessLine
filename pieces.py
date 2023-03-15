class Piece:
    '''Class that defines the different pieces'''

    def __init__(
            self,
            piece,
            position,
            is_alive=True, 
            can_promote=False, 
            in_check=False, 
            can_castle=False,
            
    ):
        self.is_alive = is_alive
        self.can_promote = can_promote
        self.in_check = in_check
        self.can_castle = can_castle
        self.position = position
        self.piece = piece
