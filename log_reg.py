import pygame
import sys
import sqlite3

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

# Функция для подключения к базе данных
def connect_db():
    conn = sqlite3.connect('game.sqlite')
    return conn

# Получить всех пользователей
def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM user")
    users = cursor.fetchall()
    conn.close()
    return [user[0] for user in users]

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
    for idx, user in enumerate(users):
        if user:
            user_text = font.render(str(user), True, WHITE)
            screen.blit(user_text, (100, user_list_start_y + idx * 40))

            # Кнопка "Играть"
            play_button = pygame.Rect(300, user_list_start_y + idx * 40, 100, 25)
            pygame.draw.rect(screen, GREEN, play_button)
            play_button_text = font.render('Играть', True, WHITE)
            screen.blit(play_button_text, (play_button.x + 15, play_button.y + 5))

    pygame.display.flip()


# экран регистрации
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

    screen.blit(character1_image, (200, 120))  # Персонаж 1
    screen.blit(character2_image, (450, 120))  # Персонаж 2
    screen.blit(character3_image, (700, 120))  # Персонаж 3

    button1 = pygame.Rect(200, 330, 150, 40)
    button2 = pygame.Rect(450, 330, 150, 40)
    button3 = pygame.Rect(700, 330, 150, 40)

    # Изменение цвета кнопок в зависимости от выбранного персонажа
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

# Функция для добавления пользователя в базу данных
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
    character_id = 0  # Изначально персонаж не выбран
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
                    user_list_start_y = 150  # Начальная позиция для списка пользователей
                    for idx, user in enumerate(users):
                        play_button = pygame.Rect(300, user_list_start_y + idx * 30, 100, 25)
                        if play_button.collidepoint(mouse_pos):
                            print(f"Игрок {user} выбрал 'Играть'")
                            current_screen = 'main'

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
                        # Регистрируем пользователя
                        if username_text and character_id != 0:  # Убедимся, что логин не пустой
                            register_user(username_text, character_id)
                            print(f"Пользователь {username_text} зарегистрирован с персонажем {character_id}")
                            username_text = ''
                            character_id = 0  # Сбросим выбор персонажа после регистрации
                            current_screen = 'main'

                    else:
                        active_input = None

            if event.type == pygame.KEYDOWN:
                if current_screen == 'register' and active_input:
                    if event.key == pygame.K_BACKSPACE:
                        username_text = username_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if username_text and character_id != 0:
                            register_user(username_text, character_id)
                            print(f"Пользователь {username_text} зарегистрирован!")
                            username_text = ''
                            character_id = 0
                            current_screen = 'main'

                    else:
                        username_text += event.unicode

        # отображение нужного экрана
        if current_screen == 'main':
            draw_main_screen()
        elif current_screen == 'login':
            draw_login_screen()
        elif current_screen == 'register':
            draw_register_screen(username_text, character_id)

        clock.tick(30)

if __name__ == '__main__':
    main()
