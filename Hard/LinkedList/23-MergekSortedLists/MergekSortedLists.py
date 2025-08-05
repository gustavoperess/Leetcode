from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return
        
        while len(lists) > 1:
            ans = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                ans(self.sortTwoLists(l1, l2))
            lists = ans                
        return lists[0]
    
    def sortTwoLists(self, head1:List[Optional[ListNode]], head2:List[Optional[ListNode]]):        
        if head1 is None:
            return
        if head2 is None:
            return
        
        if head1.val <= head2.val:
            head1.next = self.sortTwoLists(head1.next, head2)
            return head1
        else:
            head2.next = self.sortTwoLists(head1, head2.next)
            return head2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy
            while list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next 
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
                # if list1:
                #     tail.next = list1
                #     list1 = list1.next
                # if list2:
                #     tail.next = list2
                #     list2 = list2.next
                return dummy.next
        
            

result =Solution()
# result.mergeKLists(lists = [[1,4,5],[2,3,4],[2,6]])



head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
result.mergeTwoLists(head1, head2)