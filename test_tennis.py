import unittest
from tennis import TennisGame

class TestTennisGame(unittest.TestCase):
    def test_initial_score_is_0_0(self):
        game = TennisGame("Player 1", "Player 2")
        self.assertEqual(game.score(), "0-0")

    def test_player_1_scores_first_point(self):
        game = TennisGame("Player 1", "Player 2")
        game.player_scores("Player 1")
        self.assertEqual(game.score(), "15-0")
