import pygame

pygame.init()

screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GoalKeeper")

play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
pygame.quit()