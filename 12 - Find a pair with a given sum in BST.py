# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self,root,reverse = False):
        self.st = []
        self.reverse = reverse
        
        if self.reverse == True:
            while root:
                self.st.append(root)
                root = root.right
        else:
            while root:
                self.st.append(root)
                root = root.left
    def next(self):
        x = self.st.pop()
        if self.reverse == False:
            root = x.right
            while root:
                self.st.append(root)
                root = root.left
        else:
            root = x.left
            while root:
                self.st.append(root)
                root = root.right
        return x.val
    def hashnext(self):
        return len(self.st) != 0
            
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        l = BSTIterator(root,False)
        r = BSTIterator(root,True)
        
        i = l.next()
        j = r.next()
        
        while i<j:
            
            if  i+j == k:
                return True
            elif i+j < k:
                i = l.next()
            else:
                j = r.next()
        
        return False
        
        
  SC :- O(H)*2
  TC :- (n)
