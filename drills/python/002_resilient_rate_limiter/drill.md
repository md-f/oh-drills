# Resilient Rate Limiter

You are designing a rate-limiting component for a distributed system. The limiter must track user activity within a sliding time window and enforce a "cool-down" period if a user exceeds their allowed capacity.

## Problem Statement

Each user has a maximum `capacity` (total weight allowed within a window of size `W`) and a `cool_down_duration` (`D`). 

The system processes a sequence of `execute` requests. Each request is defined as `[timestamp, user_id, weight]`. The timestamps are provided in non-decreasing order.

For each request, determine if it is **accepted** or **rejected**:

1.  **Cool-down Check**: If the user is currently in a **cool-down period**, the request is **rejected**. A cool-down period starts at the timestamp of a request that was rejected due to capacity exhaustion and lasts for `D` seconds. A user is in cool-down at `timestamp` if `timestamp < cool_down_until`. 
    *   *Note*: A request rejected because the user is already in cool-down does **not** extend the cool-down period.
2.  **Capacity Check**: If the user is **not** in cool-down, calculate the total weight of all **accepted** requests for that user in the sliding window `[timestamp - W, timestamp]`.
    *   If `current_window_weight + weight <= capacity`, the request is **accepted**. The weight is added to the user's windowed total.
    *   If `current_window_weight + weight > capacity`, the request is **rejected**, and the user enters a cool-down period. The cool-down period lasts from `timestamp` until `timestamp + D`. (The user is considered in cool-down at any time `t` where `timestamp <= t < timestamp + D`).

Return a list of `1` (accepted) and `0` (rejected) for all requests.

## Function Signature

```python
def solution(requests: list[list[int]], W: int, D: int, capacity: int) -> list[int]:
    """
    :param requests: A list of [timestamp, user_id, weight]
    :param W: The sliding window size
    :param D: The cool-down duration
    :param capacity: The maximum weight capacity per window
    :return: A list of 1s and 0s representing acceptance
    """
```

## Constraints

- $1 \le \text{requests.length} \le 10^5$
- $0 \le \text{timestamp}_i \le 10^9$
- $\text{timestamp}_i \le \text{timestamp}_{i+1}$
- $1 \le \text{user\_id}_i \le 10^9$
- $1 \le \text{weight}_i \le 10^9$
- $1 \le W, D, \text{capacity} \le 10^9$
- **Time Complexity Target**: $O(N)$
- **Space Complexity Target**: $O(N)$

## Examples

### Example 1

**Input**:
`requests = [[1, 1, 6], [2, 1, 5], [4, 1, 2], [8, 1, 3], [12, 1, 5]]`
`W = 10, D = 5, capacity = 10`

**Output**:
`[1, 0, 0, 1, 1]`

**Explanation**:
- `t=1, user=1, w=6`: Not in cool-down. Window `[1-10, 1] = [-9, 1]`. Window weight = 0. `0 + 6 <= 10`. **Accepted**.
- `t=2, user=1, w=5`: Not in cool-down. Window `[2-10, 2] = [-8, 2]`. Window weight = 6. `6 + 5 = 11 > 10`. **Rejected**. User enters cool-down until `2 + 5 = 7`.
- `t=4, user=1, w=2`: User is in cool-down (`4 < 7`). **Rejected**.
- `t=8, user=1, w=3`: Not in cool-down (`8 >= 7`). Window `[8-10, 8] = [-2, 8]`. Window weight (accepted at `t=1`) = 6. `6 + 3 = 9 <= 10`. **Accepted**.
- `t=12, user=1, w=5`: Not in cool-down. Window `[12-10, 12] = [2, 12]`. The `t=1` request is outside window (`1 < 2`). Window weight = 3 (from `t=8`). `3 + 5 = 8 <= 10`. **Accepted**.

### Example 2

**Input**:
`requests = [[1, 1, 10], [2, 1, 1], [11, 1, 1]]`
`W = 5, D = 5, capacity = 10`

**Output**:
`[1, 0, 1]`

**Explanation**:
- `t=1`: `0 + 10 <= 10`. **Accepted**.
- `t=2`: `10 + 1 > 10`. **Rejected**. Cool-down until `2 + 5 = 7`.
- `t=11`: Not in cool-down. Window `[11-5, 11] = [6, 11]`. Weight at `t=1` is out of window. Window weight = 0. `0 + 1 <= 10`. **Accepted**.
