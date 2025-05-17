import pygame
import random

WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20

pygame.font.init()
FONT = pygame.font.SysFont("Consolas", 20) # Ou toute autre police que vous aimeriez
score = 0

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialiser pygame
pygame.init()

# Configuration de l'affichage
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Mise en place de l'horloge
clock = pygame.time.Clock()

# Initialisation du serpent et de la nourriture
snake_pos = [[WIDTH // 2, HEIGHT // 2]]
snake_speed = [0, BLOCK_SIZE]

teleport_walls = True