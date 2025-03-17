import pygame

from code.Cost import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check For All Events "Verificar eventos"
            # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            # pygame.quit() #Fechar Janela
            # quit() #fim do pygame
