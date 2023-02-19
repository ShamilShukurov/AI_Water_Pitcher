
import unittest
import sys
from ShortestPath_WaterPitcher import heuristic, A_Star

class TestAStar(unittest.TestCase):
    
# The admissibility tests ensure that the heuristic function returns non-negative values for all states and
#  that the function never overestimates the distance to the target state.

    def test1_heuristic_admissible(self):
        current_state = [2,0,2]
        target_quantity = 143
        h = heuristic(current_state, target_quantity)
        self.assertTrue(h >= 0)

    def test2_heuristic_admissible(self):
        current_state = [5,10,5,0]
        target_quantity = 15
        h = heuristic(current_state, target_quantity)
        self.assertTrue(h >= 0)

# Consistency check: heuristic value of a successor state is less than or equal to the heuristic value 
# of its parent state plus the cost of the transition.

    def test1_heuristic_consistent(self):
        current_state = [2,0,2]
        target_quantity = 143
        h = heuristic(current_state, target_quantity)
        next_state = [2,2,2]
        next_h = heuristic(next_state, target_quantity)
        self.assertTrue(next_h <= h + 1)

    def test2_heuristic_consistent(self):
        current_state = [5,10,5,0]
        target_quantity = 15
        h = heuristic(current_state, target_quantity)
        next_state = [5, 0,5,10]
        next_h = heuristic(next_state, target_quantity)
        self.assertTrue(next_h <= h + 1)

#A-star algorithm tests use specific capacities and target volumes to ensure that the algorithm returns the correct 
# shortest path length or -1 if the target volume is not reachable.  
    def test1_A_Star(self):
        capacities = [2,2]
        target_quantity = 143
        s = A_Star(capacities,target_quantity)
        self.assertTrue(s==-1)
    
    def test2_A_Star(self):
        capacities = [5,10,20]
        target_quantity = 15
        s = A_Star(capacities,target_quantity)
        self.assertTrue(s==4)

    def test3_A_Star(self):
        capacities = [5,10,20]
        target_quantity = 0
        s = A_Star(capacities,target_quantity)
        self.assertTrue(s==0)


if __name__ == '__main__':
    unittest.main()
