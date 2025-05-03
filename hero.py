# hero.py
from pgzero.actor import Actor
from pgzero.builtins import keys

class Hero:
    def __init__(self, pos):
        self.idle_images = ['hero_idle1', 'hero_idle2']
        self.walk_images = ['hero_walk1', 'hero_walk2']
        self.actor = Actor(self.idle_images[0], pos=pos)
        self.image_index = 0
        self.animation_timer = 0
        self.animation_interval = 0.2
        self.speed = 150
        self.velocity = [0, 0]
        self.health = 3  # Vida inicial do herói agora é 3

    def update(self, dt, keys_pressed):
        self.velocity = [0, 0]

        if keys.LEFT in keys_pressed:
            self.velocity[0] = -self.speed
        if keys.RIGHT in keys_pressed:
            self.velocity[0] = self.speed
        if keys.UP in keys_pressed:
            self.velocity[1] = -self.speed
        if keys.DOWN in keys_pressed:
            self.velocity[1] = self.speed

        self.actor.x += self.velocity[0] * dt
        self.actor.y += self.velocity[1] * dt

        self.animation_timer += dt
        if self.animation_timer >= self.animation_interval:
            self.animation_timer = 0
            self.image_index = (self.image_index + 1) % 2
            if self.velocity != [0, 0]:
                self.actor.image = self.walk_images[self.image_index]
            else:
                self.actor.image = self.idle_images[self.image_index]

    def draw(self):
        self.actor.draw()