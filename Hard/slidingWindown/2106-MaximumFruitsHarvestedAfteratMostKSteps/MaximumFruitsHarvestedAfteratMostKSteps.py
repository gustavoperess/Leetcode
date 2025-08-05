from typing import List


class Solution:
     
    def test(self, nums, k):
        l,r = 0, len(nums) -1 
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == k:
                return
            if nums[mid] < k:
                l = mid + 1
            elif nums[mid] > k:
                r = mid - 1
                
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1
        right = m + n - 1
        # [2,5,6,0,0,0]
        # [1,2,3]
        while nidx >= 0:
          
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1
                
            right -= 1

        return nums1
        
        
    def twoSum(self, nums: List[int] , target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in hashMap:
                return [hashMap[remaining], i]
            hashMap[nums[i]] = i
        return [-1, -1]
       
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashMap = {}
        l = 0
        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):
                remaining = nums[i] + nums[y]
                print(remaining, nums,i, y)
                # if remaining in hashMap:
                #     print(hashMap, i)
                # hashMap[nums[i]] = i
        


result = Solution()
#result.maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4)
#result.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# t = result.threeSum( nums = [-1,0,1, -2])
# # print(t)


v = 1
n = 49
t = v * v

while t < n:
    v += 1
    t = v * v

if t == n:
    print(f"{n} is a perfect square: {v}^2")
else:
    print(f"{n} is not a perfect square")
