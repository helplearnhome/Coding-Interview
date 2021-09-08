n=str(input())
d={}
for i in n:
	if i not in d:
		d[i]=1
	else:
		d[i]+=1
def func(x):
    return x[1]
z=sorted(d.items(),key=func,reverse=True)
st=""
for k,v in z:
	st+=f"{k}{v}"
print(st)