from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        left = 0 
        ans = []
        x = k
        firstWindow = max(nums[:k])
        ans.append(firstWindow)
        for right in range(len(nums)):
            if nums[right] in hashMap:
                hashMap[nums[right]] += 1
            else:
                hashMap[nums[right]] = 1
            
                
            if right - left + 1 == k:         
                hashMap[nums[left]] -= 1
                if hashMap[nums[left]] == 0:
                    del hashMap[nums[left]]
                left += 1
                if x < len(nums):
                    it = max(sorted(list(hashMap.keys()))[-1], nums[x])
                    ans.append(it)
                x += 1
        print(ans)
        return ans
    
    
    def maxSlidingWindowUSINGQUEUE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))
            while d and nums[d[-1]] < n:
                d.pop()
                print("\t Popped from d because d has elements and nums[d.top] < curr element")
            d.append(i)
            print("\t Added i to d")
            if d[0] == i - k:
                d.popleft()
                print("\t Popped left from d because it's outside the window's leftmost (i-k)")
            if i>=k-1:
                out.append(nums[d[0]])
                print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
        return out
      

result = Solution()
#result.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
# result.maxSlidingWindow(nums = [1], k = 1)
result.maxSlidingWindow(nums = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7], k=7)
# print(len( [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]))
# print(len([9,9,10,10,10,10,10,10,10,9,9,9,8,8]))