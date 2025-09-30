"""
Demonstrate the working of BFS Solve the n-Puzzle problem using BFS
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
    4-Puzzle problem, consists of a 2×2 board with three numbered tiles and a 
        blank space
              ----   ----            ----   ----
             | 3 |  | 2 |           |   |  | 1 |
              ----   ----            ----   ----
             | 1 |  |   |           | 2 |  | 3 |
              ----   ----            ----   ----
              Start State             Goal State    
"""
"""
initial_board = (3, 2, 1, 0)                     # Start State
goal_board = (0, 1, 2, 3)                        # Goal State
"""

import math
board_size = len(initial_board)                                        # n x n
n = int(math.sqrt(board_size))                             # only n , of n x n

"""
    initial_board, is the start state, start vertex
    
    add initial_board to the queue    
    bfs(initial_board)
    
    Breadth-first search traversal till goal reached by BFS from start state
    bfs(initial_board)
        For Input, initial_board as start state, goal_board as final state
        Output, board states in solution , in the order they are encountered 
            by BFS from initial_board to goal_board
    
        // explore(visit) iteratively all the unexplored(unvisited) 
            board states(vertices) with respect to blank space on 
            current_board (connected to vertex v)         

        while the queue is not empty 
            do            
                if current_board equals goal_board, solution reached
                    print solution
                    return
                else

                    (remove the front vertex from the queue)
                    current_board = remove the front board state(vertex) from 
                                        the queue
                    
                    (mark w as "visited")
                    mark current_board as explored (visited)                    
                    
                    (for each vertex w in V adjacent to the front vertex )
                    for all possible neighbor_board (next board/puzzle state) 
                        with respect to blank space on current_board                    
                    
                        do 
                            (if w is unvisited)
                            if neighbor_board is not yet explored                            
                            
                                (add w to the queue)
                                add neighbor_board to the queue

"""
"""
Step 1:
    For current_board = initial_board , Start State:
          ----   ----   ----
         | 7 |  | 2 |  | 4 |
          ----   ----   ----
         | 5 |  |   |  | 6 |
          ----   ----   ----
         | 8 |  | 3 |  | 1 |
          ----   ----   ----
             Start State
             
    current_board is not goal_board 
    
    Find all possible neighbors, four possibilities:
 ----  ----  ----     ----  ----  ----     ----  ----  ----     ----  ----  ----
| 7 | |   | | 4 |    | 7 | | 2 | | 4 |    | 7 | | 2 | | 4 |    | 7 | | 2 | | 4 |
 ----  ----  ----     ----  ----  ----     ----  ----  ----     ----  ----  ----
| 5 | | 2 | | 6 |    |   | | 5 | | 6 |    | 5 | | 6 | |   |    | 5 | | 3 | | 6 |
 ----  ----  ----     ----  ----  ----     ----  ----  ----     ----  ----  ----
| 8 | | 3 | | 1 |    | 8 | | 3 | | 1 |    | 8 | | 3 | | 1 |    | 8 | |   | | 1 |
 ----  ----  ----     ----  ----  ----     ----  ----  ----     ----  ----  ----
    Neighbor 1           Neighbor 2           Neighbor 3           Neighbor 4
    
    iteratively perform BFS on Neighbors
"""
"""
    For simplicity, blank space represented as 0 on board
"""

class PuzzleState:
    
    def __init__(self, board, parent=None, move=None):
        self.board = board                # Tuple representing the n x n board
        self.parent = parent
        self.move = move
    """        
        __init__(self, board, parent=None, move=None)
        default values are assigned when values not passed in as arguments
        
        Examples:
            PuzzleState(initial_board)
            that is
            PuzzleState(self, board = initial_board)
                self, is the invoking object
                board = initial_board
                parent = None , initial_board has no earlier state
                move = None , no moves made to get to initial_board state
        
        For next state(or move) PuzzleState objects
        
            PuzzleState(tuple(new_board), self, move_name)
            that is
            PuzzleState(self", board = tuple(new_board), parent = self', 
                        move = move_name)
                
                self" and self', both objects of PuzzleState
                
                self" (child) is the next state (or move) of self' (parent)
                
                self", is the invoking object
                board = tuple(new_board)
                parent = self', self' set as parent of self"
                                                       self".parent = self'
                move = move_name , is one of "up", "down", "right", or "left"
    """

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
        blank_space_row, blank_space_column = divmod(blank_space_idx, n) 
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
            if both new row and column index are in n × n board, 
                then
                    create a copy of board, new board, so that
                    neighbor and blank space can be swapped in new board, and
                    a new PuzzleState object with new board can be created 
                    append new PuzzleState to list of possible new_states
            """
            if 0 <= new_row < n and 0 <= new_col < n:
                
                new_board = list(self.board)   # new_board, a list not a tuple
                
                # Numeric tile index, and after slide where blank space appears
                numeric_tile_idx = new_row * n + new_col
                
                self.slide_numeric_tile_into_blank_space(new_board, 
                                                         blank_space_idx, 
                                                         numeric_tile_idx)
                
                """    Create new PuzzleState
                                  PuzzleState(tuple(new_board), 
                                              self, 
                                              move_name)
                       and append to list"""
                new_states.append(PuzzleState(board=tuple(new_board), 
                                              parent=self, 
                                              move=move_name))
                
        return new_states        

def print_solution(current_state, explored_set):
    
    print("\n Solution found")    
    
    print("\n Number of states explored by BFS =", len(explored_set))
    
    solution = []
    """
    Empty list to save (state, move) for all moves(states) in the sequence 
        they are encountered from goal state back to start state, 
        bottom up traversal
    
    while current_state is not None, 
        that is traversal from child to root nood is not complete
        till initial_board parent = None is not reached
    """
    while current_state: 
        solution.append((current_state.board, current_state.move))
        current_state = current_state.parent 
        """
        reassign current_state to parent of current state
            from state(or move) at t + 1 to state(or move) at t
        moving back/up the solution tree one step
        """
    """
    Path(result) of traversal saved as list from goal to initial        
    list[::-1] , ::-1 , gives list in reverse order
    """ 
    solution = solution[::-1]        # reverse list , now from start to goal state

    print("\n Number of steps in solution:", len(solution))
    print("\n Moves with respect to blank space, 0 ")
    print("\n Start state, move = None ")
    
    for step_number, (board, move) in enumerate(solution):
                        
        print("-"*32, f"\n Step: {step_number} , Move: {move}\n", "-"*4*n)
        
        for i in range(0, board_size, n):
            for j in range(i, i+n):
                print("|", board[j], end=" ")
                
            print("|\n", "-"*4*n)
            

def bfs_solve_n_puzzle(initial_board):
    
    print(f"\n Number of states in {board_size - 1}-Puzzle problem =", 
          f"{board_size}! = ", math.factorial(board_size))
    
    initial_state = PuzzleState(initial_board)     # Create PuzzleState object
    
    open_list = []                                                 # for queue
    open_list.append(initial_state)    # enqueue initial_state , append in end
    
    explored_set = set() # Empty set, save explored board states(visited nodes)
    
    while open_list:                                # while queue is not empty
    
        current_state = open_list.pop(0)     # dequeue , remove from the front
    
        # If goal state reached, raise SolutionFound to come out of recursion
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
                Add new neighbor to queue open_list
            """
            if neighbor.board not in explored_set:

                open_list.append(neighbor)
                
    """ bfs_solve_n_puzzle def ends """


bfs_solve_n_puzzle(initial_board)


"""
Output:

 Number of states in 3-Puzzle problem = 4! =  24

 Solution found

 Number of states explored by BFS = 11

 Number of steps in solution: 7

 Moves with respect to blank space, 0 

 Start state, move = None 
-------------------------------- 
 Step: 0 , Move: None
 --------
| 3 | 2 |
 --------
| 1 | 0 |
 --------
-------------------------------- 
 Step: 1 , Move: up
 --------
| 3 | 0 |
 --------
| 1 | 2 |
 --------
-------------------------------- 
 Step: 2 , Move: left
 --------
| 0 | 3 |
 --------
| 1 | 2 |
 --------
-------------------------------- 
 Step: 3 , Move: down
 --------
| 1 | 3 |
 --------
| 0 | 2 |
 --------
-------------------------------- 
 Step: 4 , Move: right
 --------
| 1 | 3 |
 --------
| 2 | 0 |
 --------
-------------------------------- 
 Step: 5 , Move: up
 --------
| 1 | 0 |
 --------
| 2 | 3 |
 --------
-------------------------------- 
 Step: 6 , Move: left
 --------
| 0 | 1 |
 --------
| 2 | 3 |
 --------
"""

"""
Output:

 Number of states in 8-Puzzle problem = 9! =  362880

 Solution found

 Number of states explored by BFS = 171711

 Number of steps in solution: 27

 Moves with respect to blank space, 0 

 Start state, move = None 
-------------------------------- 
 Step: 0 , Move: None
 ------------
| 7 | 2 | 4 |
 ------------
| 5 | 0 | 6 |
 ------------
| 8 | 3 | 1 |
 ------------
-------------------------------- 
 Step: 1 , Move: left
 ------------
| 7 | 2 | 4 |
 ------------
| 0 | 5 | 6 |
 ------------
| 8 | 3 | 1 |
 ------------
-------------------------------- 
 Step: 2 , Move: up
 ------------
| 0 | 2 | 4 |
 ------------
| 7 | 5 | 6 |
 ------------
| 8 | 3 | 1 |
 ------------
-------------------------------- 
 Step: 3 , Move: right
 ------------
| 2 | 0 | 4 |
 ------------
| 7 | 5 | 6 |
 ------------
| 8 | 3 | 1 |
 ------------
-------------------------------- 
 Step: 4 , Move: down
 ------------
| 2 | 5 | 4 |
 ------------
| 7 | 0 | 6 |
 ------------
| 8 | 3 | 1 |
 ------------
-------------------------------- 
 Step: 5 , Move: down
 ------------
| 2 | 5 | 4 |
 ------------
| 7 | 3 | 6 |
 ------------
| 8 | 0 | 1 |
 ------------
-------------------------------- 
 Step: 6 , Move: left
 ------------
| 2 | 5 | 4 |
 ------------
| 7 | 3 | 6 |
 ------------
| 0 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 7 , Move: up
 ------------
| 2 | 5 | 4 |
 ------------
| 0 | 3 | 6 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 8 , Move: right
 ------------
| 2 | 5 | 4 |
 ------------
| 3 | 0 | 6 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 9 , Move: right
 ------------
| 2 | 5 | 4 |
 ------------
| 3 | 6 | 0 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 10 , Move: up
 ------------
| 2 | 5 | 0 |
 ------------
| 3 | 6 | 4 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 11 , Move: left
 ------------
| 2 | 0 | 5 |
 ------------
| 3 | 6 | 4 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 12 , Move: left
 ------------
| 0 | 2 | 5 |
 ------------
| 3 | 6 | 4 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 13 , Move: down
 ------------
| 3 | 2 | 5 |
 ------------
| 0 | 6 | 4 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 14 , Move: right
 ------------
| 3 | 2 | 5 |
 ------------
| 6 | 0 | 4 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 15 , Move: right
 ------------
| 3 | 2 | 5 |
 ------------
| 6 | 4 | 0 |
 ------------
| 7 | 8 | 1 |
 ------------
-------------------------------- 
 Step: 16 , Move: down
 ------------
| 3 | 2 | 5 |
 ------------
| 6 | 4 | 1 |
 ------------
| 7 | 8 | 0 |
 ------------
-------------------------------- 
 Step: 17 , Move: left
 ------------
| 3 | 2 | 5 |
 ------------
| 6 | 4 | 1 |
 ------------
| 7 | 0 | 8 |
 ------------
-------------------------------- 
 Step: 18 , Move: up
 ------------
| 3 | 2 | 5 |
 ------------
| 6 | 0 | 1 |
 ------------
| 7 | 4 | 8 |
 ------------
-------------------------------- 
 Step: 19 , Move: right
 ------------
| 3 | 2 | 5 |
 ------------
| 6 | 1 | 0 |
 ------------
| 7 | 4 | 8 |
 ------------
-------------------------------- 
 Step: 20 , Move: up
 ------------
| 3 | 2 | 0 |
 ------------
| 6 | 1 | 5 |
 ------------
| 7 | 4 | 8 |
 ------------
-------------------------------- 
 Step: 21 , Move: left
 ------------
| 3 | 0 | 2 |
 ------------
| 6 | 1 | 5 |
 ------------
| 7 | 4 | 8 |
 ------------
-------------------------------- 
 Step: 22 , Move: down
 ------------
| 3 | 1 | 2 |
 ------------
| 6 | 0 | 5 |
 ------------
| 7 | 4 | 8 |
 ------------
-------------------------------- 
 Step: 23 , Move: down
 ------------
| 3 | 1 | 2 |
 ------------
| 6 | 4 | 5 |
 ------------
| 7 | 0 | 8 |
 ------------
-------------------------------- 
 Step: 24 , Move: left
 ------------
| 3 | 1 | 2 |
 ------------
| 6 | 4 | 5 |
 ------------
| 0 | 7 | 8 |
 ------------
-------------------------------- 
 Step: 25 , Move: up
 ------------
| 3 | 1 | 2 |
 ------------
| 0 | 4 | 5 |
 ------------
| 6 | 7 | 8 |
 ------------
-------------------------------- 
 Step: 26 , Move: up
 ------------
| 0 | 1 | 2 |
 ------------
| 3 | 4 | 5 |
 ------------
| 6 | 7 | 8 |
 ------------
"""