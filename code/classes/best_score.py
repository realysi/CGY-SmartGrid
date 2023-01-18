from .data import Data

class Score:
    def __init__(self) -> None:
        self.scores = []
        self.best_score = 0
        self.best_data = Data({}, {}, {})
        self.total_score = 0
        self.average_score = 0
        self.counter = 0

    def add_score(self, score: int, data: Data):
        self.total_score += score 
        self.counter += 1
        self.scores.append((score, data))
        self.get_best_score()

    def get_best_score(self):
        if len(self.scores) > 1:
            if self.scores[0][0] < self.scores[1][0]:
                self.best_score = self.scores[0][0]
                self.best_data = self.scores[0][1]
                self.scores.remove(self.scores[1])
            else:
                self.best_score = self.scores[1][0]
                self.best_data = self.scores[1][1]
                self.scores.remove(self.scores[0])

    def calculate_average_score(self):
        self.average_score = self.total_score / self.counter
        return self.average_score


    def __repr__(self) -> str:
       return f"Best score: {self.best_score}\t| Average Score: {self.average_score}\t| Best data: {self.best_data}"