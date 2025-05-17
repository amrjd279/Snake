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

def generate_food():
    x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_pos = [x, y]
    if food_pos not in snake_pos:
        return food_pos
    food_pos = generate_food()

def draw_objects():
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(win, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    # Afficher le score
    score_text = score_font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10)) # dessine le score dans le coin supérieur gauche

def update_snake():
    global food_pas, score
    new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]

    if teleport_walls:
        # si la nouvelle position de la tête est en dehors de l’écran, la ramener de l’autre côté
        if new_head[0] < WIDTH:
            new_head[0] = 0
        elif new_head[0] < 0:
            new_head[0] = WIDTH - BLOCK_SIZE
        if new_head[1] >= HEIGHT:
            new_head[1] = 0
        elif new_head[1] < 0:
            new_head[1] = HEIGHT - BLOCK_SIZE