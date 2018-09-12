def palindecomp(s):
	slen = len(s)
	out = []
	sofar = []
	palindecomputil(s,slen,0,sofar,out)
	print("out:{}".format(out))


def palindecomputil(s,slen,index,sofar,out):

	if index == slen:
		out.append("|".join(sofar))
		return

	for i in range(index,slen):
		if ispalin(s[index:i+1]):
			sofar.append(s[index:i+1])
			palindecomputil(s,slen,i+1,sofar,out)
			sofar.pop()

def ispalin(s):
	if len(s) < 2:
		return True
	return s[0]==s[-1] and ispalin(s[1:-1])





s = "abracadabra"
palindecomp(s)
