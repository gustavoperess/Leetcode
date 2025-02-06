
from typing import List
#  self.nums = {i: n for i, n in enumerate(nums) if n}
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {i: n for i, n in enumerate(nums) if n}
            

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        l = max(len(self.nums) ,len(vec.nums))
        t = 0
        if l == len(self.nums):
            t = 1
        ans = 0
        if t == 1:
            for key, value in self.nums.items():
                if key in vec.nums:
                    ans += value * vec.nums[key]
        else:
            for key, value in vec.nums.items():
                if key in self.nums:
                    ans += value * self.nums[key]
        return ans

# Your SparseVector object will be instantiated and called as such:
nums2 = [1,0,0,2,3]
nums1 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)