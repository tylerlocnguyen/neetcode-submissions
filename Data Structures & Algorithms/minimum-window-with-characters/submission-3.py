class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if s == t:
            return s
        countT, window = {}, {}
        result = [-1, -1]
        resultLength = float("infinity")
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        l = 0
        have = 0
        need = len(countT)
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resultLength:
                    result = [l,r]
                    resultLength = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        if resultLength != float("infinity"):
            return s[l:r+1]
        else:
            return "" 

        
