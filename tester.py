import game
import algorithm
import tqdm
import time

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
    games = 100
    #runs a hundred games of two algorithms against each other.
    white = 0
    start_time = time.time()
    for i in tqdm.trange(games):
        winner, states = game.play(
            algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), #algorithm for white
            algorithm.stochastic, #algorithm for black
        )
        if winner == 1: white += 1
    end_time = time.time()
    print(f'Average time per game: {(end_time-start_time)/games}')
    print(f'White Winrate: {(white*100)//games}%')


if __name__=="__main__":
<<<<<<< HEAD
    test_AsBlack(algorithm.killer_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)
    test_AsBlack(algorithm.minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)
    test_AsBlack(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic) # stochastic_minimax has a percentage of 10% to pick the second best move

    test_AsWhite(algorithm.killer_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)
    test_AsWhite(algorithm.minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)
    test_AsWhite(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic) # stochastic_minimax has a percentage of 10% to pick the second best move

=======
    test_AsBlack(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)
    #test_AsWhite(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)



    #test_AsWhite(algorithm.stochastic_minimax(algorithm.edges_heuristic, 3), algorithm.minimax(algorithm.basic_heuristic, 3))
>>>>>>> cf5eb31e633e6fb4801573d5b4046d1dfc19fda5
