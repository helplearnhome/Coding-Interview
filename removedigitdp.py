def func(a,c=0):

	while(a>0):
		x=max(list(map(int,list(str(a)))))
		a=a-x
		c+=1
	return c

print(func(int(input())))