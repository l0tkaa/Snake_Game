import pygame
from settings import BLOCK_SIZE, WIDTH, HEIGHT, FPS

class Snake:
    def __init__(self):
        self.body = [[300, 200]]
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]
       
        if self.direction == "UP":
            head_y-= BLOCK_SIZE
        elif self.direction == "DOWN":
            head_y += BLOCK_SIZE
        elif self.direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            head_x += BLOCK_SIZE

        head_x %= WIDTH
        head_y %= HEIGHT
        

        self.body.insert(0, [head_x, head_y])

    
    def grow(self):
        # Do nothing since we don't remove tail in game.py when snake eats food
        pass
    
    def check_collision(self):
        head = self.body[0]
        if head in self.body[1:]:
            return True
        return False
      
    
    def draw(self, screen, color):
        for block in self.body:
            pygame.draw.rect(screen, color, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))



