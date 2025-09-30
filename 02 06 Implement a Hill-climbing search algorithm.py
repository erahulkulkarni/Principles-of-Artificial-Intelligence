"""
Implement a Hill-climbing search algorithm

    Maximization example considered, find (local) maxima
"""
"""
    Starts with an initial solution ( random x and corresponding f(x) ) and 
        iteratively searches for a better solution by evaluating neighboring 
        solutions ( neighbor of x and its f(x) ) and moving towards the better
"""
"""
    steepest-ascent version
    
Russell Stuart J, and Peter Norvig, Artificial Intelligence: A Modern Approach, 
Pearson Education

    Figure 4.2 The hill-climbing search algorithm, which is the most basic 
        local search technique
        At each step the current node is replaced by the best neighbor; 
            in this version, that means the neighbor with the highest VALUE
    
    function HILL-CLIMBING(problem) 
        returns a state that is a local maximum
        
        current ← MAKE-NODE(problem.INITIAL-STATE)
        
        loop 
            do
                neighbor ← a highest-valued successor of current
                if neighbor.VALUE ≤ current.VALUE then 
                    return current.STATE
                
                current ← neighbor
"""
"""
Hill Climbing Algorithm:
    Inputs:
        objective_function, whose (local) maxima is to be found
        
        num_iterations, maximum number of iterations to run the algorithm
        
        step_size, magnitude of change when generating a neighbor ( of x )
    
        
    initial, an arbitrary initial x
    evaluate objective_function at initial x, find f(initial x)
    
    loop num_iterations times
    do
                    
        Get new neighbor, x
        Neighbor evaluation, get value f(new neighbor x)
        
        if f(new neighbor x) offers improvement
            move to the new neighbor 

        
    Expected to end with best x and corresponding f(x)
    Best wil be one of maximaxs
"""

import random

# Set for testing and reproducibility, remove when program working as expected
random.seed(42) 

def objective_function(x):      # Example objective function to maximize
    return -x**2 + 5            # f(x) = y = -x*x + 5
"""     
    objective_function, -x*x + 5 , single peak(maxima) at (0, 5), value of 5
    Rough sketch        
                         y 
                         |
                         - (0, 5)
                       | | |   
                      | 4|  |
                     |  3|   |
                    |   2|    |*        ← * (arbitrary initial x = 2.788536)
                   |    1|     |
        _ _ _ _ _ | _ _ _._ _ _ | _ _ _ _ _ x
             -4 -3 -2 -1 | 1  2 3 4
                |      -1|        |
               |       -2|         |
                       -3|          
                         |
    
    Hill-climbing is supposed to find maxima(peak) (0, 5) , x = 0 and f(x) = 5
    
    plot of objective_function using matplotlib.pyplot plt at end 
"""

def generate_neighbor(current_x, step_size):
    # Generate a neighboring solution by making a small change
    return current_x + random.uniform(-step_size, step_size)

line = "---"*15
def hill_climbing(objective_function, num_iterations, step_size):
                                                              # Initialization
    current_x = random.uniform(-10, 10)                     # Random initial x
    current_f_of_x = objective_function(current_x)        # Value at initial x
    
    print(line, f"\n Initial, x = {current_x:.6f} , f(x) = {current_f_of_x:.6f}")
    
    for i in range(num_iterations):
        
        # get new neighbor, evaluate objective function at new neighbor 
        neighbor_x = generate_neighbor(current_x, step_size) 
        neighbor_f_of_x = objective_function(neighbor_x)

        # If the neighbor is better, move to it
        """
        if neighbor_f_of_x < current_f_of_x: #minimization, moves towards valley        
        
                (Any other approach, to find either maxima or minima?
                 Given the conditions of:
                     objective function can be transformed 
                     and definition of hill_climbing function cannot be changed)
        """        
        if neighbor_f_of_x > current_f_of_x: #maximization, moves towards peak
            
            print(line, f"\n Iteration {i} , better x and f(x) found")
            print(f" x = {neighbor_x:.6f} , f(x) = {neighbor_f_of_x:.6f}")
            
            current_x = neighbor_x
            current_f_of_x = neighbor_f_of_x        

    return current_x, current_f_of_x

print(line, "\n objective_function = -x**2 + 5")

iterations = 50
step = 0.2
best_x, best_f_of_x = hill_climbing(objective_function, iterations, step)

print(line, "\n objective_function = -x**2 + 5")
print("\n Expected solution, maxima, x = 0.0 , f(x) = 5.0")
print(f"\n Best solution found, x = {best_x:.6f} , f(x) = {best_f_of_x:.6f}")


"""
Output:

--------------------------------------------- 
 objective_function = -x**2 + 5
--------------------------------------------- 
 Initial, x = 2.788536 , f(x) = -2.775933
--------------------------------------------- 
 Iteration 0 , better x and f(x) found
 x = 2.598540 , f(x) = -1.752412
--------------------------------------------- 
 Iteration 1 , better x and f(x) found
 x = 2.508552 , f(x) = -1.292833
--------------------------------------------- 
 Iteration 2 , better x and f(x) found
 x = 2.397836 , f(x) = -0.749619
--------------------------------------------- 
 Iteration 6 , better x and f(x) found
 x = 2.232612 , f(x) = 0.015444
--------------------------------------------- 
 Iteration 7 , better x and f(x) found
 x = 2.201381 , f(x) = 0.153924
--------------------------------------------- 
 Iteration 8 , better x and f(x) found
 x = 2.013299 , f(x) = 0.946625
--------------------------------------------- 
 Iteration 9 , better x and f(x) found
 x = 1.900755 , f(x) = 1.387132
--------------------------------------------- 
 Iteration 11 , better x and f(x) found
 x = 1.711369 , f(x) = 2.071216
--------------------------------------------- 
 Iteration 12 , better x and f(x) found
 x = 1.590904 , f(x) = 2.469024
--------------------------------------------- 
 Iteration 15 , better x and f(x) found
 x = 1.479080 , f(x) = 2.812321
--------------------------------------------- 
 Iteration 18 , better x and f(x) found
 x = 1.281680 , f(x) = 3.357297
--------------------------------------------- 
 Iteration 21 , better x and f(x) found
 x = 1.217780 , f(x) = 3.517012
--------------------------------------------- 
 Iteration 22 , better x and f(x) found
 x = 1.079972 , f(x) = 3.833661
--------------------------------------------- 
 Iteration 24 , better x and f(x) found
 x = 1.014610 , f(x) = 3.970567
--------------------------------------------- 
 Iteration 25 , better x and f(x) found
 x = 0.851708 , f(x) = 4.274593
--------------------------------------------- 
 Iteration 26 , better x and f(x) found
 x = 0.690395 , f(x) = 4.523355
--------------------------------------------- 
 Iteration 33 , better x and f(x) found
 x = 0.641808 , f(x) = 4.588082
--------------------------------------------- 
 Iteration 40 , better x and f(x) found
 x = 0.460138 , f(x) = 4.788273
--------------------------------------------- 
 Iteration 41 , better x and f(x) found
 x = 0.351297 , f(x) = 4.876590
--------------------------------------------- 
 Iteration 42 , better x and f(x) found
 x = 0.267053 , f(x) = 4.928683
--------------------------------------------- 
 Iteration 43 , better x and f(x) found
 x = 0.098969 , f(x) = 4.990205
--------------------------------------------- 
 Iteration 44 , better x and f(x) found
 x = -0.007914 , f(x) = 4.999937
--------------------------------------------- 
 objective_function = -x**2 + 5

 Expected solution, maxima, x = 0.0 , f(x) = 5.0

 Best solution found, x = -0.007914 , f(x) = 4.999937
"""


import math

# Set for testing and reproducibility, remove when program working as expected
random.seed(42)

def another_objective_function(x): 
    # f(x) = 0.5*e^-((x-1)^2) + e^-((x-4)^2)
    return 0.5*math.exp(-(x-1)**2) + math.exp(-(x-4)**2)
"""    
    Another objective function, f(x) = 0.5*e^-((x-1)^2) + e^-((x-4)^2)    
    Has two peaks(maximas), local maxima,   at (1, 0.5), value of 0.5
                         and
                            global maxima,  at (4, 1)  , value of 1
                   
                   Rough sketch    
               y
               |
     1         |                    . (4, 1)
               |                   | |
     0.75      |                  |   |
               |     (1, .5)     |     |
     0.5       |    .           |       |
               | |     |      |           |
     0.25    | |         |  *|              |
         _ |   |          |_|                _
        _ _ _ _._ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ x
         -1    0    1    2    3    4    5    6  
         
                            ↑ (arbitrary initial x = 2.788536)
                            * 
                            
    

    Hill-climbing is supposed to find either:
        global maxima (4, 1)  , x = 4 and f(x) = 1
        or
        local maxima (1, 0.5) , x = 1 and f(x) = 0.5            
    
    plot of another_objective_function using matplotlib.pyplot plt at end 
"""

print(line, "\n Another example \n")
print("\n another_objective_function = 0.5*e^-((x-1)^2) + e^-((x-4)^2)")

iterations = 100
step = 2.25 
"""
    Depending on initial x and step size, algorithm will find one of
        global maxima
        or
        local maximas
"""
best_x, best_f_of_x = hill_climbing(another_objective_function, iterations, 
                                    step)

print(line, "\n another_objective_function = 0.5*e^-((x-1)^2) + e^-((x-4)^2)")
print("\n Expected solution, maxima, x = 4.0 , f(x) = 1.0")
print(f"\n Best solution found, x = {best_x:.6f} , f(x) = {best_f_of_x:.6f}")

"""
Output:

another_objective_function = 0.5*e^-((x-1)^2) + e^-((x-4)^2)
--------------------------------------------- 
 Initial, x = 2.788536 , f(x) = 0.250872
--------------------------------------------- 
 Iteration 0 , better x and f(x) found
 x = 0.651084 , f(x) = 0.442702
--------------------------------------------- 
 Iteration 10 , better x and f(x) found
 x = 0.675183 , f(x) = 0.449950
--------------------------------------------- 
 Iteration 14 , better x and f(x) found
 x = 0.877420 , f(x) = 0.492601
--------------------------------------------- 
 Iteration 31 , better x and f(x) found
 x = 1.040446 , f(x) = 0.499340
--------------------------------------------- 
 Iteration 32 , better x and f(x) found
 x = 3.169467 , f(x) = 0.506202
--------------------------------------------- 
 Iteration 34 , better x and f(x) found
 x = 3.403650 , f(x) = 0.702278
--------------------------------------------- 
 Iteration 36 , better x and f(x) found
 x = 3.936989 , f(x) = 0.996127
--------------------------------------------- 
 Iteration 86 , better x and f(x) found
 x = 3.979857 , f(x) = 0.999664
--------------------------------------------- 
 another_objective_function = 0.5*e^-((x-1)^2) + e^-((x-4)^2)

 Expected solution, maxima, x = 4.0 , f(x) = 1.0

 Best solution found, x = 3.979857 , f(x) = 0.999664
"""


print(line, "\n Minimization , finding valley")
print("\n Yet another example, objective_function = x*x - 5 \n")

# Set for testing and reproducibility, remove when program working as expected
random.seed(42) 

def yet_another_objective_function(x):
    return x**2 - 5                     # f(x) = y = x*x - 5
"""
    yet_another_objective_function, x*x - 5 , single vally(minima) at (0, -5), 
    value of -5 , Rough sketch        
                         y 
                         |
                 |      3|       |  
                  |     2|      |
        _ _ _ _ _ _|_ _ 1._ _ _|_ _ _ _ _ _ x
             -4 -3  | -1 | 1  | 3 4
                    |  -1|    |   
                     | -2|   |
                     | -3|   |       
                      |-4|  |
                         - (0, -5)           
                         |          
                             
    Hill-climbing is supposed to find minima(valley) (0, -5), x 0 and f(x) -5
    
    plot of yet_another_objective_function using matplotlib.pyplot plt at end 
"""

# transform yet_another_objective_function as negative of objective_function
def negative_of_yet_another_objective_function(x):
    return -yet_another_objective_function(x)

iterations = 50
step = 0.2
# To find minima, pass negative of objective_function 
best_x, best_f_of_x = hill_climbing(negative_of_yet_another_objective_function, 
                                    iterations, step)

# Important, find inverse, since negative of objective_function was used
best_f_of_x = -best_f_of_x

# And then find: best_f_of_x is for which value of x
import sympy as sp
x = sp.symbols('x')                                     # Define the variable
function = x**2 - 5                          # yet_another_objective_function
equation = sp.Eq(function, best_f_of_x)   # Set the function equal to a value
best_x = sp.solve(equation, x)                           # Solve the equation

# Careful of order, first negate best_f_of_x, then find best_x

best_x = [round(x, 6) for x in best_x]

print(line, "\n objective_function = x**2 - 5 , has minima (0, -5)")
print("\n Use hill_climbing to find maxima of negative of objective_function")
print("\n Then inverse(negative) of best_f_of_x")
print("\n And find best_f_of_x is for which value of x")
print("\n Expected solution, minima, x = 0.0 , f(x) = -5.0")
print(f"\n Best solution found, x = {best_x} , f(x) = {best_f_of_x:.6f}")



# Common code for plotting objective function
import numpy as np
import matplotlib.pyplot as plt

def plot_objective_function(x, objective_function, title):
    y = objective_function(x)
    plt.plot(x, y)
    plt.title(title, fontsize=20)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Plot of, f(x) = -x**2 + 5
x = np.linspace(-3, 3, 50)
plot_objective_function(x, objective_function, r'$y = -x^2+5$')


# Plot of, f(x) = 0.5*e^-((x-1)^2) + e^-((x-4)^2)    
# Redefining, another_objective_function, using np.exp , instead of math.exp
def another_objective_function(x): 
    # f(x) = 0.5*e^-((x-1)^2) + e^-((x-4)^2)
    return 0.5*np.exp(-(x-1)**2) + np.exp(-(x-4)**2)

x = np.linspace(-1, 6, 50)
plot_objective_function(x, another_objective_function, 
                        r'$y = 0.5*e^{-(x-1)^{2}} + e^{-(x-4)^{2}}$')


#Plot of, f(x) = x**2 - 5
x = np.linspace(-3, 3, 50)
plot_objective_function(x, yet_another_objective_function, r'$y = x^2-5$')

