import pygame

class Missile(pygame.sprite.Sprite):
    def __init__(self, game, player_number=2):
        super().__init__()

        self.game = game
        self.player_number = player_number
        self.image = pygame.image.load(f"assets/missile{self.player_number}.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.velocity = 4

    def remove_missile(self):
        self.game.all_missiles.remove(self)

    def forward(self):
        self.rect.y -= self.velocity

        # verifier si le projectile est en collision
        for alien in self.game.check_collisions(self, self.game.all_aliens):
            self.remove_missile()

            # infliger les dégats
            alien.damage(1)

        if self.rect.y <= 0:
            self.remove_missile()




