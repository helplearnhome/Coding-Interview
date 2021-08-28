def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)
def gridPaths(n):
   return fact((n-1)*2)/(fact(n-1)*fact(n-1))


# n=int(input())
# grid=[]
# for _ in range(n):
#     grid.append(list(input()))
n=3
grid=[
    ['.','.','*'],
    ['.','*','.'],
    ['.','.','*']
]
set1=set()
count=0

for i in range(n):
    for j in range(n):
        if grid[i][j] == "*":
            set1.add((i,j))
print(set1)
print(len(set1))    
print(set1)           
print(int(gridPaths(n)))