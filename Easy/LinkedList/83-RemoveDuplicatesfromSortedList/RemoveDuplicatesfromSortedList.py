from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return prev

    def deleteDuplicatesMedi(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(-1)
        fake.next = head
        curr, prev = head, fake
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return head

        
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




head_values = [1,4,5,5]
solution = Solution()
head = solution.create_linked_list(head_values)
deleted = solution.deleteDuplicatesMedi(head)
solution.print_list(deleted)