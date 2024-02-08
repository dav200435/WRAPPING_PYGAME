import pygame
import sys


class SpreatSheets:
    def __init__(self, filename, rows, cols):
        
        # Obtener la imagen de los sprites de los personajes
        self.sheets = pygame.image.load(filename).convert_alpha()
        
        # COLS AND ROWS OF THE SPREET SHEET IMAGE    
        self.cols = cols
        self.rows = rows
        
        # Obtener el rectangulo de la imagen parte fundamental del sprite
        # los sprites están compuestos de rectángulo y la imagenq que es lo
        # representa la imagen
        self.rect = self.sheets.get_rect()
        
        # width y height de cada una de las imagenes
        ancho = self.rect.width / cols
        alto = self.rect.height / rows
        
        self.animation_down = []
        self.animation_up = []
        self.animation_left =[]
        self.animation_right = []      
        
        for row in range(0, rows):
            for col in range(0, cols):
                animation = pygame.Rect (ancho*col,  alto*row, ancho, alto)
                if (row == 0):
                    self.animation_down.append(self.sheets.subsurface(animation))
                
                if (row == 1):
                    self.animation_left.append(self.sheets.subsurface(animation))
                    
                if (row == 2):
                     self.animation_right.append(self.sheets.subsurface(animation))
                    
                if (row == 3):
                    self.animation_up.append(self.sheets.subsurface(animation))
                    
   ## Métodos getters para acceder a las listas ACORDAROS QUE VIMOS MÉTODOS DE ACCESO DE LAS CLASES
    def getAnimationUP (self):
        return self.animation_up
    
    def getAnimationDOWN (self):
        return self.animation_down
    
    def getAnimationLEFT (self):
        return self.animation_left
    
    def getAnimationRIGHT (self):
        return self.animation_right
 
'''
La idea de esta clase es la del personaje y llama al spreatSheet que contiene
las imágenes asociadas al personaje en diferentes arrays dependiendo de si 
va hacia la derecha y tenemos una lista, a la izuiqerda y tenemos otra lista 
arriba y abajo
'''                  
class AnimationCharacter (pygame.sprite.Sprite):
    
    def __init__(self, filename, rows, cols, DownKey,UpKey,RightKey,leftKey,velocity = 10):
        super().__init__()
        self.spreatSheet = SpreatSheets(filename, rows, cols)
        self.DownKey=DownKey
        self.UpKey=UpKey
        self.LeftKey=leftKey
        self.RightKey=RightKey
        #estas son las listas donde guardamos cada uan de las imágenes dependiendo
        #del movimiento que realiza
        self.animationUP = self.spreatSheet.getAnimationUP()
        self.animationDOWN = self.spreatSheet.getAnimationDOWN()
        self.animationLEFT = self.spreatSheet.getAnimationLEFT()
        self.animationRIGHT = self.spreatSheet.getAnimationRIGHT()
        
        self.velocity = velocity
        
        #obligatorio ponemos una dirección por defecto
        self.direction = "RIGHT"
        self.image = self.animationRIGHT[0]
        
        #En mi imagen he necesitado hacerla más pequeña
        self.image = pygame.transform.scale(self.image, (30,30))
        
        self.rect = self.image.get_rect()
        
        # Lo situo en el centro de la pantalla al personaje
        self.rect.center = (800 // 2, 600 // 2) 
        self.index = 0
    
    def update (self):
        
        if self.index >= 3:
            self.index = 0
        print (self.index)
        
        if self.direction == "RIGHT":
            self.image = self.animationRIGHT[self.index]
        if self.direction == "LEFT":
            self.image = self.animationLEFT[self.index]
        if self.direction == "UP":
            self.image = self.animationUP[self.index]
        if self.direction == "DOWN":
            self.image = self.animationDOWN[self.index]
            
            
        self.image = pygame.transform.scale(self.image, (30,30))
        self.index += 1
        
         # Obtener teclas presionadas
        keys = pygame.key.get_pressed()

        # Mover el rectángulo
        if keys[pygame.K_+self.LeftKey]:
            self.rect.x -= self.velocity
            self.direction = "LEFT"
        if keys[pygame.K_+self.RightKey]:
            self.rect.x += self.velocity
            self.direction = "RIGHT"
        if keys[pygame.K_+self.UpKey]:
            self.rect.y-= self.velocity
            self.direction = "UP"
        if keys[pygame.K_+self.DownKey]:
            self.rect.y+= self.velocity
            self.direction = "DOWN"
 
 
 ############################### La parte que crea la pantalla y añade los personajes ##############
pygame.init()
screen = pygame.display.set_mode((800, 600)) #800x600 by default  
    
# FPS
fpsClock = pygame.time.Clock()

# Crear los personajes se realiza a través de los grupos de sprites
# es una lista 
all_sprites1 = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
#personaje le paso la imagen y las filas y columnas del sprite. en una sola imagen
personaje1 =  AnimationCharacter(".\src\Characters\sprite.png",4,4,"s","w","d","a")
Personaje2 = AnimationCharacter(".\src\Characters\sprite.png",4,4,"DOWN","UP","RIGHT","LEFT")
all_sprites1.add(personaje1)
all_sprites2.add(Personaje2)

running = True

while running:            
    
    fpsClock.tick(10)
    
    # actualice la pantalla importante
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    screen.fill('black')
    # dibuja los pesronajes
    all_sprites1.draw(screen)
    all_sprites1.update()
    all_sprites2.draw(screen)
    all_sprites2.update()
    
    
    # Actualizar pantalla. Dibuja sobre la imagen principal todo !! importante tener
    pygame.display.flip()   

pygame.quit()
sys.exit()               
    
