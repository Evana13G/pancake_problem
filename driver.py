#!/usr/bin/env python

import copy
import sys
from search import Search

######### START: CONFIGS
init_state = [2, 4, 5, 1, 3]     # SET INITIAL STACK ON PANCAKES
mode = 'A*'						       # SET MODE (either 'A*' or 'UCS', defaults to uniformed)	
######### END: CONFIGS


goal_state = copy.deepcopy(init_state)
goal_state.sort()
goal_state.reverse()

S = Search(init_state, goal_state, mode)

print("Outcome: " + str(S.execute()))


