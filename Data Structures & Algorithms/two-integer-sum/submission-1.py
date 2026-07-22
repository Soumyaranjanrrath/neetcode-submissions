class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            comp = target-num
            if comp in d:
                return [d[comp],i]
            d[num] = i