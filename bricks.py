import pygame.sprite


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BRICK_ROWS = 4
BRICK_COLS = 10
BRICK_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0)]


class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def create_bricks():
    all_bricks = pygame.sprite.Group()
    for row in range(BRICK_ROWS):
        color = BRICK_COLORS[row]
        for col in range(BRICK_COLS):
            brick = Brick(color, BRICK_WIDTH, BRICK_HEIGHT,
                          col * (BRICK_WIDTH + 2) + 35,
                          row * (BRICK_HEIGHT + 2) + 50)
            all_bricks.add(brick)
    return all_bricks
