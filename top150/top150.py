from typing import List
import random
import heapq
class RandomizedSet:
    def __init__(self):
        self.hmap = {}
        self.list = []
   
    
    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.hmap[val] = len(self.list)
        self.list.append(val)
       
    def remove(self, val: int) -> bool:
        if val in self.hmap:
            last_element, idx = self.list[-1], self.hmap[val]
            self.list[idx], self.hmap[last_element] = last_element, idx
            self.list.pop()
            del self.hmap[val]            
            return True
        return False
       
    
    def getRandom(self) -> int:
        return random.choice(self.list)
class Solution:
    def removeDuplicatesEasy(self, nums: List[int]) -> int:
        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex
    
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, len(nums)
        while i < k:
            if nums[i] == val:
                del nums[i]
                k -= 1
                i -= 1
            i += 1
        return i
    
    def removeDuplicatesMed(self, nums: List[int]) -> int:
        # count = 0
        # sor = len(nums)
        # ans, l1, l2, k = 0, 0, 1, len(nums)
        # while l1 < k:
        #     while l2 < k and nums[l1] == nums[l2]:
        #         l2 += 1
        #         count += 1
        #     while count >= 2:
        #         l2 -= 1
        #         del nums[l2] 
        #         k -= 1
        #         count -= 1
        #         ans += 1
            
        #     l1 += 1
        #     l2 = l1 + 1
        #     count = 0

            
        # return sor - ans
        if not nums:
            return 0
        
        l = 0
        count = 0
        for r in range(len(nums)):
            if nums[r] == nums[r - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[l] = nums[r]
                l += 1

        return nums
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        rotated = [0] * n
        for i in range(len(nums)):
            rotated[(i + k) % n] = nums[i]
        for i in range(len(nums)):
            nums[i] = rotated[i]
    
    def maxProfitEasy(self, prices: List[int]) -> int:
        minBuy = float("inf")
        profit = 0
        for p in prices:
            minBuy = min(minBuy, p)
            profit = max(profit, p - minBuy)
        return profit
    
    # DAY 1
    def maxProfitMed(self, prices: List[int]) -> int:
        curr, curr_hold = -float("inf"), 0
        for p in prices:
            prev, prev_hold = curr, curr_hold
            curr = max(prev, prev_hold - p)
            curr_hold = max(prev_hold, prev + p)
        
    # Day 2
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        l = 0 
        r1, r2 = len(nums) - 2, len(nums) - 1
        while r1 >= l:
            if nums[r1] >= r2 - r1:  
                r1 -= 1
                r2 = r1 + 1
            else:
                r1 -= 1
        if r2 - r1 == 1:
            return True
        return False
    
    
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        # ans = 0
        # while r < len(nums) - 1:
        #     s = max(nums[l:r + 1])
        #     l = r + 1
        #     r = s
        #     ans += 1
            
        # return ans
            
    def lengthOfLastWord(self, s: str) -> int:
        l, r = 0, len(s)
        while r > 0:
            r -= 1
            if s[r] != " ":
                l += 1
            elif l > 0:
                return l
        return l
    
    #Day 3
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accumulator = 1
        prefixIndex = len(nums) - 2
        ans = [1] * len(nums)
        for i in reversed(range(1, len(nums))):
            accumulator *= nums[i]
            ans[prefixIndex] = accumulator
            prefixIndex -= 1
        sufixIndex = 1
        accumulator = 1
        for i in range(len(nums) - 1):
            accumulator *= nums[i]
            ans[sufixIndex] *= accumulator
            sufixIndex += 1
        return ans
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        prev_cos = 0
        for i in range(len(gas)):
            x = cost[i] % len(gas)
            prev_cos = prev_cos - i + gas[x]
            print(prev_cos - x, prev_cos)
            
    def hihestProduct(self, p: List[int]) -> int:
        if len(p) < 3:
            return 0
        largest = heapq.nlargest(3, p)
        smallest = heapq.nsmallest(2, p)
        ans = max(largest[0] * largest[1] * largest[2], smallest[0] * smallest[1] * largest[0])
        return ans
    
            
            
result = Solution()

result.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])
#result.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3])




