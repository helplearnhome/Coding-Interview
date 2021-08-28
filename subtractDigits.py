def desc(n):
	n=list(str(n))
	n=sorted(n,reverse=True)
	n=list(map(int,n))
	print(n)
	return n

def func(n,worked):
		if n== 0:
			return len(worked)
		if n < 0:
			return 0
		ls=desc(n)
		sum=0
		for i in ls:
			 func(n-i,worked+[i])
print(func(int(input()),[]))

