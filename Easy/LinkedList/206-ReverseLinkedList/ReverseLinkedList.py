from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
        
    def create_linked_list(self, values: List[int]) -> Optional[ListNode]:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def print_list(self, head: Optional[ListNode]) -> None:
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")



head_values = [1,2,3,4,5]
solution = Solution()
head = solution.create_linked_list(head_values)

#print("Original List:")
#solution.print_list(head)

new_head = solution.reverseList(head)

# print("Reversed List:")
# solution.print_list(new_head)
