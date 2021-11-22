import time

from ai import AI
from models import Result, Values


class Game:
    def __init__(self):
        self.initialize_game()

    def initizalize_bots(self, ai_1, ai_2):
        self.ai_1 = ai_1
        self.ai_2 = ai_2

    def initialize_game(self):
        self.current_state = [[Values.Nothing, Values.Nothing, Values.Nothing],
                              [Values.Nothing, Values.Nothing, Values.Nothing],
                              [Values.Nothing, Values.Nothing, Values.Nothing]]
        self.which_turn = Values.X

    def set_value(self, i, j, value):
        self.current_state[i][j] = value

    def get_current_result(self) -> Result:
        for i in range(0, 3):
            if (self.current_state[0][i] != Values.Nothing and
                self.current_state[0][i] == self.current_state[1][i] and
                    self.current_state[1][i] == self.current_state[2][i]):
                return Result.X_win if self.current_state[0][i] == Values.X else Result.O_win

        for i in range(0, 3):
            if (self.current_state[i] == [Values.X, Values.X, Values.X]):
                return Result.X_win
            elif (self.current_state[i] == [Values.O, Values.O, Values.O]):
                return Result.O_win

        if (self.current_state[0][0] != Values.Nothing and
            self.current_state[0][0] == self.current_state[1][1] and
                self.current_state[0][0] == self.current_state[2][2]):
            return Result.X_win if self.current_state[0][0] == Values.X else Result.O_win

        if (self.current_state[0][2] != Values.Nothing and
            self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return Result.X_win if self.current_state[0][2] == Values.X else Result.O_win

        for i in range(0, 3):
            for j in range(0, 3):
                if (self.current_state[i][j] == Values.Nothing):
                    return Result.Not_finished

        return Result.Tie

    def swap_turn(self):
        self.which_turn = Values.X if self.which_turn == Values.O else Values.O

    def play(self):
        while True:
            result = self.get_current_result()

            if result != Result.Not_finished:
                if result == Result.X_win:
                    print('The winner is X!')
                elif result == Result.O_win:
                    print('The winner is O!')
                elif result == Result.Tie:
                    print("It's a tie!")
                print(f"CPU-1: {self.ai_1.nr_of_iterations} steps")
                print(f"CPU-2: {self.ai_2.nr_of_iterations} steps")
                self.initialize_game()
                return

            (x, y) = (None, None)
            if self.which_turn == Values.X:
                (x, y) = self.ai_1.get_turn_coords(self.which_turn)
                # print(f"CPU-1: X - {x}, Y - {y}")
            else:
                (x, y) = self.ai_2.get_turn_coords(self.which_turn)
                # print(f"CPU-2: X - {x}, Y - {y}")
            self.current_state[x][y] = self.which_turn
            self.swap_turn()

    # def get_static_evaluation(self):
    #     heur_points = [[0.3, 0.2, 0.3], [0.2, 0.4, 0.2], [0.3, 0.2, 0.3]]
    #     for i in range(0, 3):
    #         for j in range(0, 3):
