import enum


class Values(enum.Enum):
    O = -1
    Nothing = 0
    X = 1


class Result(enum.Enum):
    O_win = -1
    Tie = 0
    X_win = 1
    Not_finished = ''
