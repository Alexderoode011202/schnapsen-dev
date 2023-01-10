from typing import Optional, List

from schnapsen.game import Bot, Move, PlayerPerspective, SchnapsenTrickScorer
from deck import Card, Rank, Suit


class own_bot(Bot):
    def __init__(self):
        super().__init__()

    def get_move(self, state:PlayerPerspective, leader_move: Optional[Move]) -> Move:
        moves = state.valid_moves()

        # Check whether bully is playing first

        leader = PlayerPerspective.am_i_leader()
        trump = PlayerPerspective.get_trump_suit()
        
        trump_list: list = []
        non_trump_list: list = []

        for move in moves:
            if move[1] == trump:
                # If error: use move.Suit
                trump_list.append(move)

        if leader:
            
            if len(trump_list) == 0:
                for move in moves:
                    if move[0] == Rank.NINE:
                        non_trump_list.append(tuple(move, 0))
                    elif move[0] == Rank.JACK:
                        non_trump_list.append(tuple(move, 2))
                    elif move[0] == Rank.QUEEN:
                        non_trump_list.append(tuple(move, 3))
                    elif move[0] == Rank.KING:
                        non_trump_list.append(tuple(move, 4))
                    elif move[0] == Rank.TEN:
                        non_trump_list.append(tuple(move, 10))
                    else:
                        non_trump_list.append(tuple(move, 11))

                non_trump_list = max(non_trump_list, key=lambda x: x[1])
                return non_trump_list[0]
            else:
                return trump_list[0]

        # And now we cover his actions for when he is defending
        elif not leader:
            attacking_suit= move.cards[0].suit
            same_suit_moves: list = []
            different_suit_moves: list = []
            TS = SchnapsenTrickScorer()
            
            for move in moves:
                if move[1] == attacking_suit:
                    same_suit_moves.append(tuple(move,TS.rank_to_points(move.Suit)))
                else:
                    different_suit_moves.append(tuple(move, TS.rank_to_points(move.Suit)))

            if len(same_suit_moves) == 0:
                return max(different_suit_moves, lambda x: x[1])
            else:
                same_suit_moves[0]


# make output random where need be


                
            
                

# 1.same suit
# 1A. 
# 2.Highest card

