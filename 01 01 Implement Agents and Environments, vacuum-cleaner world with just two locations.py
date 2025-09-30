"""
Implement Agents and Environments
"""
"""
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education

    Figure 2.1, Agents interact with environments through sensors and actuators
            _ _ _ _ _ _ _ _ _                 _ _ _ _
           | Agent           |               |       |
           |     Sensors <---|---------------|   E   |
           |        ↓        |   Percepts    |   n   |
           |       ---       |               |   v   |
           |      | ? |      |               |   i   |
           |       ---       |               |   r   |
           |        ↓        |   Actions     |   o   |
           |    Actuators----|-------------->|   n   |
           |_ _ _ _ _ _ _ _ _|               |_ _ _ _|
        
"""
"""
Implement Agents and Environments, vacuum-cleaner world with just two locations

Environment, Room
    Rooms, represented as two locations, Room A and Room B
    State, each room can be either "Dirty" or "Clean"

Agent, Vacuum Cleaner
    Actions: The agent can perform actions such as:
        Suck, Clean the current room
        Move Left, Move to the left room
        Move Right, Move to the right room
        
Decision-Making Process    
    Percept, agent senses its current location and the cleanliness of the room
    Rules, agent applies rules based on its percept:
        If the room is dirty, it will suck (clean)
        If the room is clean, it will move to the adjacent room    
"""



line = "---"*15

class Environment:
    def __init__(self):
        self.state = {'A': 'Dirty', 'B': 'Dirty'}
        
        print(line, "\n Environment, Room Initialized, as: ")
        for room, state in self.state.items():
            print(f" Room {room} , state {state}")

    def is_location_clean(self, location):
        return self.state[location] == 'Clean'

    def clean_location(self, location):        
        self.state[location] = 'Clean'

    def get_room_state(self, location):
        return self.state[location]
        
    def print_room_state(self, location):
        print(f" room {location} is {self.state[location]}")
                

class Agent:
    def __init__(self, environment):
        self.environment = environment
        self.location = 'A'  # Start in Room A
        
        print(line, "\n Agent, Vacuum Cleaner Initialized", 
              "\n Placed in room", self.location)

    def move(self, new_location):                
        self.location = new_location

    def clean(self):
        self.environment.clean_location(self.location)

    def run(self):
        for _ in range(5): # run for a few steps
            print(line, f"\n Agent at {self.location} ,", end="")            
            self.environment.print_room_state(self.location)
            
            if not self.environment.is_location_clean(self.location):
                print(" Agent cleans")
                self.clean()                
                
            else:
                print(" Agent moves from", self.location, end="")
                
                if self.location == 'A':
                    self.move('B')
                else:
                    self.move('A')
                    
                print(" to", self.location)
                                    

# Running the simulation
environment = Environment()
agent = Agent(environment)

print(line, "\n Vacuum cleaner starts")
agent.run()


"""
Output:

--------------------------------------------- 
 Environment, Room Initialized, as: 
 Room A , state Dirty
 Room B , state Dirty
--------------------------------------------- 
 Agent, Vacuum Cleaner Initialized 
 Placed in room A
--------------------------------------------- 
 Vacuum cleaner starts
--------------------------------------------- 
 Agent at A , room A is Dirty
 Agent cleans
--------------------------------------------- 
 Agent at A , room A is Clean
 Agent moves from A to B
--------------------------------------------- 
 Agent at B , room B is Dirty
 Agent cleans
--------------------------------------------- 
 Agent at B , room B is Clean
 Agent moves from B to A
--------------------------------------------- 
 Agent at A , room A is Clean
 Agent moves from A to B
"""
