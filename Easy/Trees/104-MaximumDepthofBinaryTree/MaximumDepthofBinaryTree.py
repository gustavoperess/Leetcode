from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if root and root.right:
        #     print("root.ri.val:", root.right.val)
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
     


def insert_level_order(arr: List[Optional[int]], root: Optional[TreeNode], i: int, n: int) -> Optional[TreeNode]:
    if i < n and arr[i] is not None:
        node = TreeNode(arr[i])
        root = node
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

arr = [3,9,20,None,None,15,7]
root = insert_level_order(arr, None, 0, len(arr))
result = Solution()
t = result.maxDepth(root)
print(t)