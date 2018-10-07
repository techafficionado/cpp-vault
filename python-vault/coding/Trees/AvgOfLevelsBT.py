from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        li = []
        #self.levelorderutil(root,li)
        return self.lo(root,li)
        #print("li:{}".format(li))
        
    def lo(self,root,li):
        q = deque([root])
        q.append(None)
        li.append(root.val)
        sums = 0
        cnt = 0
        while q:
            curnode = q.popleft()
			# this is our explicity inserted 'None' for marking end of level
            if curnode is None:
                avg = float(sums)/cnt
                li.append(avg)
                cnt = 0
                sums = 0
                q.append(None)
            else:
				# include left in sums and cnt
                if curnode.left is not None:
                    q.append(curnode.left)
                    sums += curnode.left.val
                    cnt += 1
				# include right in sums and cnt
                if curnode.right is not None:
                    q.append(curnode.right)
                    sums += curnode.right.val
                    cnt += 1
			# if this is the last None then identify and break or else we will be in an infinite loop
            if len(q) == 1 and q[0] == None:
                break
            #print("q:{}".format(q))
        #print("final li:{}".format(li))
        #print("final q:{}".format(q))  
        return li
