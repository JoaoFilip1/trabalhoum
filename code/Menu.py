import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Cost import WIN_WIDTH, COLOR_WHITE, MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load('./asset/jogo.mp3')
        pygame.mixer.music.play(-1)  # Reproduz a música em loop
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "DARK NIGHT", COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "SHOOTER", COLOR_WHITE, ((WIN_WIDTH / 2), 120))

            for i in range (len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))


            pygame.display.flip()

            # Check For All Events "Verificar eventos"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar Janela
                    quit()  # Fim do pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

