from math import *
import random
import math

from othello import State


def basic_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    return state.board.sum() + \
           state.board[([0, 0, 7, 7], [0, 7, 0, 7])].sum() * 8 + \
           state.board[0, :].sum() + state.board[:, 0].sum() + \
           state.board[7, :].sum() + state.board[:, 7].sum()
################################################################
def disc_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    total = state.board.sum()
    return total

def mobility_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    total = 0

    for x in range(8):
        for y in range(8):
            move = (x, y)
            if state.isvalid(move):
                total += 1
    return total

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

def all_heuristic(state):
    if state.winner() is not None:
        return state.winner() * 128
    return state.board.sum() + \
           state.board[([0, 0, 7, 7], [0, 7, 0, 7])].sum() * 4 + \
           state.board[0, :].sum() + state.board[:, 0].sum() + \
           state.board[7, :].sum() + state.board[:, 7].sum()


################################################################
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


def stochastic(state):
    return random.choice(state.children())