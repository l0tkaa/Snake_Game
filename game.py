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



    def run(self):
        while self.running:
            self.handle_events()

            if not self.paused:
                self.update()

            self.draw()
            self.clock.tick(self.fps)


            self.get_player_name()
            self.score_manager.display_high_scores() #show scores in terminal

    
# ask for the players name after the game is over
    def get_player_name(self):
        name_entry = NameEntry(self.screen, self.font) #use the NameEntry class
        player_name = name_entry.get_name() #NameEntry class
        self.score_manager.add_score(player_name, self.score) #use score manager class and input player_name variable and self.score (init to 0)
        



    









        pygame.quit()

        