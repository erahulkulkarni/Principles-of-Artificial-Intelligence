"""
Solve the 8-Puzzle problem using A* Algorithm
"""
"""
    8-Puzzle problem, consists of a 3×3 board with eight numbered tiles and a 
        blank space
    A tile adjacent to the blank space can slide into the space
    The objective is to reach a specified goal state
    
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education
                Figure 3.4 A typical instance of the 8-puzzle
              ----   ----   ----            ----   ----   ----
             | 7 |  | 2 |  | 4 |           |   |  | 1 |  | 2 |
              ----   ----   ----            ----   ----   ----
             | 5 |  |   |  | 6 |           | 3 |  | 4 |  | 5 |
              ----   ----   ----            ----   ----   ----
             | 8 |  | 3 |  | 1 |           | 6 |  | 7 |  | 8 |
              ----   ----   ----            ----   ----   ----             
                 Start State                    Goal State    
     8-puzzle belongs to the family of sliding-block puzzles
     8-puzzle is NP-complete
"""

initial_board = (7, 2, 4, 5, 0, 6, 8, 3, 1)                     # Start State
goal_board = (0, 1, 2, 3, 4, 5, 6, 7, 8)                        # Goal State

"""
    A* Algorithm, A star algorithm, is a best-first search algorithm,  
        that evaluates nodes by combining g(n), the cost to reach the node, and 
        h(n), the cost to get from the node to the goal
            
            f(n) = g(n) + h(n)

    g(n) gives the path cost from the start node to node n, and 
    h(n) is the estimated cost of the cheapest path from n to the goal
    f(n) = estimated cost of the cheapest solution through n    

    A* algorithm can be implemented using a priority queue (min-heap)
        to explore best(min) paths in a graph

    To solve the 8-puzzle problem using the A* algorithm
        Implement a class to represent the puzzle state
        Define the A* search function
        Use heuristics (Manhattan distance/Misplaced Tiles) to guide the search, 
            Using priority queue (min-heap) for efficient search    
"""
"""
                            Manhattan distance
Distance between two points in a grid-like layout, such as city streets, 
    summing the absolute differences of their coordinates
                            
Levitin A, Introduction to the Design and Analysis of Algorithms, Pearson
    
For points p1 (x1, y1) and p2 (x2, y2 ) in the Cartesian plane, Manhattan 
distance dM is defined as:
    
            dM (p1, p2) = |x1 − x2| + |y1 − y2|
"""
"""
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education 

    City block distance or Manhattan distance
    
    Sum of the distances of the tiles from their goal positions
    Because tiles cannot move along diagonals, the distance will be the 
        sum of the horizontal and vertical distance

        ----   ----   ----          ----   ----   ----
       |   |  | 1 |  | 2 |         | 7 |  | 2 |  | 4 |
        ----   ----   ----          ----   ----   ----
       | 3 |  | 4 |  | 5 |         | 5 |  |   |  | 6 |
        ----   ----   ----          ----   ----   ----
       | 6 |  | 7 |  | 8 |         | 8 |  | 3 |  | 1 |
        ----   ----   ----          ----   ----   ----
            Goal State                Start State

With respect to Goal State, Tile number in Start State is off by: 
              (vertical) + (horizontal)
                 (row)   +   (column)
    Tile 1 ,     ↓ 2     +     → 1      =  3
         2 ,       0     +     ← 1      =  1
         3 ,     ↓ 1     +     → 1      =  2
         4 ,     ↑ 1     +     → 1      =  2
         5 ,       0     +     ← 2      =  2
         6 ,     ↑ 1     +     → 2      =  3
         7 ,     ↑ 2     +     ← 1      =  3
         8 ,       0     +     ← 2      =  2
                     dM of Start State  = 18
"""
"""
divmod(a, b), returns a tuple, (quotient, remainder) of a/b    

for i in 0 to 8    
     row, column = divmod(i, 3) 
     
    (row, column) will represent where i would be placed(indices) on 3×3 board
    
Goal State (0, 1, 2, 3, 4, 5, 6, 7, 8), represented as (row column)
    0 (0, 0), 1 (0, 1), 2 (0, 2), 
    3 (1, 0), 4 (1, 1), 5 (1, 2), 
    6 (2, 0), 7 (2, 1), 8 (2, 2)
"""    
"""
For any valid board state:
    
    If a numbered tile is at current(row, column), 
        but instead should have been at goal(row, column)
                
    Then current tile is off by: 
        horizontal(so many columns) and vertical(so many rows)

    Manhattan distance = Difference between row column representation of 
                            current and goal state

                 ----   ----   ----          ----   ----   ----
                |   |  | 1 |  | 2 |         | 7 |  | 2 |  | 4 |
                 ----   ----   ----          ----   ----   ----
                | 3 |  | 4 |  | 5 |         | 5 |  |   |  | 6 |
                 ----   ----   ----          ----   ----   ----
                | 6 |  | 7 |  | 8 |         | 8 |  | 3 |  | 1 |
                 ----   ----   ----          ----   ----   ----
                     Goal State                Start State
                                
    Tile 7 should be at (2, 1) , but is at location (0, 0), is off by
        row + column diffewence between (2, 1) and (0, 0) = 2 + 1 = 3
    
    Tile 5 should be at (1, 2) , but is at location (1, 0), is off by
        row + column diffewence between (1, 2) and (1, 0) = 0 + 2 = 2
"""

import heapq
"""
heapq, implementation of the heap queue algorithm (priority queue algorithm)

                            Priority queue, Heap
Levitin A, Introduction to the Design and Analysis of Algorithms, Pearson    

    A priority queue is a collection of data items from a totally ordered 
        universe (order matters, usually integer or real numbers)
        
    The principal operations on a priority queue are:
        finding, deleting its largest (smallest) element, adding a new element
  
    The root of a heap always contains its largest (smallest) element
"""

"""
    For simplicity, blank space represented as 0 on board
"""

class PuzzleState:
    
    def __init__(self, board, parent=None, move=None, g_cost=0):
        self.board = board                  # Tuple representing the 3x3 board
        self.parent = parent
        self.move = move
        self.g_cost = g_cost            # Cost from start node to current node
    """        
        __init__(self, board, parent=None, move=None, g_cost=0)        
        default values are assigned when values not passed in as arguments
        
        Examples:
            PuzzleState(initial_board)
            that is
            PuzzleState(self, board = initial_board)
                self, is the invoking object
                board = initial_board
                parent = None , initial_board has no earlier state
                move = None , no moves made to get to initial_board state
                g_cost = 0 , as it is ininital state, 0 cost to reach the node
        
        For next state(or move) PuzzleState objects
        
            PuzzleState(tuple(new_board), self, move_name, self.g_cost + 1)
            that is
            PuzzleState(self", board = tuple(new_board), parent = self', 
                        move = move_name, g_cost = self'.g_cost + 1)
                
                self" and self', both objects of PuzzleState
                
                self" (child) is the next state (or move) of self' (parent)
                
                self", is the invoking object
                board = tuple(new_board)
                parent = self', self' set as parent of self"
                                                       self".parent = self'
                move = move_name , is one of "up", "down", "right", or "left"
                g_cost = self'.g_cost + 1
                    child self" cost set to one more than parent self' cost
                    self".g_cost = self'.g_cost + 1
    """            

    """ Operator overloading
        __lt__ method used to define the behavior of the less than operator (<)
        so that objects(values) of class PuzzleState can be compared
        Is self(object) f_cost value < other(object) f_cost value ? """
    def __lt__(self, other): 
        # For priority queue comparison of f_cost, f_cost = g_cost + h_cost
        self_f_cost = self.g_cost + self.manhattan_distance()
        other_f_cost = other.g_cost + other.manhattan_distance()
        
        return self_f_cost < other_f_cost    

    """ Operator overloading 
        __eq__ method defines behavior of equality operator ==
        Is self(object) board setting == other(object) board setting ? """
    def __eq__(self, other):
        return self.board == other.board

    """ Operator overloading
        __hash__ method is used to define a custom hash value for an object        
        When __eq__ is overloaded, __hash__ also has to be overloaded
            to maintain integrity of the hash value, both operating on board"""
    def __hash__(self):
        return hash(self.board)

    """ Heuristic, h , dM of entire board (excluding blank space), 
        Returns sum of Manhattan distances of misplaced tiles """
    def manhattan_distance(self):

        manhattan_distance = 0                

        for i in range(9):                        # For all tiles in 3×3 board 
             # self.board[i] has numeric value of tile
            if self.board[i] != 0:                # if it is not a blank space
                
                goal_row, goal_column = divmod(i, 3)
                
                curr_row, curr_col = divmod(self.board[i], 3)                
                                          
                horiz_dist = abs(curr_col - goal_column)  # abs( column diff )
                vert_dist = abs(curr_row - goal_row)      # abs( row diff )
                
                # Sum over all numeric tiles
                # manhattan_distance = manhattan_distance + dM(current tile)
                manhattan_distance +=  horiz_dist + vert_dist
                
        return manhattan_distance

    def get_blank_space_position(self):        
        return self.board.index(0)                     # Index of blank space
    
    def slide_numeric_tile_into_blank_space(self, board, index1, index2):
        """
        Swap values in list at specified indices
        Slide/Swap neighbor numeric tile with blank blank space in board 

            board passed here is a list, and not a tuple
            
                        (position of the: )
            index1, first element to be swapped
            index2, second element to be swapped
            
            a, b = b, a
        """
        board[index1], board[index2] = board[index2], board[index1]
        
        
    def get_possible_moves_into_blank_space(self):
        """
        Finds neighbors of blank space (at most four neighbors)
        Return list of new states (new PuzzleState objects) where 
            new state is numeric tile moving from neighbor into blank space loc
        """    
        new_states = []
        blank_space_idx = self.get_blank_space_position()  # blank space index
        blank_space_row, blank_space_column = divmod(blank_space_idx, 3) 
                  # row and column of blank space
        """
        Neighbors of, with respect to blank space location could be:
            up: row -1 , down: row +1 , no change in (same) column: 0
            no change in (same) row: 0, left: column -1 , right: column +1
        """
        #                  r, c              r, c
        moves = {  "up": (-1, 0),  "down": (+1, 0), 
                 "left": (0, -1), "right": (0, +1)}

        for move_name, (dr, dc) in moves.items(): 
                                                # for all neighbors (or moves)
            new_row = blank_space_row + dr      # add dr, change in row
            new_col = blank_space_column + dc   # add dc, change in column
            
            """
            if both new row and column index are in 3×3 board, 
                then
                    create a copy of board, new board, so that
                    neighbor and blank space can be swapped in new board, and
                    a new PuzzleState object with new board can be created 
                    append new PuzzleState to list of possible new_states
            """
            if 0 <= new_row < 3 and 0 <= new_col < 3:      
                
                new_board = list(self.board)   # new_board, a list not a tuple
                
                # Numeric tile index, and after slide where blank space appears
                numeric_tile_idx = new_row * 3 + new_col                             
                
                self.slide_numeric_tile_into_blank_space(new_board, 
                                                         blank_space_idx, 
                                                         numeric_tile_idx)
                
                """    Create new PuzzleState
                                  PuzzleState(tuple(new_board), 
                                              self, 
                                              move_name,
                                              self.g_cost + 1)
                       and append to list"""
                new_states.append(PuzzleState(board=tuple(new_board), 
                                              parent=self, 
                                              move=move_name, 
                                              g_cost=self.g_cost + 1))
                
        return new_states    
    
def print_solution(current_state, explored_set):
    
    print("\n Solution found")    
    
    print("\n Number of states explored by A* =", len(explored_set))
    
    solution = []
    """
    Empty list to save (state, move, cost, and heuristic) for all 
    moves(states) in the sequence they are encountered            
    from goal state back to start state, bottom up traversal
    
    while current_state is not None, 
        that is traversal from child to root nood is not complete
        till initial_board parent = None is not reached
    """
    while current_state: 
        solution.append((current_state.board, 
                         current_state.move, 
                         current_state.g_cost, 
                         current_state.manhattan_distance()))
        current_state = current_state.parent 
        """
        reassign current_state to parent of current state
            from state(or move) at t + 1 to state(or move) at t
        moving back/up the solution tree one step
        """
    """
    solution (result) of traversal saved as list from goal to initial            
    list[::-1] , ::-1 , gives list in reverse order
    """ 
    solution = solution[::-1]    # reverse list , now from start to goal state
    
    print("\n Number of steps in solution:", len(solution))
    print("\n Moves with respect to blank space, 0 ")
    print("\n Start state, move = None ")
    
    for step_number, (board, move, cost, heuristic) in enumerate(solution):
                        
        print("-"*42, f"\n Step: {step_number} , Move: {move} , ", end="")
        print(f"g_cost: {cost} + h: {heuristic}\n", "-"*13)
        
        for i in range(0, 9, 3):
            print(" |", board[i], "|", board[i+1], "|", board[i+2], 
                  "|\n", "-"*13)
        
from math import factorial
    
def solve_8_puzzle(initial_board):
    
    print("\n Number of states in 8-Puzzle problem = 9! =", factorial(9))
    
    initial_state = PuzzleState(initial_board)     # Create PuzzleState object
    
    open_list = []                                        # for priority queue
    heapq.heappush(open_list, initial_state)
    """
        add initial_state to queue, heapq maintains open_list as priority queue
        heapq.heappush implements a min-heap data structure,
        Smallest element remains at the root, root is at open_list[0]
        Priority is f_cost, __lt__ overload is used to compare
    """
    
    explored_set = set() #Empty set, to save explored board states, visited set

    while open_list:                       # while priority queue is not empty
        
        current_state = heapq.heappop(open_list) 
        """ heapq.heappop, pop and return the smallest item from the heap
            samllest, best of f_cost, f_cost = g_cost + h_cost
            hence Best First , A*             
        """        
        
        # If goal state reached, print solution, and return
        if current_state.board == goal_board: 
            
            print_solution(current_state, explored_set)  # call print solution
            return                                       # break out from loop

        """
            If control comes here, then Goal state has not been reached
            add current_state.board to explored_set , visited node
            indicating this board state(setting) has been explored(visited)
        """
        explored_set.add(current_state.board)  

        """
        for all possible numeric neighbor tile slide into blank space
        that is
        for all possible new PuzzleState with respect to blank space
        """
        for neighbor in current_state.get_possible_moves_into_blank_space():
            """
            Only if new neighbor board(state) is not in explored_set (visited)
                Add new neighbor to priority queue open_list
            """
            if neighbor.board not in explored_set:

                heapq.heappush(open_list, neighbor)
                
    """ solve_8_puzzle def ends """
        

solve_8_puzzle(initial_board)


"""
Output:

 Number of states in 8-Puzzle problem = 9! = 362880

 Solution found

 Number of states explored by A* = 2419

 Number of steps in solution: 27

 Moves with respect to blank space, 0 

 Start state, move = None 
------------------------------------------ 
 Step: 0 , Move: None , g_cost: 0 + h: 18
 -------------
 | 7 | 2 | 4 |
 -------------
 | 5 | 0 | 6 |
 -------------
 | 8 | 3 | 1 |
 -------------
------------------------------------------ 
 Step: 1 , Move: left , g_cost: 1 + h: 17
 -------------
 | 7 | 2 | 4 |
 -------------
 | 0 | 5 | 6 |
 -------------
 | 8 | 3 | 1 |
 -------------
------------------------------------------ 
 Step: 2 , Move: up , g_cost: 2 + h: 16
 -------------
 | 0 | 2 | 4 |
 -------------
 | 7 | 5 | 6 |
 -------------
 | 8 | 3 | 1 |
 -------------
------------------------------------------ 
 Step: 3 , Move: right , g_cost: 3 + h: 17
 -------------
 | 2 | 0 | 4 |
 -------------
 | 7 | 5 | 6 |
 -------------
 | 8 | 3 | 1 |
 -------------
------------------------------------------ 
 Step: 4 , Move: down , g_cost: 4 + h: 18
 -------------
 | 2 | 5 | 4 |
 -------------
 | 7 | 0 | 6 |
 -------------
 | 8 | 3 | 1 |
 -------------
------------------------------------------ 
 Step: 5 , Move: down , g_cost: 5 + h: 17
 -------------
 | 2 | 5 | 4 |
 -------------
 | 7 | 3 | 6 |
 -------------
 | 8 | 0 | 1 |
 -------------
------------------------------------------ 
 Step: 6 , Move: left , g_cost: 6 + h: 16
 -------------
 | 2 | 5 | 4 |
 -------------
 | 7 | 3 | 6 |
 -------------
 | 0 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 7 , Move: up , g_cost: 7 + h: 15
 -------------
 | 2 | 5 | 4 |
 -------------
 | 0 | 3 | 6 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 8 , Move: right , g_cost: 8 + h: 14
 -------------
 | 2 | 5 | 4 |
 -------------
 | 3 | 0 | 6 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 9 , Move: right , g_cost: 9 + h: 13
 -------------
 | 2 | 5 | 4 |
 -------------
 | 3 | 6 | 0 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 10 , Move: up , g_cost: 10 + h: 12
 -------------
 | 2 | 5 | 0 |
 -------------
 | 3 | 6 | 4 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 11 , Move: left , g_cost: 11 + h: 11
 -------------
 | 2 | 0 | 5 |
 -------------
 | 3 | 6 | 4 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 12 , Move: left , g_cost: 12 + h: 10
 -------------
 | 0 | 2 | 5 |
 -------------
 | 3 | 6 | 4 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 13 , Move: down , g_cost: 13 + h: 11
 -------------
 | 3 | 2 | 5 |
 -------------
 | 0 | 6 | 4 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 14 , Move: right , g_cost: 14 + h: 10
 -------------
 | 3 | 2 | 5 |
 -------------
 | 6 | 0 | 4 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 15 , Move: right , g_cost: 15 + h: 9
 -------------
 | 3 | 2 | 5 |
 -------------
 | 6 | 4 | 0 |
 -------------
 | 7 | 8 | 1 |
 -------------
------------------------------------------ 
 Step: 16 , Move: down , g_cost: 16 + h: 8
 -------------
 | 3 | 2 | 5 |
 -------------
 | 6 | 4 | 1 |
 -------------
 | 7 | 8 | 0 |
 -------------
------------------------------------------ 
 Step: 17 , Move: left , g_cost: 17 + h: 7
 -------------
 | 3 | 2 | 5 |
 -------------
 | 6 | 4 | 1 |
 -------------
 | 7 | 0 | 8 |
 -------------
------------------------------------------ 
 Step: 18 , Move: up , g_cost: 18 + h: 8
 -------------
 | 3 | 2 | 5 |
 -------------
 | 6 | 0 | 1 |
 -------------
 | 7 | 4 | 8 |
 -------------
------------------------------------------ 
 Step: 19 , Move: right , g_cost: 19 + h: 7
 -------------
 | 3 | 2 | 5 |
 -------------
 | 6 | 1 | 0 |
 -------------
 | 7 | 4 | 8 |
 -------------
------------------------------------------ 
 Step: 20 , Move: up , g_cost: 20 + h: 6
 -------------
 | 3 | 2 | 0 |
 -------------
 | 6 | 1 | 5 |
 -------------
 | 7 | 4 | 8 |
 -------------
------------------------------------------ 
 Step: 21 , Move: left , g_cost: 21 + h: 5
 -------------
 | 3 | 0 | 2 |
 -------------
 | 6 | 1 | 5 |
 -------------
 | 7 | 4 | 8 |
 -------------
------------------------------------------ 
 Step: 22 , Move: down , g_cost: 22 + h: 4
 -------------
 | 3 | 1 | 2 |
 -------------
 | 6 | 0 | 5 |
 -------------
 | 7 | 4 | 8 |
 -------------
------------------------------------------ 
 Step: 23 , Move: down , g_cost: 23 + h: 3
 -------------
 | 3 | 1 | 2 |
 -------------
 | 6 | 4 | 5 |
 -------------
 | 7 | 0 | 8 |
 -------------
------------------------------------------ 
 Step: 24 , Move: left , g_cost: 24 + h: 2
 -------------
 | 3 | 1 | 2 |
 -------------
 | 6 | 4 | 5 |
 -------------
 | 0 | 7 | 8 |
 -------------
------------------------------------------ 
 Step: 25 , Move: up , g_cost: 25 + h: 1
 -------------
 | 3 | 1 | 2 |
 -------------
 | 0 | 4 | 5 |
 -------------
 | 6 | 7 | 8 |
 -------------
------------------------------------------ 
 Step: 26 , Move: up , g_cost: 26 + h: 0
 -------------
 | 0 | 1 | 2 |
 -------------
 | 3 | 4 | 5 |
 -------------
 | 6 | 7 | 8 |
 -------------
"""


