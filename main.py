# main.py
import pgzrun
import time
from hero import Hero
from enemy import Enemy, check_collision
import pygame.mixer
from pygame import Rect

pygame.mixer.init()

WIDTH = 800
HEIGHT = 600

# Game states
MENU = 0
GAME = 1
game_state = MENU

# Menu elements
menu_items = ["Começar o Jogo", "Música: Ligada", "Sair"]
menu_y_positions = [HEIGHT // 2 - 50, HEIGHT // 2, HEIGHT // 2 + 50]
menu_font_size = 40
menu_color = (255, 255, 255)
selected_item = 0

# Game variables
hero = Hero((WIDTH // 2, HEIGHT // 2))
enemies = [
    Enemy((100, 100), (50, 150, 50, 150)),
    Enemy((700, 500), (650, 750, 450, 550))
]
last_time = time.time()
game_over = False
keys_pressed = set()
music_enabled = True
can_take_damage = True
damage_cooldown = 3.0
last_damage_time = 0.0

# Audio
music_files = [
    'c:/roguelike_game/music/background_music.mp3',
    'c:/roguelike_game/music/background_music'
]
music_loaded = False

for music_file in music_files:
    try:
        pygame.mixer.music.load(music_file)
        print(f"Música carregada com sucesso: {music_file}")
        music_loaded = True
        break
    except pygame.error as e:
        print(f"Erro ao carregar música {music_file}: {e}")

if not music_loaded:
    print("Nenhum arquivo de música encontrado!")

if music_loaded:
    pygame.mixer.music.play(-1)

collision_sound = None
try:
    collision_sound = pygame.mixer.Sound('c:/roguelike_game/sounds/collision.wav')
    print("Som de colisão carregado com sucesso!")
except pygame.error as e:
    print(f"Erro ao carregar som de colisão: {e}")

# Background loading
background = Actor('background')
background.pos = (WIDTH // 2, HEIGHT // 2)

def update():
    global last_time, game_over, game_state, music_enabled, can_take_damage, last_damage_time

    if music_enabled and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)

    current_time = time.time()
    dt = current_time - last_time
    last_time = current_time

    if game_state == GAME:
        print("Game state é GAME")
        if not game_over:
            print("Game not over")
            hero.update(dt, keys_pressed)
            print(f"Hero position: {hero.actor.pos}")

            for enemy in enemies:
                enemy.update(dt, hero.actor.pos)
                print(f"Enemy position: {enemy.actor.pos}")

            collision = check_collision(hero, enemies)
            print(f"Collision detected: {collision}")

            if collision:
                print("Colisão detectada!")
                if can_take_damage:
                    hero.health -= 1
                    print(f"Vida do herói após colisão: {hero.health}")
                    can_take_damage = False
                    last_damage_time = current_time
                    if collision_sound:
                        collision_sound.play()
                    if hero.health <= 0:
                        print("Vida do herói chegou a zero ou menos!")
                        game_over = True
                        print("game_over = True definido!")
            else:
                if current_time - last_damage_time > damage_cooldown:
                    can_take_damage = True
    elif game_state == MENU:
        pass

def draw():
    global menu_items
    screen.clear()

    if game_state == MENU:
        background.draw()
        screen.draw.text("Meu Jogo Roguelike", center=(WIDTH // 2, HEIGHT // 3), fontsize=60, color=menu_color)
        for i, item in enumerate(menu_items):
            color = menu_color
            if i == selected_item:
                color = (255, 255, 0)
            screen.draw.text(item, center=(WIDTH // 2, menu_y_positions[i]), fontsize=menu_font_size, color=color)
    elif game_state == GAME:
        background.draw()
        if game_over:
            screen.draw.text("Game Over!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="red")
        else:
            hero.draw()
            for enemy in enemies:
                enemy.draw()
        screen.draw.text(f"Vida: {hero.health}", topright=(WIDTH - 10, 10), fontsize=30, color="white")

def on_key_down(key):
    global selected_item, game_state, music_enabled, menu_items
    if game_state == MENU:
        if key == keys.UP:
            selected_item = (selected_item - 1) % len(menu_items)
        elif key == keys.DOWN:
            selected_item = (selected_item + 1) % len(menu_items)
        elif key == keys.RETURN:
            if selected_item == 0:
                game_state = GAME
                if music_enabled and not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play(-1)
            elif selected_item == 1:
                music_enabled = not music_enabled
                menu_items[1] = "Música: Ligada" if music_enabled else "Música: Desligada"
                if music_enabled:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            elif selected_item == 2:
                quit()
    elif game_state == GAME:
        keys_pressed.add(key)

def on_key_up(key):
    if game_state == GAME:
        if key in keys_pressed:
            keys_pressed.remove(key)

def on_mouse_down(pos):
    global game_state, music_enabled, menu_items
    if game_state == MENU:
        for i, y_pos in enumerate(menu_y_positions):
            text_rect = Rect(0, 0, WIDTH, menu_font_size)
            text_rect.center = (WIDTH // 2, y_pos)
            if text_rect.collidepoint(pos):
                if i == 0:
                    game_state = GAME
                    if music_enabled and not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play(-1)
                elif i == 1:
                    music_enabled = not music_enabled
                    menu_items[1] = "Música: Ligada" if music_enabled else "Música: Desligada"
                    if music_enabled:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                elif i == 2:
                    quit()

pgzrun.go()