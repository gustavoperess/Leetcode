from typing import List, Optional
import math
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
# t = result.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)





def fibonacci(n):
    if n < 2:
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2)



def sqrBinary(n):
    if n < 2:
        return n
    length = n + 1
    l = 2
    r = length - 1
    while l <= r:
        mid = (r + l) // 2
        if (mid * mid)  == n:
            return mid
        if mid * mid < n:
            l = mid  + 1
        else:
            r = mid - 1




def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    mindex = m  - 1
    nindex =  n - 1
    r = (m + n) - 1
    while nindex >= 0:
        if mindex >= 0 and nums1[mindex] > nums2[nindex]:
            nums1[r] = nums1[mindex]
            mindex -= 1
        else:
            nums1[r] = nums2[nindex]
            nindex -= 1
        r -= 1

# merge( nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)


def mergeInt(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda i: i[0])
    ans = [intervals[0]]
    for i in range(1, len(intervals)):
        laste_added = ans[-1][1]
        if laste_added >= intervals[i][0]:
            ans[-1][-1] = max(laste_added, intervals[i][1])
        else:
            ans.append([intervals[i][0], intervals[i][1]]) 
            
    return ans

# mergeInt(intervals = [[1,3],[2,6],[8,10],[15,18]])


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    ans = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            ans.append(newInterval)
            return ans + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            ans.append(intervals[i])
        else:
            mi = min(intervals[i][0], newInterval[0])
            ma = max(intervals[i][1], newInterval[1])
            newInterval = [mi, ma]
    ans.append(newInterval)
    return ans
    



def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    ans = []
    for i in range(len(firstList)):
        for y in range(len(secondList)):
            print(firstList[i], secondList[y])


# intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])

def minOperations(nums: List[int]) -> int:
    flips = 0
    start = 0
    while start + 3 <= len(nums):
        if nums[start] == 0:
            flips += 1
            nums[start] = 1
            nums[start + 1] = (nums[start + 1] + 1) % 2
            nums[start + 2] = (nums[start + 2] + 1) % 2
        start += 1
    if 0 in nums:
        return -1
    return flips


def countKConstraintSubstrings(s: str, k: int) -> int:
    hashMap = {}
    one = 0
    two = 0
    for r in range(len(s)):
        if s[r] == "1":
            one +=  1
        else:
            two += 1
        
        if one >= k and two >= k:
            print(one, r, two)
            
            

            
    

            



countKConstraintSubstrings( s = "10101", k = 1)