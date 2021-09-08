class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxi=-(10**9)
        mini = 10**9
        for i in A:
            if maxi < i:
                maxi=i
            if mini > i:
                mini = i
        return maxi+mini