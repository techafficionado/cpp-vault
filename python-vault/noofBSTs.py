# Complete the function below.

def how_many_BSTs(n):
	print("n:{}".format(n))

	if n==0 or n==1:
		return 1

	result = 0
	for i in range(n):
		print("i:{} result:{}".format(i,result))
		result += how_many_BSTs(i)*how_many_BSTs(n-i-1)
		print("result:{}".format(result))
		print("\n")
	return result


def how_many_BSTs_memo(n):
	memo = {}
	return bstutilmemo(n,memo)

def bstutilmemo(n,memo):

	if n in memo:
		return memo[n]

	if n==0 or n==1:
		memo[n] = 1
		return memo[n]

	result = 0
	for i in range(n):
		result += bstutilmemo(i,memo) * bstutilmemo(n-i-1,memo)
		memo[n]= result
	return memo[n]
	



#print("{}".format(how_many_BSTs(4)))
print("{}".format(how_many_BSTs_memo(4)))
