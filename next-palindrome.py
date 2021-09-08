def palindrome_maker_odd(temp):
    return temp[:-1]+temp[-1]+temp[-2::-1]    
                
def palindrome_maker_even(temp):
    return temp[:]+temp[::-1]

def chkpal(z):
    z=str(z)
    return z[:] == z[::-1]



def check_palindrome(s):
    x=s
    y=int(s)

    if len(x) <= 3:
        z=int(x)+1
        while(not chkpal(z)):
            z+=1
        return z

    f=0
    for i in x:
        if i == '9':
            pass
        else:
            f=1
    if f == 0:
        return int(x)+2
    
    if len(s)%2 == 1:
        temp = s[:((len(s)//2)+1)]
        temp=int(temp)+1
        temp = palindrome_maker_odd(str(temp))
        return temp
    else:
        temp = s[:len(s)//2]
        temp=int(temp)+1
        temp=palindrome_maker_even(str(temp))
        return temp

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):        
        return check_palindrome(A)

xy = Solution()
print(xy.solve('88288'))