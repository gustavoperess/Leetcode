from typing import List


class Solution:
    def countPairsBruteForce(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):
                if nums[i] == nums[y] and i * y % k == 0:
                    ans += 1
        return ans
    
    
    def countPairs(self, nums: List[int], k: int) -> int:
        # CANT FIND A BETTER ALGORITHM MAY NEED TO COME BACK
        hashMap = {}
        left = 0
        for right in range(len(nums)):
            if nums[right] in hashMap:
                hashMap[nums[right]] += 1
            else:
                hashMap[nums[right]] = 1
            # if max(hashMap.values()) >= 2:
            #     print(hashMap)
            # # while len(hashMap) > 0:
            # #     print(hashMap)
            # #     hashMap[nums[left]] -= 1
            # #     if hashMap[nums[left]] == 0:
            # #         del hashMap[nums[left]]
            # #     left += 1
      

    


result = Solution()
result.countPairs(nums = [3,1,2,2,2,1,3], k = 2)