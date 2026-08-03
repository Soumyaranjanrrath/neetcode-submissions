from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            key = tuple(count)
            if key not in group:
                group[key] = []
            group[key].append(word)
        return list(group.values())