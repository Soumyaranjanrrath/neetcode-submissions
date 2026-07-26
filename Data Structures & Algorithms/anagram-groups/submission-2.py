class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m =  {}
        for string in strs:
            key = tuple(sorted(string))
            if key not in m:
                m[key] = []
            m[key].append(string)

        return list(m.values())
