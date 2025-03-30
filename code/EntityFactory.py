from code.Background import Background
from code.Cost import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player
from code.oponente import Opponent


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT // 2))
            case 'Opponent1':
                opponent = Opponent('Opponent1', (WIN_WIDTH, WIN_HEIGHT // 2), 61, 49, 8)
                print(f"EntityFactory criou: {opponent.name}")
                return opponent