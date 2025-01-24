from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        
        queue = deque([root])
        # print("Initial queue:", [node.val for node in queue])
        while queue:
            node = queue.popleft()
            # print("Processing node:", node.val)
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
                # print("Queue after adding children:", [n.val for n in queue])
        return root
    
    def printTree(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
  
        while queue:
            node = queue.popleft()
    
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        while result and result[-1] is None:
            result.pop()
        return result
    
    
def insert_level_order(arr: List[Optional[int]], root: Optional[TreeNode], i: int, n: int) -> Optional[TreeNode]:
    if i < n and arr[i] is not None:
        node = TreeNode(arr[i])
        root = node
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root



arr = [4, 2, 7, 1, 3, 6, 9]
root = insert_level_order(arr, None, 0, len(arr))
solution = Solution()
inverted_root = solution.invertTree(root)

# Print the tree after inversion
print("Inverted Tree:", solution.printTree(inverted_root))
