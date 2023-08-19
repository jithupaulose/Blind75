def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Step 1: Sort by start time
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:  # Step 2: Check for overlap
            return False
    return True


time complexity is O(nlogn)
space complexity is  O(1)
