# Temporal Window Monitor

You are developing a real-time monitoring system for a high-frequency trading platform. The system receives a stream of log entries, where each entry represents an event occurring at a specific `timestamp`. Each event has an `element_id` and a `ttl` (Time To Live).

An event is considered **active** at a given `current_time` if it satisfies both of the following conditions:
1. **Not Expired**: The event has not reached its expiration time. That is, `current_time <= timestamp + ttl`.
2. **Within Window**: The event's `timestamp` falls within a sliding window of size `windowSize` relative to the `current_time`. That is, `timestamp >= current_time - windowSize`.

You are given a list of `logs`, where `logs[i] = [timestamp_i, element_id_i, ttl_i]`, and an integer `windowSize`. The logs are provided in non-decreasing order of `timestamp`.

Your task is to implement a function that, for each log entry in the stream, returns the number of **unique** `element_id`s that are currently **active** at the moment the `timestamp` of that log entry is processed.

## Function Signature

```python
def solution(logs: list[list[int]], windowSize: int) -> list[int]:
    """
    :param logs: A list of logs, where logs[i] = [timestamp, element_id, ttl]
    :param windowSize: The size of the sliding temporal window
    :return: A list of integers representing the count of unique active element_ids for each log entry
    """
```

## Constraints

- $1 \le \text{logs.length} \le 10^5$
- $0 \le \text{timestamp}_i \le 10^9$
- $\text{timestamp}_i \le \text{timestamp}_{i+1}$
- $1 \le \text{element\_id}_i \le 10^9$
- $1 \le \text{ttl}_i \le 10^9$
- $1 \le \text{windowSize} \le 10^9$
- **Time Complexity Target**: $O(N \log N)$ or $O(N)$
- **Space Complexity Target**: $O(N)$

## Examples

### Example 1
**Input**: 
`logs = [[1, 10, 5], [2, 20, 2], [5, 10, 5], [6, 30, 1]]`
`windowSize = 3`

**Output**: 
`[1, 2, 1, 2]`

**Explanation**:
- At `t=1`: Window `[1-3, 1] = [-2, 1]`. Active: `[1, 10, 5]` (Valid). Unique IDs: `{10}`. Count: 1.
- At `t=2`: Window `[2-3, 2] = [-1, 2]`. Active: `[1, 10, 5]` (Valid), `[2, 20, 2]` (Valid). Unique IDs: `{10, 20}`. Count: 2.
- At `t=5`: Window `[5-3, 5] = [2, 5]`. 
    - `[1, 10, 5]` is out of window (`1 < 2`).
    - `[2, 20, 2]` is expired (`2 + 2 < 5`).
    - `[5, 10, 5]` is valid. Unique IDs: `{10}`. Count: 1.
- At `t=6`: Window `[6-3, 6] = [3, 6]`.
    - `[5, 10, 5]` is valid.
    - `[6, 30, 1]` is valid. Unique IDs: `{10, 30}`. Count: 2.

### Example 2
**Input**: 
`logs = [[1, 1, 10], [10, 1, 10]]`
`windowSize = 5`

**Output**: 
`[1, 1]`

**Explanation**:
- At `t=1`: Active: `{1}`. Count: 1.
- At `t=10`: Window `[5, 10]`. The entry at `t=1` is out of window (`1 < 5`). The entry at `t=10` is valid. Unique IDs: `{1}`. Count: 1.

### Example 3
**Input**: 
`logs = [[1, 5, 1], [2, 5, 1], [3, 5, 1]]`
`windowSize = 10`

**Output**: 
`[1, 1, 1]`

**Explanation**:
- At `t=1`: `{5}`. Count 1.
- At `t=2`: `[1, 5, 1]` expired (`1+1 < 2`). `[2, 5, 1]` valid. Count 1.
- At `t=3`: `[2, 5, 1]` expired (`2+1 < 3`). `[3, 5, 1]` valid. Count 1.
