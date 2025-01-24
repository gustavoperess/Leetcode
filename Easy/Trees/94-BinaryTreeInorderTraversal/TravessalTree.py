from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: 
        result = []
        
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return result
      
def insert_level_order(arr: List[Optional[int]], root: Optional[TreeNode], i: int, n: int) -> Optional[TreeNode]:
    if i < n and arr[i] is not None:
        node = TreeNode(arr[i])
        root = node
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

# Input array representation of the tree
arr = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, None, None, 9, None]

# Build the binary tree
root = insert_level_order(arr, None, 0, len(arr))

# Create the Solution object and perform in-order traversal
solution = Solution()
t = solution.inorderTraversal(root)

# Print the in-order traversal result
print("In-order Traversal Result:", t)
