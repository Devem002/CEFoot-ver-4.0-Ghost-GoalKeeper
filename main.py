import pygame, sys
import teams_page as T
import draw_text as D

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

res = (800, 800)
main_font = pygame.font.SysFont(None, 50)
regular_font = pygame.font.SysFont(None, 30)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("GoalKeeper")

width = screen.get_width() 
height = screen.get_height() 

#click = False

def main_menu():
    play = True
    while play:

        screen.fill((56, 172, 113))
        D.draw_Text("Main Menu", main_font, (255,255,255), screen, 20,20)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(20, 100, 200, 50)
        button_2 = pygame.Rect(20, 200, 200, 50)


        if button_1.collidepoint((mx, my)):
            if click:
                T.Teams()
                #Teams()
        if button_2.collidepoint((mx, my)): 
            if click:
                print("Boton 2")

        pygame.draw.rect(screen, (0,0,0), button_1)
        pygame.draw.rect(screen, (0,0,0), button_2)

        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True     


        pygame.display.update() 
        mainClock.tick(60)

main_menu()