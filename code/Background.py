import pygame

from code.Cost import WIN_WIDTH
from code.Entity import Entity

class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.position = position
        self.surf = pygame.image.load(f'./asset/{name}.png')
        self.rect = self.surf.get_rect(topleft=self.position)

    def move(self):
        self.rect.centerx -= 2
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
            pass
