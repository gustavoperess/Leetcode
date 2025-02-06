from typing import Optional, List
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findGCD(n1, n2):
            while n2:
                n1, n2 = n2, n1%n2
            return n1
        current = head
        
        while current and current.next:
            gcd_val = findGCD(current.val, current.next.val)
            gcd_node = ListNode(gcd_val)
            
            gcd_node.next = current.next
            current.next = gcd_node
        
            current = gcd_node.next
        
        return head


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

head_values = [18,6,10,3]
head = create_linked_list(head_values)
solution = Solution()
new_head = solution.insertGreatestCommonDivisors(head)