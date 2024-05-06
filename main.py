import time
import pygame, sys
import functions as D
from reader import *

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

team_1_game = []
team_2_game = []
teams_gameplay = [[],[]]

res = (1200, 704)
main_font = pygame.font.SysFont(None, 50) #fuente básica de la pantalla
regular_font = pygame.font.SysFont(None, 30) #fuente de menor tamaño
about_font = pygame.font.SysFont(None, 22)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("GoalKeeper")

width = screen.get_width() 
height = screen.get_height() 
image =pygame.image.load("images/FondoPrincipal.gif")
image2 = pygame.image.load("images/Fondo1.gif")

def background_skye (image):
      size = pygame.transform.scale(image,res)
      screen.blit(size,(0,0))

bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

clicked = False

class button():
		
	#colours for button and text
	button_col = (0, 0, 0)
	hover_col = (55, 55, 55)
	click_col = (255, 255, 255)
	text_col = white
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = regular_font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action
      
play = button(60, 120, "Play!")
teams = button(60, 320, "Teams")
about = button(60, 520, "About")
exit = button(960, 520, "Exit")

def main_menu():
    game = True
    brasil_sound = pygame.mixer.Sound("sounds/Brasil.mp3")
    i = 0

    while game:
        if i == 0:
            brasil_sound.set_volume(0.1)
            brasil_sound.play()
            brasil_sound.fadeout(100000)
            i+= 1

        screen.fill((56, 172, 113))
        background_skye(image)
        
        D.draw_Text("Main Menu", main_font, (255,255,255), screen, 60,20)

        if play.draw_button():
             main_play_page()
        if teams.draw_button():
              Teams()
        if about.draw_button():
              about_page()
        if exit.draw_button():
              sys.exit()

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
                    clicked = True     


        pygame.display.update() 
        mainClock.tick(60)

data = readData() #obtiene los diccionarios del jason
team1 = data['Teams']['teams'][0] #
team2 = data['Teams']['teams'][1] #Separa los diccionarios  
team3 = data['Teams']['teams'][2] # de acuerdo al equipo
team4 = data['Teams']['teams'][3] #

def Teams():
    running = True

    while running:
        
        screen.fill((56, 172, 113))
        background_skye(image)
        D.draw_Text("Teams", main_font,white, screen, 60,20)

        team_1 = button(60, 120, team1["name"])
        team_2 = button(60, 220, team2["name"])
        team_3 = button(60, 320, team3["name"])
        team_4 = button(60, 420, team4["name"])
        exit = button(60, 520, "Back to Menu")
        
        if team_1.draw_button():
             team1_screen()
        if team_2.draw_button():
             team2_screen()
        if team_3.draw_button():
             team3_screen()
        if team_4.draw_button():
            team4_screen()
        if exit.draw_button():
            main_menu()
        
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
        background_skye(image2)
        shield = pygame.image.load(team1["shield"])
        screen.blit(shield, (600, 10))
 
        #Escribe en pantalla a los jugadores
        D.draw_Text(team1["name"], main_font, white, screen, 20, 10)
        D.draw_Text("Main Goalkeeper: " + team1["main_goalkeeper"], regular_font, white, screen, 20, 80)
        D.draw_Text("Player one: " + team1["player_one"], regular_font, white, screen, 20, 120)
        D.draw_Text("Player two: " + team1["player_two"], regular_font, white, screen, 20, 160)
        D.draw_Text("Player three: " + team1["player_three"], regular_font, white, screen, 20, 200)
        D.draw_Text("Player four: " + team1["player_four"], regular_font, white, screen, 20, 240)
        D.draw_Text("Player five :" + team1["player_five"], regular_font,white, screen, 20, 280)
        D.draw_Text("Bench Goalkeeper: " + team1["bench_goalkeeper"], regular_font, white, screen, 20, 320)
        D.draw_Text("Bench player one : " + team1["bench_one"], regular_font, white, screen, 20, 360)
        D.draw_Text("Bench player two : " + team1["bench_two"], regular_font, white, screen, 20, 400)
        D.draw_Text("Bench player three : " + team1["bench_three"], regular_font, white, screen, 20, 440)
        
        exit = button (960, 520, "Back to Teams")
        if exit.draw_button():
             Teams()


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
        background_skye(image2)
        shield = pygame.image.load(team2["shield"])
        screen.blit(shield, (700, 10))
 
         #Escribe en pantalla a los jugadores
        D.draw_Text(team2["name"], main_font, white, screen, 20, 10)
        D.draw_Text("Main Goalkeeper: " + team2["main_goalkeeper"], regular_font, white, screen, 20, 80)
        D.draw_Text("Player one: " + team2["player_one"], regular_font, white, screen, 20, 120)
        D.draw_Text("Player two: " + team2["player_two"], regular_font, white, screen, 20, 160)
        D.draw_Text("Player three: " + team2["player_three"], regular_font, white, screen, 20, 200)
        D.draw_Text("Player four: " + team2["player_four"], regular_font, white, screen, 20, 240)
        D.draw_Text("Player five :" + team2["player_five"], regular_font, white, screen, 20, 280)
        D.draw_Text("Bench Goalkeeper: " + team2["bench_goalkeeper"], regular_font, white, screen, 20, 320)
        D.draw_Text("Bench player one : " + team2["bench_one"], regular_font, white, screen, 20, 360)
        D.draw_Text("Bench player two : " + team2["bench_two"], regular_font, white, screen, 20, 400)
        D.draw_Text("Bench player three : " + team2["bench_three"], regular_font, white, screen, 20, 440)

        exit = button (960, 520, "Back to Teams")
        if exit.draw_button():
             Teams()


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
        background_skye(image2)
        shield = pygame.image.load(team3["shield"])
        screen.blit(shield, (700, 10))
 
         #Escribe en pantalla a los jugadores
        D.draw_Text(team3["name"], main_font, white, screen, 20, 10)
        D.draw_Text("Main Goalkeeper: " + team3["main_goalkeeper"], regular_font, white, screen, 20, 80)
        D.draw_Text("Player one: " + team3["player_one"], regular_font, white, screen, 20, 120)
        D.draw_Text("Player two: " + team3["player_two"], regular_font, white, screen, 20, 160)
        D.draw_Text("Player three: " + team3["player_three"], regular_font, white, screen, 20, 200)
        D.draw_Text("Player four: " + team3["player_four"], regular_font, white, screen, 20, 240)
        D.draw_Text("Player five :" + team3["player_five"], regular_font, white, screen, 20, 280)
        D.draw_Text("Bench Goalkeeper: " + team3["bench_goalkeeper"], regular_font, white, screen, 20, 320)
        D.draw_Text("Bench player one : " + team3["bench_one"], regular_font, white, screen, 20, 360)
        D.draw_Text("Bench player two : " + team3["bench_two"], regular_font, white, screen, 20, 400)
        D.draw_Text("Bench player three : " + team3["bench_three"], regular_font, white, screen, 20, 440)

        exit = button (960, 520, "Back to Teams")
        if exit.draw_button():
             Teams()


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
        background_skye(image2)
        shield = pygame.image.load(team4["shield"])
        screen.blit(shield, (700, 10))
 
         #Escribe en pantalla a los jugadores
        D.draw_Text(team4["name"], main_font, white, screen, 20, 10)
        D.draw_Text("Main Goalkeeper: " + team4["main_goalkeeper"], regular_font, white, screen, 20, 80)
        D.draw_Text("Player one: " + team4["player_one"], regular_font, white, screen, 20, 120)
        D.draw_Text("Player two: " + team4["player_two"], regular_font, white, screen, 20, 160)
        D.draw_Text("Player three: " + team4["player_three"], regular_font, white, screen, 20, 200)
        D.draw_Text("Player four: " + team4["player_four"], regular_font, white, screen, 20, 240)
        D.draw_Text("Player five :" + team4["player_five"], regular_font, white, screen, 20, 280)
        D.draw_Text("Bench Goalkeeper: " + team4["bench_goalkeeper"], regular_font, white, screen, 20, 320)
        D.draw_Text("Bench player one : " + team4["bench_one"], regular_font, white, screen, 20, 360)
        D.draw_Text("Bench player two : " + team4["bench_two"], regular_font, white, screen, 20, 400)
        D.draw_Text("Bench player three : " + team4["bench_three"], regular_font, white, screen, 20, 440)

        exit = button (960, 520, "Back to Teams")
        if exit.draw_button():
             Teams()


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


def about_page():
     running = True

     while running:
          
        screen.fill((55,55,55))
        click = False

        D.draw_Text("About", main_font, white,screen, 40, 60 )
        D.draw_Text("Programa creado por Adam , David y Diego", about_font, (255,255,255),screen, 40, 160 )
        D.draw_Text("Creado entre abril y mayo del 2024", about_font, (255,255,255),screen, 40, 210 )
        D.draw_Text("El proyecto corresponde a la materia de: Fundamentos de sistemas computacionales de la carrera ingenieria en computadores del Tecnologico de Costa Rica", about_font, (255,255,255),screen, 40, 260 )
        D.draw_Text("Profesor: Luis Alberto Chavarria", about_font, (255,255,255),screen, 40, 310 )
        D.draw_Text("Producido en Costa Rica", about_font, (255,255,255),screen, 40, 360 )
        D.draw_Text("Version 1.3", about_font, (255,255,255),screen, 40, 410 )
        D.draw_Text("El programa continua en desarrollo, cualquier problema o aporte contactar a los creadores", about_font, (255,255,255),screen, 40, 460 )

        exit = button(40, 520, "Back to menu")

        if exit.draw_button():
             main_menu()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)

def main_play_page():
    running = True

    while running:

        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text("Choose Team 1", main_font, white, screen, 60, 20)

        team_1_page = button(60, 120, team1["name"])
        team2_page = button(60, 220, team2["name"])
        team3_page = button(60, 320, team3["name"])
        team4_page = button(60, 420, team4["name"])
        exit = button(60, 520, "Back to menu")

        if team_1_page.draw_button():
             no_team1_page()
        if team2_page.draw_button():
             no_team2_page()
        if team3_page.draw_button():
             no_team3_page()
        if team4_page.draw_button():
             no_team4_page()

        if exit.draw_button():
             main_menu()

    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)


def no_team1_page():
     running = True
     while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text("Choose team 2", main_font, white, screen, 60, 20)

        team2_page = button(60, 120, team2["name"])
        team3_page = button(60, 220, team3["name"])
        team4_page = button(60, 320, team4["name"])
        exit = button(60, 420, "Back to team 1")

        if team2_page.draw_button():
             choose_team1xteam2()
        if team3_page.draw_button():
             choose_team1xteam3()
        if team4_page.draw_button():
             choose_team1xteam4()
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)

def no_team2_page():
     running = True
     while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text("Choose team 2", main_font, white, screen, 60, 20)

        team1_page = button(60, 120, team1["name"])
        team3_page = button(60, 220, team3["name"])
        team4_page = button(60, 320, team4["name"])
        exit = button(60, 420, "Back to team 1")

        if team1_page.draw_button():
             choose_team2xteam1()
        if team3_page.draw_button():
             choose_team2xteam3()
        if team4_page.draw_button():
             choose_team2xteam4()
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)

def no_team3_page():
     running = True
     while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text("Choose team 2", main_font, white, screen, 60, 20)

        team2_page = button(60, 120, team2["name"])
        team1_page = button(60, 220, team1["name"])
        team4_page = button(60, 320, team4["name"])
        exit = button(60, 420, "Back to team 1")

        if team2_page.draw_button():
             choose_team3xteam2()
        if team1_page.draw_button():
             choose_team3xteam1()
        if team4_page.draw_button():
             choose_team3xteam4()
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)

def no_team4_page():
     running = True
     while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text("Choose team 2", main_font, white, screen, 60, 20)

        team2_page = button(60, 120, team2["name"])
        team3_page = button(60, 220, team3["name"])
        team1_page = button(60, 320, team1["name"])
        exit = button(60, 420, "Back to team 1")

        if team2_page.draw_button():
             choose_team4xteam2()
        if team3_page.draw_button():
             choose_team4xteam3()
        if team1_page.draw_button():
             choose_team4xteam1()
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)

def choose_team1xteam2():
     global team_2_game, team_1_game
     running = True
     while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team1["name"] + " - " + team2["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
             team_1_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["player_three"], team1["player_four"], team1["player_five"]]
             team_2_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["player_three"], team2["player_four"], team2["player_five"]]
             play_game()
        if bench.draw_button():
             team_1_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["bench_one"], team1["bench_two"], team1["bench_three"]]
             team_2_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["bench_one"], team2["bench_two"], team2["bench_three"]]
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team1xteam3():
     running = True
     while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team1["name"] +" - "+ team3["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_1_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["player_three"], team1["player_four"], team1["player_five"]]
            team_2_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["player_three"], team3["player_four"], team3["player_five"]]

        if bench.draw_button():
             team_1_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["bench_one"], team1["bench_two"], team1["bench_three"]]
             team_2_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["bench_one"], team3["bench_two"], team3["bench_three"]]

        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team1xteam4():
     running = True
     while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team1["name"] + " - " + team4["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_1_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["player_three"], team1["player_four"], team1["player_five"]]
            team_2_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["player_three"], team4["player_four"], team4["player_five"]]

        if bench.draw_button():
             team_1_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["bench_one"], team1["bench_two"], team1["bench_three"]]
             team_2_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["bench_one"], team4["bench_two"], team4["bench_three"]]

        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team2xteam1():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team2["name"] + " - "+ team1["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_2_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["player_three"], team1["player_four"], team1["player_five"]]
            team_1_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["player_three"], team2["player_four"], team2["player_five"]]

        if bench.draw_button():
             team_2_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["bench_one"], team1["bench_two"], team1["bench_three"]]
             team_1_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["bench_one"], team2["bench_two"], team2["bench_three"]]

        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team2xteam3():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team2["name"] + " - "+ team3["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_2_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["player_three"], team3["player_four"], team3["player_five"]]
            team_1_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["player_three"], team2["player_four"], team2["player_five"]]

        if bench.draw_button():
             team_1_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["bench_one"], team2["bench_two"], team2["bench_three"]]
             team_2_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["bench_one"], team3["bench_two"], team3["bench_three"]]

        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team2xteam4():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team2["name"] + " - "+ team4["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_2_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["player_three"], team4["player_four"], team4["player_five"]]
            team_1_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["player_three"], team2["player_four"], team2["player_five"]]

        if bench.draw_button():
             team_1_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["bench_one"], team2["bench_two"], team2["bench_three"]]
             team_2_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["bench_one"], team4["bench_two"], team4["bench_three"]]

        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team3xteam1():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team3["name"] + " - " + team1["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_2_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["player_three"], team1["player_four"], team1["player_five"]]
            team_1_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["player_three"], team3["player_four"], team3["player_five"]]

        if bench.draw_button():
             team_2_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["bench_one"], team1["bench_two"], team1["bench_three"]]
             team_1_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["bench_one"], team3["bench_two"], team3["bench_three"]]
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team3xteam2():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team3["name"] + " - " + team2["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_1_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["player_three"], team3["player_four"], team3["player_five"]]
            team_2_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["player_three"], team2["player_four"], team2["player_five"]]

        if bench.draw_button():
             team_2_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["bench_one"], team2["bench_two"], team2["bench_three"]]
             team_1_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["bench_one"], team3["bench_two"], team3["bench_three"]]
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team3xteam4():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team3["name"] + " - " + team4["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_1_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["player_three"], team3["player_four"], team3["player_five"]]
            team_2_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["player_three"], team4["player_four"], team4["player_five"]]

        if bench.draw_button():
             team_2_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["bench_one"], team4["bench_two"], team4["bench_three"]]
             team_1_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["bench_one"], team3["bench_two"], team3["bench_three"]]
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team4xteam1():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team4["name"] + " - " + team1["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_2_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["player_three"], team1["player_four"], team1["player_five"]]
            team_1_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["player_three"], team4["player_four"], team4["player_five"]]

        if bench.draw_button():
             team_2_game = [team1["main_goalkeeper"], team1["player_one"], team1["player_two"], team1["bench_one"], team1["bench_two"], team1["bench_three"]]
             team_1_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["bench_one"], team4["bench_two"], team4["bench_three"]]
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team4xteam2():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team4["name"] + " - " + team2["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_1_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["player_three"], team4["player_four"], team4["player_five"]]
            team_2_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["player_three"], team2["player_four"], team2["player_five"]]

        if bench.draw_button():
             team_2_game = [team2["main_goalkeeper"], team2["player_one"], team2["player_two"], team2["bench_one"], team2["bench_two"], team2["bench_three"]]
             team_1_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["bench_one"], team4["bench_two"], team4["bench_three"]]
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)
def choose_team4xteam3():
    running = True
    while running:
        screen.fill((56, 172, 113))
        background_skye(image)

        click = False
        D.draw_Text(team4["name"] + " - " + team3["name"], main_font, white, screen, 60, 20)

        standard = button(60, 320, "Standard")
        bench = button(960, 320, "Bench")
        exit = button(60, 620, "Back to choose")

        if standard.draw_button():
            team_2_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["player_three"], team3["player_four"], team3["player_five"]]
            team_1_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["player_three"], team4["player_four"], team4["player_five"]]

        if bench.draw_button():
             team_1_game = [team4["main_goalkeeper"], team4["player_one"], team4["player_two"], team4["bench_one"], team4["bench_two"], team4["bench_three"]]
             team_2_game = [team3["main_goalkeeper"], team3["player_one"], team3["player_two"], team3["bench_one"], team3["bench_two"], team3["bench_three"]]
        if exit.draw_button():
             main_play_page()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)


def play_game():
    running = True
    print(team_2_game)
    teams_gameplay[0], teams_gameplay[1] = team_1_game, team_2_game
    coin = D.flip_coin()

    if coin == 0:
        print ("Team 1 starts \n")            
        print (teams_gameplay[0])
    else:
        print("Team 2 starts \n")
        print(teams_gameplay[1])
    while running:
        
        screen.fill((56, 172, 113))
        background_skye(image)

        players = 5
        count = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
            pygame.display.update()
            mainClock.tick(60)

main_menu()

