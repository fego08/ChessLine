import chess

class ChessLine:

    def __init__(self):

        self.board = chess.Board()
        self.board.set_board_fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        print(f'\n{self.board}')


if __name__ == '__main__':
    cl = ChessLine()