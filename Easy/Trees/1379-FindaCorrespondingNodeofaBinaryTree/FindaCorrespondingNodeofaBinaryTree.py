from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node1, node2):
            if not node1 or not node2:
                return None
            elif node1 == target:
                print(node1.val)
                return node2
            
            return dfs(node1.left, node2.left) or dfs(node1.right, node2.right)
   
        return dfs(original, cloned)
        
    
def insert_level_order(arr: List[Optional[int]], root: Optional[TreeNode], i: int, n: int) -> Optional[TreeNode]:
    if i < n and arr[i] is not None:
        node = TreeNode(arr[i])
        root = node
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

arr = [7,4,3,None,None,6,19]
root = insert_level_order(arr, None, 0, len(arr))
target = root.right
result = Solution()
t = result.getTargetCopy(root, root, target)
print(t.val)