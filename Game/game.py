from time import sleep
import pygame
import pytmx
import pyscroll

from Game.Player.player import Player
from Game.dialog import DialogBox
from Game.map import MapManager


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Solar - Pierre et Gabriel')
        
        self.player = Player('player', 0, 0)
        self.mapManager = MapManager(self.screen, self.player)
        self.dialogBox = DialogBox()

    def handleKeybordInput(self):
        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_UP] or keyPressed[pygame.K_z]:
            self.player.moveUp()
            self.player.changeAnimation('up')
        elif keyPressed[pygame.K_DOWN] or keyPressed[pygame.K_s]:
            self.player.moveDown()
            self.player.changeAnimation('down')
        elif keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_q]:
            self.player.moveLeft()
            self.player.changeAnimation('left')
        elif keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d]:
            self.player.moveRight()
            self.player.changeAnimation('right')

    def update(self):
        self.mapManager.update()
        
    def run(self):

        clock = pygame.time.Clock()
        isPlaying = True

        while isPlaying:
            self.player.saveLocation()
            self.handleKeybordInput()
            self.update()
            self.mapManager.draw()
            self.dialogBox.renderText(self.screen)
            pygame.display.flip()
            tmxData = pytmx.util_pygame.load_pygame(f'Game/assets/house.tmx')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isPlaying = False
                elif self.mapManager.currentMap == 'house':
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.dialogBox.exec()

            clock.tick(60)

        pygame.quit()