#!/usr/bin/env python

import copy 

from queue import PriorityQueue
from sets import Set

class Search:
    def __init__(self, _init_state, _goal_state, _mode='uniformed'):
        self.curr_state = _init_state
        self.goal_state = _goal_state
        self.frontier = PriorityQueue()
        self.b_cost_history = 0
        self.frontier.put((0, _init_state))
        self.visited_states = []
        self.mode = _mode

    def execute(self, fullIO=True):
        if fullIO == True:
            print("\n************************************\n")
            print("       ~~~ Initial Stack ~~~         \n")
            self.print_curr_stack()
            print("\n************************************")
            print("****  Begin Flipping Pancakes!  ****")
            print("************************************\n")
        else:
            print("\n....Running Pancake Flipping....\n")

        flip_number = 0 

        while(1):
            # print("Frontier")
            # self.safeprint_frontier()
            if self.frontier.empty():
                return 'FAILED'
            next_state = self.frontier.get()[1]
            self.visited_states.append(next_state)
            latest_b_cost = self.get_backward_cost(next_state) - self.b_cost_history
            self.b_cost_history = self.b_cost_history + latest_b_cost
            self.curr_state = next_state
            
            if fullIO == True: 
                if flip_number != 0:
                    print("\n---Flip # " + str(flip_number) + ": ") 
                    self.print_curr_stack()

            if next_state == self.goal_state:
                return 'SUCCEEDED'

            self.successor_function()
            flip_number = flip_number + 1

    def successor_function(self):
        state = copy.deepcopy(self.curr_state)
        for i in range(len(state)-1): # n-1 possible flips
            new_stack = state[:i]
            flip_stack = state[i:]
            flip_stack.reverse()
            new_stack.extend(flip_stack)
            f_cost = self.get_forward_cost(new_stack)
            b_cost = self.get_backward_cost(new_stack)
            
            if self.mode == 'A*':
                total_cost = f_cost + b_cost
            elif self.mode == 'UCS':
                total_cost = b_cost
            else:
                total_cost = 1 #completely uniformed search
            
            self.frontier_check((total_cost, new_stack))

    def get_forward_cost(self, state, h_function='gap'):
        forward_cost = 0
        if h_function == 'euclidean':
            for i in range(len(state)):
                p_cost = abs(state[i] - self.goal_state[i])
                forward_cost = forward_cost + p_cost
            return forward_cost
        elif h_function == 'gap':
            for i in range(len(state)-1):
                p_cost =  1 if (abs(state[i] - state[i+1]) > 1) else 0
                forward_cost = forward_cost + p_cost
            return forward_cost

        else: #Unitary
            for i in range(len(state)):
                p_cost =  0 if (i == state[i]) else 1
                forward_cost = forward_cost + p_cost
            return forward_cost

    def get_backward_cost(self, state):
        backward_cost = len(state) + self.b_cost_history
        for i in range(len(state)):
            if state[i] != self.curr_state[i]:
                return backward_cost
            backward_cost = backward_cost - 1
        # return 1
        return backward_cost

    def frontier_check(self, child_state):
        queue_states = []
        inserted = False
        while not self.frontier.empty():
            next_item = self.frontier.get()
            if next_item[1] == child_state[1]:
                if next_item[0] > child_state[0]:
                    next_item = child_state
                inserted = True
            queue_states.append(next_item)
            
        if inserted == False:
            queue_states.append(child_state)

        # new frontier 
        for state in queue_states:
            if state[1] not in self.visited_states:
                self.frontier.put(state)        

    def safeprint_frontier(self):
        queue_states = []
        while not self.frontier.empty():
            next_item = self.frontier.get()
            queue_states.append(next_item)
            print(next_item)

        for state in queue_states:
            self.frontier.put(state)

    ###################### I/O ######################
    def print_curr_stack(self):
        s = ''
        stack = copy.deepcopy(self.curr_state)
        stack.reverse()
        for pancake in stack:
            d = '-'
            for dash in range(pancake):
                d = d + '-'
            d = d + '  '
            s = s + d +  str(pancake) + '\n'
        print(s)

