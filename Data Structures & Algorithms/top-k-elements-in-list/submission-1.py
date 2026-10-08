#bruteforce
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for n in nums:
            f[n]=f.get(n,0)+1
        sorted_element = sorted(f,key=f.get,reverse=True)
        return sorted_element[:k]