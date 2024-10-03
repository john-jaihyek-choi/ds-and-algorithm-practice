from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time
import math

# Note:
    # timestamps are STRICTLY IN INCREASING ORDER
    # time stamp is of type "int"
    # set method:
        # parameters:
            # key str: key string
            # value str: value of the key
            # timestamp int: INTEGER indicating the time that the key is being set
    # get method:
        # parameters:
            # key str: key string trying to get
            # timestamp int: INTEGER indicating the time that the key was being set
                # if prev_timestamp <= timestamp return prev_timestamp
                    # then return the key
                # if prev_timestamp > timestamp or there's no key at all
                    # return empty string
        

# Brainstorm 1:
    # the goal of the set method is to simply store the key value pair at a given time:
        # ex) each key/value pair looks like...
        # {            0           1       2   
        #   "key": ["value 1", "value 2", ....]
        # }
        # Given the above, we'll use dictionary to store the people
    #  get method => get the value at a given timestamp for the given key
        # 2 search criteria:
            # key (string representing the person)
            # timestamp (index of an array)
        # array indexing logic:
            # linear time ( O(1) ):

# Pesudocode (INVALID DUE TO EDGE CASE):
    # initialize a people variable in the constructor with an empty defaultdict with default value of [] (people)
    # set method:
        # append value to the people[key] property
    # get method:
        # if timestamp >= len(self.people[key]) - 1
            # return value at self.people[key][-1]
        # return get self.people[key][timestamp]

class TimeMap1:
    def __init__(self):
        self.people = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.people[key].append(value)
        return 

    def get(self, key: str, timestamp: int) -> str:
        if timestamp >= len(self.people[key]) - 1:
            return self.people[key][-1]
        
        return self.people[key][timestamp]
    
# Solution 1:
    # the goal of the set method is to simply store the key value pair at a given time:
        # ex) each key/value pair looks like...
        # {            
        #   "key": [ [value, timestamp] ]
        # }
        # Given the above, we'll use dictionary to store the people, and an array of arrays to store the value and timestamp
    #  get method => get the value at a given timestamp for the given key
        # 2 search criteria:
            # key (string representing the person)
            # timestamp (index of an array)
        # if prev_timestamp <= timestamp:
            # return prev_timestamp

class TimeMap1:
    def __init__(self):
        self.people = defaultdict(list[str, int])
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.people[key].append([value, timestamp])
        return 

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.people[key]

        l, r = 0, len(timestamps) - 1
        latest=''
        while l <= r:
            m = (r + l) // 2
            val, time = timestamps[m]

            if time <= timestamp:
                latest = val

            if time == timestamp:
                return val
            elif time < timestamp:
                l = m + 1
            else:
                r = m - 1

        return latest

# Solution 2: Same concept, less code
class TimeMap2:
    def __init__(self):
        self.people = defaultdict(list[str, int])
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.people[key].append([value, timestamp])
        return 

    def get(self, key: str, timestamp: int) -> str:
        res, timestamps = "", self.people[key]

        l, r = 0, len(timestamps) - 1
        while l <= r:
            m = (r + l) // 2
            val, time = timestamps[m]

            if time <= timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1

        return res

timeMap = TimeMap1()
print(
None,
timeMap.set("test", "one", 10),
timeMap.set("test", "two", 20),
timeMap.set("test", "three", 30),
timeMap.get("test", 15),
timeMap.get("test", 25),          
timeMap.get("test", 35)
)