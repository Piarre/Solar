import pygame

from Game.Player.playerAnimation import playerAnimation

class Player(playerAnimation):

    def __init__(self, name, x, y):
        super().__init__(name)

        self.image = self.getImage(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.velocity = 3.2

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.oldPos = self.position.copy()

    def saveLocation(self): self.oldPos = self.position.copy()

    def moveUp(self): self.position[1] -= self.velocity

    def moveDown(self): self.position[1] += self.velocity

    def moveRight(self): self.position[0] += self.velocity

    def moveLeft(self): self.position[0] -= self.velocity

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def moveBack(self):
        self.position = self.oldPos
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def getImage(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.spriteSheet, (0, 0), (x, y, 32, 32))
        return image
