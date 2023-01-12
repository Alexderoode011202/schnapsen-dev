""" 
They assist
"""

from typing import Optional, List

from schnapsen.game import Bot, Move, PlayerPerspective, SchnapsenTrickScorer
from schnapsen.deck import Card, Rank, Suit
import random

def helper_highest(self, hand: list) -> Move:
        """ 
        :param hand: takes a list of moves (and already assumes that the list has been filtered correctly).
        Takes the highest card out of all possible moves.
        It is a helper function from sorting_hand() and assumes the hand contains all the relevant and filtered moves 
        """
        STS = SchnapsenTrickScorer
        best_value: int = -1000
        best_card: Move = None

        for move in hand:
            if STS.rank_to_points(move) > best_value:
                best_card = move
                best_value = STS.rank_to_points(move)
            else:
                continue
        
        return best_card

def helper_lowest(self, hand: list) -> Move:
    """ 
    is a helper function for the sort_cards() function and takes the lowest card from the bunch
    """

    STS = SchnapsenTrickScorer
    best_value: int = 1000
    best_card: Move = None

    for move in hand:
        if STS.rank_to_points(move) < best_value:
            best_card = move
            best_value = STS.rank_to_points(move)
        else:
            continue
    
    return best_card
    

def helper_random(self, hand: list) -> Move:
    """ 
    Is a helper function of the sort_cards() function and returns a random move from the list of moves
    """
    return random.sample(hand, 1)