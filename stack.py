#!/usr/bin/env python

class Stack:
    def __init__(self):
        self.pancakes = [0,1,2,3,4,5,6,7,8,9]

    # Heuristic 
    def get_forward_cost(self):
        return 1

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