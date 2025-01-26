import pygame
import sys
import sqlite3
from menu import *
import json

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

SELECTED = (200, 200, 0)

font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 14)

background_image = pygame.image.load('images/for_levels/background/background2.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

character_id = 0
character1_image = pygame.image.load('images/character/character1/idle/Idle_1.png')
character2_image = pygame.image.load('images/character/character2/idle/Idle_1.png')
character3_image = pygame.image.load('images/character/character3/idle/Idle_1.png')
character1_image = pygame.transform.scale(character1_image, (200, 200))
character2_image = pygame.transform.scale(character2_image, (200, 200))
character3_image = pygame.transform.scale(character3_image, (200, 200))


def connect_db():
    conn = sqlite3.connect('game.sqlite')
    return conn


# Получить всех пользователей
def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username, character_id FROM user")
    users = cursor.fetchall()
    conn.close()
    return users


# главный экран
def draw_main_screen():
    screen.blit(background_image, (0, 0))

    login_button = pygame.Rect(450, 200, 200, 60)
    register_button = pygame.Rect(450, 300, 200, 60)

    pygame.draw.rect(screen, (0, 0, 0), login_button)
    pygame.draw.rect(screen, (0, 0, 0), register_button)

    login_text = font.render('Вход', True, WHITE)
    register_text = font.render('Регистрация', True, WHITE)
    screen.blit(login_text, (login_button.x + 70, login_button.y + 20))
    screen.blit(register_text, (register_button.x + 26, register_button.y + 20))

    pygame.display.flip()


# экран входа
def draw_login_screen():
    screen.fill(BLACK)
    back_button = pygame.Rect(5, 5, 100, 30)
    pygame.draw.rect(screen, BLACK, back_button)
    back_button_text = font.render('← Назад', True, WHITE)
    screen.blit(back_button_text, (back_button.x + 5, back_button.y + 5))

    login_title = font.render('Вход', True, WHITE)
    screen.blit(login_title, (500, 10))

    # Отображение списка пользователей с кнопками "Играть"
    users = get_all_users()
    user_list_start_y = 150
    for idx, (username, _) in enumerate(users):
        if username:
            user_text = font.render(str(username), True, WHITE)
            screen.blit(user_text, (100, user_list_start_y + idx * 40))

            play_button = pygame.Rect(300, user_list_start_y + idx * 40, 100, 25)
            pygame.draw.rect(screen, GREEN, play_button)
            play_button_text = font.render('Играть', True, WHITE)
            screen.blit(play_button_text, (play_button.x + 15, play_button.y + 5))

    pygame.display.flip()


def draw_game_scene(character_id, level_id):
    game_scene_image = pygame.image.load('images/for_levels/background/background1.png')
    game_scene_image = pygame.transform.scale(game_scene_image, (WIDTH, HEIGHT))
    screen.blit(game_scene_image, (0, 0))

    coin_png = pygame.image.load('images/for_levels/coin.png').convert_alpha()
    platform_png = pygame.image.load('images/for_levels/platform.png').convert_alpha()

    animations = {'attack': 0, 'death': 1, 'fallattack': 2, 'hurt': 3, 'idle': 4, 'jump': 5,
                  'jumpattack': 6, 'run': 7, 'runattack': 8, 'squat': 9, 'walk': 10, 'walkattack': 11}

    character_num = str(character_id)
    character_animations = {}
    for action in animations.keys():
        action_images = []
        if action == 'death' or action == 'jump':
            n = 8
        elif action == 'hurt' or action == 'idle' or action == 'squat':
            n = 4
        else:
            n = 6

        for i in range(1, n):
            try:
                image = pygame.image.load(
                    f'images/character/character{character_num}/{action}/{action.capitalize()}_{i}.png').convert_alpha()
                action_images.append(image)
            except pygame.error:
                break
        character_animations[action] = action_images

    characters = [[character_animations[action] for action in animations.keys()]]

    for i in range(len(characters)):
        for j in range(len(characters[i])):
            for w in range(len(characters[i][j])):
                sprite = pygame.sprite.Sprite()
                sprite.image = characters[i][j][w]
                sprite.rect = sprite.image.get_rect()
                sprite.mask = pygame.mask.from_surface(sprite.image)
                sprite.rect.x, sprite.rect.y = 0, 528
                characters[i][j][w] = sprite

    background = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    player = pygame.sprite.Group()
    coords_platform = []

    def create_background(level):
        background.empty()
        coords_platform.clear()

        f = open(f"levels/{level}.json")

        data = json.load(f)
        for i in data["platforms"]:
            platform = pygame.sprite.Sprite()
            platform.image = platform_png
            platform.rect = platform.image.get_rect()
            platform.rect.x, platform.rect.y = i["x"], i["y"]
            platform.mask = pygame.mask.from_surface(platform.image)
            background.add(platform)
            coords_platform.append((i["x"], i["y"]))

        f.close()
        f = open(f"levels_background/{level}.txt")
        image = pygame.image.load(f'images/for_levels/background/background{f.read()}.png').convert_alpha()
        f.close()
        screen.blit(image, (0, 0))
        background.draw(screen)

    def create_coins(level):
        coins.empty()

        f = open(f"levels_coins/{level}.json")

        data = json.load(f)
        for i in data["platforms"]:
            coin = pygame.sprite.Sprite()
            coin.image = coin_png
            coin.rect = coin.image.get_rect()
            coin.rect.x, coin.rect.y = i["x"], i["y"]
            coin.mask = pygame.mask.from_surface(coin.image)
            coins.add(coin)

        f.close()
        coins.draw(screen)

    def change_player(group, animation, stage, x, y, inversion=0):
        try:
            group.remove()
            group.empty()
            if inversion:
                for i in range(len(characters[0])):
                    for j in range(len(characters[0][i])):
                        characters[0][i][j].image = pygame.transform.flip(
                            characters[0][i][j].image, True, False)
            characters[0][animations[animation]][stage].rect.x = x
            characters[0][animations[animation]][stage].rect.y = y
            characters[0][animations[animation]][stage].mask = pygame.mask.from_surface(
                characters[0][animations[animation]][stage].image)
            group.add(characters[0][animations[animation]][stage])
        except Exception:
            pass

    def check_coins():
        for el in coins:
            for player_mask in player:
                if pygame.sprite.collide_mask(el, player_mask):
                    el.kill()

    create_background(level_id)
    create_coins(level_id)

    running = True
    falling_speed = 6
    jump_height = 9
    fps = 60
    clock = pygame.time.Clock()
    player_x, player_y = 0, 528
    is_update = True
    is_jump = False
    is_inversion = False
    is_right = True
    animation = 'idle'
    stage = 0
    count_events = 0
    change_player(player, animation, 0, player_x, player_y)
    player.draw(screen)

    while running:
        events = pygame.key.get_pressed()
        if not is_jump:
            if events[pygame.K_UP] or events[pygame.K_SPACE] or events[pygame.K_w]:
                is_jump = True
                jump_height = 9
                animation = 'jump'
                stage = 0
                count_events += 1
        else:
            stage = (stage + 0.25) % len(characters[0][animations[animation]])
            animation = 'jump'
            if jump_height >= -9:
                if jump_height > 0:
                    player_y -= (jump_height ** 2) / 2
                else:
                    player_y += (jump_height ** 2) / 2
                jump_height -= 1
            else:
                is_jump = False
            is_update = True

        if events[pygame.K_DOWN]:
            pass

        if events[pygame.K_LSHIFT] or events[pygame.K_RSHIFT]:
            is_shift = True
        else:
            is_shift = False

        if (events[pygame.K_RIGHT] or events[pygame.K_d]) and (events[pygame.K_LEFT] or events[pygame.K_a]):
            pass
        elif events[pygame.K_RIGHT] or events[pygame.K_d]:
            count_events += 1
            if not is_jump:
                if is_shift:
                    animation = 'run'
                    player_x += 7
                else:
                    animation = 'walk'
                    player_x += 4
                stage = (stage + 0.25) % len(characters[0][animations[animation]])
            else:
                if is_shift:
                    player_x += 7
                else:
                    player_x += 4
            if is_right:
                is_inversion = False
            else:
                is_inversion = True
            is_right = True
            is_update = True

        elif events[pygame.K_LEFT] or events[pygame.K_a]:
            count_events += 1
            if not is_jump:
                if is_shift:
                    animation = 'run'
                    player_x -= 7
                else:
                    animation = 'walk'
                    player_x -= 4
                stage = (stage + 0.25) % len(characters[0][animations[animation]])
            else:
                if is_shift:
                    player_x -= 7
                else:
                    player_x -= 4
            if is_right:
                is_inversion = True
            else:
                is_inversion = False
            is_right = False
            is_update = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        if is_update:
            intersection = False
            intersection2 = False
            create_background(level_id)
            coins.draw(screen)
            old_x, old_y = 0, 528
            el_y = 0
            for player_mask in player:
                old_x, old_y = player_mask.rect.x, player_mask.rect.y
            change_player(player, animation, int(stage), player_x, player_y, is_inversion)
            is_inversion = False
            for el in background:
                for player_mask in player:
                    if pygame.sprite.collide_mask(el, player_mask):
                        intersection = True
            change_player(player, animation, int(stage), player_x, player_y, is_inversion)
            if intersection:
                player_x, player_y = old_x, old_y
            change_player(player, animation, int(stage), player_x, player_y, is_inversion)
            for el in background:
                for player_mask in player:
                    if pygame.sprite.collide_mask(el, player_mask):
                        if pygame.sprite.collide_mask(el, player_mask)[1] < 2:
                            el_y = el.rect.y - 42
                        else:
                            el_y = player_y
                        intersection2 = True
            if intersection2:
                player_y = el_y
            else:
                player_y += falling_speed
                intersection2 = False
                change_player(player, animation, int(stage), player_x, player_y, is_inversion)
                for el in background:
                    for player_mask in player:
                        if pygame.sprite.collide_mask(el, player_mask):
                            if pygame.sprite.collide_mask(el, player_mask)[1] < 2:
                                el_y = el.rect.y - 42
                            else:
                                el_y = player_y
                            intersection2 = True
                if intersection2:
                    player_y = el_y
            change_player(player, animation, int(stage), player_x, player_y, is_inversion)
            check_coins()
            if (count_events == 0) and not is_jump:
                animation = 'idle'
                stage = (stage + 0.15) % 3
            if player_y >= 624:
                player_x, player_y = 0, 528
                stage = 0
                change_player(player, animation, int(stage), player_x, player_y, is_inversion)
            check_coins()
            player.draw(screen)
            count_events = 0
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


def draw_register_screen(username_text, character_id):
    screen.fill(BLACK)

    back_button = pygame.Rect(5, 5, 100, 30)
    pygame.draw.rect(screen, BLACK, back_button)
    back_button_text = font.render('← Назад', True, WHITE)
    screen.blit(back_button_text, (back_button.x + 5, back_button.y + 5))

    register_title = font.render('Регистрация', True, WHITE)
    screen.blit(register_title, (470, 10))

    # Поле имени пользователя
    username_box = pygame.Rect(80, 70, 950, 30)
    pygame.draw.rect(screen, WHITE, username_box, 2)
    username_input = font.render(f'Имя: {username_text}', True, WHITE)
    screen.blit(username_input, (username_box.x - 55, username_box.y + 6))

    screen.blit(character1_image, (200, 120))
    screen.blit(character2_image, (450, 120))
    screen.blit(character3_image, (700, 120))

    button1 = pygame.Rect(200, 330, 150, 40)
    button2 = pygame.Rect(450, 330, 150, 40)
    button3 = pygame.Rect(700, 330, 150, 40)

    # цвет кнопок
    button1_color = SELECTED if character_id == 1 else GREY
    button2_color = SELECTED if character_id == 2 else GREY
    button3_color = SELECTED if character_id == 3 else GREY

    pygame.draw.rect(screen, button1_color, button1)
    pygame.draw.rect(screen, button2_color, button2)
    pygame.draw.rect(screen, button3_color, button3)

    button1_text = font.render('Выбрать', True, WHITE)
    button2_text = font.render('Выбрать', True, WHITE)
    button3_text = font.render('Выбрать', True, WHITE)

    screen.blit(button1_text, (button1.x + 27, button1.y + 11))
    screen.blit(button2_text, (button2.x + 27, button2.y + 11))
    screen.blit(button3_text, (button3.x + 27, button3.y + 11))

    # Кнопка регистрации
    register_button = pygame.Rect(390, 500, 270, 50)
    pygame.draw.rect(screen, GREEN, register_button)
    register_button_text = font.render('Зарегистрироваться', True, WHITE)
    screen.blit(register_button_text, (register_button.x + 10, register_button.y + 15))

    pygame.display.flip()


# добавление пользователя в бд
def register_user(username, character_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (username, character_id) VALUES (?, ?)", (username, character_id))
    conn.commit()
    conn.close()


def main():
    clock = pygame.time.Clock()
    current_screen = 'main'
    username_text = ''
    character_id = 0
    active_input = None  # 'username'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if current_screen == 'main':
                    login_button = pygame.Rect(450, 200, 200, 60)
                    register_button = pygame.Rect(450, 300, 200, 60)

                    if login_button.collidepoint(mouse_pos):
                        current_screen = 'login'
                    elif register_button.collidepoint(mouse_pos):
                        current_screen = 'register'

                if current_screen == 'login':
                    back_button = pygame.Rect(5, 5, 100, 30)

                    if back_button.collidepoint(mouse_pos):
                        current_screen = 'main'

                    users = get_all_users()
                    user_list_start_y = 150
                    for idx, (username, char_id) in enumerate(users):
                        play_button = pygame.Rect(300, user_list_start_y + idx * 40, 100, 25)
                        if play_button.collidepoint(mouse_pos):
                            character_id = char_id
                            current_screen = 'game_scene'

                if current_screen == 'register':
                    username_box = pygame.Rect(80, 70, 950, 30)
                    register_button = pygame.Rect(390, 500, 270, 50)

                    button1 = pygame.Rect(200, 330, 150, 40)
                    button2 = pygame.Rect(450, 330, 150, 40)
                    button3 = pygame.Rect(700, 330, 150, 40)

                    back_button = pygame.Rect(5, 5, 100, 30)

                    if back_button.collidepoint(mouse_pos):
                        current_screen = 'main'

                    if button1.collidepoint(mouse_pos):
                        if username_text:
                            character_id = 1
                    elif button2.collidepoint(mouse_pos):
                        if username_text:
                            character_id = 2
                    elif button3.collidepoint(mouse_pos):
                        if username_text:
                            character_id = 3

                    if username_box.collidepoint(mouse_pos):
                        active_input = 'username'

                    elif register_button.collidepoint(mouse_pos):
                        if username_text and character_id != 0:
                            register_user(username_text, character_id)
                            current_screen = 'game_scene'
                    else:
                        active_input = None

            if event.type == pygame.KEYDOWN:
                if current_screen == 'register' and active_input:
                    if event.key == pygame.K_BACKSPACE:
                        username_text = username_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if username_text and character_id != 0:
                            register_user(username_text, character_id)
                            current_screen = 'game_scene'
                    else:
                        username_text += event.unicode

        if current_screen == 'main':
            draw_main_screen()
        elif current_screen == 'login':
            draw_login_screen()
        elif current_screen == 'register':
            draw_register_screen(username_text, character_id)
        elif current_screen == 'game_scene':
            menu(character_id)

        clock.tick(30)


if __name__ == '__main__':
    main()
