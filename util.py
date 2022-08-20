class Board:
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.whiteToMove = True
        self.log = []

    def validPawn(self, x, y, moves):
        if self.whiteToMove:
            if self.board[x - 1][y] == '':
                moves.append(Move((x, y), (x - 1, y), self.board))
                if x == 6 and self.board[x - 2][y] == '':
                    moves.append(Move((x, y), (x - 2, y), self.board))
            if y > 0 and self.board[x - 1][y - 1] != '' and self.board[x - 1][y - 1][0] == 'b':
                moves.append(Move((x, y), (x - 1, y - 1), self.board))
            if y < 7 and self.board[x - 1][y + 1] != '' and self.board[x - 1][y + 1][0] == 'b':
                moves.append(Move((x, y), (x - 1, y + 1), self.board))
        else: 
            if self.board[x + 1][y] == '':
                moves.append(Move((x, y), (x + 1, y), self.board))
                if x == 1 and self.board[x + 2][y] == '':
                    moves.append(Move((x, y), (x + 2, y), self.board))
            if y > 0 and self.board[x + 1][y - 1] != '' and self.board[x + 1][y - 1][0] == 'w':
                moves.append(Move((x, y), (x + 1, y - 1), self.board))
            if y < 7 and self.board[x + 1][y + 1] != '' and self.board[x + 1][y + 1][0] == 'w':
                moves.append(Move((x, y), (x + 1, y + 1), self.board))
        return moves
    
    def validBishop(self, x, y, moves):
        dir = [-1, 1]
        piece = self.board[x][y][0]
        lockEdge = {
            (i, j): False
            for i in dir for j in dir
        }
        for n in range(1, 7):
            if all([v for k, v in lockEdge.items()]):
                break
            for i in dir:
                for j in dir:
                    if lockEdge[(i, j)]:
                        continue
                    dx = (i * n) + x
                    dy = (j * n) + y
                    if dx < 8 and dx >= 0 and dy >= 0 and dy < 8:
                        if self.board[dx][dy] == '' or self.board[dx][dy][0] != piece:
                            moves.append(Move((x, y), (dx, dy), self.board))
                            continue
                        lockEdge[(i, j)] = True
        return moves

    def validRook(self, x, y, moves):
        i = x
        j = y
        piece = self.board[x][y][0]
        while i > 0:
            i -= 1
            if self.board[i][y] == '' or self.board[i][y][0] != piece:
                moves.append(Move((x, y), (i, y), self.board))
            else: break
        i = x
        while i < 7:
            i += 1
            if self.board[i][y] == '' or self.board[i][y][0] != piece:
                moves.append(Move((x, y), (i, y), self.board))
            else: break

        while j > 0:
            j -= 1
            if self.board[x][j] == '' or self.board[x][j][0] != piece:
                moves.append(Move((x, y), (x, j), self.board))
            else: break
        j = y
        while j < 7:
            j += 1
            if self.board[x][j] == '' or self.board[x][j][0] != piece:
                moves.append(Move((x, y), (x, j), self.board))
            else: break
        return moves

    def validKnight(self, x, y, moves):
        dir = [(-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2)]
        piece = self.board[x][y][0]
        for n in dir:
            dx = x + n[0]
            dy = y + n[1]
            if dx >= 0 and dx < 8 and dy >= 0 and dy < 8:
                if self.board[dx][dy] == '' or self.board[dx][dy][0] != piece:
                    moves.append(Move((x, y), (dx, dy), self.board))
        return moves

    def validKing(self, x, y, moves):
        dir = [-1, 0, 1]
        piece = self.board[x][y][0]
        for i in dir:
            for j in dir:
                if i + x < 8 and i + x > 0 and j + y > 0 and j + y < 8:
                    if self.board[i + x][j + y] == '' or self.board[i + x][j + y][0] != piece:
                        moves.append(Move((x, y), (i + x, j + y), self.board))
        return moves

    def validQueen(self, x, y, moves):
        self.validBishop(x, y, moves)
        self.validRook(x, y, moves)

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

        # for move in validMoves:
        #     self.quiescenceCheck(move, validMoves)
        return validMoves
                    

class Move:
    def __init__(self, start, end, board):
        self.sRow = start[0]
        self.sCol = start[1]
        self.eRow = end[0]
        self.eCol = end[1]
        self.piece = board[self.sRow][self.sCol]
        self.captured = board[self.eRow][self.eCol]
        self.id = f'{self.sRow + self.sCol * 1000}{self.piece}{self.captured}{self.eRow + self.eCol * 10}'

    def __str__(self):
        return f'{self.piece}: {self.notation()}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.id == other.id
        return False

    def notation(self):
        ranks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return (f'{ranks[self.sRow]}{str(8-int(self.sCol))}', 
                f'{ranks[self.eRow]}{str(8-int(self.eCol))}')
