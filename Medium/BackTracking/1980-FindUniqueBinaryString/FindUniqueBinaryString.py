from typing import List



class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        subset = []
        def dfs(n, current=""):
            if len(current) == n:
                subset.append(current)
                return
            dfs(n , current + "0")
            dfs(n , current + "1")
         
        
        dfs(len(nums[0]), "")
            
   
        for s in subset:
            if s not in nums:
                return s
            
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        hashMap = {}
        count = 0
        for i in range(len(students)):
            if students[i][1] in hashMap:
                hashMap[students[i][1]].append(students[i][0])
            else:
                hashMap[students[i][1]] = [students[i][0]]

        for value in hashMap.values():
            t = len(set(value))
            count = max(t, count)
        return count
    
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        y = 0
        for i in range(len(boxes)):
            if boxes[i] == "0":
               pass
                
        y += 1
    
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # t1 = sorted(nums1)
        # t2 = sorted(nums2,reverse=True)
        # ans = 0
        # for one, two in zip(t1, t2):
        #     ans += one * two
        # return t2
    
        nums1count, nums2count = [0]*101, [0]*101
        m, n = len(nums1), len(nums1count)
        
        # Fill counting arrays
        for i in range(m):
            nums1count[nums1[i]] += 1
            nums2count[nums2[i]] += 1
        
        l, r, product_sum = 0, n-1, 0
        while 0 < r and l < n:
            if not nums1count[l]:
                l += 1
            if not nums2count[r]:
                r -= 1
            if 0 < r and l < n and nums1count[l] and nums2count[r]:
                min_ = min(nums1count[l], nums2count[r])
                product_sum += l*r*min_
                nums1count[l] -= min_
                nums2count[r] -= min_
        return product_sum
        


result = Solution()
result.minOperations(boxes = "001011")
result.minProductSum(nums1 = [5,3,4,2], nums2 = [4,2,2,5])

