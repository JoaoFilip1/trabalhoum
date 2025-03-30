import pygame
from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name: str, position: tuple, frame_width: int, frame_height: int, frame_count: int):
        self.name = name
        try:
            self.spritesheet = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        except pygame.error as e:
            self.spritesheet = None

        self.rect = pygame.Rect(position[0], position[1], frame_width, frame_height)
        self.frames = self.load_frames(frame_width, frame_height, frame_count) if self.spritesheet else []
        self.current_frame = 0
        self.surf = self.frames[0] if self.frames else pygame.Surface((frame_width, frame_height))
        self.speed = 0
        self.dead = False  # Adiciona um atributo para marcar se a entidade deve ser removida

    def load_frames(self, frame_width, frame_height, frame_count):
        frames = []
        for i in range(frame_count):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frames.append(self.spritesheet.subsurface(frame_rect))
        return frames

    def animate(self):
        if self.frames:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.surf = self.frames[self.current_frame]

    def kill(self):

        self.dead = True

    @abstractmethod
    def move(self):
        pass
