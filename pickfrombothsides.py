# # Recursive
def func(A,B,i,j,sum):
    if B == 0:
        # print(sum)
        return sum
    return max(func(A,B-1,i+1,j,sum+A[i]),func(A,B-1,i,j-1,sum+A[j]))

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # print(B)
        return func(A,B,0,-1,0)

# x = Solution()
# print(x.solve([1,9,8,1,1,7],3))

#Wrong way
#Iterative
# def func(A,B,i,j,sum):
#     while(B>0 and i<=j):
#         if (A[i] > A[j]):
#             sum+=A[i]
#             i+=1
#         else:
#             sum+=A[j]
#             j-=1
#         B-=1

#     return sum

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         # print(B)
#         return func(A,B,0,len(A)-1,0)
# x = Solution()
# print(x.solve([1,9,8,1,1,7],3))



#iterative

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sum=0
        maxi=0
        for i in range(B):
            sum+=A[i]
        maxi=sum
        for j in range(1,B+1):
            sum-=A[B-j]
            sum+=A[-j]
            if maxi < sum:
                maxi=sum
        return maxi

x = Solution()
print(x.solve([0,0,0,1,1,7],3))



#pavana
# int Solution::solve(vector<int> &A, int B) {
#     vector<int> dp1(B,0),dp2(B,0);
#     int n=A.size();

#     dp1[0]=A[0];
#     for(int i=1;i<B;i++)
#         dp1[i]=dp1[i-1]+A[i];
    
#     dp2[0]=A[n-1];
#     for(int i=1;i<B;i++)
#         dp2[i]=dp2[i-1]+A[n-1-i];
    
#     int ans=max(dp1[B-1],dp2[B-1]);
#     for(int i=0;i<B-1;i++)
#         ans=max(ans,dp1[i]+dp2[B-2-i]);

#     return ans;
# }