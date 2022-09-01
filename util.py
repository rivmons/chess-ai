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
        self.checkmate = False
        self.stalemate = False
        self.whiteToMove = True
        self.log = []
        self.wK = (7, 4)
        self.bK = (0, 4)
        self.wKCastle = True
        self.bKCastle = True
        self.wKSCastle = True
        self.wQSCastle = True
        self.bKSCastle = True
        self.bQSCastle = True


    def validPawn(self, x, y, moves):
        enPassant = False
        if len(self.log) > 0:
            enPassant = self.log[-1].epPossible
        if self.whiteToMove:
            if self.board[x - 1][y] == '':
                moves.append(Move((x, y), (x - 1, y), self.board))
                if x == 6 and self.board[x - 2][y] == '':
                    moves.append(Move((x, y), (x - 2, y), self.board, epPossible=(x - 1, y)))
            if y > 0 and self.board[x - 1][y - 1] != '' and self.board[x - 1][y - 1][0] == 'b': # left
                moves.append(Move((x, y), (x - 1, y - 1), self.board))
            if y > 0 and self.board[x - 1][y - 1] == '' and enPassant == (x - 1, y - 1):
                moves.append(Move((x, y), (x - 1, y - 1), self.board, epMade=True))
            if y < 7 and self.board[x - 1][y + 1] != '' and self.board[x - 1][y + 1][0] == 'b': # right
                moves.append(Move((x, y), (x - 1, y + 1), self.board))
            if y < 7 and self.board[x - 1][y + 1] == '' and enPassant == (x - 1, y + 1):
                moves.append(Move((x, y), (x - 1, y + 1), self.board, epMade=True))
        else: 
            if self.board[x + 1][y] == '':
                moves.append(Move((x, y), (x + 1, y), self.board))
                if x == 1 and self.board[x + 2][y] == '':
                    moves.append(Move((x, y), (x + 2, y), self.board, epPossible=(x + 1, y)))
            if y > 0 and self.board[x + 1][y - 1] != '' and self.board[x + 1][y - 1][0] == 'w': # left
                moves.append(Move((x, y), (x + 1, y - 1), self.board))
            if y > 0 and self.board[x + 1][y - 1] == '' and enPassant == (x + 1, y - 1):
                moves.append(Move((x, y), (x + 1, y - 1), self.board, epMade=True))
            if y < 7 and self.board[x + 1][y + 1] != '' and self.board[x + 1][y + 1][0] == 'w': # right
                moves.append(Move((x, y), (x + 1, y + 1), self.board))
            if y < 7 and self.board[x + 1][y + 1] == '' and enPassant == (x + 1, y + 1):
                moves.append(Move((x, y), (x + 1, y + 1), self.board, epMade=True))
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
                            if self.board[dx][dy] != '':
                                lockEdge[(i, j)] = True
                            continue
                        else:
                            lockEdge[(i, j)] = True
        return moves

    def validRook(self, x, y, moves):
        dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        # i = x
        # j = y
        # piece = self.board[x][y][0]
        # while i > 0:
        #     i -= 1
        #     if self.board[i][y] == '' or self.board[i][y][0] != piece:
        #         moves.append(Move((x, y), (i, y), self.board))
        #     else: break
        # i = x
        # while i < 7:
        #     i += 1
        #     if self.board[i][y] == '' or self.board[i][y][0] != piece:
        #         moves.append(Move((x, y), (i, y), self.board))
        #     else: break

        # while j > 0:
        #     j -= 1
        #     if self.board[x][j] == '' or self.board[x][j][0] != piece:
        #         moves.append(Move((x, y), (x, j), self.board))
        #     else: break
        # j = y
        # while j < 7:
        #     j += 1
        #     if self.board[x][j] == '' or self.board[x][j][0] != piece:
        #         moves.append(Move((x, y), (x, j), self.board))
        #     else: break
        # return moves
        piece = self.board[x][y][0]
        lockEdge = {
            (i[0], i[1]): False
            for i in dir
        }
        for n in range(1, 8):
            if all([v for k, v in lockEdge.items()]):
                break
            for i in dir:
                if lockEdge[(i[0], i[1])]:
                    continue
                dx = (i[0] * n) + x
                dy = (i[1] * n) + y
                if dx < 8 and dx >= 0 and dy >= 0 and dy < 8:
                    if self.board[dx][dy] == '' or self.board[dx][dy][0] != piece:
                        moves.append(Move((x, y), (dx, dy), self.board))
                        if self.board[dx][dy] != '':
                            lockEdge[(i[0], i[1])] = True
                        continue
                    else:
                        lockEdge[(i[0], i[1])] = True
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

    def validCastle(self, x, y, moves):
        piece = self.board[x][y][0]
        if piece == "w" and self.wKCastle:
            if self.wKSCastle and (self.board[7][5] == '' and self.board[7][6] == ''):
                for i in range(2):
                    if not self.pieceSafe(7, 5 + i):
                        break
                    if i == 1:
                        moves.append(Move((x, y), (7, 6), self.board, castleMade=True))
            if self.wQSCastle and (self.board[7][1] == '' and self.board[7][2] == '' and self.board[7][3] == ''):
                for i in range(3):
                    if not self.pieceSafe(7, 3 - i):
                        break
                    if i == 2:
                        moves.append(Move((x, y), (7, 2), self.board, castleMade=True))
        elif piece == "b" and self.bKCastle:
            if self.bKSCastle and (self.board[0][5] == '' and self.board[0][6] == ''):
                for i in range(2):
                    if not self.pieceSafe(0, 5 + i):
                        break
                    if i == 1:
                        moves.append(Move((x, y), (0, 6), self.board, castleMade=True))
            if self.bQSCastle and (self.board[0][1] == '' and self.board[0][2] == '' and self.board[0][3] == ''):
                for i in range(3):
                    if not self.pieceSafe(0, 3 - i):
                        break
                    if i == 2:
                        moves.append(Move((x, y), (0, 2), self.board, castleMade=True))

    def quiescenceCheck(self, move, moves):
        self.move(move)
        self.whiteToMove = not self.whiteToMove
        if self.attacked():
            moves.remove(move)
        self.whiteToMove = not self.whiteToMove
        self.undo()

    def pieceSafe(self, x, y):
        self.whiteToMove = not self.whiteToMove
        altMoves = self.getValidMoves(False)
        self.whiteToMove = not self.whiteToMove
        for move in altMoves:
            if move.eRow == x and move.eCol == y:
                return False
        return True

    def attacked(self):
        x, y = 0, 0
        if self.whiteToMove:
            x, y = self.wK[0], self.wK[1]
        else:
            x, y = self.bK[0], self.bK[1]
        self.whiteToMove = not self.whiteToMove
        altMoves = self.getValidMoves(False)
        self.whiteToMove = not self.whiteToMove
        for move in altMoves:
            if move.eRow == x and move.eCol == y:
                return True
        return False

    def getValidMoves(self, eval):
        validMoves = []
        piece = "w" if self.whiteToMove else "b"
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != '' and self.board[i][j][0] == piece:
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
                        if eval:
                            self.validCastle(i, j, validMoves)
                    if self.board[i][j][1] == 'Q':
                        self.validQueen(i, j, validMoves)
        if eval:
            for n in range(len(validMoves) - 1, -1, -1):
                self.quiescenceCheck(validMoves[n], validMoves)

        if len(validMoves) == 0:
            if self.attacked():
                self.checkmate = True
            else: self.stalemate = True
        return validMoves

    def move(self, move):
        promoted = False
        castled = False
        if (move.piece == "wp" and move.eRow == 0) or (move.piece == "bp" and move.eRow == 7):
            self.board[move.sRow][move.sCol] = f'{move.piece[0]}Q'
            self.promotions.append(move)
            promoted = True
        if move.piece[1] == "K":
            if self.whiteToMove: self.wK = (move.eRow, move.eCol)
            else: self.bK = (move.eRow, move.eCol)
        self.board[move.eRow][move.eCol], self.board[move.sRow][move.sCol] = self.board[move.sRow][move.sCol], ''                    
        self.whiteToMove = not self.whiteToMove
        self.log.append(move)

        if move.epMade:
            self.board[move.sRow][move.eCol] = ''

        if move.castleMade:
            if move.sRow == 7:
                if move.eCol == 6:
                    self.board[7][7], self.board[7][5] = "", "wR"
                    self.wKSCastle = False
                if move.eCol == 2:
                    self.board[7][0], self.board[7][3] = "", "wR"
                    self.wQSCastle = False
                self.wKCastle = False
            if move.sRow == 0:
                if move.eCol == 6:
                    self.board[0][7], self.board[0][5] = "", "bR"
                    self.bKSCastle = False
                if move.eCol == 2:
                    self.board[0][0], self.board[0][3] = "", "bR"
                    self.bQSCastle = False
                self.bKCastle = False
            castled = True
        return {"promoted": promoted, "castled": castled}

    def undo(self):
        if len(self.log) > 0:
            move = self.log.pop()
            self.board[move.sRow][move.sCol], self.board[move.eRow][move.eCol] = move.piece, move.captured
            self.whiteToMove = not self.whiteToMove
            if move.epMade:
                type = "b" if self.whiteToMove else "w"
                self.board[move.sRow][move.eCol] = f'{type}p'
            if move.castleMade:
                if move.sRow == 7:
                    if move.eCol == 6:
                        self.board[7][7], self.board[7][5] = "wR", ""
                        self.wKSCastle = True
                    if move.eCol == 2:
                        self.board[7][0], self.board[7][3] = "wR", ""
                        self.wQSCastle = True
                    self.wKCastle = True
                if move.sRow == 0:
                    if move.eCol == 6:
                        self.board[0][7], self.board[0][5] = "bR", ""
                        self.bKSCastle = True
                    if move.eCol == 2:
                        self.board[0][0], self.board[0][3] = "bR", ""
                        self.bQSCastle = True
                    self.bKCastle = True
            if move.piece[1] == "K":
                if self.whiteToMove: self.wK = (move.sRow, move.sCol)
                else: self.bK = (move.sRow, move.sCol)
            self.checkmate = False
            self.stalemate = False
                    

class Move:
    def __init__(self, start, end, board, epPossible=(), epMade=False, castleMade=False):
        self.sRow = start[0]
        self.sCol = start[1]
        self.eRow = end[0]
        self.eCol = end[1]
        self.piece = board[self.sRow][self.sCol]
        self.captured = board[self.eRow][self.eCol]
        self.epPossible = epPossible
        self.epMade = epMade
        self.castleMade = castleMade
        self.id = f'{self.sRow + self.sCol * 1000}{self.piece}{self.captured}{self.eRow + self.eCol * 10}'

    def __str__(self):
        return f'{self.piece}: {self.notation()[0]}{self.notation()[1]}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.id == other.id

    def notation(self):
        ranks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return (f'{ranks[self.sCol]}{str(8-int(self.sRow))}', 
                f'{ranks[self.eCol]}{str(8-int(self.eRow))}')
