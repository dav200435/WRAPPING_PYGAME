import pygame
from Arms.BasicArm import BasicArm
import random

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Color Change Example")
class Character (pygame.sprite.Sprite):
    
    '''
    Tiene que tener unas coordenadas de inicio
    un personaje se puede mover
    un personaje tiene una representación 
    un personaje puede tener sprite y se puede gestionar desde aquí
    
    '''

    def __init__(self,screen,x,y):
        super().__init__()
        self.image = pygame.Surface((10, 20))  # Tamaño del sprite (ancho,alto)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)  # Posición inicial del sprite
        self.color_change_timer = 25  # Configura el temporizador a un valor diferente
        self.screen = screen
        self.x=x
        self.y=y
        self.color = (255, 0, 0)  # Cambia el color inicial a rojo
        self.image.fill(self.color)  # Rellena el sprite con el color inicial
        self.bullets = []
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
            self.change_color()
        if keys[pygame.K_d]:
            self.rect.x += 5
            self.change_color()
        if keys[pygame.K_w]:
            self.rect.y -= 5
            self.change_color()
        if keys[pygame.K_s]:
            self.rect.y += 5
            self.change_color()
        
         # Disparar balas
        if keys[pygame.K_SPACE]:
            self.bullets.append(BasicArm(self.x + self.width // 2, self.y, 80))   
            
        for bullet in self.bullets[:]:
            bullet.update()
            bullet.draw(self.screen)
            if bullet.x > 800 or bullet.x < 0:
                self.bullets.remove(bullet)

        # limits--> Hay que crear clases que controlen los límites del mapa o bien añadirlo al mapa
        #TODO: configurar height and with
        #self.x = max(0, min(self.x, 10 - 5))
        #self.y = max(0, min(self.y, 20 - 5))
        print (self.x)
        print (self.y)
        # draw the new position
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 10, 20))

        # disply update after movements
        pygame.display.flip()
        pygame.time.delay(30) 
            
    def change_color(self):
        # Cambiar de color cuando el temporizador alcanza cero
        if self.color_change_timer <= 0:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.image.fill(self.color)  # Rellena el sprite con el nuevo color
            self.color_change_timer = 25  # Reinicia el temporizador
        else:
            self.color_change_timer -= 1
            
        
        
    # basic rectangle element in screen with movements  
    def draw (self):
        
       #size by while this!!
       pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, 10, 20))         

