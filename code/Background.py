import pygame
from code.Entity import Entity
from code.Cost import WIN_WIDTH


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        surf = pygame.image.load(f'./asset/{name}.png')  # Carrega a imagem antes
        frame_width, frame_height = surf.get_size()
        frame_count = 1  # Apenas um frame estático

        super().__init__(name, position, frame_width, frame_height, frame_count)

        self.surf = surf  # Usa a imagem carregada
        self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        self.rect.centerx -= 2
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
