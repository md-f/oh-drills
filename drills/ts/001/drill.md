# Problem Statement & Constraints

You are building a real-time monitoring system for a high-traffic website. The system receives a stream of user activity logs. Each log consists of a `timestamp` and a `userId`. You need to implement a tracker that can answer queries about the number of unique users active within a specific sliding time window.

The tracker supports two operations:

1. `ADD(timestamp, userId)`: A user performs an action at a specific `timestamp`. 
   - The `timestamp` values in `ADD` operations are provided in non-decreasing order.
2. `QUERY(timestamp, windowSize)`: Calculate the number of **unique** users who performed at least one action in the time interval `[timestamp - windowSize, timestamp]`.

### Constraints

- $1 \le \text{number of operations} \le 10^5$
- $0 \le \text{timestamp} \le 10^9$
- $1 \le \text{windowSize} \le 10^9$
- The `timestamp` in `ADD` operations is monotonically non-decreasing.
- The `timestamp` in `QUERY` operations is also monotonically non-decreasing.
- **Time Limit**: 2.0s
- **Memory Limit**: 256MB
- **Target Complexity**: $O(N \log N)$ total.

## Function Signature

```typescript
interface Operation {
    type: 'ADD' | 'QUERY';
    timestamp: number;
    userId?: string;
    windowSize?: number;
}

function solve(operations: Operation[]): number[]
```

## Examples

### Example 1
**Input:**
```typescript
const ops = [
    { type: 'ADD', timestamp: 10, userId: 'user1' },
    { type: 'ADD', timestamp: 20, userId: 'user2' },
    { type: 'QUERY', timestamp: 25, windowSize: 5 }, // Window [20, 25]
    { type: 'QUERY', timestamp: 25, windowSize: 15 }, // Window [10, 25]
    { type: 'ADD', timestamp: 30, userId: 'user1' },
    { type: 'QUERY', timestamp: 35, windowSize: 10 } // Window [25, 35]
];
```
**Output:**
`[1, 2, 1]`

*Explanation:*
- `QUERY(25, 5)`: Only `user2` (at $t=20$) is in $[20, 25]$. Count: 1.
- `QUERY(25, 15)`: `user1` (at $t=10$) and `user2` (at $t=20$) are in $[10, 25]$. Count: 2.
- `QUERY(35, 10)`: Only `user1` (at $t=30$) is in $[25, 35]$. Count: 1.

### Example 2
**Input:**
```typescript
const ops = [
    { type: 'ADD', timestamp: 5, userId: 'A' },
    { type: 'ADD', timestamp: 5, userId: 'B' },
    { type: 'QUERY', timestamp: 5, windowSize: 0 }, // Window [5, 5]
    { type: 'ADD', timestamp: 10, userId: 'A' },
    { type: 'QUERY', timestamp: 10, windowSize: 2 } // Window [8, 10]
];
```
**Output:**
`[2, 1]`

*Explanation:*
- `QUERY(5, 0)`: Both 'A' and 'B' are at $t=5$. Count: 2.
- `QUERY(10, 2)`: Only 'A' (at $t=10$) is in $[8, 10]$. Count: 1.
