# enemy.py
import time
from pgzero.actor import Actor
from pygame import Rect
import random

class Enemy:
    def __init__(self, pos, patrol_area):
        self.idle_images = ['enemy_idle1', 'enemy_idle2'] # Substitua pelos seus sprites de idle
        self.walk_images = ['enemy_walk1', 'enemy_walk2'] # Substitua pelos seus sprites de movimento
        self.actor = Actor(self.idle_images[0], pos=pos)
        self.patrol_area = Rect(patrol_area)
        self.speed = 50
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])] # Movimento horizontal e vertical inicial
        self.image_index = 0
        self.animation_timer = 0
        self.animation_interval = 0.2
        self.last_move_time = time.time()
        self.move_interval = 1.5 # Tempo entre mudanças de direção

    def update(self, dt, hero_pos):
        current_time = time.time()
        if current_time - self.last_move_time > self.move_interval:
            # Escolhe uma nova direção com alguma probabilidade de manter a direção atual
            if random.random() < 0.8: # 80% de chance de mudar a direção
                self.direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]
            self.last_move_time = current_time

        self.actor.x += self.direction[0] * self.speed * dt
        self.actor.y += self.direction[1] * self.speed * dt

        # Manter dentro da área de patrulha
        if self.actor.left < self.patrol_area.left:
            self.actor.left = self.patrol_area.left
            self.direction[0] = 1
        elif self.actor.right > self.patrol_area.right:
            self.actor.right = self.patrol_area.right
            self.direction[0] = -1
        if self.actor.top < self.patrol_area.top:
            self.actor.top = self.patrol_area.top
            self.direction[1] = 1
        elif self.actor.bottom > self.patrol_area.bottom:
            self.actor.bottom = self.patrol_area.bottom
            self.direction[1] = -1

        # Lógica de animação
        self.animation_timer += dt
        if self.animation_timer >= self.animation_interval:
            self.animation_timer = 0
            if self.direction != [0, 0]:
                self.image_index = (self.image_index + 1) % len(self.walk_images)
                self.actor.image = self.walk_images[self.image_index]
            else:
                self.image_index = (self.image_index + 1) % len(self.idle_images)
                self.actor.image = self.idle_images[self.image_index]

    def draw(self):
        self.actor.draw()

def check_collision(hero, enemies):
    for enemy in enemies:
        if hero.actor.colliderect(enemy.actor):
            return True
    return False