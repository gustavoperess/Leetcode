# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
        
    def __repr__(self):
        return f"[{self.start}, {self.end}]"

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        flattened = [item for sublist in schedule for item in sublist]
        flattened.sort(key=lambda x: x.start)
        mergedItems = [flattened[0]]
        
        for i in range(1, len(flattened)):
            if flattened[i].start <= mergedItems[-1].end:
                mergedItems[-1].end = max(flattened[i].end, mergedItems[-1].end)
            else:
                mergedItems.append(flattened[i])
        
        ans = []
        for i in range(len(mergedItems) - 1):
            ans.append(Interval(mergedItems[i].end, mergedItems[i + 1].start))
        
        return ans


# Example test
schedule = [
    [Interval(1, 2), Interval(5, 6)],
    [Interval(1, 3)],
    [Interval(4, 10)]
]

print(Solution().employeeFreeTime(schedule))
# Output: [[3, 4]]
