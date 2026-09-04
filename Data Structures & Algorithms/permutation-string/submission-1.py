from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = Counter(s1)
        windowCount = defaultdict(int)

        l, r = 0, len(s1) - 1
        for i in range(len(s1)):
           windowCount[s2[i]] += 1
        

        while r < len(s2) - 1:
            if s1Count == windowCount:
                return True
            windowCount[s2[l]] -= 1
            if windowCount[s2[l]] == 0:
                windowCount.pop(s2[l])
            l += 1
            r += 1
            windowCount[s2[r]] += 1
        return s1Count == windowCount







[]
