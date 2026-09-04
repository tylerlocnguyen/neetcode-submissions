class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")" : "(", "}" : "{", "]" : "["}
        for i in s:
            if i not in map:
                stack.append(i)
            else:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

        