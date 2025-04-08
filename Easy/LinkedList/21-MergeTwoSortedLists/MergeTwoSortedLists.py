from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        
        return dummy.next
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = ListNode()
        index = 0
        while head:
            
            node.next = head.next
            head = head.next
        return node.next
            
            
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


solution = Solution()
head = [3,2,0,-4]
m = solution.create_linked_list(head)
solution.hasCycle(m)
# list1 = solution.create_linked_list([1,2,4])
# list2 = solution.create_linked_list([1,3,4])
# merged = solution.mergeTwoLists(list1, list2)
# solution.print_list(merged)
