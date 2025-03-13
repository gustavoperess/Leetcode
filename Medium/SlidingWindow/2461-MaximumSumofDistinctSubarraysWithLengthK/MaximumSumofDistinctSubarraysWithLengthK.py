from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
            #TLE
            # ans = 0
            # for i in range(len(nums)):
            #     s = nums[i:k + i]
            #     x = set(s)
            #     if len(x) == k:
            #         ans = max(ans, sum(s))
            # return ans
            # l, r = 0, len(nums) - 1
            # x = 0
            # ans = 0
            # while l < r:
            #     subsets = []
            #     while x < r and len(subsets) < k and nums[x] not in subsets:
            #         subsets.append(nums[x])
            #         x += 1
            #     l += 1
            #     x = l
            #     if len(subsets) == k:
            #         ans = max(ans, sum(subsets))
            # return ans
            hashMap = {}
            l = 0
            curr_sum = 0
            ans = 0
            for r in range(len(nums)):
                curr_sum += nums[r]
                if nums[r] in hashMap:
                    hashMap[nums[r]] += 1
                else:
                    hashMap[nums[r]] = 1
                
                if r - l + 1 > k:
                    hashMap[nums[l]] -= 1
                    if hashMap[nums[l]] == 0:
                        hashMap.pop(nums[l])
                    curr_sum -= nums[l]
                    l += 1

                if len(hashMap) == k and r - l + 1 == k:
                    ans = max(ans, curr_sum)
            return ans


result = Solution()
result.maximumSubarraySum(nums = [1,5,4,2,9,9,9], k = 3)