from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = Counter(s1)
        s2Count = defaultdict(int)
        print(s1Count)

        l, r = 0, len(s1) - 1
        for i in range(len(s1)):
            s2Count[s2[i]] += 1
            print(s2Count)
        
        


        if s1Count == s2Count:
            return True

        while r < len(s2) - 1:
            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == 0:
                s2Count.pop(s2[l])
            l += 1
            r += 1
            s2Count[s2[r]] += 1
            print(s1Count)
            print(s2Count)
            if s1Count == s2Count:
                return True
        return False







[]
