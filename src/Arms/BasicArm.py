import pygame

class BasicArm(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, direction):
        super().__init__()
        self.velocity = velocity
        self.direction = direction
        self.image = pygame.Surface((5, 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.direction == "RIGHT":
            self.rect.x += self.velocity
        elif self.direction == "LEFT":
            self.rect.x -= self.velocity
        elif self.direction == "UP":
            self.rect.y -= self.velocity
        elif self.direction == "DOWN":
            self.rect.y += self.velocity

class ArmsSpreatSheets:
    def __init__(self, filename, rows, cols):
        self.sheets = pygame.image.load(filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.rect = self.sheets.get_rect()
        ancho = self.rect.width / cols
        alto = self.rect.height / rows
        self.animation = []
        for row in range(0, rows):
            for col in range(0, cols):
                animation = pygame.Rect(ancho * col, alto * row, ancho, alto)
                self.animation.append(self.sheets.subsurface(animation))

    def getAnimationUP(self):
        return self.animation

bullets = ArmsSpreatSheets("./src/Arms/disparo.png",1,2)