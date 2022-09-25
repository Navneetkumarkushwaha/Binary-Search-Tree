# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,arr,bound):
        if self.i == len(arr) or arr[self.i]>bound:
            return None
        root = TreeNode(arr[self.i])
        self.i += 1
        root.left = self.build(arr,root.val)
        root.right = self.build(arr,bound)
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        return self.build(preorder,float("inf"))
        
 Time complexity O(3n)
 space complexity O(1)
