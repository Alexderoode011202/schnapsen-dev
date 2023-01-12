from typing import Optional, List

from schnapsen.game import Bot, Move, PlayerPerspective, SchnapsenTrickScorer
from schnapsen.deck import Card, Rank, Suit
import random

class random_test(Bot):
    def __init__(self):
        super().__init__()

    def get_move(self, player_state: PlayerPerspective, leader_move: Optional[Move]) -> Move:
        moves = player_state.valid_moves()

        return random.sample(moves, 1)