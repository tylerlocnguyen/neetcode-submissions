# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 1
        currMax = root.val #2
        

        def dfs(node, maxVal):
            if not node:
                return
            if node.val >= maxVal:
                self.res += 1
                maxVal = node.val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        dfs(root.left, currMax)
        dfs(root.right, currMax)

        return self.res

            




        