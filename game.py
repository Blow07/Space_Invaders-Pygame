import time

import pygame
import random
from player import Player
from alien import Green, Red, Yellow
from sound import SoundManager


class Game:
    def __init__(self):

        self.is_playing = False
        self.score = 0
        self.font = pygame.font.Font("assets/Preahvihear-Regular.ttf", 16)
        self.sound_manager = SoundManager()

        # Generate player
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)

        # Generate Missiles and roquets
        self.all_missiles = pygame.sprite.Group()
        self.all_aliens = pygame.sprite.Group()
        self.all_roquets = pygame.sprite.Group()

        self.pressed = {}
        self.flag = 0

    def check_victory(self):
        if len(self.all_aliens) == 0:
            self.game_over()

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        self.erase()
        self.is_playing = False
        self.sound_manager.stop("bg2")


    def check_collisions(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def make_aliens(self):
        # Making the green line
        for x in range(100, 700, 50):
            green = Green(x=x, y=50, game=self)
            self.all_aliens.add(green)

        # Making the yellow line
        for x in range(100, 700, 50):
            yellow = Yellow(x=x, y=100, game=self)
            self.all_aliens.add(yellow)

        # Making the red line
        for x in range(100, 700, 50):
            red = Red(x=x, y=150, game=self)
            self.all_aliens.add(red)

        # Remaking the green line
        for x in range(100, 700, 50):
            green = Green(x=x, y=200, game=self)
            self.all_aliens.add(green)

    def erase(self):
        #Overwrite on the sprites
        self.all_players = pygame.sprite.Group()
        self.all_missiles = pygame.sprite.Group()
        self.all_aliens = pygame.sprite.Group()
        self.all_roquets = pygame.sprite.Group()

    def start(self, player_number):
        self.erase()
        self.is_playing = True
        self.player = Player(self, player_number=player_number)
        self.all_players.add(self.player)
        self.player.fill_attack_bar()

        self.make_aliens()

    def update(self, screen):

        if self.is_playing:
            # Write the score
            scored_text = self.font.render(f"Score: {self.score}", 2, (0, 0, 0))
            screen.blit(scored_text, (20, 10))

            # Apply the player image
            screen.blit(self.player.image, self.player.rect)

            # Apply the missiles images and the aliens images and the roquets images
            self.all_missiles.draw(screen)
            self.all_aliens.draw(screen)
            self.all_roquets.draw(screen)

            # Refresh the live bar of the player and the attack bar
            self.player.update_health_bar(screen)
            self.player.update_attack_bar(screen)

            # Handling the movements of the player
            if self.pressed.get(pygame.K_UP) and self.player.rect.y >= 500:
                self.player.move_up()

            if self.pressed.get(pygame.K_DOWN) and self.player.rect.y <= 600:
                self.player.move_down()

            if self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= 0:
                self.player.move_left()

            if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width <= screen.get_width():
                self.player.move_right()

            for missile in self.all_missiles:
                missile.forward()

            for alien in self.all_aliens:
                alien.move()
                chance = random.randint(1, 1500)
                if chance == 50:
                    alien.launch_roquet()

            for roquet in self.all_roquets:
                velocity = random.randint(3, 4)
                roquet.forward(velocity, screen)

            self.check_victory()

        else:
            self.game_over()



