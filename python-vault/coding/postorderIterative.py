#!/bin/python

import sys

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(data):
    def deserialize():
        val = next(vals,None)
        if val == None:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize()
        node.right = deserialize()
        return node
    vals = iter(data.split())

    return deserialize()

def printInorder(root):
    if root == None:
        return
    printInorder(root.left)
    print root.val, 
    printInorder(root.right)


# Complete the function below.

from collections import deque
def  postorderTraversal(root):
    st1 = deque([root])
    st2 = deque([root])
    curnode = root
    while curnode is not None and st1:
        curnode = st1.pop()
        if curnode is not root:
            st2.append(curnode)
        if curnode.left is not None:
            st1.append(curnode.left)
        if curnode.right is not None:
            st1.append(curnode.right)
    #lis = []
    while st2:
        #lis.append(st2.pop())
        node = st2.pop()
        #print(node.val, end=" ")
        if node is not None:
            print node.val,
    #return lis 

_size = int(raw_input());


_str = raw_input()
root = createTree(_str);
postorderTraversal(root);
