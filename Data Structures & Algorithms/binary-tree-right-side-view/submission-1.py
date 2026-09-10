# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            q_len = len(queue)

            for i in range(q_len):
                curr_node = queue.popleft()

                if i == q_len - 1:
                    result.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return result
