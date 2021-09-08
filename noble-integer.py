
# class Solution:
# 	# @param A : list of integers
# 	# @return an integer

# 	def solve(self, A):
#             d={}

#             for i in range(len(A)):
#                 if A[i] not in d:
#                     d[A[i]]=1
#                 else:    
#                     d[A[i]]+=1
#             ds=dict(d)
#             for i in range(len(A)):
#                 d=dict(ds)
#                 c=0
#                 for k,v in d.items():
#                     if A[i] < k:
#                         c+=v
#                         if i == 1:
#                             print(d,c,v)
#                 if c == A[i]:
#                     return 1
#             return -1
# x=Solution()
# print(x.solve([3, 2, 1, 3]))
# print(x.solve([1, 1, 3]))
# print(x.solve([6,7,5]))






#by sorting
class Solution:
	# @param A : list of integers
	# @return an integer

	def solve(self, A):
            A=sorted(A)

            if len(A) == 0:
                return -1
            if len(A) == 1 and A[i] == 0:
                return 1
            if len(A) == 1:
                return -1
            
            for i in range(len(A)):
                if i == len(A)-1:
                    if A[i] == 0:
                        return 1
                if i !=0:
                    if A[i-1] != A[i]:
                        if A[i-1] == len(A[i:]):
                            return 1
                else:
                    if A[i] != A[i+1]:
                        if A[i] == len(A[i+1:]):
                            return 1
                        else:
                            pass
            return -1
x=Solution()
# print(x.solve([3, 2, 1, 3]))
# print(x.solve([1, 1, 3]))
# print(x.solve([6,7,5]))
print(x.solve([ -4, -2, 0, -1, -6 ]))

#keep in mind about all edge cases like even null or single and ends and not exist.
#i-1 did not work for last case remember




#Seeing soln

class Solution:
	# @param A : list of integers
	# @return an integer

	def solve(self, A):
            A=sorted(A)
            n=len(A)
            # if len(A) == 1 and A[0] == 0:
            #     return 1
            if A[n-1] == 0:
                return 1
            for i in range(0,n-1):
                if A[i] !=A[i+1]:
                    if A[i] == n-i-1:
                        return 1
            return -1