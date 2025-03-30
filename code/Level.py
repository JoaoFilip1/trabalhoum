import sys
import random
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Cost import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # Adiciona o fundo
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))

        # Adiciona o jogador
        self.player = EntityFactory.get_entity('Player1')
        self.entity_list.append(self.player)

        # Inicializa o temporizador para criar oponentes
        self.opponent_spawn_timer = 0
        self.opponent_spawn_interval = 3000
        self.timeout = 20000

    def run(self):
        clock = pygame.time.Clock()
        self.opponent_spawn_timer = 0

        while True:
            clock.tick(50)
            self.window.fill((0, 0, 0))

            print(f"Tempo do temporizador: {self.opponent_spawn_timer:.2f}, Intervalo: {self.opponent_spawn_interval}")

            # Cria novos oponentes aleatoriamente
            self.opponent_spawn_timer += clock.get_time()
            if self.opponent_spawn_timer >= self.opponent_spawn_interval:
                self.opponent_spawn_timer = 0
                self.add_random_opponent()

            opponents = [ent for ent in self.entity_list if ent.name == 'Opponent1']

            for ent in self.entity_list:
                if not hasattr(ent, "rect") or ent.rect is None:
                    continue

                if hasattr(ent, 'image'):
                    self.window.blit(ent.image, ent.rect)
                else:
                    self.window.blit(ent.surf, ent.rect)

                if ent == self.player:
                    ent.move(opponents)
                else:
                    ent.move()

            # Remover entidades marcadas como "mortas"
            self.entity_list = [ent for ent in self.entity_list if not getattr(ent, "dead", False)]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Exibe informações na tela
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

    def add_random_opponent(self):
        opponent = EntityFactory.get_entity('Opponent1')

        if opponent is None or not hasattr(opponent, "rect"):
            return

        # Define a posição inicial fora da tela à direita
        opponent.rect.x = random.randint(WIN_WIDTH, WIN_WIDTH + 100)
        opponent.rect.y = random.randint(50, WIN_HEIGHT - 100)
        opponent.level = self  # Adiciona a referência ao Level
        self.entity_list.append(opponent)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
