from typing import Optional, List

from schnapsen.game import Bot, Move, PlayerPerspective
from deck import Card, Rank, Suit

class own_bot(Bot):
    def __init__(self):
        super().__init__()

    def get_move(self, state: PlayerPerspective, leader_move: Optional[Move]) -> Move:
        """ 
        Here we choose what move the bot should make
        """
        moves = state.valid_moves()
        #-----HERE WE DO THE ATTACKING PART------
        #First we determine whether we are "attacking" or "defending"
        ...

        # Here we determine the possible marriages
        if len(self.check_for_marriages(moves)) >0: 
            marr_list = self.check_for_marriages(moves)

        #If we are attacking, we announce a marriage and play the queen of that marriage
        ...

        #If we are attacking but don't have a marriage ready, we play a low-value card like a jack
        ...

        #-----HERE WE SWITCH TO DEFENDING----



    def prioritize(self, moves_list: list) -> list:
        """ 
        returns a the list of moves in an ordered fashion based on the heuristic function I made
        :param moves_list: is the list of available moves'
        :param heuristic_function: Is the function which we base the values of our moves on
        """
        value_list: list = []
        # value_dict: dict = {}
        for move in moves_list:
            value_list.append(tuple(move, func(move)))

    

    def check_for_marriages(self, moves_list)-> list:
        """
        Here we check whether a marriage is possible
        It is means to be part of the heuristic function
        :param moves_list: takes the moves that can be made by the player
        :returns: a list of tuples of cards which would make for a marriage. 
        However, if there are not marriages, the functions returns False
        """
        marriages_list: List[tuple] = []
        for move in moves_list:
            if move[0] == Rank.QUEEN:
                for another_move in moves_list:
                    if another_move[0] == Rank.KING and move[1] == another_move[1]:
                        # If we get here we have found a valid marriage
                        marriages_list.append(tuple(move, another_move))

            elif move[0] == Rank.KING:
                for another_move in moves_list:
                    if another_move[0] == Rank.QUEEN and move[1] == another_move[1]:
                        marriages_list.append(tuple(move, another_move))
        if marriages_list == []:
            return False
        else:
            return marriages_list

    def heuristic_function(self, move: Move) -> float:
            """ 
            Returns the heuristic value of a particular move in a given gamestate
            :param move: contains the move we want to calculate the heuristic value of
            :returns: float containing the heuristic value of the given move
            """
            if check_for_marriages() == False

            return some_score


                
            

