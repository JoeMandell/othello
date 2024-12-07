import game
import algorithm
import tqdm
import tqdm

#runs a hundred games of two algorithms against each other.
white = 0
for i in tqdm.trange(100):
    winner, states = game.play(
        algorithm.stochastic, #algorithm for white
        algorithm.stochastic_minimax(algorithm.basic_heuristic, 3), #algorithm for black
    )
    if winner == 1: white += 1
print(f'Winrate: {white}%')
#the winrate i