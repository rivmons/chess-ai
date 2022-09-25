import pygame
import sys

from util import Board, Move, AI

width, height = 512, 512
dimension = 64
pieceImages = {
    'bB': None,
    'bK': None,
    'bN': None,
    'bp': None,
    'bQ': None,
    'bR': None,
    'wB': None,
    'wK': None,
    'wN': None,
    'wp': None,
    'wQ': None,
    'wR': None
}

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess AI')
pygame.font.init()
font = pygame.font.SysFont('freesansbold.tf', 40)

def drawBoard(board, piece, x, y):
    sqColors = [pygame.color.Color(232, 235, 239), pygame.color.Color(125, 135, 150)]
    currPiece = [None, None]
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(screen, sqColors[(i+j)%2], pygame.Rect(j*dimension, i*dimension, dimension, dimension))

    for k in range(8):
        for v in range(8):
            if board[k][v] != '':
                if piece is not None and (k,v) == (piece[0], piece[1]):
                    currPiece[0] = k
                    currPiece[1] = v
                else:
                    screen.blit(pieceImages[board[k][v]], (v*dimension, k*dimension))

    if currPiece[0] is not None:
        screen.blit(pieceImages[board[currPiece[0]][currPiece[1]]], (x, y))
                    

def genPieces():
    for piece in pieceImages:
        pieceImages[piece] = pygame.image.load(f'static/{piece}.png')

def display(text):
    text = text
    displayText = True

def main():

    gs = Board()
    board = gs.board

    pygame.init()
    clock = pygame.time.Clock()
    running = True
    drag = False
    ai = AI(gs)
    aiToMove = False
    aiMove = None

    genPieces()
    drawBoard(board, None, None, None)
    piece = []
    text = ''

    while running:
        y, x = [i//dimension for i in pygame.mouse.get_pos()]
        posX, posY = pygame.mouse.get_pos()
        if not gs.whiteToMove:
            aiToMove = True
            validMoves = gs.getValidMoves(True)

            # create structures for all pieces representing points and optimal board positions

            aiMove = ai.move(board, validMoves)
            print(f'AI: {aiMove}')
            aiToMove = False
            drawBoard(board, None, None, None)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                y, x = [i//dimension for i in pygame.mouse.get_pos()]
                if board[x][y] != '':
                    if gs.whiteToMove and board[x][y][0] == 'w':
                        drag = True
                        piece = [x, y]
                        pass

            # wont work with current ai functionality; can def another func to undo 2 moves back to player turn
            # if e.type == pygame.KEYDOWN:
            #     gs.undo()
            #     drawBoard(board, None, None, None)
            
            if e.type == pygame.MOUSEBUTTONUP:
                if drag:
                    y, x = [i//dimension for i in pygame.mouse.get_pos()]
                    move = Move((piece[0], piece[1]), (x, y), board)
                    if piece != [move.eRow, move.eCol]:
                        validMoves = gs.getValidMoves(True)
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                val = gs.move(validMoves[i])
                                print(f'Player: {move}')
                                aiToMove = not aiToMove
                                if val["promoted"] == True: 
                                    drawBoard(board, None, None, None)
                                if val["castled"] == True:
                                    drawBoard(board, None, None, None)
                                if move.piece[1] == "K":
                                    if move.piece[0] == "w":
                                        gs.wKCastle = False
                                    elif move.piece[0] == "b":
                                        gs.bKCastle = False
                                if move.piece[1] == "R":
                                    if move.piece[0] == "w":
                                        if move.sRow == 7 and move.sCol == 0 and gs.wQSCastle == True:
                                            gs.wQSCastle = False
                                        elif move.sRow == 7 and move.sCol == 7 and gs.wKSCastle == True:
                                            gs.wKSCastle = False
                                    elif move.piece[0] == "b":
                                        if x == 1 and y == 0 and gs.bQSCastle == True:
                                            gs.bQSCastle = False
                                        elif x == 1 and y == 7 and gs.bKSCastle == True:
                                            gs.bKSCastle = False
                                _check = gs.getValidMoves(True)
                                if gs.checkmate:
                                    text = f'Game over. {"black" if gs.whiteToMove else "white"} won by checkmate'
                                if gs.stalemate:
                                    text = f'Game over. Stalemate.'
                    piece = []
                    drag = False
                    drawBoard(board, None, None, None)

        if drag:
            drawBoard(board, piece, posX - 20, posY - 20)
        if text != '':
            xCoord = 100
            if len(text) > 4:
                xCoord = 10
            textSurface = font.render(text, False, (0, 0, 0))
            screen.blit(textSurface, (xCoord, height / 2))
            
        pygame.display.flip()
        clock.tick(60)

main()