from code.Cost import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity
import pygame

class Player(Entity):
    def __init__(self, name: str, position: tuple):

        self.move_frame_width = 128
        self.move_frame_height = 127
        move_frame_count = 8

        super().__init__(name, position, self.move_frame_width, self.move_frame_height, move_frame_count)

        # Inicialização
        self.move_rect = self.surf.get_rect(topleft=position)
        self.rect = self.move_rect  # Inicialmente usa o rect de movimento
        self.speed = ENTITY_SPEED.get(self.name, 3)
        self.direction = pygame.math.Vector2(0, 0)
        self.frame_index = 0
        self.animation_speed = 2
        self.frame_counter = 0

        # animação de ataque
        self.attack_spritesheet = pygame.image.load(f'./asset/Attack.png').convert_alpha()
        self.attack_frame_widths = [131, 108]
        self.attack_frame_height = 78
        self.attack_frames = self.load_attack_frames(self.attack_frame_widths, self.attack_frame_height)
        self.attack_frame_count = len(self.attack_frame_widths)
        self.is_attacking = False
        self.attack_frame_index = 0
        self.attack_frame_counter = 0
        self.attack_animation_speed = 1
        self.attack_rect = pygame.Rect(0, 0, 0, 0)  # Rect de ataque
        self.attacking_timer = 0
        self.attack_duration = 300

        # Ajuste inicial do rect
        self.rect.height = self.move_frame_height

    def load_attack_frames(self, frame_widths: list, frame_height: int):
        frames = []
        x_offset = 0
        for width in frame_widths:
            frame_rect = pygame.Rect(x_offset, 0, width, frame_height)
            frames.append(self.attack_spritesheet.subsurface(frame_rect))
            x_offset += width
        return frames

    def get_attack_rect(self):
        if self.is_attacking:
            if self.attack_frame_index == 1:  # Frame do ataque
                offset_x = 20
                self.attack_rect.topleft = (self.rect.x + offset_x, self.rect.y)
                self.attack_rect.size = (80, self.attack_frame_height)
                return self.attack_rect
        return pygame.Rect(0, 0, 0, 0)

    def check_enemy_collision(self, enemies):
        if self.is_attacking:
            attack_rect = self.get_attack_rect()
            print(f"Attack Rect no collision check: {attack_rect}")
            for enemy in enemies:
                if attack_rect.colliderect(enemy.rect):
                    print(f"Colisão detectada com {enemy.name}!")
                    enemy.kill()


    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_attacking:
            self.is_attacking = True
            self.attack_frame_index = 0
            self.attack_frame_counter = 0
            self.attacking_timer = pygame.time.get_ticks()  # Inicializa o timer no início do ataque
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

    def move(self, enemies=None):

        if self.is_attacking:
            self.animate_attack()
            self.rect.height = self.attack_frame_height
            attack_rect = self.get_attack_rect()
            self.check_enemy_collision(enemies)
            if pygame.time.get_ticks() - self.attacking_timer >= self.attack_duration:
                self.is_attacking = False
                self.attacking_timer = 0
                self.attack_frame_index = 0
        else:
            self.get_input()
            self.move_rect.x += self.direction.x * self.speed
            self.move_rect.y += self.direction.y * self.speed
            self.rect = self.move_rect
            self.animate()

        # Manter o jogador dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT

    def animate_attack(self):
        if self.attack_frames and self.is_attacking:  # Mantém a animação enquanto estiver atacando
            self.attack_frame_counter += 1
            if self.attack_frame_counter >= self.attack_animation_speed:
                self.attack_frame_counter = 0
                self.attack_frame_index = (self.attack_frame_index + 1) % len(self.attack_frames)
                self.surf = self.attack_frames[self.attack_frame_index]

    def draw(self, surface):
        surface.blit(self.surf, self.rect)
        if self.is_attacking:
            pygame.draw.rect(surface, (255, 0, 0), self.get_attack_rect(), 2)