#Optimal
class Solution:
    def reverse(self, x: int) -> int:
        sign =-1 if x<0 else 1
        x=abs(x)
        limit= 2**31 if sign==-1 else 2**31-1
        rev=0
        while(x>0):
            digit=x%10
            if rev>(limit-digit)//10:
                return 0
            rev=rev*10+digit
            x//=10
        return sign*rev