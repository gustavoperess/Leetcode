from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i in nums:
            if i > 0:
                arr1.append(i)
            else:
                arr2.append(i)
        ans = [0] * len(nums)
        l1, k1 = 0, 0
        l2, k2 = 0, 0
        while l1 < len(ans) and l2 < len(ans):
            if l1 % 2 == 0:
                ans[l1] = arr1[k1]
                k1 += 1
            if l2 % 2 == 1:
                ans[l2] = arr2[k2]
                k2 += 1          
            l1 += 1
            l2 += 1

        return ans
    def rearrangeArrayOptimized(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2
        return ans
