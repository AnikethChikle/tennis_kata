class TennisGame:
    SCORES = [0, 15, 30, 40]

    def __init__(self, player1, player2):
        self.scores = {player1: 0, player2: 0}
        self.players = [player1, player2]

    def player_scores(self, player):
        self.scores[player] += 1

    def score(self):
        return f"{self.SCORES[self.scores[self.players[0]]]}-{self.SCORES[self.scores[self.players[1]]]}"


if __name__ == "__main__":
    game = TennisGame("Player 1", "Player 2")
    print(game.score())  # Initial score: 0-0

    game.player_scores("Player 1")
    print(game.score())  # After Player 1 scores: 15-0

    game.player_scores("Player 2")
    print(game.score())  # After Player 2 scores: 15-15
