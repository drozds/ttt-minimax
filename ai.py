
from models import Result, Values
from random import randrange


class AI:

    def __init__(self, game, depth, is_stupid=False, with_ab=False) -> None:
        self._game = game
        self._depth = depth
        self._is_stupid = is_stupid
        self.with_ab = with_ab
        self.nr_of_iterations = 0

    def get_turn_coords(self, current_turn: Values):
        if self._is_stupid:
            (x, y) = (randrange(0, 3), randrange(0, 3))
            while self._game.current_state[x][y] != Values.Nothing:
                (x, y) = (randrange(0, 3), randrange(0, 3))
            return x, y
        else:
            (_, coords) = self.minimax(self._depth, current_turn == Values.X)
            return coords

    def minimax(self, depth, is_maximizing, alpha=Result.O_win.value - 1, beta=Result.X_win.value + 1):
        self.nr_of_iterations += 1
        result = self._game.get_current_result()
        final_coords = (None, None)
        if depth == 0 or result is not Result.Not_finished:
            if result == Result.X_win:
                return (1, None)
            elif result == Result.O_win:
                return (-1, None)
            else:
                return (0, None)
        result_eval = Result.O_win.value - 1 if is_maximizing else Result.X_win.value + 1
        for i in range(0, 3):
            for j in range(0, 3):
                if self._game.current_state[i][j] == Values.Nothing:
                    self._game.set_value(
                        i, j, Values.X if is_maximizing else Values.O)

                    (eval, _) = self.minimax(
                        depth - 1, not is_maximizing, alpha, beta)
                    if (is_maximizing and eval > result_eval) or (not is_maximizing and eval < result_eval):
                        result_eval = eval
                        final_coords = (i, j)
                    if self.with_ab:
                        if is_maximizing:
                            alpha = max(alpha, eval)
                            if beta <= alpha:
                                break
                        else:
                            beta = min(beta, eval)
                            if beta <= alpha:
                                break
                    self._game.set_value(i, j, Values.Nothing)
            else:
                continue
            break
        return result_eval, final_coords
