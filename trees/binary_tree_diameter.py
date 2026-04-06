from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def tree_depth(root):
            if not root:
                return 0
            depth_left = tree_depth(root.left)
            depth_right = tree_depth(root.right)
            self.max_diameter = max(self.max_diameter, depth_left+ depth_right)
            return 1 + max(depth_left,depth_right)
        tree_depth(root)
        return self.max_diameter