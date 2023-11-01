import pygame
from roquet import Roquet


class Alien(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.velocity = 3
        self.flag = True

    def launch_roquet(self):
        roquet = Roquet(game=self.game)
        self.game.all_roquets.add(roquet)
        roquet.rect.x = self.rect.x + 35
        roquet.rect.y = self.rect.y + 50


    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.remove_alien()

    def remove_alien(self):
        self.game.all_aliens.remove(self)

    def move(self):
        # Moveset of aliens: by using the booleen flag we can alternate with two directions: going left, going right
        if self.rect.x > 0 and self.flag:
            self.rect.x -= 1
        elif self.rect.x < 720 and self.flag == False:
            self.rect.x += 1
        elif self.rect.y <= 500:
            self.rect.y += 50
            self.flag = not self.flag # Each time the aliens move down we switch direction

        if self.rect.y >=500:
            self.game.is_playing = False




class Green(Alien):
    def __init__(self, x, y, game):
        super().__init__(game)

        self.image = pygame.image.load("assets/green.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 1

class Yellow(Alien):
    def __init__(self, x, y, game):
        super().__init__(game)

        self.image = pygame.image.load("assets/yellow.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 1


class Red(Alien):
    def __init__(self, x, y, game):
        super().__init__(game)

        self.image = pygame.image.load("assets/red.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 1
