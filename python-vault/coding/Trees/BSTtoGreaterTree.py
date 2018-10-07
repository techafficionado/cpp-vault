from collections import deque

'''
		5
	  /   \
	 2    13

		to

		18
	  /    \
     20    13

Option 1: compute the whole sum of the tree with iterative in order traversal
	then do a second recursive inorder and keep removing running sum from total sum and assign it to node value

Option 2: ** Better approach 
		 Do a reverse in order and keep running sum and subtract from current ndoe value


'''
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        li = []
        if root is None:
            return li
        sum=self.allsum(root)
        self.gtree(root,sum,0)
        return root

	def gtree(self,root,sum,rsum):
        
        st = deque([])
        while root is not None or st:
            while root is not None:
                st.append(root)
                root = root.left
            root = st.pop()
            #print("root val:{}".format(root.val))
            oldrval = root.val
            root.val = sum - rsum
            #print("new root val:{}".format(root.val))
            rsum += oldrval            
            root = root.right

	def allsum(self,root):
			st = deque([])
			
			sum = 0
			curnode = root
			while curnode is not None or st:
				while curnode is not None:
					#print("Appending:{}".format(curnode.val))
					st.append(curnode)
					curnode = curnode.left
				#print("st:{}".format(st))
				curnode = st.pop()
				#print("curnode:{}".format(curnode.val))
				sum += curnode.val
				curnode = curnode.right
			return sum
			#print("sum:{}".format(sum))    



	######## APPROACH 2 - BETTER APPROACH ############

	def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        '''
        li = []
        if root is None:
            return li
        sum=self.allsum(root)
        self.gtree(root,sum,0)
        return root
        '''
        self.sums  = 0
        self.inorderrec(root)
        return root
    
    def inorderrec(self, root):
        #global sums
        if root is None:
            return None
        self.inorderrec(root.right)
        print("root val:{}".format(root.val))
        root.val += self.sums
        self.sums  = root.val
        self.inorderrec(root.left)
