import pygame

class Roquet(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.image = pygame.image.load("assets/rocket.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotozoom(self.image, 180, 1)
        self.rect = self.image.get_rect()
        self.velocity = 5

    def remove_roquet(self):
        self.game.all_roquets.remove(self)

    def forward(self, velocity, screen):
        self.rect.y += velocity

        # verifier si le projectile est en collision
        for player in self.game.check_collisions(self, self.game.all_players):
            self.remove_roquet()

            # infliger les dégats
            player.damage(10)

        if self.rect.y > 630:
            self.remove_roquet()


