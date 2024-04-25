import random

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
def flip_coin():
    coin = random.randint(0,1)
    if coin == 0:
        print("Equipo 1")
        return True
    print("Equipo 2")
    return False

#E: no recibe nada
#S: no posee
# dado un  numero aleatorio y uno ingresado dicta si el numero es igual
def reveal_goalkeeper():
    ball = int(input("Ingrese un numero del 1 al 6: "))
    goalkeeper = random.randint(1,6)

    if ball == goalkeeper:
        print ("Goal")
        return
    print("Fail")
    return 

