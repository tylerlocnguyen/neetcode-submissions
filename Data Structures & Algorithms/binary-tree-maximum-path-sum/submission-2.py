# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = root.val

        def dfs(node):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            if leftMax + rightMax + node.val > self.res:
                self.res = leftMax + rightMax + node.val
            if leftMax + node.val > self.res:
                self.res = leftMax + node.val
            if rightMax + node.val > self.res:
                self.res = rightMax + node.val
            if node.val > self.res:
                self.res = node.val
            return max(leftMax + node.val, rightMax + node.val, node.val)
        dfs(root)
        return self.res

            
        