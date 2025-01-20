import sys
import pygame

border_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

class Border(pygame.sprite.Sprite):
    def __init__(self, group, x1, y1, x2, y2):
        super().__init__(group)
        self.image = pygame.image.load('../../images/for_levels/platform.png').convert()
        self.image = pygame.transform.scale(self.image, (x2 - x1, y2 - y1))
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1

class Player(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.image.load('../../images/character/character1/walk/Walk_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 5

    def update(self):
        if not pygame.sprite.spritecollideany(self, border_group):
            self.rect.y += self.velocity_y

pygame.init()
size = width, height = 1066, 600
screen = pygame.display.set_mode(size)

background = pygame.image.load('../../images/for_levels/background/background1.png').convert()

Border(border_group, 400, 500, 500, 600)
player = Player(player_group, 450, 200)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    player_group.update()
    screen.blit(background, (0, 0))
    border_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)
