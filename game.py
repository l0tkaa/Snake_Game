import pygame
from game_manager import GameManager
from settings import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        """Initialize the game and pass components to GameManager."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        # Create GameManager
        self.game_manager = GameManager(self.screen, self.clock, FPS)

    def run(self):
        """Start the game loop by calling GameManager."""
        self.game_manager.run_game_loop()

if __name__ == "__main__":
    game = Game()
    game.run()
