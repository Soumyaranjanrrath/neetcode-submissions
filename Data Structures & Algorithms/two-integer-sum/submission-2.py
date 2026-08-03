class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= {}
        for i in range (len(nums)):
            num =nums[i]
            comp = target- num
            if comp in s:
                return [s[comp],i]
            s[num]=i