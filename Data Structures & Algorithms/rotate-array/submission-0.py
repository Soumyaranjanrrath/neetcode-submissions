#brute force
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        for i in range(k) :
            last=nums[-1]
            for j in range(n-1,0,-1):
                nums[j]=nums[j-1]
            nums[0]=last