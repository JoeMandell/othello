import math

class MCTSnode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        #these two values are how we tell how successful this node is
        #if visits = 3, wins = 1, it means we had 1 win and (3-1)=2 losses from this node.
        self.visits = 0
        self.wins = 0
        self.untried = state.children()
        self.amaf_wins = {}
        self.amaf_visits = {}
        self.rave_visits = 0

    #returns true if someone has won the game, otherwise false
    #REFACTOR - winner is long, could reduce to simply check for an end state instead
    def is_terminal(self):
        return self.state.winner() != None
    
    def fully_expanded(self):
        return len(self.untried) == 0
    
    def add_child(self,child):
        self.children.append(child)
    
    #select which child is the best - this is where we implement different policies.
    #this is the default one with sqrt2 as the exploration constant, hardcoded in.
    #if we are doing AMAF we need to use tobytes() to make the ndarray of the board hashable.
    def best_child(self):
        beta = 0.5
        return max(
            self.children,
            key=lambda c:  (c.wins/c.visits) + 1.41* math.sqrt(math.log(self.visits)/c.visits) 
                    # + beta*(c.amaf_wins.get(c.state.board.tobytes(),0)/max(c.amaf_visits.get(c.state.board.tobytes(),1 ),1))
        )
    
    def rave_best_child(self):
        def rave_score(node, child, beta=0.5):
            # Standard MCTS score
            uct_score = child.wins / max(child.visits, 1)
            
            # AMAF statistics
            move_key = child.state.board.tobytes()  # Assuming board state uniquely identifies moves
            amaf_wins = node.amaf_wins.get(move_key, 0)
            amaf_visits = node.amaf_visits.get(move_key, 1)
            amaf_score = amaf_wins / max(amaf_visits, 1)

            # Combine MCTS and AMAF scores
            return beta * amaf_score + (1 - beta) * uct_score
        beta = 0.5
        return max(
            self.children,
            key=lambda c: rave_score(self, c, beta) + 
                      1.41 * math.sqrt(math.log(self.visits) / max(c.visits, 1))  # Exploration term
        )

    
#activate python REPL with shift enter - might be useful?
