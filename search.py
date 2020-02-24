#!/usr/bin/env python
from queue import PriorityQueue
import copy 

class Search:
    def __init__(self, _init_state, _goal_state=[0,1,2,3,4,5,6,7,8,9], _mode='A*'):
        self.curr_state = _init_state
        self.goal_state = _goal_state
        self.frontier = PriorityQueue()
        self.b_cost_history = 0
        self.frontier.put((0, _init_state))
        self.mode = _mode
        self.frontier_stack = []

    def execute(self):
        # self.print_curr_stack()

            print("trial")
            self.print_curr_stack()
            # self.safeprint_frontier()
            if self.frontier.empty():
                return 'FAILED'
            self.curr_state = self.frontier.get()[1]
            curr_cost, curr_leaf = self.successor_function()
            self.curr_state = curr_leaf #chose the smallest cost node
            #print( self.curr_state )
            while(1):
                print("trial")
                self.print_curr_stack()
                # self.safeprint_frontier()
                if self.frontier.empty():
                    return 'FAILED'
                self.curr_state = self.frontier.get()
                curr_cost, curr_leaf = self.successor_function()
                self.curr_state = curr_leaf  # chose the smallest cost node
                #print(self.curr_state)





            #self.successor_function()


    def successor_function(self):
        state = copy.deepcopy(self.curr_state)
        small_state = []
        count = 100
        for i in range(len(self.curr_state) - 1): # n-1 possible flips
            new_stack = self.curr_state[:i]
            flip_stack = self.curr_state[i:]
            flip_stack.reverse()
            new_stack.extend(flip_stack)
            f_cost = self.get_forward_cost(new_stack)
            b_cost = self.get_backward_cost(new_stack)
            #print(new_stack)
            total_cost = f_cost + b_cost
            if total_cost <= count:
                count = total_cost
                small_state = new_stack
            if new_stack == self.goal_state:
                self.curr_state = new_stack
                self.print_curr_stack()
                print( 'SUCCEEDED')
                exit()
            self.frontier.put(new_stack)
            self.frontier_check((total_cost, new_stack))
        #self.frontier.get()
        return count, small_state


    def get_forward_cost(self, state):
        forward_cost = 0
        for i in range(len(state)):
            p_cost = abs(i - state[i])
            forward_cost = forward_cost + p_cost
        return forward_cost

    def get_backward_cost(self, state):
        backward_cost = 0
        for i in range(len(state)):
            if i == state[i]:
                return backward_cost
            backward_cost = backward_cost + 1
        return backward_cost

    def frontier_check(self, child_state):
        queue_states = []
        # temp_frontier = copy.deepcopy(self.frontier)
        # while not temp_frontier.empty():
        while not self.frontier.empty():
            next_item = self.frontier.get()
            if next_item[1] == child_state[1]:
                if next_item[0] > child_state[0]:
                    next_item = child_state
            queue_states.append(next_item)

        # new frontier
        for state in queue_states:
            self.frontier.put(state)

    def safeprint_frontier(self):
        temp_frontier = copy.deepcopy(self.frontier)
        print("---Frontier: ")
        while not temp_frontier.empty():
            next_item = temp_frontier.get()
            print(next_item)

    ###################### I/O ######################
    def print_curr_stack(self):
        s = ''
        for pancake in self.curr_state:
            d = ''
            for dash in range(pancake):
                d = d + '-'
            d = d + '  '
            s = s + d +  str(pancake) + '\n'
        print(s)

    # def __str__(self):
    #     return str(self.pancakes)






