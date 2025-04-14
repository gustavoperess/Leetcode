from typing import Optional, List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        print(current.val, current.next.val)
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        print(head, head.next, head.val)
        
    
    
    def create_linked_list(self, values: List[int]) -> Optional[ListNode]:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head



head_values = [1,1,2,2,2]
reoder = [1,2,3,4]
solution = Solution()
head = solution.create_linked_list(head_values)
new_headTwo = solution.create_linked_list(reoder)
solution.reorderList(new_headTwo)
new_head = solution.frequenciesOfElements(head)
