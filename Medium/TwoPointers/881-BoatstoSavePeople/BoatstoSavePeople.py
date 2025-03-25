from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        # print(people)
        t = []
        while l <= r:
            if people[l] + people[r] <= limit:
                t.append([people[l], people[r]])  
                l += 1
            else:
                t.append([people[r]])   
            r -= 1
            res += 1
                
        print(t, res)
        return res
        
        
        


result = Solution()
result.numRescueBoats(people = [1,2], limit = 3)
result.numRescueBoats(people = [1,2,2,3], limit = 3)
result.numRescueBoats(people = [3,5,3,4], limit = 5)
result.numRescueBoats([3,8,7,1,4], 9)