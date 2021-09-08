class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        n=len(A)
        dp=[0]*n
        dpr=[10**9]*n
        dp[0]=A[0]
        dpr[n-1]=A[n-1]
        for i in range(1,n):
            dp[i]=max(dp[i-1],A[i])
        
        for i in range(n-2,-1,-1):
            dpr[i] = min(dpr[i+1],A[i])
        # print(A)
        # print(dp)
        # print(dpr)
        for i in range(1,n-1):
            if dp[i] == dpr[i]:
                if not (A[i] == dpr[i+1] or A[i] == dp[i-1]):    
                    return 1
        return 0

x=Solution()
print(x.perfectPeak([ 1, 2, 3, 4, 5, 4, 3, 2, 3, 10 ]))


        
