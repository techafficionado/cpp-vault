#!/bin/python

import os
import sys


# Complete the function below.

from collections import deque

class minstack(object):
    def __init__(self):
        # declare actual stack 
        # declare stack that maintains a minimum

		# Minstack contains corresponding min upto that point in actual stack
		# If element of Actual stack is popped, pop on min stack side too, the peek of min stack would
		# be the new current min
        '''
        Eg 
             Actual   Min
			 stack    Stack
                1     1
                7     2
                5     2
				2     2
                10    10
				

        '''
        self.actualst = deque()
        self.minst = deque()
        self.minval = float('inf')
    def push(self,val):
        self.actualst.append(val)
        if self.minst:
            self.minval = min(self.peek(self.minst),val) 
        else:
        #    minval = float('inf')
            self.minval = val
        self.minst.append(self.minval)
        #print("push minst:{}".format(self.minst))
        
    def pop(self):
        if self.actualst:
            popval = self.actualst.pop()
            self.minst.pop()
            if self.minst:
                self.minval = self.peek(self.minst)
        else:
            popval = -1
            if self.minst:
                self.minst.pop()
                self.minval = self.peek(self.minst)
            #else:
            #    self.minval = float('inf')
        #print("pop minst:{}".format(self.minst))
        return popval
        
    def peek(self,st):
        if st:
            return st[-1]
        else:
            return None
    def getmin(self):
        minval = self.peek(self.minst)
        if minval is not None:
            return minval
        else:
            return -1
            
def min_stack(operations):
    mins = minstack()
    out = []
    for i in range(len(operations)):
        #print("{}".format(operations[i]))
        
        if operations[i] == 0:
            out.append(mins.getmin())
        
        elif operations[i] == -1:
            #out.append(mins.pop())
            mins.pop()
        
        else:
            mins.push(operations[i])
    return out    


if __name__ == "__main__":
    f = sys.stdout

    operations_size = int(input())

    operations = []
    for _ in range(operations_size):
        operations_item = int(input())
        operations.append(operations_item)


    res = min_stack(operations)

    f.write('\n'.join(map(str, res)))

    f.write('\n')
    f.close()

