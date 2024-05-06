import random
import time
import pygame

pygame.init()

#E: recive el string a dibujar, la fuente, el color, donde será dibujada y sus medidas
#S: no retorna nada
#Dibuja en pantalla el texto selecionado
def draw_Text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#E: no recibe nada
#S: retorna true en caso de salir el primer equipo y false en caso contrario
#simula el tiro de una mondeda
def flip_coin()-> int:
    return random.randint(0,1)

#E: un entero
#S: un booleano
#funciones indice que determinan el lugar de los porteros
def AN1 (ball: int):
    palet_list = [
        [1,2],[3,4],[5,6]
    ]
    goalkeeper = random.randint(0, 2)
    goalkeeper_list = palet_list[goalkeeper]
    if ball in goalkeeper_list:
        return False
    return True

def AN2 (ball: int):
    palet_list = [
        [1,2,3],[4,5,6]
    ]

    goalkeeper = random.randint(0,1)
    goalkeeper_list = palet_list[goalkeeper]
    if ball in goalkeeper_list:
        return False
    return True

def AN3 (ball:int):
    palet_list = [
        [1,3],[2,5],[4,6]
    ]
    
    goalkeeper = random.randint(0,2)
    goalkeeper_list = palet_list[goalkeeper]
    print(goalkeeper_list)
    if ball in goalkeeper_list:
        return False
    return True

#E: no recibe nada
#S: no posee
# dado un  numero aleatorio y uno ingresado dicta si el numero es igual
def reveal_goalkeeper():

    duration = 5
    flag = True
    bu_sound = pygame.mixer.Sound("sounds/buu.mp3")
    ye_sound = pygame.mixer.Sound("sounds/yee.mp3") 
    while duration != 0:
        if flag:
            ball = int(input("Ingrese un numero del 1 al 6: "))
            goalkeeper = random.randint(1,3)
            if goalkeeper == 1:
                print("AN1")
                if not AN1(ball):
                    ye_sound.play()
                    print ("Goal")
                    return
                bu_sound.play()
                print("Fail")
                return
            if goalkeeper == 2:
                print("AN2")
                if not AN2:
                    ye_sound.play()
                    print ("Goal")
                    return
                bu_sound.play()
                print("Fail")
                return
            if goalkeeper == 3:
                print("AN3")
                if not AN3:
                    ye_sound.play()
                    print ("Goal")
                    return
                bu_sound.play()
                print("Fail")
                return
        duration -= 1
        time.sleep(1) 

    bu_sound.play()
    print("No time")
    return

#reveal_goalkeeper()


