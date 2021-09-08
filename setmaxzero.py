def makezeros(a,i,j,n,m):
    if j+1<m:
        if a[i][j+1] != 'x':
            k=j+1
            while(k<m):
                if a[i][k] == 'x':
                    break
                a[i][k]=0
                k+=1
    if j-1 > -1:
        if a[i][j-1] != 'x':
            k=j-1
            while(k>-1):
                if a[i][k] == 'x':
                    break
                a[i][k]=0
                k-=1
    if i+1 < n:
        if a[i+1][j] != 'x':
            k=i+1
            while(k<n):
                if a[k][j] == 'x':
                    break
                a[k][j] = 0
                k+=1
    if i-1 > -1:
        if a[i-1][j] != 'x':
            k=i-1
            while(k>-1):
                if a[k][j] == 'x':
                    break
                a[k][j] = 0
                k-=1
    return a

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        n=len(A)
        m=len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    A[i][j] = 'x'

        for i in range(n):
            for j in range(m):
                if A[i][j] == 'x':
                    # print(i,j)
                    A=makezeros(A,i,j,n,m)

        for i in range(n):
            for j in range(m):
                if A[i][j] == 'x':
                    A[i][j]=0
        return A
        
xy=Solution()
print(xy.setZeroes(    [   
    [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]

))