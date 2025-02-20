
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.lonely_nodes = []
        def dfs(node):
            if not node:
                return
            if node.left and not node.right:
                self.lonely_nodes.append(node.left.val)
            if node.right and not node.left:
                self.lonely_nodes.append(node.right.val)

            dfs(node.left)
            dfs(node.right)
            
 
        dfs(root)
        return self.lonely_nodes
       


def insert_level_order(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while i < len(arr):
        curr = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1

    return root


arr = [1,2,3,None,4]
# arr = [11,99,88,77,None,None,66,55,None,None,44,33,None,None,22]
arr = [7,1,4,6,None,5,3,None,None,None,None,None,2]
root = insert_level_order(arr)
solution = Solution()
t = solution.getLonelyNodes(root)