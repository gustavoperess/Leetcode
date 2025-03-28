from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while len(students) > count:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            else:
                students.append(students[0])
                count += 1
            students.pop(0)
                
        return len(students)

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # seconds = 0
        # while tickets[k] > 0:
        #     for i in range(len(tickets)):
        #         if tickets[i] > 0:       
        #             tickets[i] -= 1
        #             seconds += 1
                
        #         if tickets[k] == 0:
        #             return seconds
        total = 0
        for i,x in enumerate(tickets):
            if i <= k:
                print(tickets[i], tickets[k])
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)
         
        print(total)
        
            


result = Solution()
result.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1])
#result.timeRequiredToBuy(tickets = [2,3,2], k = 2)
result.timeRequiredToBuy(tickets = [5,1,1,1], k = 0)
#result.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])