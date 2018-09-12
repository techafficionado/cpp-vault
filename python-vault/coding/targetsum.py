
def sumpossible(arr,k):
	return sumpossibleutil(arr,k,0,0)

# atleastone makes sure the sum is 0 with element included but not the initial sum 0
def sumpossibleutil(arr,k,index,atleastone):
	print("k:{} atleastone:{}".format(k,atleastone))
	if k == 0 and atleastone:
		return True

	if k == 0 and not atleastone and index == len(arr):
		return False

	if index == len(arr) and k != 0:
		return False

	return sumpossibleutil(arr,k,index+1,0) or sumpossibleutil(arr,k-arr[index],index+1,1)



arr = [2,4,8]
k=0
print("sum:{}".format(sumpossible(arr, k)))
