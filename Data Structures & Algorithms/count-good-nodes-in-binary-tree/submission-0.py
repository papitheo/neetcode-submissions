# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr_node, curr_max):
            if not curr_node:
                return 0
            if curr_node.val >= curr_max:
                is_good = 1
            else:
                is_good = 0
            
            curr_max = max(curr_node.val, curr_max)
            
            return(
                is_good
                + dfs(curr_node.left, curr_max)
                + dfs(curr_node.right, curr_max)
            )
        return dfs(root, float("-inf"))

        