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
            return True
        for i in range(left, right + 1):
            if is_prime(i):
                prime.append(i)
     
        minV = float('inf')
        min_pair = [-1,-1]
        for i in range(len(prime) - 1):
            t = abs(prime[i] - prime[i + 1])
            if t < minV:  
                minV = t
                min_pair = [prime[i], prime[i + 1]]
        return min_pair
        


result = Solution()
result.closestPrimes(left = 1, right = 1000000)