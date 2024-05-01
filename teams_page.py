import pygame
import sys
import reader
import functions as D

pygame.init()
mainClock = pygame.time.Clock()
from pygame.locals import *


data = reader.readData() #obtiene los diccionarios del jason
team1 = data['Teams']['teams'][0] #
team2 = data['Teams']['teams'][1] #Separa los diccionarios  
team3 = data['Teams']['teams'][2] # de acuerdo al equipo
team4 = data['Teams']['teams'][3] #

res = (800, 800)
main_font = pygame.font.SysFont(None, 50) #fuente básica de la pantalla
regular_font = pygame.font.SysFont(None, 30)   #fuente de menor tamaño
screen = pygame.display.set_mode(res)
pygame.display.set_caption("GoalKeeper")


def Teams():
    running = True

    while running:
        
        screen.fill((56, 172, 113))
        D.draw_Text("Teams", main_font,(255,255,255), screen, 20,20)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(20, 100, 200, 50)
        button_2 = pygame.Rect(20, 200, 200, 50)
        button_3 = pygame.Rect(20, 300, 200, 50)
        button_4 = pygame.Rect(20, 400, 200, 50)

        
        if button_1.collidepoint((mx, my)):
            if click:
                #M.main_menu()
                team1_screen()
        if button_2.collidepoint((mx, my)):
            if click:
                team2_screen()
        if button_3.collidepoint((mx, my)):
            if click:
                team3_screen()
        if button_4.collidepoint((mx, my)):
            if click:
                team4_screen()  
        pygame.draw.rect(screen, (0,0,0), button_1)
        pygame.draw.rect(screen, (0,0,0), button_2)
        pygame.draw.rect(screen, (0,0,0), button_3)
        pygame.draw.rect(screen, (0,0,0), button_4)

        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

def team1_screen():
    running = True
    while running:
        screen.fill((56, 172, 113))
 
        #Escribe en pantalla a los jugadores
        D.draw_Text(team1["name"], main_font, (255, 255, 255), screen, 20, 10)
        D.draw_Text("Main Goalkeeper: " + team1["main_goalkeeper"], regular_font, (255,255,255), screen, 20, 80)
        D.draw_Text("Player one: " + team1["player_one"], regular_font, (255,255,255), screen, 20, 120)
        D.draw_Text("Player two: " + team1["player_two"], regular_font, (255,255,255), screen, 20, 160)
        D.draw_Text("Player three: " + team1["player_three"], regular_font, (255,255,255), screen, 20, 200)
        D.draw_Text("Player four: " + team1["player_four"], regular_font, (255,255,255), screen, 20, 240)
        D.draw_Text("Player five :" + team1["player_five"], regular_font, (255,255,255), screen, 20, 280)
        D.draw_Text("Bench Goalkeeper: " + team1["bench_goalkeeper"], regular_font, (255,255,255), screen, 20, 320)
        D.draw_Text("Bench player one : " + team1["bench_one"], regular_font, (255,255,255), screen, 20, 360)
        D.draw_Text("Bench player two : " + team1["bench_two"], regular_font, (255,255,255), screen, 20, 400)
        D.draw_Text("Bench player three : " + team1["bench_three"], regular_font, (255,255,255), screen, 20, 440)
        
        mx, my = pygame.mouse.get_pos()
        exit_button = pygame.Rect(20, 700, 200, 50)
        
        if exit_button.collidepoint((mx, my)):
            if click:
                Teams()
        
        pygame.draw.rect(screen, (0,0,0), exit_button)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def team2_screen():
    running = True
    while running:
        screen.fill((56, 172, 113))
 
         #Escribe en pantalla a los jugadores
        D.draw_Text(team2["name"], main_font, (255, 255, 255), screen, 20, 10)
        D.draw_Text("Main Goalkeeper: " + team2["main_goalkeeper"], regular_font, (255,255,255), screen, 20, 80)
        D.draw_Text("Player one: " + team2["player_one"], regular_font, (255,255,255), screen, 20, 120)
        D.draw_Text("Player two: " + team2["player_two"], regular_font, (255,255,255), screen, 20, 160)
        D.draw_Text("Player three: " + team2["player_three"], regular_font, (255,255,255), screen, 20, 200)
        D.draw_Text("Player four: " + team2["player_four"], regular_font, (255,255,255), screen, 20, 240)
        D.draw_Text("Player five :" + team2["player_five"], regular_font, (255,255,255), screen, 20, 280)
        D.draw_Text("Bench Goalkeeper: " + team2["bench_goalkeeper"], regular_font, (255,255,255), screen, 20, 320)
        D.draw_Text("Bench player one : " + team2["bench_one"], regular_font, (255,255,255), screen, 20, 360)
        D.draw_Text("Bench player two : " + team2["bench_two"], regular_font, (255,255,255), screen, 20, 400)
        D.draw_Text("Bench player three : " + team2["bench_three"], regular_font, (255,255,255), screen, 20, 440)

        mx, my = pygame.mouse.get_pos()
        exit_button = pygame.Rect(20, 700, 200, 50)
        
        if exit_button.collidepoint((mx, my)):
            if click:
                Teams()
        
        pygame.draw.rect(screen, (0,0,0), exit_button)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def team3_screen():
    running = True
    while running:
        screen.fill((56, 172, 113))
 
         #Escribe en pantalla a los jugadores
        D.draw_Text(team3["name"], main_font, (255, 255, 255), screen, 20, 10)
        D.draw_Text("Main Goalkeeper: " + team3["main_goalkeeper"], regular_font, (255,255,255), screen, 20, 80)
        D.draw_Text("Player one: " + team3["player_one"], regular_font, (255,255,255), screen, 20, 120)
        D.draw_Text("Player two: " + team3["player_two"], regular_font, (255,255,255), screen, 20, 160)
        D.draw_Text("Player three: " + team3["player_three"], regular_font, (255,255,255), screen, 20, 200)
        D.draw_Text("Player four: " + team3["player_four"], regular_font, (255,255,255), screen, 20, 240)
        D.draw_Text("Player five :" + team3["player_five"], regular_font, (255,255,255), screen, 20, 280)
        D.draw_Text("Bench Goalkeeper: " + team3["bench_goalkeeper"], regular_font, (255,255,255), screen, 20, 320)
        D.draw_Text("Bench player one : " + team3["bench_one"], regular_font, (255,255,255), screen, 20, 360)
        D.draw_Text("Bench player two : " + team3["bench_two"], regular_font, (255,255,255), screen, 20, 400)
        D.draw_Text("Bench player three : " + team3["bench_three"], regular_font, (255,255,255), screen, 20, 440)

        mx, my = pygame.mouse.get_pos()
        exit_button = pygame.Rect(20, 700, 200, 50)
        
        if exit_button.collidepoint((mx, my)):
            if click:
                Teams()
        
        pygame.draw.rect(screen, (0,0,0), exit_button)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def team4_screen():
    running = True
    while running:
        screen.fill((56, 172, 113))
 
         #Escribe en pantalla a los jugadores
        D.draw_Text(team4["name"], main_font, (255, 255, 255), screen, 20, 10)
        D.draw_Text("Main Goalkeeper: " + team4["main_goalkeeper"], regular_font, (255,255,255), screen, 20, 80)
        D.draw_Text("Player one: " + team4["player_one"], regular_font, (255,255,255), screen, 20, 120)
        D.draw_Text("Player two: " + team4["player_two"], regular_font, (255,255,255), screen, 20, 160)
        D.draw_Text("Player three: " + team4["player_three"], regular_font, (255,255,255), screen, 20, 200)
        D.draw_Text("Player four: " + team4["player_four"], regular_font, (255,255,255), screen, 20, 240)
        D.draw_Text("Player five :" + team4["player_five"], regular_font, (255,255,255), screen, 20, 280)
        D.draw_Text("Bench Goalkeeper: " + team4["bench_goalkeeper"], regular_font, (255,255,255), screen, 20, 320)
        D.draw_Text("Bench player one : " + team4["bench_one"], regular_font, (255,255,255), screen, 20, 360)
        D.draw_Text("Bench player two : " + team4["bench_two"], regular_font, (255,255,255), screen, 20, 400)
        D.draw_Text("Bench player three : " + team4["bench_three"], regular_font, (255,255,255), screen, 20, 440)

        mx, my = pygame.mouse.get_pos()
        exit_button = pygame.Rect(20, 700, 200, 50)
        
        if exit_button.collidepoint((mx, my)):
            if click:
                Teams()
        
        pygame.draw.rect(screen, (0,0,0), exit_button)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
Teams()