import game
import algorithm
import tqdm
import matplotlib.pyplot as plt

#define a parameter that you want to change in the test algorithm
#could be search depth for minimax, iteration count for monte carlo, etc.
variable = range(1,4)

#setup
y_values = []
batchsize = 50

for value in variable:
    print(value)

    #define your algorithm and benchmark
    test_algo = algorithm.minimax(algorithm.basic_heuristic, value)
    bench_algo = algorithm.stochastic

    wins = 0
    for _ in range(batchsize):
        result, state = game.play(test_algo, bench_algo)
        if result == 1:
            wins += 1
        print(f'{result}, so far {wins} wins.')
    wins /= batchsize #convert to a percent winrate
    y_values.append(wins)

print(y_values)

#adjust label text if you want
label_text = "winrate of minimax algorithm with different search depths, playing against another minimax with depth = 1"
label_stats = f'batchsize: {batchsize}  variable range {variable}'


plt.plot(range(len(variable)), y_values)
plt.title(label_text + "\n" + label_stats)
plt.show()