
#Leet 235- LCA of BST

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #if root is None:
        #    return None
        
        # if root is less than p and also q that means both those values are on the right side of the root, so iterate
        # on the right side
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        # if root is greater than p and also q that means both those values are on the left side of the root, so iterate
        # on the right side
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        return root
