# Leet 98. Validate Binary Search Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        rmin = float('-inf')
        rmax = float('inf')
        
        isbst = self.isbstutil(root,rmin,rmax)
        #print("isbst:{}".format(isbst))
        return isbst
        
    def isbstutil(self, root, rmin, rmax):
        if root is None:
            return True
        
        if root.val <= rmin or root.val >= rmax:
            return False
        
        return self.isbstutil(root.left,rmin,root.val) and self.isbstutil(root.right,root.val,rmax)
