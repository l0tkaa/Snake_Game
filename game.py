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

            self.enter_name()
            self.score_manager.display_high_scores() #show scores in terminal

    
# ask for the players name after the game is over
    def enter_name(self):
        name = ""
        font = pygame.font.SysFont("Arial", 32)
        input_active = True

        while input_active:
            self.screen.fill(BLACK)
            prompt_text = font.render("Enter your name (or press Enter for Guest):":, True, WHITE)
            name_text = font.render(name or "Guest", True, GREEN)
            self.screen.blit(prompt_text, (WIDTH // 6, HEIGHT // 3))
            self.screen.blit(name_text, (WIDTH // 2 - 50, HEIGHT // 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key = pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

        name = name.strip() if name.strip() else "Guest"
        self.score_manager.add_score(name, self.score)
        



    









        pygame.quit()

        