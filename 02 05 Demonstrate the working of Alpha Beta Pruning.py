"""
Demonstrate the working of Alpha-Beta Pruning.
"""
"""
Pruning is the selective removal of certain parts of a plant, 
    such as branches, buds, or roots.
"""
"""
For games with two players, like chess and tic-tac-toe, players named as MAX 
    and MIN respectively
    MAX moves first, and then they take turns moving until the game is over
    At the end of the game, points are awarded to the winning player and 
        penalties are given to the loser

Game tree, tree where the nodes are game states and the edges are moves
    Includes initial state, actions, and results
        initial state, specifies how the game is set up at the start
        actions, set of legal moves in a state
        results, results of moves
    
Given a game tree, the optimal strategy can be determined from the minimax 
    value of each node
    
Pruning, eliminates large parts of the game tree from consideration
"""
"""
Alpha-beta pruning is an optimization technique for the minimax algorithm used 
    in decision-making for two-player games
    It reduces the number of nodes evaluated in the game tree by eliminating 
        branches that cannot influence the final decision
    Making the search faster, but still ensuring optimal decision is reached
        
    Achieved by maintaining two values, alpha and beta

    Alpha, best value that the maximizing player can guarantee at a given level
        or above
    Beta, best value that the minimizing player can guarantee at a given level
        or below    
"""
"""
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education

    Figure 5.7 The alpha–beta search algorithm. 
    Notice that these routines are the same as the MINIMAX functions in 
        Figure 5.3, except for the two lines in each of MIN-V ALUE and
        MAX-VALUE that maintain α and β 
        (and the bookkeeping to pass these parameters along).
        
        function ALPHA-BETA-SEARCH (state) 
            returns an action
            
            v ← MAX-VALUE (state, −∞, +∞)
            
            return the action in ACTIONS (state) with value v
        
        function MAX-VALUE(state, α, β) 
            returns a utility value
            
            if TERMINAL-TEST(state) then 
                return UTILITY(state)
        
            v ← −∞
        
            for each a in ACTIONS(state) 
                do            
                    v ← MAX(v , MIN -VALUE (RESULT(s,a), α, β))
            
                    if v ≥ β then 
                        return v
            
                    α ← MAX(α, v)
                
            return v
        
        function MIN-VALUE(state, α, β) 
            returns a utility value
        
            if TERMINAL-TEST(state) then 
                return UTILITY(state)
            
            v ← +∞
            
            for each a in ACTIONS(state) 
                do
                    v ← MIN(v, MAX-VALUE (RESULT(s,a) , α, β))
                    
                    if v ≤ α then 
                        return v
                    
                    β ← MIN(β, v)
                    
            return v        

"""

import math

line = "---"*14

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    """Recursively evaluates the game tree, 
        applying minimax algorithm with alpha-beta pruning logic

        node, current node in the game tree
        depth, current depth of the search
        alpha, best (highest) value that the maximizer can guarantee
        beta, best (lowest) value that the minimizer can guarantee
        maximizing_player, boolean indicating if it's maximizing player's turn

        Return optimal value for the current node    
    """
    if depth == 0 or not node.children:  # Base case: Leaf node or depth limit
        print(f"\n {node.name}, value = {node.value}")
        
        return node.value

    if maximizing_player:
        
        max_eval = -math.inf      # Start with assumption of minus infinity
        
        for child in node.children:            
            eval_val = alpha_beta(child, depth - 1, alpha, beta, False)            
            max_eval = max(max_eval, eval_val)
            alpha = max(alpha, eval_val)
            
            if beta <= alpha:     # Alpha-beta pruning
                print(f"\n Alpha-beta pruning, beta {beta} <= alpha {alpha}")
                break
            
        print(f"\n {node.name}, max player, max_eval = {max_eval}\n", line)
        
        return max_eval
    
    else:   # Minimizing player
        
        min_eval = math.inf        # Start with assumption of plus infinity
                
        for child in node.children:
            
            eval_val = alpha_beta(child, depth - 1, alpha, beta, True)
            
            min_eval = min(min_eval, eval_val)
            beta = min(beta, eval_val)
            
            if beta <= alpha:  # Alpha-beta pruning
                print(f"\n Alpha-beta pruning, beta {beta} <= alpha {alpha}")
                break
            
        print(f"\n {node.name}, min player, min_eval = {min_eval}\n", line)
        
        return min_eval    
    


class Node: # Represents each node in the game tree, has name, value, and children
    def __init__(self, name, value=None, children=None):
        self.name = name
        self.value = value
        self.children = children if children is not None else []

"""
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education

    Figure 5.2 A two-ply game tree, using structure, and only values of leaves

        MAX                            /A|
                                     /  |  |  
                               /        |      |  
                            /           |          |
        MIN              |B/            |C/            |D/ 
                   /  |  |           /  |  |            /  |  | 
                /    |   |          /   |   |          /   |   |  
              /     |    |        /     |    |        /     |    | 
          /_|    /_|    /_|      /_|    /_|   /_|    /_|    /_|   /_|
           3     12      8        2      4     6      14     5     2

    two-ply , two moves considered, one each by max and min player

    (Even in documentation, using just(only) backslash (in) other than 
         at end of comment/documentation(line), throws syntax warning, 
         its syntax warning, and not syntax error)
"""
"""      
Construct simple game tree for Figure 5.2, bottom up, leaves to root

    Structure is same, only leaves get values, 
        Node B, C, D, and A will get children assigned and not values
            
    Values for Node B, C, D, and A will be calculated later
        using alpha_beta(game tree)

Using list comprehension, instead of individual Node calls for each Node
"""
leaves_of_b = [Node(nam, val) for nam, val in 
               zip(["leaf_b1", "leaf_b2", "leaf_b3"], [3, 12, 8])]

leaves_of_c = [Node(nam, val) for nam, val in 
               zip(["leaf_c1", "leaf_c2", "leaf_c3"], [2, 4, 6])]

leaves_of_d = [Node(nam, val) for nam, val in 
               zip(["leaf_d1", "leaf_d2", "leaf_d3"], [14, 5, 2])] 

children_b_c_d = [Node(name, children=child) for name, child in 
                  zip(["child_b", "child_c", "child_d"], 
                      [leaves_of_b, leaves_of_c, leaves_of_d])]

"""
root, is directly assigned Node, and not [Node]
"""

root_a = Node("root_a", children=children_b_c_d)

# Computes optimal value using the alpha-beta pruning algorithm
optimal_value = alpha_beta(root_a, depth=3, alpha=-math.inf, beta=math.inf, 
                           maximizing_player=True)

print("\n The optimal value is:", optimal_value)


"""
Output:

 leaf_b1, value = 3

 leaf_b2, value = 12

 leaf_b3, value = 8

 child_b, min player, min_eval = 3
 ------------------------------------------

 leaf_c1, value = 2

 Alpha-beta pruning, beta 2 <= alpha 3

 child_c, min player, min_eval = 2
 ------------------------------------------

 leaf_d1, value = 14

 leaf_d2, value = 5

 leaf_d3, value = 2

 Alpha-beta pruning, beta 2 <= alpha 3

 child_d, min player, min_eval = 2
 ------------------------------------------

 root_a, max player, max_eval = 3
 ------------------------------------------

 The optimal value is: 3    
"""


























"""
One more example from:    
    University of Wisconsin, CS 540 - Introduction to Artificial Intelligence
    Homework problem: https://pages.cs.wisc.edu/~dyer/cs540/hw/hw2/HW2.pdf        
        
        Problem 1 (b) Use the Alpha-Beta pruning algorithm
        
    Solution: https://pages.cs.wisc.edu/~dyer/cs540/hw/hw2/HW2_written_sol.pdf
"""
"""
Problem 1 (b)

    Four-ply , four moves considered, two each by max and min player
    
                                                                                    
    MAX                                     A
    
    MIN                 B                   C                   D
    
    MAX          E       F       16         G       12          H       I
    
    MIN     4   13      J  11           K   9   L           10  8  M    7  4
    
                      5  10           1  8      6  12           2  5  7
"""
leaves_of_e = [Node(nam, val) for nam, val in 
               zip(["leaf_e1", "leaf_e2"], [4, 13])]
leaves_of_j = [Node(nam, val) for nam, val in 
               zip(["leaf_j1", "leaf_j2"], [5, 10])]
leaves_of_f = [Node("leaf_f1", 11)]
leaves_of_b = [Node("leaf_b1", 16)]

leaves_of_k = [Node(nam, val) for nam, val in 
               zip(["leaf_k1", "leaf_k2"], [1, 8])]
leaves_of_g = [Node("leaf_g1", 9)]
leaves_of_l = [Node(nam, val) for nam, val in 
               zip(["leaf_l1", "leaf_l2"], [6, 12])]
leaves_of_c = [Node("leaf_c1", 12)]

leaves_of_h = [Node(nam, val) for nam, val in 
               zip(["leaf_h1", "leaf_h2"], [10, 8])]
leaves_of_m = [Node(nam, val) for nam, val in 
               zip(["leaf_m1", "leaf_m2", "leaf_m3"], [2, 5, 7])]
leaves_of_i = [Node(nam, val) for nam, val in 
               zip(["leaf_i1", "leaf_i2"], [7, 4])]

child_e = [Node("child_e", children=leaves_of_e)]
child_j = [Node("child_j", children=leaves_of_j)]
child_f = [Node("child_f", children=child_j + leaves_of_f)]
child_b = [Node("child_b", children=child_e + child_f + leaves_of_b)]

child_k = [Node("child_k", children=leaves_of_k)]
child_l = [Node("child_l", children=leaves_of_l)]
child_g = [Node("child_g", children=child_k + leaves_of_g + child_l)]
child_c = [Node("child_c", children=child_g + leaves_of_c)]

child_m = [Node("child_m", children=leaves_of_m)]
child_h = [Node("child_h", children=leaves_of_h + child_m)]
child_i = [Node("child_i", children=leaves_of_i)]
child_d = [Node("child_d", children=child_h + child_i)]

root_a = Node("root_a", children=child_b + child_c + child_d)

print(line, "\n Run of another example \n", line)

optimal_value = alpha_beta(root_a, depth=5, alpha=-math.inf, beta=math.inf, 
                           maximizing_player=True)

print("\n Another example, optimal value is:", optimal_value)

"""
Expected: Solution to Problem 1 (b) 
                                                                                
MAX                                    11

MIN                11                   9                   10

MAX        13       11       16         9       12          10       I

MIN     4   13      5  11           1   9   6           10  8  2    7  4

                  5  10           1  8      6  12           2  5  7
"""
"""
Output:

 leaf_e1, value = 4

 leaf_e2, value = 13

 child_e, max player, max_eval = 13
 ------------------------------------------

 leaf_j1, value = 5

 leaf_j2, value = 10

 child_j, min player, min_eval = 5
 ------------------------------------------

 leaf_f1, value = 11

 child_f, max player, max_eval = 11
 ------------------------------------------

 leaf_b1, value = 16

 child_b, min player, min_eval = 11
 ------------------------------------------

 leaf_k1, value = 1

 Alpha-beta pruning, beta 1 <= alpha 11

 child_k, min player, min_eval = 1
 ------------------------------------------

 leaf_g1, value = 9

 leaf_l1, value = 6

 Alpha-beta pruning, beta 6 <= alpha 11

 child_l, min player, min_eval = 6
 ------------------------------------------

 child_g, max player, max_eval = 9
 ------------------------------------------

 Alpha-beta pruning, beta 9 <= alpha 11

 child_c, min player, min_eval = 9
 ------------------------------------------

 leaf_h1, value = 10

 leaf_h2, value = 8

 leaf_m1, value = 2

 Alpha-beta pruning, beta 2 <= alpha 11

 child_m, min player, min_eval = 2
 ------------------------------------------

 child_h, max player, max_eval = 10
 ------------------------------------------

 Alpha-beta pruning, beta 10 <= alpha 11

 child_d, min player, min_eval = 10
 ------------------------------------------

 root_a, max player, max_eval = 11
 ------------------------------------------

 Another example, optimal value is: 11
"""