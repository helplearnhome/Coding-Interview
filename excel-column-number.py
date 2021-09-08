class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
            d={
                'A':1,
                'B':2,
                'C':3,
                'D':4,
                'E':5,
                'F':6,
                'G':7,
                'H':8,
                'I':9,
                'J':10,
                'K':11,
                'L':12,
                'M':13,
                'N':14,
                'O':15,
                'P':16,
                'Q':17,
                'R':18,
                'S':19,
                'T':20,
                'U':21,
                'V':22,
                'W':23,
                'X':24,
                'Y':25,
                'Z':26
            }

            sum=0
            print(A)
            for index,i in enumerate(A):
                if index != 0:
                    sum=sum*26+d[i]
                else:
                    sum=sum+d[i]
                print(index,i,sum)

            return sum

x = Solution()
print(x.titleToNumber('AA'))

#edge cases see and do. Most times you may modify edge cases conditions and it may work. Here first edge was
#needed to modify. Last if modified produced error. As we needed that.