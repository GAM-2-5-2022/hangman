import pygame
import sys
import random
from pygame.locals import *


def draw_btns(BUTTONS):
    for button,letter in BUTTONS:
        btn_text = btn_font.render(letter, True, BLACK)
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, BLACK, button, 2)
        screen.blit(btn_text, btn_text_rect)


def display_guess():
    display_word = ''

    for letter in WORD:
        if letter in GUESSED:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    text = letter_font.render(display_word, True, BLACK)
    screen.blit(text, (400, 200))


pygame.init()
WIDTH, HEIGHT = 1100, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman sa metal bendovima")

game_over = False

# boje
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)

# slike
IMAGES = []
hangman_satus = 0

for i in range(7):
    image = pygame.image.load(f"Slike_Hangman/hangman{i}.png")
    IMAGES.append(image)


# botuni
ROWS = 2
COLS = 13
GAP = 20
SIZE = 40
BOXES = []

for row in range(ROWS):
    for col in range(COLS):
        x = ((GAP * col) + GAP) + (SIZE * col)
        y = ((GAP * row) + GAP) + (SIZE * row) + 330
        box = pygame.Rect(x,y,SIZE,SIZE)
        BOXES.append(box)

A = 65
BUTTONS = []

for ind, box in enumerate(BOXES):
    letter = chr(A+ind)
    button = ([box, letter])
    BUTTONS.append(button)

# font
btn_font = pygame.font.SysFont('arial', 30)
letter_font = pygame.font.SysFont('arial', 60)
game_font = pygame.font.SysFont('arial', 80)


# rijec
rijeci = ['SUFFOCATION','GOJIRA','SEPULTURA','MAYHEM','BATHORY','FERVENT']
WORD = random.choice(rijeci)
GUESSED = []

# naslov
title = "Hangman sa metal bendovima"
title_text = game_font.render(title, True, BLACK)
title_text_rect = title_text.get_rect(center=(WIDTH//2,title_text.get_height()//2+10))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            clicked_pos = event.pos

            for button, letter in BUTTONS:
                if button.collidepoint(clicked_pos):
                    GUESSED.append(letter)

                    if letter not in WORD:
                        hangman_satus += 1

                    if hangman_satus == 6:
                        game_over = True

                    BUTTONS.remove([button, letter])

    screen.fill(BLUE)
    screen.blit(IMAGES[hangman_satus], (150,100))
    screen.blit(title_text, title_text_rect)
    draw_btns(BUTTONS)
    display_guess()

    won = True

    for letter in WORD:
        if letter not in GUESSED:
            won = False

    if won:
        game_over = True
        display_text = 'Pobijedio si !!!'
    else:
        display_text = 'Izgubio si !!!'

    pygame.display.update()

    if game_over:
        screen.fill(BLUE)
        game_over_text = game_font.render(display_text, True, BLACK)
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2))
        screen.blit(game_over_text, game_over_text_rect)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()
