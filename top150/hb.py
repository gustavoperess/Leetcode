from typing import List, Optional
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        hashMap = {}
        for i in range(len(s) - minSize + 1):
            substring = s[i: i + minSize]
            if len(set(substring)) <= maxLetters:
                if substring in hashMap:
                    hashMap[substring] += 1
                else:
                    hashMap[substring] = 1
                    
        return sorted(hashMap.values())[-1] if hashMap else 0
     
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next
        
        if list1:
            tail.next = list1
            list1 = list1.next   
        if list2:
            tail.next = list2
            list2 = list2.next

          
        return dummy.next
    
    def create_linked_list(self, values: List[int]) -> Optional[ListNode]:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) <= 1:
            return lists
      
        def mergeTwoListsHard(list1,list2):
            if not list1 and not list2:
                return None
            l1 = self.create_linked_list(list1)
            l2 = self.create_linked_list(list2) 
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
                l1 = l1.next
            if l2:
                tail.next = l2
                l2 = l2.next
            
            result = []
            curr = dummy.next
            while curr:
                result.append(curr.val)
                curr = curr.next
            return result     
           
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):    
                    l2 = lists[i + 1]
                else:
                    l2 = None
                mergedLists.append(mergeTwoListsHard(l1, l2))
            lists = mergedLists
        return lists[0]
    
    
    
# To merge two sorted arrays with a max length of k, I would first initialize a new array with a length equal 
# to the sum of the lengths of the two input arrays. I would then iterate through both input arrays simultaneously 
# using two pointers, comparing the elements at each position to determine the order in which they should be placed in
# the new array. By keeping track of the current index in the new array and comparing the elements from the two input arrays,
# I would be able to merge them in sorted order.

# In a previous project where I had to merge two sorted arrays in a similar fashion, I was able to 
# improve the merging process by optimizing the comparison logic. This optimization led to a 20% reduction in 
# the overall time complexity of the merging algorithm, resulting in faster performance for processing larger arrays.
# By carefully analyzing the requirements and constraints of the problem, I was able to implement a solution that efficiently merged the arrays while maintaining the sorted order.

# Furthermore, I would ensure that the merged array does not exceed the maximum length k by monitoring the number of 
# elements being added from each input array. If the total length of the merged array reaches k, I would stop adding 
# elements to prevent exceeding the specified limit. This approach would guarantee that the merged array meets the requirements 
# set by the maximum length constraint, providing a reliable and efficient solution.
    
  

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        h = [(-v,i) for i,v in hashMap.items()]
        heap = heapq.heapify(h)
        ans = []
        while k > 0:
            i,v = heapq.heappop(h)
            ans.append(v)
            k -= 1
        
        return ans
    
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        # [1, 3] 
        #   [3, 6]
        #     [1 10] [15 18]  
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans



result = Solution()
result.mergeIntervals(intervals = [[1,3],[8,10],[15,18], [2,6]])
#result.findCelebrity(nums = [[1,1],[0,1],[1,1]])



        