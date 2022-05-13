import dataclasses
from tkinter import dialog
import pygame, pytmx, pyscroll
from dataclasses import dataclass

@dataclass
class Portal:
   fromWorld: str
   originPoint: str
   targetWorld: str
   tpPoint: str

@dataclass
class Map:
   name: str
   walls: list[pygame.Rect]
   group: pyscroll.PyscrollGroup
   tmxData: pytmx.TiledMap
   portals: list[Portal]

class MapManager:

   def __init__(self, screen, player):
      self.maps = dict()  
      self.currentMap = 'world'
      self.screen = screen
      self.player = player

      self.registerMap('world', portals=[Portal(fromWorld="world", originPoint="solarEnter", targetWorld="house", tpPoint="exitSpawnSolar")])
      self.registerMap('house', portals=[Portal(fromWorld="house", originPoint="exitExitSolar", targetWorld="world", tpPoint="exitSolar")])
      self.registerMap('solar', portals=[Portal(fromWorld="house", originPoint="entersolar", targetWorld="solar", tpPoint="spawn")])

      self.teleportPlayer('spawn')

   def collisionManager(self):
      for portal in self.getMap().portals:
         if portal.fromWorld == self.currentMap:
            point = self.getObject(portal.originPoint)
            rect = pygame.Rect(point.x, point.y, point.width, point.height)

            if self.player.feet.colliderect(rect):
               copyPortal = portal
               self.currentMap = portal.targetWorld
               self.teleportPlayer(copyPortal.tpPoint)

      for sprite in self.getGroup().sprites():
         if sprite.feet.collidelist(self.getWalls()) > -1:
            sprite.moveBack()

   def teleportPlayer(self, name):
      point = self.getObject(name)
      self.player.position[0] = point.x
      self.player.position[1] = point.y
      self.player.saveLocation()
   
   def registerMap(self, name, portals=[]):
      tmxData = pytmx.util_pygame.load_pygame(f'Game/assets/{name}.tmx')
      mapData = pyscroll.data.TiledMapData(tmxData)
      mapLayer = pyscroll.BufferedRenderer(mapData, self.screen.get_size())
      mapLayer.zoom = 2

      walls = []

      for object in tmxData.objects:
         if object.type == 'collision':
            walls.append(pygame.Rect(object.x, object.y, object.width, object.height))

      group = pyscroll.PyscrollGroup(map_layer=mapLayer, default_layer=4)
      group.add(self.player)

      self.maps[name] = Map(name, walls, group, tmxData, portals)

   def getMap(self): return self.maps[self.currentMap]

   def getGroup(self): return self.getMap().group

   def getWalls(self): return self.getMap().walls

   def getObject(self, name): return self.getMap().tmxData.get_object_by_name(name)

   def draw(self): 
      self.getGroup().draw(self.screen)
      self.getGroup().center(self.player.rect.center)

   def update(self): 
      self.getGroup().update()
      self.collisionManager()