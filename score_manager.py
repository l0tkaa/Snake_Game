import os

class ScoreManager:
    def __init__(self, filename="highscores.txt", max_scores=5):
        """Initialize the score manager with a file for storing high scores."""
        self.filename = filename
        self.max_scores = max_scores
        self.high_scores = self.load_high_scores()

    def load_high_scores(self):
        """Load high scores from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return [(name, int(score)) for name, score in (line.strip().split(" - ") for line in file)]
        return []

    def save_high_scores(self):
        """Save high scores to the file."""
        with open(self.filename, "w") as file:
            for name, score in self.high_scores[:self.max_scores]:
                file.write(f"{name} - {score}\n")

    def add_score(self, name, score):
        """Add a new score, sort, and save."""
        self.high_scores.append((name, score))
        self.high_scores.sort(key=lambda x: x[1], reverse=True)
        self.save_high_scores()
