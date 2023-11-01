"""import pygame


pygame.init()

# Paramètres de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balle Lancée")

# Couleurs
white = (255, 255, 255)
red = (255, 0, 0)

# Paramètres de la balle
ball_radius = 20
ball_color = red
ball_x = width // 2
ball_y = height - ball_radius
ball_velocity_x = 5
ball_velocity_y = -10
gravity = 0.5
bounce_factor = 0.7

# Boucle de jeu
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour de la position de la balle
    ball_x += ball_velocity_x
    ball_velocity_y += gravity
    ball_y += ball_velocity_y

    # Rebond sur les bords
    if ball_x <= ball_radius or ball_x >= width - ball_radius:
        ball_velocity_x *= -1
    if ball_y >= height - ball_radius:
        ball_y = height - ball_radius
        ball_velocity_y *= -bounce_factor

    # Effacer l'écran
    screen.fill(white)

    # Dessiner la balle
    pygame.draw.circle(screen, ball_color, (ball_x, int(ball_y)), ball_radius)

    # Mise à jour de l'affichage
    pygame.display.flip()

    clock.tick(60)

pygame.quit()"""
import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width = 800
height = 600

# Couleurs
white = (255, 255, 255)
blue = (0, 0, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Missile Game')

# Paramètres du rectangle (missile)
missile_width = 20
missile_height = 10
missile_x = 100
missile_y = height - missile_height

# Vitesse du missile
missile_speed = 5

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement du missile
    missile_x += missile_speed

    # Effacer l'écran
    screen.fill(white)

    # Dessiner le missile
    pygame.draw.rect(screen, blue, (missile_x, missile_y, missile_width, missile_height))

    # Rafraîchir l'écran
    pygame.display.flip()

    # Limiter le taux de rafraîchissement
    pygame.time.Clock().tick(60)

# Quitter Pygame
pygame.quit()
sys.exit()


