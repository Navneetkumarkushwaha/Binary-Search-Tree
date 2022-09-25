# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,lb,ub):
        if not root:
            return True
        if lb >= root.val or root.val >= ub:
            return False 
        
        return self.check(root.left,lb,root.val) and self.check(root.right,root.val,ub)
       
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root,float('-inf'),float('inf'))
      
      
TC : - O(n)
SC : - O(1)
        
        
        
        
        
        
        
        
        
