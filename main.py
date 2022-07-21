import pygame
import sys

from util import Board, Move

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

def main():

    cboard = Board()
    board = cboard.board
    whiteToMove = cboard.whiteToMove

    pygame.init()
    clock = pygame.time.Clock()
    running = True
    drag = False

    genPieces()
    drawBoard(board, None, None, None)
    piece = []

    while running:
        y, x = [i//dimension for i in pygame.mouse.get_pos()]
        posX, posY = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                y, x = [i//dimension for i in pygame.mouse.get_pos()]
                if board[x][y] != '':
                    if whiteToMove and board[x][y][0] == 'w':
                        drag = True
                        piece = [x, y]
                        pass
                    elif not whiteToMove and board[x][y][0] == 'b':
                        drag = True
                        piece = [x, y]
                        pass
            elif e.type == pygame.MOUSEBUTTONUP:
                if drag:
                    y, x = [i//dimension for i in pygame.mouse.get_pos()]

                    move = Move((piece[1], piece[0]), (y, x), board[piece[0]][piece[1]])
                    # validMoves = cboard.getValidMoves()

                    # cboard.log.append((board[piece[0]][piece[1]], move.notation()[0], move.notation()[1]))

                    # validate captures with class method
                    # log moves, Move class?
                    board[x][y], board[piece[0]][piece[1]] = board[piece[0]][piece[1]], board[x][y]                    

                    piece = []
                    drag = False
                    whiteToMove = not whiteToMove
                    drawBoard(board, None, None, None)

        if drag:
            drawBoard(board, piece, posX - 20, posY - 20)
            
        pygame.display.flip()
        clock.tick(60)

main()