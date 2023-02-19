import sys
import heapq

INFINITY = float('inf')

# Function for calculating heuristic
# state : list of states of pitchers 
def heuristic(state:list,goal:int)->int:
    # return (goal - volume in infinite pitcher), if it doesn't exceed goal
    return goal - state[-1] if state[-1]<=goal else INFINITY 

# Main A* algorithm
def A_Star(caps:list,goal:int)->int:
    # Check if input values are valid
    if(goal<0 or min(caps)<=0):
        return -1

    # Add an infinite capacity pitcher
    caps = caps + [INFINITY]
    
    # Initialize the initial state
    init_state = [0]*len(caps)

    # Initializing the priority queue by adding the initial tuple (heuristic,step,state)
    pq = [(heuristic(init_state,goal), 0, init_state)]
    # Note : first step is 0

    # Keep track of visited states
    visited = set()

    # A* search
    while pq:
        # Extract the state with the minimum f value from the priority queue
        h_cur , step, cur_state =  heapq.heappop(pq)                
        if cur_state[-1] == goal:
            # We have reached the goal, return the number of steps
            return step
        
        elif cur_state[-1] > goal:
            # Current state has a greater volume than the goal, continue to next iteration
            continue

        # Add the current state to visited set
        visited.add(tuple(cur_state))

        # For 2 pitchers at a time, we will pour water from one to another
        # or fill one of them from an infinite source
        for i in range(len(caps)):
            for j in range(len(caps)):
                if i==j:
                    continue

                # Copy current state
                state_next = cur_state.copy()

                # Fill i if j is empty
                if(state_next[j]==0 and i!=len(caps)-1):
                    state_next[i] = caps[i]
                # Pour from j to i
                else:
                    if(j!=len(caps)-1):
                        if (state_next[i]+state_next[j] <= caps[i]):
                            state_next[i] = state_next[i]+state_next[j]
                            state_next[j]=0
                        else:
                            dif = caps[i] - state_next[i]
                            state_next[i] = caps[i]
                            state_next[j] = state_next[j]-dif
                    else:
                        state_next[i] = caps[i]

                if tuple(state_next) not in visited:
                    # Calculate the f value of the next state and add it to the priority queue
                    heapq.heappush(pq, (step+1+heuristic(state_next,goal),step+1, state_next))

    # The goal is not reachable from the initial state
    return -1

# Function to read inputs from a file
def get_inputs(filepath):
    with open(filepath,"r") as f:
        caps = list(map(int,f.readline().split(",")))
        goal = int(f.readline())
    return caps, goal

# Main function
if __name__ == '__main__':
    if len(sys.argv)==2:
        caps, goal = get_inputs(sys.argv[1])
        print("Capacities: {}".format(caps))
        print("Goal: {}".format(goal))
        print("Steps to achieve the goal: {}".format(A_Star(caps,goal)))
    else:
        print("Usage: <ShortestPath_WaterPitcher.py> <filepath>")
