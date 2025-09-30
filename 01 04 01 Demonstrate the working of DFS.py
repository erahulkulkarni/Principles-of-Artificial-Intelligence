"""
Demonstrate the working of DFS
"""
"""
Levitin A, Introduction to the Design and Analysis of Algorithms, Pearson

    v, is the start vertex
    
    mark v as "visited" , print(v)
    dfs(v)
    
    Depth-first search traversal of a given graph   
    dfs(v)
        For Input, Graph G = V, E    
        Output, vertices in the order they are first encountered by DFS    
        
        // visits recursively all the unvisited vertices connected to vertex v
        // by a path(i.e. if edge exists) in the order they are encountered
                
        for each vertex w in V adjacent to v 
            do
                if w is unvisited
                
                    mark w as "visited" , print(w)
                    dfs(w)
"""
"""
Perform Depth-First Search (DFS) on a graph
    dfs(node)
        uses graph, a dictionary representing the graph, where keys are nodes
                and values are lists of their adjacent nodes
        node, node of graph to continue DFS on

Print nodes in the order they were visited by DFS
"""
"""
 list to keep track of visited nodes, visited, declared and initialized later
 graph, dictionay of adjacency lists, declared and initialized later
"""
def dfs(node):              # recursive 
    
    if node not in visited:         # If node is not visited
        
        visited.append(node)           # then add node to visited list
        
        for neighbor in graph[node]:   # and perform DFS on all neighbors
            
            if neighbor not in visited:
                
                dfs(neighbor)

"""
For network of: same example as used in "Demonstrate the working of BFS.py"

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
# Graph represented as dictionay of adjacency lists
graph = {'Sankeshwar': ['Hattargi', 'Hukkeri'],
         'Hukkeri': ['Hattargi', 'Sankeshwar'], 
         'Hattargi': ['Belagavi', 'Sankeshwar', 'Hukkeri'], 
         'Belagavi': ['Khanapur', 'Hattargi', 'Kittur'], 
         'Khanapur': ['Alnavar', 'Belagavi'], 
         'Kittur': ['Dharwad', 'Belagavi'], 
         'Alnavar': ['Dharwad', 'Khanapur'], 
         'Dharwad': ['Alnavar', 'Kittur']}

# Perform DFS starting from node 'Belagavi'
start = 'Belagavi'
visited = list()            # List to keep track of visited nodes
dfs(start)
print(f"DFS traversal starting from '{start}': \n{visited}")


"""
Output: 
    
DFS traversal starting from 'Belagavi': 
['Belagavi', 'Khanapur', 'Alnavar', 'Dharwad', 'Kittur', 'Hattargi', 'Sankeshwar', 'Hukkeri']
"""

"""
Output: 
    
DFS traversal starting from 'Sankeshwar': 
['Sankeshwar', 'Hattargi', 'Belagavi', 'Khanapur', 'Alnavar', 'Dharwad', 'Kittur', 'Hukkeri']
"""

"""
Output: 
    
DFS traversal starting from 'Dharwad': 
['Dharwad', 'Alnavar', 'Khanapur', 'Belagavi', 'Hattargi', 'Sankeshwar', 'Hukkeri', 'Kittur']
"""