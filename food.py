import pygame
import random
from settings import WIDTH, HEIGHT, BLOCK_SIZE, RED

class Food:
    def __init__(self):
        self.position = self.spawn_food()

    def spawn_food(self):
        return [random.randrange(1, WIDTH//BLOCK_SIZE) * BLOCK_SIZE,
        random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE]
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))
    


