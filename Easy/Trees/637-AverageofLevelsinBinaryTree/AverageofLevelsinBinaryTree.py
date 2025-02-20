
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.mediumVal = {}
        def dfs(node, depth):
            if not node:
                return
            self.mediumVal[0] = [root.val]
            if node.left:
                if depth in self.mediumVal:
                    self.mediumVal[depth].append(node.left.val)
                else:
                    self.mediumVal[depth] = [node.left.val]
            if node.right:
                if depth in self.mediumVal:
                    self.mediumVal[depth].append(node.right.val)
                else:
                    self.mediumVal[depth] = [node.right.val]
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
           
 
        dfs(root, 1)
        ans = []
        for val in self.mediumVal.values():
            m = sum(val) / len(val)
            ans.append(m)
        return ans




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


arr = [3,9,20,None,None,15,7]
# arr = [7,1,4,6,None,5,3,None,None,None,None,None,2]
root = insert_level_order(arr)
solution = Solution()
t = solution.averageOfLevels(root)