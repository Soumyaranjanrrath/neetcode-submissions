#better then brute force (using hashset)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_xor=len(nums)
        for i in range(len(nums)):
            n_xor ^= i
            n_xor ^= nums[i]
        return n_xor