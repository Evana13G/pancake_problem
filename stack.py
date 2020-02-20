#!/usr/bin/env python
# import math

class Stack:
    def __init__(self, _pancakes=[0,1,2,3,4,5,6,7,8,9]):
        self.pancakes = _pancakes

    # Heuristic Fuction
    def get_forward_cost(self, mode='euclidean'):
        total_cost = 0
        if mode == 'euclidean':
            for i in range(len(self.pancakes)):
                p_cost = abs(i - self.pancakes[i])
                total_cost = total_cost + p_cost
        elif mode == 'unitary': 
            for i in range(len(self.pancakes)):
                p_cost = 0 if (i == self.pancakes[i]) else 1
                total_cost = total_cost + p_cost
        else:
            print("Please specify a distance metric")

        return total_cost

    def get_backward_cost(self):
        return 1

    ###################### I/O ######################
    def print_stack(self):
        s = ''
        for pancake in self.pancakes:
            d = ''
            for dash in range(pancake):
                d = d + '-'
            d = d + '  '
            s = s + d +  str(pancake) + '\n'
        print(s)

    def __str__(self):
        return str(self.pancakes)