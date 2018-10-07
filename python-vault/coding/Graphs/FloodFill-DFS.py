class Solution(object):
    def getneighbors(self,row,col,image,oldColor,rlen,clen):
        neig = [[-1,0],[0,1],[1,0],[0,-1]]
        resneigh = []
        for r,c in neig:
            nr,nc = row+r,c+col
            if nr>=0 and nr<rlen and nc>=0 and nc<clen and image[nr][nc]==oldColor:
                resneigh.append([nr,nc])
        #print("resneigh:{}".format(resneigh))
        return resneigh
        
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        # a = [[0 for x in range(columns)] for y in range(rows)]
        visited = [[0]*cols for i in range(rows)]
        
        #print("visited:{}".format(visited))
        oldColor = image[sr][sc]
        self.dfsutil(image,sr,sc,oldColor,newColor,visited)
        return image
        
        
    def dfsutil(self,image,sr,sc,oldColor,newColor,visited):
        #print("image before:{}".format(image))
        #print("sr:{} sc:{}".format(sr,sc))
        
        if image[sr][sc] == oldColor:
            image[sr][sc] = newColor
        visited[sr][sc] = 1
        
        neigh = self.getneighbors(sr,sc,image,oldColor,len(image),len(image[0]))
        #print("sr:{} sc:{}".format(sr,sc))
        for r,c in neigh:
            #print("loop visited:{}".format(visited))
            if visited[r][c] == 0:
                self.dfsutil(image,r,c,oldColor,newColor,visited)
                
            
        #print("image:{}".format(image))
        
        
    
