import pygame

pygame.init()

res = (800, 800)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("GoalKeeper")

width = screen.get_width() 
height = screen.get_height() 

play = True

while play:
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit()     
    # updates the frames of the game 
    pygame.display.update() 
pygame.quit()