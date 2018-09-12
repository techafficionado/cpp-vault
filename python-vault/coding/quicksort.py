def quicksort(arr):
	qsutil(arr,0,len(arr)-1)


def qsutil(arr,start,end):

	print("start:{} end:{}".format(start,end))

	if start>=end:
		return
	
	# choose pivot
	pividx = start + (end-start)/2
	
	# partition (rearrange as per pivot and return the idx for partitions)
	part = partition(arr, start, end)#, pividx)

	print("part:{}".format(part))

	qsutil(arr,start, part-1)
	qsutil(arr, part+1, end)

def partition(arr,start,end):#,pividx):
	# swap pivot to the end	
	#arr[end],arr[pividx] = arr[pividx],arr[end]

	print("initial array:{}".format(arr))
	pividx = end

	print("pivot:{}".format(arr[pividx]))
	partidx = start # first index with values greater than pivot


	'''
	# this is Lamuto's Algorithm	
	i=start
	while i < end: # start to end-1
		print("in while i:{} arr[i]:{} arr[pividx]:{}".format(i,arr[i],arr[pividx]))
		if arr[i] <= arr[pividx]:
			print("in if")
			arr[i],arr[partidx] = arr[partidx],arr[i]
			print("incrementing partidx, current val:{}".format(partidx))
			partidx += 1
			print("end i:{} partidx:{} arr[i]:{} arr[partidx]:{}".format(i,partidx,arr[i],arr[partidx]))
		i += 1
	print("partidx:{} pividx:{}".format(partidx,pividx))
	arr[partidx],arr[pividx] = arr[pividx],arr[partidx]

	return partidx			
	'''

	# this is Hoare's Algorithm
	lptr = start
	rptr = end-1
	print("lptr:{} rptr:{}".format(lptr,rptr))
	while True:
		while arr[lptr] < arr[pividx]:
			lptr += 1
		print("after while lptr:{}".format(lptr))
		while arr[rptr] > arr[pividx]:
			rptr -= 1
		print("after while rptr:{}".format(rptr))
		
		if lptr >= rptr:
			break
	
		arr[lptr],arr[rptr] = arr[rptr],arr[lptr]
	
	arr[lptr],arr[pividx] = arr[pividx],arr[lptr]

	return lptr

	
	

arr = [6,3,4,56,22,1,5,9,23,2,0]
print("Original arr:{}".format(arr))
quicksort(arr)
print("arr:{}".format(arr))
