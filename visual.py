import game
import algorithm
import tqdm
# import neural
import tqdm
import tkinter

#if you skip the second algorithm, player gets to play.
#if you put in two algorithms they play against each other.
try:
    game.play_gui(
        algorithm.stochastic_minimax(algorithm.corners_heuristic, 3),
        #algorithm.stochastic,
        delay=1,
        heuristic=algorithm.basic_heuristic
    )
    # game.play_gui(
    #     algorithm.stochastic_minimax(algorithm.basic_heuristic, 5),
    #     # algorithm.stochastic_minimax(algorithm.basic_heuristic, 5),
    #     delay=1,
    #     heuristic=algorithm.basic_heuristic
    # )
    game.play_gui(algorithm.mcts(80))
except (tkinter.TclError, KeyboardInterrupt, EOFError):
    print('\nQuit')
    exit(1)