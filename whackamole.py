import pygame
import random
mole_image = pygame.image.load('mole.png')

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        # mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_x = random.randint(0, WIDTH // SQUARE_SIZE - 1)
                    mole_y = random.randint(0, HEIGHT // SQUARE_SIZE - 1)
            screen.fill("light green")
            draw_grid(screen)
            draw_mole(screen, mole_x, mole_y)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


def draw_grid(screen):
    #draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )
    #draw vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_mole(screen,x,y):
    screen.blit(mole_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))

WIDTH = 640
HEIGHT = 512
LINE_WIDTH = 1
BOARD_ROWS = 16
BOARD_COLS = 20
SQUARE_SIZE = 32
LINE_COLOR = (0, 0, 0)

if __name__ == "__main__":
    main()
