from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            res = TreeNode(root1.val + root2.val)
            res.right = self.mergeTrees(root1.right, root2.right) 
            res.left = self.mergeTrees(root1.left, root2.left)
            if res.left and res.left.val:
                print("left", res.left.val)
            if res.right and res.right.val:
                print("right", res.right.val)
            return res
 
        
    
def insert_level_order(arr: List[Optional[int]], root: Optional[TreeNode], i: int, n: int) -> Optional[TreeNode]:
    if i < n and arr[i] is not None:
        node = TreeNode(arr[i])
        root = node
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

arr1 = [1,3,2,5]
arr2 = [2,1,3,None,4,None,7]
root = insert_level_order(arr1, None, 0, len(arr1))
root2 = insert_level_order(arr2, None, 0, len(arr2))
result = Solution()
t = result.mergeTrees(root, root2)
# print(t.val)