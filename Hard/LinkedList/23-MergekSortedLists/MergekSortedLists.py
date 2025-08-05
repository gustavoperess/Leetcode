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
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mindex = m - 1
        nindex = n - 1
        right = (m + n) - 1
        while nindex >= 0:
            if nums1[mindex] > nums2[nindex]:
                nums1[right] =  nums1[mindex]
                mindex -= 1
            else:
                nums1[right] = nums2[nindex]
                nindex -= 1
            right -= 1
        return nums1
    
    
result =Solution()
t = result.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
