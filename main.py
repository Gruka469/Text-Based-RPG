import pygame
import os

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorcerers & Sentinels: A Wordbound Odyssey")

WHITE = (255,255,255)

BG = pygame.transform.scale(pygame.image.load("forest_theme.jpg"), (WIDTH, HEIGHT))
FPS = 60
TEXT_BOX_WIDTH, TEXT_BOXE_HEIGHT = 1000, 225

TEXT_BOX_IMAGE = pygame.image.load(os.path.join('text_box.png'))
TEXT_BOX = pygame.transform.scale(TEXT_BOX_IMAGE, (TEXT_BOX_WIDTH, TEXT_BOXE_HEIGHT))

def draw():
    WIN.blit(BG, (0, 0))
    WIN.blit(TEXT_BOX, (75, 500))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()