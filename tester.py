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
    test_AsBlack(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)
    test_AsWhite(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic)

    test_AsWhite(algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), algorithm.stochastic) #89 Winrate
   # test_AsWhite(algorithm.stochastic_minimax(algorithm.new_new_mobility_heuristic, 2), algorithm.stochastic) #49 Winrate
    #test_AsWhite(algorithm.stochastic_minimax(algorithm.mobility_heuristic, 3), algorithm.stochastic) #49 Winrate
    #test_AsWhite(algorithm.stochastic_minimax(algorithm.disc_heuristic, 3), algorithm.stochastic) #86 Winrate
    #test_AsWhite(algorithm.stochastic_minimax(algorithm.corners_heuristic, 3), algorithm.stochastic) #91
    #test_AsWhite(algorithm.stochastic_minimax(algorithm.edges_heuristic, 3), algorithm.stochastic) #97
    #test_AsWhite(algorithm.stochastic_minimax(algorithm.corners_heuristic, 3), algorithm.greedy(algorithm.disc_heuristic)) #91
