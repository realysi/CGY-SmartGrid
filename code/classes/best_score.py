from .data import Data

class Score:
    def __init__(self) -> None:
        self.scores = {}
        self.best_score = 10000000 #average score random is around 43000, so this highscore will be beat
        self.best_score_id = 0
        self.average_score = 0
        self.runs = 0

    def score_append(self, run, data:Data):
        self.scores[run] = data

    def score_data(self):
        scores = 0
        for run in self.scores:
            score = self.scores[run].cost 
            scores += score
            if score < self.best_score:
                self.best_score = score
                self.best_score_id = run

        self.runs += 1
        self.average_score = scores / len(self.scores)

        return self.average_score

    def __repr__(self) -> str:
            return f"Total scores: {self.runs}\t| Average Score: {self.average_score}\t| Bestscore: {self.best_score}"