from time import sleep
import pygame, pytmx, pyscroll

from Game.map import MapManager

class DialogBox:
   xPOS = 60
   yPOS = 470 

   def __init__(self):
      self.box = pygame.image.load('Game/assets/dialogs/dialog.png')
      self.box = pygame.transform.scale(self.box, (700, 100))
      self.texts = [
         'Qu\'est ce les panneaux solaires ?',
         'Les panneaux solaires sont des équipements qui permettent de',
         'récupérer de l\'énergie solaire.',
         'Ils sont situés sur les différents sols de la planète.',
         'Ceci est un moyen écologique de produire de l\'électricé.',
         'Comment fonctionne les panneaux solaires ?',
         'Tout d\'abbord déplacez-vous en haut à gauche de la maison.',
         'Ceci est un onduleur, il permet de convertir,',
         'le courant continue en courant alternatif.',
         'pour pouvoir utilié cette énergie ',
         'Pierre Et Gabriel 3ème3' 
         ]
      self.textIndex = 0
      self.letterIndex = 10
      self.font = pygame.font.Font('Game/assets/dialogs/dialog_font.ttf', 15)
      self.reading = False

   def exec(self):
      if self.reading:
         self.passText()
      else:
         self.reading = True
         self.textIndex = 0

   def renderText(self, screen):
      if self.reading:
         self.letterIndex += 1

         if self.letterIndex >= len(self.texts[self.textIndex]):
            self.letterIndex = self.letterIndex

         screen.blit(self.box, (self.xPOS, self.yPOS))
         text = self.font.render(self.texts[self.textIndex][0:self.letterIndex], False, (0, 0, 0))
         screen.blit(text, (self.xPOS + 62, self.yPOS + 27))

   def passText(self):
      self.textIndex += 1
      self.letterIndex = 0

      if self.textIndex >= len(self.texts):
         self.reading = False
         pygame.quit()