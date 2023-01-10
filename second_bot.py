from typing import Optional, List

from schnapsen.game import Bot, Move, PlayerPerspective, SchnapsenTrickScorer
from deck import Card, Rank, Suit

class own_bot(Bot):
    def __init__(self):
        super().__init__()

    def get_move(self, state: PlayerPerspective, leader_move: Optional[Move]) -> Move:

        own_points: int = PlayerPerspective.get_my_score()
        opponent_score: int = PlayerPerspective.get_opponent_score()
        
