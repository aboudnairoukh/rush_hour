import sys
import helper
from car import Car
from board import Board


class Game:
    """
    This class represents the game itself
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        print(self.board)
        user_input = input(
            "What car would you like to move, and in what direction? ")
        if user_input != '!':
            while (len(user_input) != 3 or
                   not self.board.move_car(user_input[0], user_input[2])) and \
                    user_input != '!':
                user_input = input(
                    "The input is not valid, please enter again what car "
                    "would you like to move, and in what direction? ")
        return user_input

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        if self.board.cell_content(self.board.target_location()) is not None:
            print("\nYou placed a car in the exit and completed the game\n")
        else:
            user_input = self.__single_turn()
            while self.board.cell_content(self.board.target_location()) is \
                    None and user_input != '!':
                user_input = self.__single_turn()
            if user_input != '!':
                print("\nYou have completed the game!\n")


if __name__ == "__main__":
    game_dict = helper.load_json(sys.argv[1])
    board = Board()
    for car_dict in game_dict:
        if car_dict in {'Y', 'B', 'O', 'G', 'W', 'R'}:
            car_lst = game_dict[car_dict]
            if (isinstance(car_lst[0], int) and isinstance(car_lst[1],
                                                           list) and
                    isinstance(car_lst[2], int)):
                location = car_lst[1]
                if (2 <= car_lst[0] <= 4 and 0 <= location[0] <= 6 and
                        0 <= location[1] <= 6 and car_lst[2] in {0, 1}):
                    board.add_car(Car(car_dict, car_lst[0], location,
                                      car_lst[2]))
    game = Game(board)
    game.play()
