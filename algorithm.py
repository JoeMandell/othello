from math import *
import random
import math

from othello import State
import MCTSnode

test = False

def basic_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    return state.board.sum() + \
           state.board[([0, 0, 7, 7], [0, 7, 0, 7])].sum() * 4 + \
           state.board[0, :].sum() + state.board[:, 0].sum() * 2 + \
           state.board[7, :].sum() + state.board[:, 7].sum() * 2

def new_basic_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    return state.board[([0, 0, 7, 7], [0, 7, 0, 7])].sum() + \
           state.board[0, :].sum() + state.board[:, 0].sum() + \
           state.board[7, :].sum() + state.board[:, 7].sum()

################################################################ Nate
def disc_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    total = state.board.sum()
    return total

def mobility_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    total = 0

    current_player_mobility = 0
    opponent_mobility = 0

    for x in range(8):
        for y in range(8):
            move = (x, y)
            if state.isvalid(move):
                if state.player == -1:  # Current player is black (-1)
                    current_player_mobility += 1
                else:  # Current player is white (1)
                    opponent_mobility += 1
    return current_player_mobility - opponent_mobility

def corners_heuristic(state):
    winner = state.winner()
    if winner is not None:
        return winner * 128
    total = state.board[([0, 0, 7, 7], [0, 7, 0, 7])].sum() * 4
    return total

def edges_heuristic(state):
    winner = state.winner()
    if winner is not None:
        return winner * 128
    total = state.board[0, :].sum() + state.board[:, 0].sum() + \
            state.board[7, :].sum() + state.board[:, 7].sum()
    return total

################################################################ Nate
# helper for weighted heuristic
WEIGHTS = [4, -3, 2, 2, 2, 2, -3, 4,
            -3, -4, -1, -1, -1, -1, -4, -3,
            2, -1, 1, 0, 0, 1, -1, 2,
            2, -1, 0, 1, 1, 0, -1, 2,
            2, -1, 0, 1, 1, 0, -1, 2,
            2, -1, 1, 0, 0, 1, -1, 2,
            -3, -4, -1, -1, -1, -1, -4, -3,
            4, -3, 2, 2, 2, 2, -3, 4]

def cornerweight(state):
    total = 0;
    i = 0;
    while i < 64:
        if state.board[(i//8, i%8)] == state.player:
            total += WEIGHTS[i];
            #print "weights" + str(i) + "number:"+ str(StudentEngine.WEIGHTS[i])
        if state.board[(i//8, i%8)] == -state.player:
            total -= WEIGHTS[i];
            #print "weights" + str(i) + "number:"+ str(StudentEngine.WEIGHTS[i])
        i += 1
    #print "cornerweight" + str(total)
    return total

def _get_cost(state):
    """ Return the difference in number of pieces after the given move 
    is executed. """

    # Create a deepcopy of the board to preserve the state of the actual board
    #newboard = deepcopy(board)
    #newboard.execute_move(move, color)

    # Count the # of pieces of each color on the board
    num_pieces_op = (state.board == -state.player).sum()
    num_pieces_me = (state.board == state.player).sum()
    #print "_get_cost" + str(num_pieces_me - num_pieces_op)
    # Return the difference in number of pieces
    return num_pieces_me - num_pieces_op


def weighted_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    return 2 * cornerweight(state) + 3 * _get_cost(state)
    

def greedy(heuristic):
    return lambda s: max(s.children(), key=lambda x: heuristic(x) * s.player)


def human(state):
    print(state)
    nxt = state.place(eval('({0})'.format(input('> '))))
    if nxt in state.children():
        print(nxt)
    return nxt


def _evaluate(state, depth, alpha, beta, heuristic):
    if depth == 1:
        return heuristic(state)
    elif state.player == 1:
        value = -inf
        for i in state.children():
            value = max(value, _evaluate(i, depth - 1, alpha, beta, heuristic))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = inf
        for i in state.children():
            value = min(value, _evaluate(i, depth - 1, alpha, beta, heuristic))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


def minimax(heuristic, max_depth):
    return lambda s: max(s.children(), key=lambda x: _evaluate(
        x, max_depth, -inf, inf, heuristic) * s.player)


def stochastic_minimax(heuristic, max_depth):
    def select(state):
        result = sorted(state.children(), key=lambda x: -_evaluate(
            x, max_depth, -inf, inf, heuristic) * state.player)[:2]
        if random.random() < 0.1:
            return result[-1]
        else:
            return result[0]

    return select

#MCTS helper functions
def selection(node):
    while node.fully_expanded() and not node.is_terminal():
        node = node.best_child()
    # print(node.state)
    return node

def expansion(node):
    new_state = node.untried.pop()
    child_node = MCTSnode.MCTSnode(state=new_state,parent=node)
    node.add_child(child_node)
    return child_node  

def simulation(node):
    state = node.state
    #playout by picking random moves
    while not state.is_terminal() and state.children() != []:
        state = random.choice(state.children())

    return state.winner()

def backpropagation(node,result,desired_winner):
    while node is not None:
        node.visits += 1
        if result == desired_winner:
            node.wins += 1
        node = node.parent

#this method does NOT need to know which player is calling it, since it only goes on number of visits
def most_visited_child(node):
    return max(node.children, key=lambda c: c.visits)
    
"""
Lecture implementation
def monte_carlo_tree_search(state):
    tree = Node(state)
    while is_time_remaining():
        leaf = Select(tree)
        child = Expand(leaf)
        result = Simulate(child)
        BackPropagate(result, child)
    return the move in Actions(state) whose node has highest number of playouts

GPT implementation
def mcts(root_state, iterations):
    root_node = MCTSNode(state=root_state)
    for _ in range(iterations):
        node = selection(root_node)
        if not node.is_terminal():
            child = expansion(node)
            result = simulation(child)
            backpropagation(child, result)
        else:
            backpropagation(node, node.state.winner())
    return best_child(root_node)
"""

#currently trying to make white win
def mcts(iterations):
    desired_winner = 1
    
    def select(root_state):
        root_node = MCTSnode.MCTSnode(root_state)
        for i in range(iterations):
            #select a node
            node = selection(root_node)
            if not node.is_terminal():
                child = expansion(node)
                result = simulation(child)
                backpropagation(child, result, desired_winner)
            else:
                backpropagation(node, node.state.winner(), desired_winner)
        # print(best_child(root_node).state)
            # print(f'{root_node.wins} / {root_node.visits}')
        # most_visited = most_visited_child(root_node)
        # print(f'{most_visited.wins} / {most_visited.visits}')
        return most_visited_child(root_node).state
    return select




def stochastic(state):
    return random.choice(state.children())

def killer_evaluate(state, depth, alpha, beta, heuristic, killers=None, cnt=[0]):
    # Initialize the killer move table if not provided
    if killers is None:
        killers = {}

    # Ensure the killers dictionary has a key for this depth
    if depth not in killers:
        killers[depth] = []  # Initialize an empty list for this depth

    cnt[0] += 1  # Increment the counter for every node explored

    if depth == 1 or state.is_terminal():
        return heuristic(state), killers, cnt

    children = state.children()
    children = sorted(children, key=lambda x: heuristic(x), reverse=(state.player == 1))
    # Separate killer and non-killer children
# Ensure children are comparable by value, not by object identity
    killer_children = [child for child in children if any(child == killer for killer in killers[depth])]
    non_killer_children = [child for child in children if child not in killer_children]

    # Combine killer and non-killer children
    ordered_children = killer_children + non_killer_children

    if state.player == 1:  # Maximizing player
        value = -inf
        for child in ordered_children:
            cnt[0] += 1
            temp_value, killers, cnt = killer_evaluate(child, depth - 1, alpha, beta, heuristic, killers, cnt)
            value = max(value, temp_value)
            if value > alpha:
                alpha = value
                # Add child to killer moves if it causes a beta cutoff
                if alpha >= beta:
                    if child not in killers[depth]:
                        if len(killers[depth]) >= 5:  # Limit to 2 killer moves
                            killers[depth].pop(0)
                        killers[depth].append(child)
                    break
        return value, killers, cnt
    else:  # Minimizing player
        value = inf
        for child in ordered_children:
            cnt[0] += 1
            temp_value, killers, cnt = killer_evaluate(child, depth - 1, alpha, beta, heuristic, killers, cnt)
            value = min(value, temp_value)
            if value < beta:
                beta = value
                # Add child to killer moves if it causes an alpha cutoff
                if beta <= alpha:
                    if child not in killers[depth]:
                        if len(killers[depth]) >= 2:  # Limit to 2 killer moves
                            killers[depth].pop(0)
                        killers[depth].append(child)
                    break
        return value, killers, cnt


    
def killer_minimax(heuristic, max_depth):
    counter = [0]  # Initialize the counter
    return lambda s: max(s.children(), key=lambda x: killer_evaluate(
        x, max_depth, -inf, inf, heuristic, {}, counter)[0] * s.player)
