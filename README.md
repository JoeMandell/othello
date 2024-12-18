# othello

This repo has three ways to run the algorithms.
1. You can play against a selected algorithm by running `visual.py`, this will open up a GUI where you can play.
2. You can test the effect of changing a single algorithm parameter using `graphmaker.py`, this will run batches of test games and generate graphs.
3. You can use the tester file to run batches of algorithms against each other and measure winrate by the color. Tester.py outputs text to the terminal.

### Nate's tester code
In the tester there are two ways to run tests.
You can make a new function for your test and call it in main fucntion.
You can also input algorithms into the test functions and call it in main function.
You can have it so our algorithms can play as White or Black but input stays the same (OurAlgorithm, Opponent)


A basic version of Monte Carlo tree search is present in the main code. Experimental approaches for AMAF and RAVE methods are in the MCTS-Optimization branch.



### References
This code is based on work by Vivek Myers, which you can find here
https://github.com/vivekmyers/Othello


