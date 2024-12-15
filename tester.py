import game
import algorithm
import tqdm
import tqdm

#runs a hundred games of two algorithms against each other.
white = 0
games = 10
for i in tqdm.trange(games):
    winner, states = game.play(
        algorithm.mcts(80), #algorithm for white
        algorithm.minimax(algorithm.basic_heuristic, 3), #algorithm for black
        # algorithm.stochastic
    )
    print(winner)
    if winner == 1: white += 1
print(f'Winrate: {(white*100)//games}%')
#the winrate i