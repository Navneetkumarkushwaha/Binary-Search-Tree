# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root:
            self.solve(root.left)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
            self.solve(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.k = k
        self.ans = None
        self.solve(root)
        return self.ans
      

kth smallest element is 25

Time Complexity: O(min(K,N))

Space Complexity: O(min(K,N))  
      
      
      
      
    
