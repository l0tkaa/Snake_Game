
import pygame

class NameEntry:
    def __init__(self, screen, font, default_name="Guest"):
        """Initialize the name entry screen."""
        self.screen = screen
        self.font = font
        self.name = ""
        self.default_name = default_name

    def get_name(self):
        """Display a name input screen and return the entered name."""
        input_active = True

        while input_active:
            self.screen.fill((0, 0, 0))  # Clear screen

            # Render text
            prompt_text = self.font.render("Enter your name (or press Enter for Guest):", True, (255, 255, 255))
            name_text = self.font.render(self.name or self.default_name, True, (0, 255, 0))

            # Display text on screen
            self.screen.blit(prompt_text, (50, 100))
            self.screen.blit(name_text, (200, 200))
            pygame.display.flip()  # Refresh the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter key to confirm name
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:  # Backspace to delete last character
                        self.name = self.name[:-1]
                    else:  # Add typed character to name
                        self.name += event.unicode

        return self.name.strip() if self.name.strip() else self.default_name  # Return entered name or default
