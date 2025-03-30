import random
from code.Cost import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity


class Opponent(Entity):
    def __init__(self, name: str, position: tuple, frame_width: int, frame_height: int, frame_count: int):
        super().__init__('oponente1', position, frame_width, frame_height, frame_count)
        self.name = name
        self.direction = -1  # Agora começa indo para a esquerda (-1)
        self.frame_index = 1  # Frame inicial
        self.animation_speed = 10  # Velocidade da animação
        self.frame_counter = 0
        self.speed = ENTITY_SPEED['oponente1'] / 2
        self.dead = False  # Garante que o oponente aparece

        # Posiciona o oponente inicialmente à direita da tela
        self.rect.x = random.randint(WIN_WIDTH // 2, WIN_WIDTH - 50)
        self.rect.y = random.randint(100, WIN_HEIGHT - 100)

    def move(self):
        if not self.dead:  # Só move se não estiver morto
            self.rect.x += self.speed * self.direction
            self.animate()

        # Se sair da tela pela esquerda, marcar como morto
        if self.rect.right < 0:
            self.dead = True

    def animate(self):

        if not self.frames or self.dead:
            return

        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)

        # Define o frame atual
        self.image = self.frames[self.frame_index]

