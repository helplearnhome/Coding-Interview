class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        a=A
        n=len(a)
        se=0
        so=0
        dp=[0]*n
        dpr=[0]*n
        for i in range(len(a)):
            if i%2==1:
                so+=a[i]
                dp[i]=so
            else:
                se+=a[i]
                dp[i]=se
        see=0
        soo=0
        i=n-1
        while(i!=-1):
            if i%2==1:
                soo+=a[i]
                dpr[i]=soo
            else:
                see+=a[i]
                dpr[i]=see
            i-=1

        # print(a)
        c=0
        for i in range(n):
            se=0
            so=0
            # if i == 1:
                # print('i',dp[i-1] if i-1 > -1 else 0)
                # print('i',dpr[i+2] if i+2 <n else 0)
                # print(se)
            se=((dp[i-1] if i-1 > -1 else 0) + (dpr[i+2] if i+2 <n else 0))
            so=((dp[i-2] if i-2 > -1 else 0) + (dpr[i+1] if i+1 <n else 0))
            
            # print(i,se,so)
            if se == so:
                c+=1
        return c

x=Solution()
print(x.solve([5,5,2,5,8]))


# se = dp[i-1]...
# Without parenthesis won't work