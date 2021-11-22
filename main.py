from ai import AI
from game import Game


def main():
    game = Game()
    cpu_1 = AI(game, 9,  is_stupid=False, with_ab=False)
    cpu_2 = AI(game, 9, is_stupid=False, with_ab=True)
    game.initizalize_bots(cpu_1, cpu_2)
    game.play()


if __name__ == "__main__":
    main()
