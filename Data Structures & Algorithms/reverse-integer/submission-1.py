#Bruteforce
class Solution:
    def reverse(self, x: int) -> int:
        sign= -1 if x<0 else 1
        rev_num=int(str(abs(x))[::-1])*sign
        if rev_num < -2**31 or rev_num > 2**31-1:
            return 0
        return rev_num