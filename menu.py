import pygame
import sys
from os import walk
from reg_move import draw_game_scene

pygame.init()

WIDTH, HEIGHT = 1066, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Платформер')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (100, 100, 100)

font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 14)
background_image = pygame.image.load('images/for_levels/background/background2.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


def draw_menu(levels) -> {str: pygame.Rect}:
    screen.blit(background_image, (0, 0))

    caption = pygame.Rect(450, 50, 200, 60)

    pygame.draw.rect(screen, BLACK, caption)

    caption_text = font.render('Меню', True, WHITE)
    screen.blit(caption_text, (caption.x + 70, caption.y + 20))
    filenames = next(walk("levels/platforms"), (None, None, []))[2]

    buttons = dict()
    for i in range(len(filenames)):
        x = (i % 6) * 100 + 100
        y = (i // 6) * 100 + 150
        button = pygame.Rect(x, y, 100, 100)
        if filenames[i][:-5] not in levels:
            pygame.draw.rect(screen, BLACK, button)
        else:
            pygame.draw.rect(screen, (105, 179, 104), button)
        buttons[filenames[i]] = button
        button_text = font.render(filenames[i].rstrip(".json"), True, WHITE)
        screen.blit(button_text, (x + 40, y + 40))

    pygame.display.flip()
    return buttons


def menu(id, levels, id_user):
    clock = pygame.time.Clock()
    buttons: {str: pygame.Rect} = draw_menu(levels)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for key, value in buttons.items():
                    mouse_pos = event.pos
                    if value.collidepoint(mouse_pos):
                        draw_game_scene(id, key[:-5], id_user)

        clock.tick(30)


if __name__ == '__main__':
    menu(1, [], 0)
