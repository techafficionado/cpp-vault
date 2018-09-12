def brackets(n):
	out = []
	bracketsutil(n,"",0,0,0,out)

	print("out:{}".format(out))


def bracketsutil(n,sofar,index,openb,closedb,out):

	if index == n and openb == n//2 and openb == closedb:
		out.append(sofar)
		return

	if openb < n//2:
		bracketsutil(n,sofar+'(',index+1,openb+1,closedb,out)
	if closedb < openb:
		bracketsutil(n,sofar+')',index+1,openb,closedb+1,out)


brackets(4)
