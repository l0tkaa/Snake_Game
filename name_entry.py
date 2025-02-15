import pygame

class NameEntry:
    def __init__(self, screen, font):
        """Initialize the name entry screen."""
        self.screen = screen
        self.font = font
        self.name = ""

    def get_name(self):
        """Display a name input screen and return the entered name."""
        input_active = True

        while input_active:
            self.screen.fill((0, 0, 0))

            prompt_text = self.font.render("Enter your name (or press Enter for Guest):", True, (255, 255, 255))
            name_text = self.font.render(self.name or "Guest", True, (0, 255, 0))

            self.screen.blit(prompt_text, (50, 100))
            self.screen.blit(name_text, (200, 200))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                    else:
                        self.name += event.unicode

        return self.name.strip() if self.name.strip() else "Guest"
