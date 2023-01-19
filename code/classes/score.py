from .data import Data
from typing import Tuple, Dict, List

class Score:
    def __init__(self) -> None:
        self.scores: List[Tuple[int, Data]] = []
        self.best_score: int = None
        self.best_data: Data = Data({}, {})
        self.total_score: int = 0
        self.average_score: int = 0
        self.counter: int = 0

    # Adds scores of all runs and counts number of runs
    def add_score(self, score: int, data: Data) -> None:
        self.total_score += score 
        self.counter += 1
        self.scores.append((score, data))
        self.get_best_score()

    def get_best_score(self):
        if len(self.scores) > 1:
            if self.scores[0][0] < self.scores[1][0]:
                self.best_score = self.scores[0][0]  # Best (lowest) score is saved
                self.best_data = self.scores[0][1] # Corresponding data object is saved
                self.scores.remove(self.scores[1]) # Removes tuple with worse score
            else:
                self.best_score = self.scores[1][0]
                self.best_data = self.scores[1][1]
                self.scores.remove(self.scores[0])

    def calculate_average_score(self):
        self.average_score = self.total_score / self.counter

    def __repr__(self) -> str:
        return f"Best score: {self.best_score}\t| Average Score: {self.average_score}"
       