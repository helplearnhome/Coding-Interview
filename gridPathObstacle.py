
def gridPaths(n,m):
   global grid
   if n == len(grid) or m == len(grid[0]):
       return 0
   if grid[n][m] == '*':
       return 0
   if n == len(grid)-1 and m == len(grid[0])-1:
       return 1
   return ((gridPaths(n,m+1)+gridPaths(n+1,m))%((10**9)+7))

# grid = [
#     ['.','.','.'],
#     ['.','.','.'],
#     ['.','.','*'],
# ]
# grid = [
#     ['*','.'],
#     ['.','.'],

# ]
# n=int(input())
# grid=[]
# for _ in range(n):
#     grid.append(list(map(str,input().split())))

n=int(input())
grid=[]
for _ in range(n):
    grid.append(list(input()))
print(gridPaths(0,0))