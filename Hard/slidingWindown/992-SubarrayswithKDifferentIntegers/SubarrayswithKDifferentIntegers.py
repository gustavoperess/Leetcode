from typing import List

class Solution:
    def subarraysWithKDistinctBruteForce(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for y in range(i, len(nums)):
                subarrays = nums[i:y + 1]
                if len(set(subarrays)) == k:
                    count += 1
        
        return count
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        farLeft, nearLeft, res = 0, 0, 0
        hashMap = {}
        for r in range(len(nums)):
            if nums[r] in hashMap:
                hashMap[nums[r]] += 1
            else:
                hashMap[nums[r]] = 1
            
            while len(hashMap) > k:
            
                hashMap[nums[nearLeft]] -= 1
                if hashMap[nums[nearLeft]] == 0:
                    del hashMap[nums[nearLeft]]
                nearLeft += 1
                farLeft = nearLeft
          
            while hashMap[nums[nearLeft]] > 1:
                hashMap[nums[nearLeft]] -= 1
                nearLeft += 1    
                    
            if len(hashMap) == k:
                res += nearLeft - farLeft + 1
                
        return res
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        hashMapOne, lOne, ansOne = {},0,0
        hashMapTwo, lTwo, ansTwo = {},0,0
        maxL, maxR = 0, 0
        for r in range(len(nums)):
            if nums[r] in hashMapOne:
                hashMapOne[nums[r]] += 1
            else:
                hashMapOne[nums[r]] = 1 
            
            while (r - lOne + 1) >= firstLen:
                currentSum = sum(nums[lOne:r + 1])
             
                if currentSum > ansOne:
                    ansOne = currentSum
                    maxL, maxR = lOne, r 
                hashMapOne[nums[lOne]] -= 1
                if hashMapOne[nums[lOne]] == 0:
                    del hashMapOne[nums[lOne]]
                lOne += 1
        
        arr = []
        for r in range(len(nums)):
            if r > maxR or r < maxL:
                arr.append(nums[r])
    
        for r in range(len(arr)):
            if arr[r] in hashMapTwo:
                hashMapTwo[arr[r]] += 1
            else:
                hashMapTwo[arr[r]] = 1 
            
            while (r - lTwo + 1) >= secondLen:
                currentSum = sum(arr[lTwo:r + 1])
                if currentSum > ansTwo:
                    ansTwo = currentSum
                hashMapTwo[arr[lTwo]] -= 1
                if hashMapTwo[arr[lTwo]] == 0:
                    del hashMapTwo[arr[lTwo]]
                lTwo += 1
        return ansOne + ansTwo
    
   

result = Solution()



