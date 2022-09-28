# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve1(self,root):
        
        self.prev = None
        
        def flatten(root):
            if not root:
                return 
            flatten(root.right)
            flatten(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root
        flatten(root)
        return self.prev
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        return self.solve1(root)
        
        
   Time complexity :- O(n)
   Space Complexity :- O(n)
