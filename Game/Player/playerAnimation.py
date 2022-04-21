import pygame

class playerAnimation(pygame.sprite.Sprite):
   
   def __init__(self, name):
      super().__init__()
      self.spriteSheet = pygame.image.load(f'Game/Player/assets/{name}.png')
      self.animationIndex = 0
      self.images = {
         'down': self.getImages(0),
         'left': self.getImages(32),
         'right': self.getImages(64),
         'up': self.getImages(96),
      }
      self.speed = 2
      self.clock = 0

   def changeAnimation(self, name: str):
      self.image = self.images[name][self.animationIndex]
      self.image.set_colorkey(0, 0)
      self.clock += self.speed * 10

      if self.clock >= 100:

         self.animationIndex += 1
         if self.animationIndex >= len(self.images[name]):
            self.animationIndex = 0
         self.clock = 0

   def getImages(self, y):
      images = []

      for i in range(0, 3):
         x = i * 32
         image = self.getImage(x, y)
         images.append(image)
      return images

   def getImage(self, x, y):
      image = pygame.Surface([32, 32])
      image.blit(self.spriteSheet, (0, 0), (x, y, 32, 32))
      return image