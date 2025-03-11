from typing import List
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [] # TLE
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        for num in range(max(2, left), right + 1):
            if is_prime(num):
                prime .append(num)

         
        if len(prime) < 2:
            return [-1, -1]
            
        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(prime)):
            gap = prime[i] - prime[i-1]
            if gap < min_gap:
                min_gap = gap
                result = [prime[i-1], prime[i]]
                
        return result
        
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashMap = {}
        ans = []
        for n in nums:
            if n in hashMap:
                ans.append(n)
                hashMap[n] += 1
            else:
                hashMap[n] = 1

        return ans
  
        
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = blocks[:k].count('W')
        #print(white_count, blocks[:k])
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                white_count -= 1
            if blocks[i] == "W":
                white_count += 1
            
            #print(white_count, blocks[i], blocks[i - k])
        
  
            
result = Solution()
result.countOfSubstrings(word = "aeiou", k = 0)
