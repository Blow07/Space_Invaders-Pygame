import pygame
from missile import Missile

class Player(pygame.sprite.Sprite):
    def __init__(self, game, player_number=2):
        super().__init__()

        self.game = game
        self.player_number = player_number
        self.image = pygame.image.load(f"assets/Player{self.player_number}.png")
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 550
        self.velocity = 2
        self.health = 100
        self.max_health = 100
        self.percent = 0

    def add_percent(self):
        if self.percent < 0:
            self.percent *= -1
        self.percent += 0.2

    def is_full_loaded(self):
        return self.percent >= 100

    def fill_attack_bar(self):
        self.percent = 100

    def update_health_bar(self, screen):
        pygame.draw.rect(screen, (60, 63, 60), [self.rect.x-10, self.rect.y+80, self.max_health, 5])
        pygame.draw.rect(screen, (111, 210, 46), [self.rect.x-10, self.rect.y+80, self.health, 5])

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity

    def launch_projectile(self):
        if self.percent > 20:
            missile = Missile(self.game, self.player_number)
            self.game.all_missiles.add(missile)
            self.game.sound_manager.play("tir")

            missile.rect.x = self.rect.x + 10
            missile.rect.y = self.rect.y - 20
            self.percent -= 20

    def update_attack_bar(self, screen):
        self.add_percent()

        if self.percent < 100:
            # barre noir
            pygame.draw.rect(screen, (0, 0, 0), [
                self.rect.x - 10, # axe x
                self.rect.y + 90, # axe y
                100, # longueur de la barre
                5 # épaisseur
            ])
            # barre rouge
            pygame.draw.rect(screen, (187, 11, 11), [
                self.rect.x - 10, # axe x
                self.rect.y + 90, # axe y
                ( 100 / 100 ) * self.percent , # longueur de la barre ( c juste du pourcentage )
                5 # épaisseur
            ])
