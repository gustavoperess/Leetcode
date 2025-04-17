from typing import Optional, List

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        pass
        
        
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB
        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        print(one)
        return one

    
    
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


listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]

one = solution.create_linked_list(listA)
two = solution.create_linked_list(listB)
solution.getIntersectionNode(one, two)