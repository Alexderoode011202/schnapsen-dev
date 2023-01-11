from typing import Optional, List
import random
from schnapsen.game import Bot, Move, PlayerPerspective, SchnapsenTrickScorer
from deck import Card, Rank, Suit

class own_bot(Bot):
    def __init__(self):
        super().__init__()

    def get_move(self, state: PlayerPerspective, leader_move: Optional[Move]) -> Move:

        moves = state.valid_moves()
        chosen_move = None
        last_move = PlayerPerspective.get_game_history()[-1]
        last_suit = last_move[1]
        value_list: list = []
        TS = SchnapsenTrickScorer

        # This is step 2
        if PlayerPerspective.get_my_score < PlayerPerspective.get_opponent_score():
            for move in moves:
                if move.is_marriage() or move.is_trump_exchange():
                    chosen_move = move
                else:
                    continue
            
            #Here we go to step 3
            if chosen_move == None:
                same_suit_list = [ move.Suit == last_suit for move in moves]
                for move in same_suit_list:
                    value_list.append(tuple(move, TS.rank_to_points(move.Rank)))
                chosen_move = min(value_list, key= lambda x: x[1])
                # And here goes step 4
                if len(same_suit_list) == 0:
                    chosen_move = random.sample(moves, 1)
                    
        return chosen_move



"""  
1.If your score of the bot is lower than the opponent
2.Try to play a marriage or trump exchange (if this is a valid move)
3.Elsif tries to play the same suit it played in the previous turn (if that is a valid move),  if there are multiple cards of that suit, it chooses the lowest one. 
4.Else, it plays a random valid move (which is not a marriage or trump exchange). 
"""