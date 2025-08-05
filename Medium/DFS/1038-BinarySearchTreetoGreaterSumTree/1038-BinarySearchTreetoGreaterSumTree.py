from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        if root.left:
            print("Left child of", root.val, "is", root.left.val)
        else:
            print("No left child for", root.val,)
        
        self.bstToGst(root.left)
        self.bstToGst(root.right)
        
        
def insert_level_order(arr: List[Optional[int]], root: Optional[TreeNode], i: int, n: int) -> Optional[TreeNode]:
    if i < n and arr[i] is not None:
        node = TreeNode(arr[i])
        root = node
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


result = Solution()
arr =[4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
root = insert_level_order(arr, None, 0, len(arr))
result.bstToGst(root)