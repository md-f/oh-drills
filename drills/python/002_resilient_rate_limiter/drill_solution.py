from collections import deque

def solution(requests: list[list[int]], W: int, D: int, capacity: int) -> list[int]:
    # user_id -> deque of (timestamp, weight)
    user_windows = {}
    # user_id -> current_sum_in_window
    user_sums = {}
    # user_id -> cool_down_until (exclusive)
    user_cool_down = {}
    
    results = []
    
    for ts, uid, w in requests:
        # Initialize user state if new
        if uid not in user_windows:
            user_windows[uid] = deque()
            user_sums[uid] = 0
            user_cool_down[uid] = -1
        
        # 1. Check Cool-down
        if ts < user_cool_down[uid]:
            results.append(0)
            continue
            
        # 2. Capacity Check (Clean old entries first)
        window_start = ts - W
        dq = user_windows[uid]
        while dq and dq[0][0] < window_start:
            old_ts, old_w = dq.popleft()
            user_sums[uid] -= old_w
            
        if user_sums[uid] + w <= capacity:
            # Accepted
            dq.append((ts, w))
            user_sums[uid] += w
            results.append(1)
        else:
            # Rejected due to capacity -> enter cool-down
            user_cool_down[uid] = ts + D
            results.append(0)
            
    return results

if __name__ == "__main__":
    # Example 1
    req1 = [[1, 1, 6], [2, 1, 5], [4, 1, 2], [8, 1, 3], [12, 1, 5]]
    W1, D1, Cap1 = 10, 5, 10
    expected1 = [1, 0, 0, 1, 1]
    result1 = solution(req1, W1, D1, Cap1)
    print(f"Example 1: {'PASS' if result1 == expected1 else f'FAIL (got {result1})'}")

    # Example 2
    req2 = [[1, 1, 10], [2, 1, 1], [11, 1, 1]]
    W2, D2, Cap2 = 5, 5, 10
    expected2 = [1, 0, 1]
    result2 = solution(req2, W2, D2, Cap2)
    print(f"Example 2: {'PASS' if result2 == expected2 else f'FAIL (got {result2})'}")

    # Edge Case: Multiple Users
    req3 = [[1, 1, 5], [1, 2, 5], [2, 1, 6], [2, 2, 6]]
    W3, D3, Cap3 = 10, 5, 10
    expected3 = [1, 1, 0, 0]
    result3 = solution(req3, W3, D3, Cap3)
    print(f"Edge Case (Multi-user): {'PASS' if result3 == expected3 else f'FAIL (got {result3})'}")

    # Edge Case: Capacity exactly met
    req4 = [[1, 1, 5], [2, 1, 5], [3, 1, 1]]
    W4, D4, Cap4 = 10, 5, 10
    expected4 = [1, 1, 0]
    result4 = solution(req4, W4, D4, Cap4)
    print(f"Edge Case (Exact Capacity): {'PASS' if result4 == expected4 else f'FAIL (got {result4})'}")
