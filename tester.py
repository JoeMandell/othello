import game
import algorithm
import tqdm

def test_AsWhite(OurAlgorithm, Opponent):
    #runs a hundred games of two algorithms against each other.
    white = 0
    for i in tqdm.trange(100):
        winner, states = game.play(
            OurAlgorithm, #algorithm for white
            Opponent, #algorithm for black
        )
        if winner == 1: white += 1
    print(f'White Winrate: {white}%')

def test_AsBlack(OurAlgorithm, Opponent):
    #runs a hundred games of two algorithms against each other.
    black = 0
    for i in tqdm.trange(100):
        winner, states = game.play(
            Opponent, #algorithm for white
            OurAlgorithm, #algorithm for black
        )
        if winner == -1: black += 1
    print(f'Black Winrate: {black}%')

def original_test():
    #runs a hundred games of two algorithms against each other.
    white = 0
    for i in tqdm.trange(100):
        winner, states = game.play(
            algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), #algorithm for white
            algorithm.stochastic, #algorithm for black
        )
        if winner == 1: white += 1
    print(f'Winrate: {white}%')


if __name__=="__main__":
    test_AsBlack(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)
    test_AsWhite(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)