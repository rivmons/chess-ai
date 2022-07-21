class Board:
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR']
        ]
        self.whiteToMove = True
        self.log = []

    def validPawn(self, x, y, moves):
        pass
    
    def validBishop(self, x, y, moves):
        pass

    def validRook(self, x, y, moves):
        pass

    def validKnight(self, x, y, moves):
        pass

    def validQueen(self, x, y, moves):
        pass

    def validKing(self, x, y, moves):
        pass


    def quiescenceCheck(self, move, moves):
        pass

    def getValidMoves(self):
        validMoves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != '':
                    if self.board[i][j][1] == 'p':
                        self.validPawn(i, j, validMoves)
                    if self.board[i][j][1] == 'R':
                        self.validRook(i, j, validMoves)
                    if self.board[i][j][1] == 'B':
                        self.validBishop(i, j, validMoves)
                    if self.board[i][j][1] == 'N':
                        self.validKnight(i, j, validMoves)
                    if self.board[i][j][1] == 'K':
                        self.validKing(i, j, validMoves)
                    if self.board[i][j][1] == 'Q':
                        self.validQueen(i, j, validMoves)

        for move in validMoves:
            self.quiescenceCheck(move, validMoves)

        return validMoves
                    

class Move:
    def __init__(self, start, end, piece):
        self.start = start
        self.end = end
        self.piece = piece

    # debug
    def __str__(self):
        return f'{self.piece}: (start: {self.start}), (end: {self.end})'

    def notation(self):
        ranks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return (f'{ranks[self.start[0]]}{str(8-int(self.start[1]))}', 
                f'{ranks[self.end[0]]}{str(8-int(self.end[1]))}')
