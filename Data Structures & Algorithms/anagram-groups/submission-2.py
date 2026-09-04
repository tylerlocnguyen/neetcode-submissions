class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        used = set()
        for i in range(len(strs)):
            if i in used:
                continue
            temp = [strs[i]]
            used.add(i)
            for j in range(len(strs)):
                if i == j or j in used:
                    pass
                else:
                    if sorted(strs[i]) == sorted(strs[j]):
                        temp.append(strs[j])
                        used.add(j)
            anagrams.append(temp)
        return anagrams

