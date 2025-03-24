
from typing import List


class Solution:
    # def countDays(self, days: int, meetings: List[List[int]]) -> int:
    #     #TLE
    #     numbers = []
    #     for i in range(len(meetings)):
    #         for x in range(meetings[i][0], meetings[i][1] + 1):
    #             numbers.append(x)
    #     ans = 0
    #     for n in range(1, days + 1):
    #         if n not in numbers:
    #             ans += 1
    #     return ans
    
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged_meetings = []
        for meeting in meetings:
            if not merged_meetings or meeting[0] > merged_meetings[-1][1]:
                merged_meetings.append(meeting)
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])
        meeting_days_count = 0       
        for start, end in merged_meetings:
            meeting_days_count += end - start + 1
        
        return days - meeting_days_count

result = Solution()
result.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]])
#result.countDays(days = 5, meetings = [[2,4],[1,3]])