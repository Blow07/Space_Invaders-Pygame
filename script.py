import pygame
from game import Game
from player import *

# Initialization of pygame
pygame.init()

# Making the window
pygame.display.set_caption("Space_invaders")
screen = pygame.display.set_mode((800, 630))
screen_size = screen.get_size()
background2_height = screen.get_width() // 2

# load the icon
icon = pygame.image.load('assets/GameIcon.png')
pygame.display.set_icon(icon)


# Making and adjusting the background images
backgroung_image = pygame.image.load("assets/SpaceInvaders_Background.png")
backgroung_image = pygame.transform.scale(backgroung_image, screen_size)
backgroung_image_building = pygame.image.load("assets/SpaceInvaders_BackgroundBuildings.png")
backgroung_image_building = pygame.transform.scale(backgroung_image_building, (800, background2_height))
logo_image = pygame.image.load("assets/SpaceInvaders_LogoLarge.png")
borders_image = pygame.image.load("assets/SpaceInvaders_Borders.png")
borders_image = pygame.transform.scale(borders_image, (200,50))

# Making and adjusting the players images
player1_image = pygame.image.load("assets/Player1.png")
player1_rect = player1_image.get_rect()
player1_rect.topleft = (550, 450)  # Position de l'image du player 3

player2_image = pygame.image.load("assets/Player2.png")
player2_rect = player2_image.get_rect()
player2_rect.topleft = (100, 500)  # Position de l'image du player 2

player3_image = pygame.image.load("assets/Player3.png")
player3_rect = player3_image.get_rect()
player3_rect.topleft = (300, 400)  # Position de l'image du player 3


# Instance of Game
game = Game()

running = True
while running:

    # Apply the background
    screen.blit(backgroung_image, (0, 0))
    screen.blit(backgroung_image_building, (0, 250))
    screen.blit(borders_image, (0, 0))

    if game.is_playing:
        game.sound_manager.stop("bg1")

        game.update(screen)
    else:
        # For the menu
        game.sound_manager.play("bg1")
        screen.blit(logo_image, (100, 120))
        screen.blit(player1_image, (550, 450))
        screen.blit(player2_image, (100, 500))
        screen.blit(player3_image, (300, 400))



    # Refresh the screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()

        # Handling the buttons
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

            if event.key == pygame.K_ESCAPE:
                game.game_over()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # Handling the player selection
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player2_rect.collidepoint(event.pos):
                game.start(player_number=2)
            elif player3_rect.collidepoint(event.pos):
                game.start(player_number=3)
            elif player1_rect.collidepoint(event.pos):
                game.start(player_number=1)






