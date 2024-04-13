import pygame
import button

pygame.init()

res = (800, 800)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("GoalKeeper")

width = screen.get_width() 
height = screen.get_height() 

play = True

def draw_Text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))


while play:


    screen.fill((56, 172, 113))

    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit()     


    pygame.display.update() 
pygame.quit()