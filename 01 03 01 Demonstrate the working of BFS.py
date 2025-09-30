"""
Demonstrate the working of BFS
"""
"""
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education

    Figure 3.11, Breadth-first search on a graph

    function BREADTH-FIRST-SEARCH (problem) 
        returns a solution, or failure

        node ← a , node with STATE = problem.INITIAL-STATE
        PATH-COST = 0
        
        if problem.GOAL-TEST(node.STATE) 
            then return SOLUTION(node)
        
        frontier ← a FIFO queue with node as the only element
        explored ← an empty set
        
        loop do
            if EMPTY?(frontier) 
                then return failure
            
            node ← POP(frontier) , chooses the shallowest node in frontier
            
            add node.STATE to explored
            
            for each action in problem.ACTIONS(node.STATE) 
                do
                    child ← CHILD-NODE(problem, node, action)
                    
                    if child.STATE is not in explored or frontier 
                        then
                        
                        if problem.GOAL-TEST(child.STATE)
                            then 
                            return SOLUTION(child)
                        
                        frontier ← INSERT(child, frontier)
"""
"""
Levitin A, Introduction to the Design and Analysis of Algorithms, Pearson

    v, is the start vertex
    
    add v to the queue
    mark v as "visited"
    print(v)
    bfs(v)
    
    Breadth-first search traversal of a given graph
    bfs(v)
        For Input, Graph G = V, E    
        Output, vertices in the order they are first encountered by BFS    
    
        // visits iteratively all the unvisited vertices connected to vertex v
        // by a path(i.e. if edge exists) in the order they are encountered

        while the queue is not empty 
            do
                for each vertex w in V adjacent to the front vertex 
                    do
                        if w is unvisited
                        
                            add w to the queue
                            mark w as "visited"
                            print(w)
                            
                remove the front vertex from the queue

"""
"""
Perform Breadth-First Search (BFS) on a graph
    bfs(graph, start)
        graph, a dictionary representing the graph, where keys are nodes
                and values are lists of their adjacent nodes
        start, node to start the BFS from

        Return, list of nodes in the order they were visited by BFS
"""

from collections import deque

def bfs(graph, start):        # iterative  

    visited = []                          # List to keep track of visited nodes
    queue = deque([start])    # Queue for nodes to visit, initialize with start

    while queue:                  # Till queue is not empty
        node = queue.popleft()         # Dequeue a node
        if node not in visited:        # If node has not been visited
        
            visited.append(node)          #  Then add node to visited list
            
            for neighbor in graph[node]:  # For all neighbors of node
                if neighbor not in visited: # If neighbor has not been visited
                    queue.append(neighbor)    # Then enqueue unvisited neighbor

    return visited

"""
For network of:
                Sankeshwar
                  |      |
                  |     Hukkeri
                  |     /
                 Hattargi
                    |
                 Belagavi
                  |      |
             Khanapur    |
                 |       Kittur
               Alnavar     |
                     |     |
                      Dharwad
                      
"""
# Graph represented as dictionay of adjacent lists
graph = {'Sankeshwar': ['Hattargi', 'Hukkeri'],
         'Hukkeri': ['Hattargi', 'Sankeshwar'], 
         'Hattargi': ['Belagavi', 'Sankeshwar', 'Hukkeri'], 
         'Belagavi': ['Khanapur', 'Hattargi', 'Kittur'], 
         'Khanapur': ['Alnavar', 'Belagavi'], 
         'Kittur': ['Dharwad', 'Belagavi'], 
         'Alnavar': ['Dharwad', 'Khanapur'], 
         'Dharwad': ['Alnavar', 'Kittur']}

# Perform BFS starting from node 'Belagavi'
start = 'Belagavi'
bfs_result = bfs(graph, start)
print(f"BFS traversal starting from '{start}': \n{bfs_result}")


"""
Output: 
    
BFS traversal starting from 'Belagavi': 
['Belagavi', 'Khanapur', 'Hattargi', 'Kittur', 'Alnavar', 'Sankeshwar', 'Hukkeri', 'Dharwad']
"""

"""
Output: 

BFS traversal starting from 'Sankeshwar': 
['Sankeshwar', 'Hattargi', 'Hukkeri', 'Belagavi', 'Khanapur', 'Kittur', 'Alnavar', 'Dharwad']    
"""

"""
Output: 
    
BFS traversal starting from 'Dharwad': 
['Dharwad', 'Alnavar', 'Kittur', 'Khanapur', 'Belagavi', 'Hattargi', 'Sankeshwar', 'Hukkeri']
"""