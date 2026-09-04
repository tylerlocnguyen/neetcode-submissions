class Solution:
    def isAlpha(self, s):
        if(ord("A") <= ord(s) <= ord("Z") or
        ord("a") <= ord(s) <= ord("z") or
        ord("0") <= ord(s) <= ord("9")):
            return True
        else:
            return False


    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not self.isAlpha(s[i]):
                i += 1
            while i< j and not self.isAlpha(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True