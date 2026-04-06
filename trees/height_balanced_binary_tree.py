from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_height_balanced = True
        def get_depth(root):
            if not root:
                return 0
            left = get_depth(root.left)
            right = get_depth(root.right)
            if left - right > 1 or left-right < -1:
                self.is_height_balanced = False

            return 1 + max(left,right)
        get_depth(root)
        return self.is_height_balanced