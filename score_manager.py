import os

class ScoreManager:


    # initialize the score manager with a file for storing high scores
    def __init__(self, filename= "highscores.txt", max_scores=5):
        self.filename = filename # the file where the scores will be saved
        self.max_scores = max_scores # max number of scores to keep
        self.high_scores = self.load_high_scores() # load existing high scores when starting



# load high scores from file, returning a list of (name, score) tuples.
    def load_high_scores(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                scores = [line.strip().split(" - ") for line in file.readlines()]
                return[(name, int(score)) for name, score in scores]
        return[]
    



# save high scores to a file, keeping only the top 'max_scores' entires.
    def save_high_scores(self):
        with open(self.filename, "w") as file:
            for name, score in self.high_scores[:self.max_scores]: 
                file.write(f"{name}-{score}\n")



# add a new score, sort the list, save update scores.
    def add_score(self, name, score):
        self.high_scores.append((name, score))
        self.high_scores.sort(key=lambda x: x[1], reverse = True) # sort in descending order
        self.save_high_scores()




# print the high scores for debugging or in-game display
    def display_high_scores(self):
        print("\n HIGH SCORES ")
        for i, (name, score) in enumerate(self.high_scores[:self.max_scores]):
            print(f"{i+1} {name} - {score}")