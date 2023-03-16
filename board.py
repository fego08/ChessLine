class Board:
    '''Makes a Chessboard'''

    def square(self, coordinates=(chr,int), is_occupied=False):
        '''Defines a square and its coordinates'''
        
        self.coordinates = coordinates
        self.is_occupied = is_occupied
        
        return {
            'coordinates':self.coordinates,
            'is_occupied':self.is_occupied,
        }

    def make_board(self):
        '''Makes the board from squares'''

        self.coord_chars = [chr(97+x) for x in range(8)]
        self.board = []
        for i in range(64):
            
            if i in range(7):
                number = 1
            if i in range(8,15):
                number = 2
            if i in range(16,23):
                number = 3
            if i in range(24,31):
                number = 4
            if i in range(32,39):
                number = 5
            if i in range(40,47):
                number = 6
            if i in range(48,55):
                number = 7
            if i in range(56,63):
                number = 8
            char = self.coord_chars[i%len(self.coord_chars)]
            self.board.append(self.square((char,number), is_occupied=True))
        
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])
        print(self.board[3])
        print(self.board[4])
        print(self.board[5])
        print(self.board[6])
        print(self.board[7])

    def visualize_board(self):
        '''takes data from make_board() and makes it readable'''

        self.make_board()
        self.board_vis = []

        for square in self.board:
            if square['is_occupied'] == False:
                self.board_vis.append(square['coordinates'])
            else:
                self.board_vis.append('x')
        
        # print(self.board_vis[:8])
        # print(self.board_vis[8:16])
        # print(self.board_vis[16:24])
        # print(self.board_vis[24:32])
        # print(self.board_vis[32:40])
        # print(self.board_vis[40:48])
        # print(self.board_vis[48:56])
        # print(self.board_vis[56:64])
