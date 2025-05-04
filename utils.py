from pygame import Rect

def check_collision(hero, enemies):
    hero_rect = Rect(hero.actor.x - hero.actor.width / 2, hero.actor.y - hero.actor.height / 2, hero.actor.width, hero.actor.height)
    for enemy in enemies:
        enemy_rect = Rect(enemy.actor.x - enemy.actor.width / 2, enemy.actor.y - enemy.actor.height / 2, enemy.actor.width, enemy.actor.height)
        if hero_rect.colliderect(enemy_rect):
            return True
    return False