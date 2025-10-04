"""
Develop a Knowledge based agent capable of making informed decisions within a 
specific environment
"""
"""
Wumpus world
"""
"""
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education

   Knowledge-based agents can 
    accept new tasks in the form of explicitly described goals
    achieve competence quickly by being told/learning new knowledge about env
    adapt to changes in the environment by updating the relevant knowledge
    
    A knowledge base is a set of sentences
    TELL, add new sentences to the knowledge base 
    ASK, query what is known

            Figure 7.1  A generic knowledge-based agent
    Given a percept, the agent adds the percept to its knowledge base
    Asks the knowledge base for the best action, and 
    Tells the knowledge base that it has in fact taken that action
    
        function KB-AGENT(percept) takes percept as input and returns action
        
            persistent: KB , a knowledge base
            t , a counter, initially 0, indicating time
        
            TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
            action ← ASK(KB, MAKE-ACTION-QUERY(t))
            TELL (KB, MAKE-ACTION-SENTENCE(action, t ))
            t ← t + 1
            return action
"""
"""        
    loop    
        1. MAKE-PERCEPT-SENTENCE, TELL s the knowledge base what it perceives                
        2. MAKE-ACTION-QUERY, ASK s the knowledge base what action it should 
            perform                
        3. MAKE-ACTION-SENTENCE, TELL s the knowledge base which action chosen, 
            agent executes action
"""
"""
Environment, the wumpus world
    cave consisting of rooms connected by passageways
    wumpus, eats anyone who enters its room
    some rooms contain bottomless pits, trap anyone (except for the wumpus)
    possibility of finding a heap of gold
    
    Figure 7.2 , A typical wumpus world
             -----------------              
         4   | s |   | b | p |              a, agent
             -----------------              b, breeze
         3   | w |bsg| p | b |              g, gold (glitter)
             -----------------              p, pit
         2   | s |   | b |   |              s, stench       
             -----------------              w, wumpus
         1   | a | b | p | b |
             -----------------
               1   2   3   4

Environment
    4 × 4 grid of rooms
    agent always starts in the square labeled [1,1]
    gold and the wumpus in squares other than the start square
    each square other than the start can be a pit

Agent,
    can move
    dies, if it enters a square containing a pit or a live wumpus
               
Agent, perceive(sensors)
    In the square 
        containing the wumpus and in the directly (not diagonally) adjacent 
            squares, the agent will perceive stench
        directly adjacent to a pit, the agent will perceive breeze
        where the gold is, the agent will perceive glitter
"""
"""
Adjacent room(square) have stench or breeze if wumpus or pit are present
                wumpus stench              pit breeze
                     ----                      ----
                    | s |                     | b |
                 ------------              ------------
                | s | w | s |             | b | p | b |
                 ------------              ------------
                    | s |                     | b |
                     ----                      ----    

Agent, can 
    perceive only in the current/present square it is in
    anticipate presence of wumpus or pit relative to current square
        based on current/present square having stench or breeze
        
    in each case for which the agent draws a conclusion from the available 
        information, that conclusion is guaranteed to be correct if the 
        available information is correct
"""        
"""
(Indices, textbook example uses 1 based indexing)
                                                      -------------------------
Figure 7.2 ,                                       4  |     |     |     |     |
A typical wumpus world      Agent, initial state      |     |     |     |     |
    -----------------         -----------------       -------------------------
4   | s |   | b | p |     4   |   |   |   |   |    3  |     |     |     |     |
    -----------------         -----------------       |     |     |     |     |
3   | w |bsg| p | b |     3   |   |   |   |   |       -------------------------
    -----------------         -----------------    2  |     |     |     |     |
2   | s |   | b |   |     2   |   |   |   |   |       |     |     |     |     |
    -----------------         -----------------       -------------------------
1   | a | b | p | b |     1   | a |   |   |   |    1  | a   |     |     |     |
    -----------------         -----------------       | ok  |     |     |     |
      1   2   3   4             1   2   3   4         -------------------------
                                                         1     2      3     4  
    ok: safe square,  v: visited,  !: found,  ?: possible,  [1,1] is ok
"""
"""
 Steps:
 ---------------------------------------------------------------------------
 Explore unvisited ok locations, [1, 1]             -------------------------
                                                4   |     |     |     |     |
 [1,1] has no stench, no breeze,                    |     |     |     |     |
 so adjacent room do not have wumpus or pit         -------------------------
 Adjacent locations [1,2] and [2,1] are ok      3   |     |     |     |     |        
                                                    |     |     |     |     |
 Mark [1, 1] as visited                             -------------------------
                                                2   |     |     |     |     |
                                                    | ok  |     |     |     |
                                                    -------------------------
                                                1   | a   |     |     |     |
                                                    | ok  | ok  |     |     |
                                                    -------------------------
                                                       1     2      3     4   
 ---------------------------------------------------------------------------
 Explore unvisited ok locations, [1, 2] or [2, 1]   -------------------------
 [1, 2]                                         4   |     |     |     |     |
 [1, 2] has breeze                                  |     |     |     |     |
 There must be a pit in adjacent location           -------------------------
 adjacent location [1, 3] or [2, 2], p?         3   |     |     |     |     |            
                                                    |     |     |     |     |
 Mark [1, 2] as visited                             -------------------------
                                                2   |     |  p? |     |     |
                                                    | ok  |     |     |     |
                                                    -------------------------
                                                1   | v   | a,b |  p? |     |
                                                    | ok  | ok  |     |     |
                                                    -------------------------
                                                       1     2      3     4    
 ---------------------------------------------------------------------------
 Explore unvisited ok locations, [2, 1]             -------------------------
 Move to [1, 1], move to [2, 1]                 4   |     |     |     |     |
                                                    |     |     |     |     |
 [2, 1] has stench, but no breeze                   -------------------------
 [2, 1] has stench,                             3   | w!  |     |     |     |
 Wumpus can be in [3, 1], or [2, 2]                 |     |     |     |     |
 Inference: It is not in adjacent [2, 2], as        ------------------------- 
  there was no stench in [1, 2], there must     2   | a,s |     |     |     |
  be wumpus in adjacent location [3, 1]             |  ok | ok  |     |     |
 [3, 1], Wumpus found, w!                           -------------------------
                                                1   | v   |   b |  p! |     |
 [2, 1] has no breeze                               | ok  | ok  |     |     |
 Inference: No pit in adjacent [2, 2]               -------------------------
  [2, 2] is ok                                          1     2      3     4
  Breeze in [1, 2] must have been for pit 
  in [1, 3], pit found, p!, 
  
 Mark [2, 1] as visted
 ---------------------------------------------------------------------------
 Explore unvisited ok locations, [2, 2]
 
"""
"""
    Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern 
    Approach, Pearson Education, indices, in example uses 1 based indexing
    
    Implementaion, uses 0 based indexing, initialize environment, (row, column)
row
 ↑   -----------------------        -----------------         ----------------
 0   (0,0) (0,1) (0,2) (0,3)     0  |   |   |   | p |        |s  |   |b  |p  |    
     -----------------------        -----------------         ----------------    
 1   (1,0) (1,1) (1,2) (1,3)     1  | w | g | p |   |        |w  |gsb|p  |b  |
     -----------------------        -----------------         ----------------
 2   (2,0) (2,1) (2,2) (2,3)     2  |   |   |   |   |        |s  |   |b  |   |
     -----------------------        -----------------         ----------------
 3   (3,0) (3,1) (3,2) (3,3)     3  | a |   | p |   |        | a |b  |p  |b  |
     -----------------------        -----------------         ----------------
col ←   0     1     2     3           0   1   2   3           Agent at (3, 0)                                            
"""

agent_start_position = (3, 0)                              # Starting position
wumpus_position = (1, 0)                                     # Wumpus position
gold_position = (1, 1)                                      # Position of gold
pits_position = [(3, 2), (1, 2), (0, 3)]                   # Positions of pits 
size = 4                                           # n , in n x n grid , 4 x 4
"""
Adjacent room(square) indices , relative to . (current row, column) , can be:
same row (0, dc), different col, ← . left -1 (0, -1), . → right +1 (0, +1)
                                 ↑ 
same col (dr, 0), different row, .   up +1   (+1, 0), .   down -1  (-1, 0)
                                                      ↓
                                       above
                   left .     . right    .        .
                                                below
"""

adjacent_squares = [(0, -1), (0, +1), (+1, 0), (-1, 0)] # or adj room/location

def in_range_adj_idx(size, row, col):        # return adjacent indices in grid
    adj_idx = []
    for dr, dc in adjacent_squares:
        adj_row, adj_col = row + dr, col + dc
        if 0 <= adj_row < size and 0 <= adj_col < size: # if index is in range
            adj_idx.append((adj_row, adj_col))         # append (r, c) to list    
    return adj_idx        

class WumpusWorld:                                               # Environment
    """
    Environment WumpusWorld        
        initialized with, grid, list of lists, with
            agent_start_position, wumpus_position, pits_position, gold_position        
            stench and breeze, based on wumpus_position and pits_position            
            grid entry can be (environment valid) combination of 
                wumpus, pit, gold and percepts of stench, breeze, and glitter        
        Can return if (current row, column) has stench, breeze, and glitter        
        Can move agent in environment, and return move status
    """    
    def __init__(self, size, agent_start_position, wumpus_position, 
                 pits_position, gold_position):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]           
        self.agent_pos = agent_start_position                    # Place agent        
        x, y = wumpus_position
        self.grid[x][y] += 'w'                          # place, concat wumpus        
        x, y = gold_position
        self.grid[x][y] += 'g'                            # place, concat gold        
        for (x, y) in pits_position:
            self.grid[x][y] += 'p'                        # place, concat pits            
        for x in range(self.size):                     # for all rooms in cave
            for y in range(self.size):                
                if 'w' in self.grid[x][y]:                 # if wumpus in room
                    #update adj rooms, concat stench s if not already included
                    for adj_row, adj_col in in_range_adj_idx(self.size, x, y):                         
                        if 's' not in self.grid[adj_row][adj_col]:
                            self.grid[adj_row][adj_col] += 's'         # cat s                         
                if 'p' in self.grid[x][y]:                    # if pit in room
                    #update adj rooms, concat breeze b if not already included
                    for adj_row, adj_col in in_range_adj_idx(self.size, x, y):                        
                        if 'b' not in self.grid[adj_row][adj_col]:
                            self.grid[adj_row][adj_col] += 'b'         # cat b                        
        self.print_wumpus_world()
                        
    def print_wumpus_world(self):        
        line = "-" * self.size * self.size        
        print("\n\t WumpusWorld\n   ", line)        
        for x in range(self.size):
            print(f" {x} ", end="")                               # row number            
            for y in range(self.size):
                print(f"|{self.grid[x][y]:3}", end = "")          # grid entry
            print("|\n   ", line)        
        print("   ", end="")        
        for y in range(self.size):
            print(f"{y:4}", end="")                            # column number
                
    def get_percepts(self, row, col):        
        percepts = []        
        if 's' in self.grid[row][col]: percepts.append('stench')            
        if 'b' in self.grid[row][col]: percepts.append('breeze')            
        if 'g' in self.grid[row][col]: percepts.append('glitter')        
        return percepts

    def move_agent(self, new_pos):      # returns True if move is into ok room
                               # False if move is into room with wumpus or pit
        self.agent_pos = new_pos        
        x, y = new_pos        
        if self.grid[x][y] == 'p':                          # falling into pit
            print("\n Agent fell into a pit")
            return False        
        if self.grid[x][y] == 'w':                        # wumpus encountered
            print("\n Agent encountered wumpus")
            return False        
        return True                           # move into ok square successful

class WumpusAgent:                                                     # Agent
    """
    Agent
        Percives, stench, breeze, and glitter            
        Actions, move        
        Knowledge Base, kb, of known facts, dictionary of sets, 
            key (row, col): values can be {'safe', 'visited', 'breeze', 'p_pbl', 
                                           'stench', 'w_pbl', 'glitter'}
        Anticipate possible location of wumpus and pit based on percepts and kb
        Infer safety using kb, update kb
    """
    def __init__(self, world_size, agent_start_position):         # Initialize        
        self.world_size = world_size        
        self.visited = set()                        # locations visited, empty
        self.current_pos = agent_start_position # Initialize starting location
        self.kb = dict()                               # Knowledge Base, empty   
        self.kb[self.current_pos] = {'safe'}      # kb, start location is safe

    def add_to_kb(self, pos, fact):              # add facts to Knowledge Base    
        if pos not in self.kb:              # if key (row, col) does not exist
            self.kb[pos] = set()                       # start with a empy set            
        self.kb[pos].add(fact)                               # add fact to set
        
    def update_knowledge_base(self, row, col, percepts):        
        self.visited.add((row, col))           # add (row, col) to visited set        
        self.add_to_kb((row, col), 'visited') # add 'visited' to kb (row, col)        
                                    # move in square was successful, no w or p
        self.add_to_kb((row, col), 'safe')               # add new fact 'safe'
        self.kb[(row, col)].discard('w_pbl')      # remove contradicting facts
        self.kb[(row, col)].discard('p_pbl')         
        # anticipate info about neighbor, based on percepts in curr (row, col)
        for adj_row, adj_col in in_range_adj_idx(self.world_size, row, col):            
            # if no stench breeze in (row, col), then adj room is also safe
            if 'stench' not in percepts and 'breeze' not in percepts:                                
                self.add_to_kb((adj_row, adj_col), 'safe')
                self.kb[(adj_row, adj_col)].discard('w_pbl')
                self.kb[(adj_row, adj_col)].discard('p_pbl')            
                                       # Does not update already visited rooms    
            if (adj_row, adj_col) not in self.visited:    # if not yet visited                
                # if stench in curr (row, col), then adj room may have wumpus
                if 'stench' in percepts:
                    self.add_to_kb((adj_row, adj_col), 'w_pbl')   # w possible                
                # if breeze in curr (row, col), then adj room may have pit
                if 'breeze' in percepts:
                    self.add_to_kb((adj_row, adj_col), 'p_pbl')   # p possible            
        print("\n Updated kb: ", self.kb)
    
    def find_gold(self, world, queue, safe_search):     # breadth first search
        """        
            find_gold(self, world, queue, safe_search) using breadth first search
                while queue not empty
                    (x, y) = dequeue to get (square/room) move
                    update position in agent and world
                    Exit if move kills agent
                    Get agent percepts
                    Exit if gold found
                    Add safe unvisited adjacent squares to queue 
                    if queue empty, then add unsafe unvisited adj sqr to queue 
                    
                No safe path if queue empty
        """    
        print(f"\n\n Initial kb: {agent.kb}")
        print("\n Agent can move and perceive stench, breeze, glitter")
        print("\n Agent does(can) not:\n\t shoot wumpus, rotate, face direction,", 
              "\n\t bump into wall, grab gold , trace back to climb out,", 
              "\n\t use proposition logic inference, entails")        
        print("\n Agent starts")
        while queue:
            row, col = queue.pop()          # Ask, next room to visit, dequeue            
            agent.current_pos = (row, col)# Update agent position in agent and 
            move_into_ok_square = world.move_agent(agent.current_pos)#in world        
            if not move_into_ok_square: 
                break      # break, because moved into room with wumpus or pit                        
            print("", "-"*30, f"\n Agent moves to ({row}, {col}) ,", end="")            
            percepts = world.get_percepts(row, col)  # get percepts from world            
            print(f" and percieves: {percepts}")            
            #if control comes here, then move_into_ok_square is True/successful
            # Tell, update knowledge base, with percepts at current (row, col) 
            agent.update_knowledge_base(row, col, percepts)   # with no w or p
            if 'glitter' in percepts:                       # gold found, exit
                print("\n Agent found gold. Climbing out.") 
                break                                        
            # Safe search, explore next (add to queue) safe unvisited adj sqrs
            for adj_row, adj_col in in_range_adj_idx(agent.world_size, row, 
                                                     col):                
                # get kb entry of (adj_row, adj_col) if exists, else empty set
                kb_entry = agent.kb.get((adj_row, adj_col), set())                
                if ('safe' in  kb_entry and 'visited' not in kb_entry):                    
                    queue.append((adj_row, adj_col))      # Tell, add to queue            
            # safe search exhausted(explored) all safe squares, queue is empty
            # unsafe search, take risk, explore unvisited whether safe or not
            if not queue and not safe_search:                
                for adj_row, adj_col in in_range_adj_idx(agent.world_size, row, 
                                                         col):                    
                    kb_entry = agent.kb.get((adj_row, adj_col), set())                    
                    if ('visited' not in kb_entry):                        
                        queue.append((adj_row, adj_col))                # Tell                        
        if len(queue) == 0:
            print("\n Agent cannot find a safe path. Climbing out.")        
        """ def find_gold ends """        
    """ class WumpusAgent ends"""

print("", "-"*60, "\n Run of Agent that takes no risk")
world = WumpusWorld(size, agent_start_position, wumpus_position, 
                    pits_position, gold_position)
agent = WumpusAgent(world.size, world.agent_pos)
queue = list([agent.current_pos])

safe_search = True
agent.find_gold(world, queue, safe_search)

print("", "-"*60, "\n Run of Agent that takes risk")
world = WumpusWorld(size, agent_start_position, wumpus_position, 
                    pits_position, gold_position)
agent = WumpusAgent(world.size, world.agent_pos)
queue = list([agent.current_pos])

safe_search = False
agent.find_gold(world, queue, safe_search)

"""
Output:
 ------------------------------------------------------------ 
 Run of Agent that takes no risk

	 WumpusWorld
    ----------------
 0 |s  |   |b  |p  |
    ----------------
 1 |w  |gsb|p  |b  |
    ----------------
 2 |s  |   |b  |   |
    ----------------
 3 |   |b  |p  |b  |
    ----------------
      0   1   2   3

 Initial kb: {(3, 0): {'safe'}}

 Agent can move and perceive stench, breeze, glitter

 Agent does(can) not:
	 shoot wumpus, rotate, face direction, 
	 bump into wall, grab gold , trace back to climb out, 
	 use proposition logic inference, entails

 Agent starts
 ------------------------------ 
 Agent moves to (3, 0) , and percieves: []

 Updated kb:  {(3, 0): {'visited', 'safe'}, (3, 1): {'safe'}, (2, 0): {'safe'}}
 ------------------------------ 
 Agent moves to (2, 0) , and percieves: ['stench']

 Updated kb:  {(3, 0): {'visited', 'safe'}, (3, 1): {'safe'}, 
               (2, 0): {'visited', 'safe'}, (2, 1): {'w_pbl'}, (1, 0): {'w_pbl'}}
 ------------------------------ 
 Agent moves to (3, 1) , and percieves: ['breeze']

 Updated kb:  {(3, 0): {'visited', 'safe'}, (3, 1): {'visited', 'safe'}, 
               (2, 0): {'visited', 'safe'}, (2, 1): {'p_pbl', 'w_pbl'}, 
               (1, 0): {'w_pbl'}, (3, 2): {'p_pbl'}}

 Agent cannot find a safe path. Climbing out.
 ------------------------------------------------------------ 
 Run of Agent that takes risk

	 WumpusWorld
    ----------------
 0 |s  |   |b  |p  |
    ----------------
 1 |w  |gsb|p  |b  |
    ----------------
 2 |s  |   |b  |   |
    ----------------
 3 |   |b  |p  |b  |
    ----------------
      0   1   2   3

 Initial kb: {(3, 0): {'safe'}}

 Agent can move and perceive stench, breeze, glitter

 Agent does(can) not:
	 shoot wumpus, rotate, face direction, 
	 bump into wall, grab gold , trace back to climb out, 
	 use proposition logic inference, entails

 Agent starts
 ------------------------------ 
 Agent moves to (3, 0) , and percieves: []

 Updated kb:  {(3, 0): {'visited', 'safe'}, (3, 1): {'safe'}, (2, 0): {'safe'}}
 ------------------------------ 
 Agent moves to (2, 0) , and percieves: ['stench']

 Updated kb:  {(3, 0): {'visited', 'safe'}, (3, 1): {'safe'}, 
               (2, 0): {'visited', 'safe'}, (2, 1): {'w_pbl'}, (1, 0): {'w_pbl'}}
 ------------------------------ 
 Agent moves to (3, 1) , and percieves: ['breeze']

 Updated kb:  {(3, 0): {'visited', 'safe'}, (3, 1): {'visited', 'safe'}, 
               (2, 0): {'visited', 'safe'}, (2, 1): {'p_pbl', 'w_pbl'}, 
               (1, 0): {'w_pbl'}, (3, 2): {'p_pbl'}}
 ------------------------------ 
 Agent moves to (2, 1) , and percieves: []

 Updated kb:  {(3, 0): {'visited', 'safe'}, (3, 1): {'visited', 'safe'}, 
               (2, 0): {'visited', 'safe'}, (2, 1): {'visited', 'safe'}, 
               (1, 0): {'w_pbl'}, (3, 2): {'p_pbl'}, (2, 2): {'safe'}, 
               (1, 1): {'safe'}}
 ------------------------------ 
 Agent moves to (1, 1) , and percieves: ['stench', 'breeze', 'glitter']

 Updated kb:  {(3, 0): {'visited', 'safe'}, (3, 1): {'visited', 'safe'}, 
               (2, 0): {'visited', 'safe'}, (2, 1): {'visited', 'safe'}, 
               (1, 0): {'p_pbl', 'w_pbl'}, (3, 2): {'p_pbl'}, (2, 2): {'safe'}, 
               (1, 1): {'visited', 'safe'}, (1, 2): {'p_pbl', 'w_pbl'}, 
               (0, 1): {'p_pbl', 'w_pbl'}}

 Agent found gold. Climbing out.
"""
