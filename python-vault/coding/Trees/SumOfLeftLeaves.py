#404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #st = deque([root])
        if root is None:
            return 0
        self.totsum = 0
        self.inorder(root)
        #print("totsum:{}".format(self.totsum))
        return self.totsum
        
    def inorder(self,root):
        if root is None:
            return None
        if root.left is not None and root.left.left is None and root.left.right is None:
            self.totsum += root.left.val
        self.inorder(root.left)
        self.inorder(root.right)
        
