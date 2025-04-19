import time
from typing import List

# Leetcode 253


# retried 4/19/2025
class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        # goal:
            # given array of time intervals (start and end), return the minimum number of conference rooms required
        # idea:
            # iterate and collect each event type into a list:
                # intervals[0] = meeting start = 1
                # intervals[1] = meeting end = -1
            # sort the events in chronological order
            # iterate the sorted event timeline:
                # if event type is 1 (start):
                    # increment active by 1
                # else (event type is end):
                    # decrement active by 1
                # update max active
        """

        # TC: O(N log N) / SC: O(2N) == O(N)
        timeline = []
        for interval in intervals:
            start, end = [interval[0], 1], [interval[1], -1]

            timeline.append(start)
            timeline.append(end)

        timeline.sort()
        active = min_rooms = 0

        for time, event_type in timeline:
            active += event_type
            min_rooms = max(active, min_rooms)

        return min_rooms


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        # objective:
            # given array of meeting time intervals, return minimum nubmer of conference rooms required
        # keywords:
            # interval:
                # intervals[i] = [start, end]
        # brainstorm:
            # intuition:
                # as a person wanting to enter a room, the person would look at meeting rooms linearly
                    # ex) check room 1 -> if not open -> check room 2 -> if not open -> ....
                # Let's assume that there are infinite number of meeting rooms available, and there are 10 groups
                    # if people can't find a room, they will go for next room, then next room, ...
                # However, the intervals in the example scenario can vary:
                    # one group might start earlier than others
                    # a group might even end their meeting before another group needs a meeting room
                # To find the minimum required rooms for all meeting groups:
                    # I can look at meeting intervals in a chronological order:
                        #        g1.    g2.     g3
                        # ex) [[0,30],[5,10],[15,20]]
                        # on a timeline scale, it would look like below:
                        #           0        5          10           15           20             30
                        # G1 <-- g1 enters ----------------------------------------------------g1 leaves->
                        # G2 <------------g2 enters----g2 leaves----------------------------------------->
                        # G3 <------------------------------------g3 enters----g3 leaves----------------->
                    # so as visualized above, we know right off the bat that a same room can be used for G2 and G3 where as G1 would need their own room since they take longer than the combined session of G2 and G3
                # if I want to order the entrance time and exit time in chronological order programatically:
                    # I can iterate on the entire intervals and get their start/end time and list them in a list
                        # ex) events = [ (0, 1), (30, -1), (5, 1), (10, -1), (15, 1), (20, -1) ]
                            # events[i][0] = event time
                            # events[i][1] = event type
                                # enter = 1
                                # exit = -1
                    # Then, I can take the events and sort the events - by event time
                        # ex) sorted_events = [ (0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (30, -1)]
                        # here, I could careless about sorting by event type, because I'm computing max_rooms AFTER updating active_rooms
                    # once I have the events sorted out, I can iterate on the sorted events and keep track of 2 states:
                        # 1. how many rooms are active at a each state in time
                            # assuming event = sorted_events[i]
                            # if event[1] (event type) == 1 (start)
                                # increment active_rooms by 1
                            # if event[1] (event type) == -1 (end)
                                # decrement active_rooms by 1
                            # Note:
                                # because I'm using 1 for start and -1 for end, I can take direct event type value and add to active_rooms
                        # 2. max_rooms at each given state in time
                            # at each iteration, update max_room with the currently active rooms vs max_room itself
        # pseudocode:
            # initailize events = [] (events[i][0] = eventTime, events[i][1] = eventType)
            # iterate on intervals (interval = intervals[i])
                # append (interval[0], 1) for entrance event
                # append (interval[1], -1) for exit event
            # sort the events by eventTime
            # intialize 2 variables to track:
                # active_rooms = 0
                # max_rooms = 0
            # iterate on events (sorted already): (event_time = event[0], event_type = event[1])
                # active_rooms += event_type
                # max_rooms = max(max_rooms, active_rooms)
            # return max_rooms"
        """

        # TC: O(n log n) / SC: O(n)
        events = []  # SC O(2n) -> O(n)
        for interval in intervals:  # TC O(n)
            events.append(tuple([interval[0], 1]))
            events.append(tuple([interval[1], -1]))

        events.sort()  # TC O(2(n log n)) -> O(n log n)

        active_rooms = max_rooms = 0
        for _, event_type in events:  # TC O(2n) -> O(n)
            active_rooms += event_type
            max_rooms = max(max_rooms, active_rooms)

        return max_rooms


solution = Solution()
start_time = time.time()
answer = solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
print("--- %s seconds ---" % (time.time() - start_time))
