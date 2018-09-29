#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'hasCycle' function below.
#
# The function accepts INTEGER N, INTEGER M and 2D_INTEGER_ARRAY edges as parameter.
# The function is expected to return a BOOLEAN.
#

def hasCycle(N, M, edges):
    # Write your code here
	visiting = []
	visited = set()
	hmap = buildAdjList(edges)

	iscycle = dfs(hmap)
	print("iscycle:{}".format(iscycle))
	return iscycle
    
def dfs(hmap):
	visited = set()
	for v in hmap:
		#if v not in visited:
			#visited.add(v)#append(v)
		visiting = set()
		#visiting.append(v)
		if (dfsutil(hmap, v, visited, visiting)): # implies there was a loop found
			return True
		print("back from dfs")
		print("back from continous dfs")
	return False

def dfsutil(hmap,v, visited,visiting):
	if v in visiting:
		print("found in visiting v:{}".format(v))
		return True
	if v in visited:
		return False

	visiting.add(v)
	print("visiting:{}".format(visiting))
	if v in hmap:
		for i in hmap[v]:
			print("i:{}".format(v))
			if(dfsutil(hmap,i,visited,visiting)):
				print("dfsutil is true")
				return True

	visiting.remove(v)
	visited.add(v)
	return False
	




'''    
def dfsutil(hmap,vertex, visited, visiting):
    
	res = False

	print("visiting:{}".format(visiting))
	print("visited:{}".format(visited))

	#if vertex in visiting:
	#	print("revisiting vertex:{} that is already in visiting set:{}".format(vertex,visiting))
	#	res = True
	#	return True

	#if vertex in visited:
	#	return False

	visiting.append(vertex)
	#visited.add(vertex)#append(vertex)

	if vertex in hmap:
		adjlist = hmap[vertex]
		for i in adjlist:
			#visited.append(i)
			if i in visited:
				continue
			if i in visiting:
				print("revisiting i:{} that is already in visiting set:{}".format(i,visiting))
				res = True
				return res
			#    break
			#visiting.append(i)
			#print("visiting:{}".format(visiting))
			if(dfsutil(hmap,i,visited,visiting)):
				res= True
				return res
				#break
			#visiting.remove(vertex)
		#if res is True:
		#	return True
		visiting.remove(vertex)
		visited.append(vertex)

	return res
'''
    
def buildAdjList(edges):
    hmap = {}
    for edge in edges:
        print("edge:{}".format(edge))
        vertex = edge[0]
        if vertex in hmap:
            print("vertex already in hmap:{}".format(vertex))
            continue
        print("vertex:{}".format(vertex))
        adjlist = []
        for l,r in edges:
            if l == vertex:
                adjlist.append(r)
        hmap[vertex] = adjlist
    print("hmap:{}".format(hmap))
    return hmap


if __name__ == "__main__":
    N = int(input().strip())
    M = int(input().strip())

    edges = []

    for _ in range(M):
        edges.append(list(map(int, input().rstrip().split())))

    fptr = sys.stdout

    result = hasCycle(N, M, edges)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
            
