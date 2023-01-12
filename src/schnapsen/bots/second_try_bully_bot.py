from typing import Optional, List

from schnapsen.game import Bot, Move, PlayerPerspective, SchnapsenTrickScorer
from schnapsen.deck import Card, Rank, Suit
import random

class second_bully(Bot):
    def __init__(self):
        super().__init__()

    def get_move(self, player_state: PlayerPerspective, leader_move: Optional[Move]) -> Move:
        # IF ATTACKING:
        # 1. Play random trump card
        # 2. Play highest card

        # IF DEFENDING:
        # 1. If having same card as attacking suit, play one of those at random
        # 2. Play Highest card

        moves = player_state.valid_moves()
        trump_suit = player_state.get_trump_suit()
        
        # None, Trump, ExceptTrump and a card from which it will derive the suit ((Not relevant))

        ### If we are attacking
        if player_state.am_i_leader():
            # If we have a trump card, we play a random one
            if len(move.cards[0].suit == trump_suit for move in moves) > 0:
                return sorting_hand(moves, state = player_state, suit="trump", priority= "random")
            # Otherwise we play the highest card
            else: 
                return sorting_hand(moves, state = player_state, suit= None, priority= "random")
        
        ### If we are defending
        else:
            attack_suit = leader_move.cards[0].suit
            
            # If we have the same suit as the attacking card, we (try to) deflect with a random one of those
            if len(move.cards[0].suit == attack_suit for move in moves) > 0:
                return sorting_hand(moves, state = player_state, suit=leader_move, priority = "random")
            # If we don't have any of those cards, we return a random card
            else: 
                return sorting_hand(moves, state= player_state, suit= None, priority= "random")


    
def sorting_hand(moves: List[Move],state: PlayerPerspective, suit: any = None, priority: str = "highest") -> Move:
    """ 
    Sorts the moves the player can make based on what is needed.
    :param moves: is the list of playable, legal moves the player can make
    :param state: Is the playerperspective that needs to be imported
    :param suit: allows the user to filter for a specific suit. By default it is none, which means there is no filter applied
    it accepts as input: None, Trump, ExceptTrump and a card from which it will derive the suit
    :param priority: can either be: "lowest", "highest", "random" (is "highest" by default)
    Returns: move with the highest priority
    """
    
    # Information start
    trump_suit = state.get_trump_suit()
    #Information End

    ### If no filter
    if suit == None:
        # If prioritizing highest
        if priority.lower() == "highest":
            return helper_highest(moves)
        # If prioritizing lowest
        elif priority.lower() == "lowest":
            return helper_lowest(moves)
        # If no priority
        elif priority.lower() == "random":
            return helper_random(moves)
    
    ### If filtering for trump suit
    elif suit == "Trump":
        trump_moves: list = [move.cards[0].suit == trump_suit for move in moves]

        # If prioritizing highest
        if priority.lower() == "highest":
            return helper_highest(trump_moves)
        #If prioritizing lowest
        elif priority.lower() == "lowest":
            return helper_lowest(trump_moves)
        #If no priority
        elif priority.lower() == "random":
            return helper_random(trump_moves)

    
    ### If filtering or everything EXCEPT trump suit
    elif suit == "ExceptTrump":
        except_trump_moves: list = [move.cards[0].suit != trump_suit for move in moves]
        # If prioritizing highest
        if priority.lower() == "highest":
            return helper_highest(except_trump_moves)
        # If prioritizing lowest
        elif priority.lower() == "lowest":
            return helper_lowest(except_trump_moves)
        # If no priority
        elif priority.lower() == "random":
            return helper_random(except_trump_moves)

    ### If filtering for a specific, suit
    else:
        exclusive_hand = [move.cards[0].suit == suit.cards[0].suit for move in moves]
        # If prioritizing highest
        if priority.lower() == "highest":
            return helper_highest(exclusive_hand)
        # If prioritizing lowest
        elif priority.lower() == "lowest":
            return helper_lowest(exclusive_hand)
        elif priority.lower() == "random":
            return helper_lowest(exclusive_hand)


def helper_highest(hand: list) -> Move:
    """ 
    :param hand: takes a list of moves (and already assumes that the list has been filtered correctly).
    Takes the highest card out of all possible moves.
    It is a helper function from sorting_hand() and assumes the hand contains all the relevant and filtered moves 
    """
    STS = SchnapsenTrickScorer()
    best_value: int = -1000
    best_card: Move = None

    for move in hand:
        if STS.rank_to_points(move) > best_value:
            best_card = move
            best_value = STS.rank_to_points(move)
        else:
            continue
    
    return best_card

def helper_lowest(hand: list) -> Move:
    """ 
    is a helper function for the sort_cards() function and takes the lowest card from the bunch
    """

    STS = SchnapsenTrickScorer()
    best_value: int = 1000
    best_card: Move = None

    for move in hand:
        if STS.rank_to_points(move) < best_value:
            best_card = move
            best_value = STS.rank_to_points(move)
        else:
            continue
    
    return best_card
    

def helper_random(hand: list) -> Move:
    """ 
    Is a helper function of the sort_cards() function and returns a random move from the list of moves
    """
    return random.sample(hand, 1)

""" 
Other debugging attempts:
##1.use move.suit instead of move.cards[0].suit (in discord it is moves.cards[0]. suit)
##2.Check whether the parameters were used right for the sorter
##3.Check for distinction between attacking and defending
4.Maybe the slicing went wrong
5.maybe there is a mistake in a helper function
6.Maybe add file instead of class in server.py
"""
    
        