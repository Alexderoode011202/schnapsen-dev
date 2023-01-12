from typing import Optional, List

from schnapsen.game import Bot, Move, PlayerPerspective, SchnapsenTrickScorer
from schnapsen.deck import Card, Rank, Suit
import random


class own_bot(Bot):
    def __init__(self):
        super().__init__()

    def get_move(self, state:PlayerPerspective, leader_move: Optional[Move]) -> Move:
        moves = state.valid_moves()

        # Check whether bully is playing first

        leader = state.am_i_leader(self)
        trump = state.get_trump_suit(self)
        
        trump_list: list = []
        non_trump_list: list = []

        for move in moves:
            if move.cards[0].suit == trump:
                # If error: use move.Suit
                trump_list.append(move)

        if leader:
            
            if len(trump_list) == 0:
                for move in moves:
                    if  move.cards[0].suit == Rank.NINE:
                        non_trump_list.append(tuple(move, 0))
                    elif  move.cards[0].suit == Rank.JACK:
                        non_trump_list.append(tuple(move, 2))
                    elif  move.cards[0].suit == Rank.QUEEN:
                        non_trump_list.append(tuple(move, 3))
                    elif  move.cards[0].suit == Rank.KING:
                        non_trump_list.append(tuple(move, 4))
                    elif  move.cards[0].suit == Rank.TEN:
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
                if  move.cards[0].suit == attacking_suit:
                    same_suit_moves.append(tuple(move,TS.rank_to_points(move.Rank)))
                else:
                    different_suit_moves.append(tuple(move, TS.rank_to_points(move.Rank)))

            if len(same_suit_moves) == 0:
                return max(different_suit_moves, lambda x: x[1])
            else:
                # Added this line
                return same_suit_moves[0]

    def sorting_hand(self, moves: List[Move], suit: Suit, priority: str = "highest") -> Move:
        """ 
        Sorts the moves the player can make based on what is needed.
        :param hand: is the list of playable, legal moves the player can make
        :param priority: can either be: "lowest", "highest", "random" (is "highest" by default)
        :param trump: only looks at the trump cards if set to True (is False by default)
        Returns: move with the highest priority
        """
        
        # Information start
        STS = SchnapsenTrickScorer()
        best_move: int = -1000
        best_card: Card = None
        trump = PlayerPerspective.get_trump_suit()
        #Information End

        if trump:
            if priority.lower() == "highest":
                for move in moves:
                    if move.cards[0].suit == trump:
                        if STS.rank_to_points(move) > best_move:
                            best_move = STS.rank_to_points(move)
                            best_card = move
                        else:
                            continue

            elif priority.lower() == "Lowest":
                best_move = 1000
                for move in moves:
                    if move.cards[0].suit == trump:
                        if STS.rank_to_points(move) < best_move:
                            best_move = STS.rank_to_points(move)
                            best_card = move

                    else:
                        continue

            elif priority.lower() == "random":
                trump_moves: list = [move.cards[0].suit == trump for move in moves]
                return random.sample(trump_moves,1)

            else:
                raise ValueError

        # Non-trump selection
        else:

            if priority == "highest":
                for move in moves:
                    if move.cards[0].suit != trump:
                        if STS.rank_to_points(move) > best_move:
                            best_move = STS.rank_to_points(move)
                            best_card = move
                    else:
                        continue

            elif priority.lower() == "lowest":
                best_move = 1000
                for move in moves:
                    if move.cards[0].suit != trump:
                        if STS.rank_to_points(move) < best_move:
                            best_move = STS.rank_to_points(move)
                            best_card = move

            elif priority.lower() == "random":
                non_trump_suit = [move.cards[0].suit != trump for move in moves]
                return random.sample(non_trump_suit,1)

            else:
                raise ValueError

# make output random where need be
#  move.cards[0].suit
# 1.same suit
# 1A. 
# 2.Highest card

