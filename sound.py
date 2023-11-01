import pygame


class SoundManager:
    def __init__(self):
       self.sounds = {
            "click": pygame.mixer.Sound("sounds/click.wav"),
            "game_over": pygame.mixer.Sound("sounds/game_over.wav"),
            "meteorite": pygame.mixer.Sound("sounds/meteorite.wav"),
            "tir": pygame.mixer.Sound("sounds/tir.wav"),
            "bg1": pygame.mixer.Sound("sounds/bleeps-and-bloops-classic-arcade-game-116838.mp3"),
            "bg2": pygame.mixer.Sound("sounds/play-again-classic-arcade-game-116820.mp3"),
            "damage": pygame.mixer.Sound("sounds/damage.wav")
        }


    def play(self, name):
        self.sounds[name].play()

    def stop(self, name):
        self.sounds[name].stop()
