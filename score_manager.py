import os

class ScoreManager:
    def __init__(self, filename= "highscores.txt", max_scores=0):

def load_high_scores(self):
        """Load high scores from a file """
        if os.path.exists("highscores.txt"):
            with open("highscores.txt", "r") as file:
                scores = [line.strip().split(" - ") for line in file.readlines()]
                return[(name, int(score)) for name, score in scores]
        return[] #return empty list if no file exists
    

def save_high_scores(self):
    """Save high scores to a file"""
    with open("highscores.txt", "w") as file:
        for name, score in self.high_scores[:5]:
            file.write(f"{name} - {score}\n")

def add_score():

def display_high_scores():