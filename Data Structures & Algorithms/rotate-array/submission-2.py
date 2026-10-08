#brute force
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            new_index = (i + k) % n
            result[new_index] = nums[i]

        nums[:] = result