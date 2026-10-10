from collections import deque, namedtuple
from typing import List

def solution(logs: List[List[int]], windowSize: int) -> List[int]:
    """
    :param logs: A list of logs, where logs[i] = [timestamp, element_id, ttl]
    :param windowSize: The size of the sliding temporal window
    :return: A list of integers representing the count of unique active element_ids for each log entry
    """
    dq = deque()
    active_counter = {}
    out = []
    Event = namedtuple('Event', ('timestamp', 'id', 'ttl'))

    for cur_time, event_id, ttl in logs:
        event = Event(cur_time, event_id, ttl)
        dq.append(event)
        active_counter[event_id] = active_counter.get(event_id, 0) + 1 

        while dq:
            earliest = dq[0]
 
            if (earliest.timestamp < cur_time - windowSize) or (earliest.timestamp + earliest.ttl < cur_time):
                dq.popleft()
                active_counter[earliest.id] -= 1
                if active_counter[earliest.id] == 0:
                    del active_counter[earliest.id]
            else:
                break

        out.append(len(active_counter))

    return out




def run_tests():
    test_cases = [
        {
            "name": "Example 1",
            "logs": [[1, 10, 5], [2, 20, 2], [5, 10, 5], [6, 30, 1]],
            "windowSize": 3,
            "expected": [1, 2, 1, 2]
        },
        {
            "name": "Example 2",
            "logs": [[1, 1, 10], [10, 1, 10]],
            "windowSize": 5,
            "expected": [1, 1]
        },
        {
            "name": "Example 3",
            "logs": [[1, 5, 1], [2, 5, 1], [3, 5, 1]],
            "windowSize": 10,
            "expected": [1, 1, 1]
        },
        {
            "name": "All Expired",
            "logs": [[1, 10, 1], [5, 20, 1], [10, 30, 1]],
            "windowSize": 10,
            "expected": [1, 1, 1]
        }
    ]

    for tc in test_cases:
        result = solution(tc["logs"], tc["windowSize"])
        if result == tc["expected"]:
            print(f"✅ {tc['name']} passed!")
        else:
            print(f"❌ {tc['name']} failed! Expected {tc['expected']}, got {result}")

if __name__ == "__main__":
    run_tests()
