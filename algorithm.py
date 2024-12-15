from math import *
import random
import MCTSnode

test = False

def basic_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    return state.board.sum() + \
           state.board[([0, 0, 7, 7], [0, 7, 0, 7])].sum() * 4 + \
           state.board[0, :].sum() + state.board[:, 0].sum() + \
           state.board[7, :].sum() + state.board[:, 7].sum()


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
    return node

def expansion(node):
    move = node.untried.pop()
    new_state = node.state.place(move)
    child_node = MCTSnode.MCTSnode(state=new_state,parent=node)
    child_node.move = move
    node.add_child(child_node)
    return child_node  

def simulation(node):
    depth = 0
    max_depth = 2
    state = node.state
    #tried to make the simulation stop at a given depth. Not sure if this is correct.
    while not state.is_terminal() and state.valid_moves(state) != [] and depth < max_depth:
        state = state.place(random.choice(state.valid_moves(state)))
        depth += 1

    #this should make the algorithm return a heuristic at the max depth.
    if depth == max_depth and not state.is_terminal():
        return basic_heuristic(state)
    
    return state.winner()

def backpropagation(node,result):
    while node is not None:
        node.visits += 1
        if result == node.state.player:
            node.wins += 1
        node = node.parent

def best_child(node):
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

def mcts(iterations):
    print("hello")
    
    def select(root_state):
        root_node = MCTSnode.MCTSnode(root_state)
        for i in range(iterations):
            #select a node
            if test: print("selectioning")
            node = selection(root_node)
            #if it's not a term
            if not node.is_terminal():
                if test: print("running loop")
                if test: print("expanding")
                child = expansion(node)
                if test: print("simulationing")
                result = simulation(child)
                if test: print("backproping")
                backpropagation(child, result)
            else:
                if test: print("alternate backprop case")
                backpropagation(node, node.state.winner())
        print(best_child(root_node).move)
        return best_child(root_node).move
    return select




def stochastic(state):
    return random.choice(state.children())