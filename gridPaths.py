
def gridPaths(n,m,sum):
    global grid
    if n == len(grid) or m == len(grid[0]):
       return 0
    if n == len(grid)-1 and m == len(grid[0])-1:
       return 1
    sum = gridPaths(n,m+1,sum)+gridPaths(n+1,m,sum)
    return sum
grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
     [0,0,0,0]
]
# grid = [
# [0,0,0],
# [0,0,0],
# [0,0,0]
# ]
 
print(gridPaths(0,0,0))