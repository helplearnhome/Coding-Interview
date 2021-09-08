def func(A):
    if len(A) == 1 or len(A) == 0:
        return A
    ls=list(A)
    n=len(ls)
    for i in range(n-2,-1,-1): #here n-2 so length 1 should do..
        if sorted(ls[i:],reverse=True) == ls[i:]:
            pass
        else:
            return ''.join(ls[:i]+sorted(ls[i:]))


    if ''.join(sorted(list(A),reverse=True)) == A:
            return -1        
    

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
		    return func(A)

xy=Solution()
print(xy.solve("1152"))