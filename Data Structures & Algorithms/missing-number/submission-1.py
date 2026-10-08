#better then brute force (using hashset)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number=set(nums)
        for i in range(len(nums)+1):
            if i not in number:
                return i