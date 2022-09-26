#User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def solve(self,root):
        if root:
            
            self.solve(root.right)
            
            self.cnt += 1
            if self.k == self.cnt:
                self.ans = root.data
            
            self.solve(root.left)
            
            
    def kthLargest(self,root, k):
        self.ans = None
        self.k = k
        self.cnt = 0
        self.solve(root)
        return self.ans
      
      
      
      kth largest element is 40

Time Complexity: O(min(K,N))

Space Complexity: O(min(K,N))
