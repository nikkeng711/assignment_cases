import bisect

class Calendar:
    def __init__(self):
        self.events = []  

    def book(self, start: int, end: int) -> bool:
        pos = bisect.bisect_left(self.events, (start, end))
        if pos > 0 and self.events[pos - 1][1] > start:
            return False
        if pos < len(self.events) and self.events[pos][0] < end:
            return False
        bisect.insort(self.events, (start, end))
        return True

calendar = Calendar()
print(calendar.book(5, 10)) 
print(calendar.book(8, 13))  
print(calendar.book(10, 15)) 
