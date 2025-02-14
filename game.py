import pygame
from settings import WIDTH, HEIGHT, BLACK, GREEN, FPS, WHITE, RED
from snake import Snake
from food import Food
from score_manager import ScoreManager
from name_entry import NameEntry
import os

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.snake = Snake()
        self.food = Food()
        self.running = True
        self.paused = False
        self.clock = pygame.time.Clock()
        self.score = 0
        self.fps = FPS
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial",24)
        self.score_manager = ScoreManager()
    

        self.high_scores.append((name, self.score)) #add new score
        self.high_scores.sort(key=lambda x: x[1], reverse=True) #sort descending



    def run(self):
        while self.running:
            self.handle_events()

            if not self.paused:
                self.update()
            self.draw()
            self.clock.tick(self.fps)
            self.enter_name()
            self.save_high_scores()
            self.show_high_scores()
        #modify to use game_manager

        pygame.quit()

        