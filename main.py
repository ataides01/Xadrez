import pygame
import chess

# CONFIG
WIDTH, HEIGHT = 640, 640
SQ_SIZE = WIDTH // 8

# CORES
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
HIGHLIGHT = (186, 202, 68)

# INICIAR
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xadrez em Python")

# CARREGAR IMAGENS
pieces = {}

def load_images():
    names = ['wp','wr','wn','wb','wq','wk','bp','br','bn','bb','bq','bk']
    for name in names:
        image = pygame.image.load(f"assets/{name}.png")
        pieces[name] = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))

# DESENHAR TABULEIRO
def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# DESENHAR PEÇAS
def draw_pieces(screen, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            row = 7 - (square // 8)
            col = square % 8

            name = piece.symbol()
            color = 'w' if name.isupper() else 'b'
            name = name.lower()

            key = color + name
            screen.blit(pieces[key], (col*SQ_SIZE, row*SQ_SIZE))

# MAIN
def main():
    board = chess.Board()
    load_images()

    selected_square = None
    running = True

    while running:
        draw_board(screen)
        draw_pieces(screen, board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // SQ_SIZE
                row = 7 - (y // SQ_SIZE)
                square = chess.square(col, row)

                if selected_square is None:
                    selected_square = square
                else:
                    move = chess.Move(selected_square, square)

                    if move in board.legal_moves:
                        board.push(move)

                    selected_square = None

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()