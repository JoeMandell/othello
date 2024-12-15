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
    def best_child(self):
        return max(
            self.children,
            key=lambda c:(c.wins/c.visits) + 1.41* math.sqrt(math.log(self.visits)/c.visits)
        )

    
#activate python REPL with shift enter - might be useful?
