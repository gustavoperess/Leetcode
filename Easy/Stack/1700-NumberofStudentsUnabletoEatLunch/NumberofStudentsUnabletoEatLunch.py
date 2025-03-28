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



result = Solution()
result.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1])
#result.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])