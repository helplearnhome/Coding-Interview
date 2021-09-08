# def func(A,B):
#     while(A>0 and B>0):
#         if A>B:
#             A=A-B
#         else:
#             B=B-A
#         # print(A,B)
#     if A == 0:
#         return B
#     if B == 0:
#         return A



# class Solution:
# 	# @param A : integer
# 	# @param B : integer
# 	# @return an integer
# 	def gcd(self, A, B):
#             return func(A,B)
# x=Solution()
# print(x.gcd(45,10))



def func(A,B):
    # print(A,B)
    if A == 0:
        return B
    if B == 0:
        return A
    
    if A>=B:
        return func(A-B,B)
    if B>A:
        return func(A,B-A)



class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
            return func(A,B)

x=Solution()
print(x.gcd(45,10))


#for both remember >= equal to. The iterative I had unknowingly given else.