class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect.bisect_right(self.calender, (startTime, endTime))

        if((idx>0 and self.calender[idx-1][1]>startTime) or (idx<len(self.calender) and self.calender[idx][0]<endTime)):
            return False
        bisect.insort(self.calender, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)