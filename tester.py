import game
import algorithm
import tqdm
import time

#runs a hundred games of two algorithms against each other.
white = 0
games = 10
start_time = time.time()
for i in tqdm.trange(games):
    winner, states = game.play(
        algorithm.mcts(10), #algorithm for white
        algorithm.minimax(algorithm.basic_heuristic, 3), #algorithm for black
        # algorithm.stochastic
    )
    print(winner)
    if winner == 1: white += 1

end_time = time.time()
print(f'Elapsed time: {(end_time-start_time)/games}')

print(f'Winrate: {(white*100)//games}%')
#the winrate i