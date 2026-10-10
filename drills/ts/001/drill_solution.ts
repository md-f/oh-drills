interface Operation {
    type: 'ADD' | 'QUERY';
    timestamp: number;
    userId?: string;
    windowSize?: number;
}

/**
 * Implementation of the Windowed Activity Tracker.
 * Expected Complexity: O(N log N)
 */
function solve(operations: Operation[]): number[] {
    // TODO: Implement the logic
    return [];
}

// --- Test Runner ---

function runTest(name: string, ops: Operation[], expected: number[]) {
    const result = solve(ops);
    const passed = JSON.stringify(result) === JSON.stringify(expected);
    if (passed) {
        console.log(`✅ ${name} PASSED`);
    } else {
        console.error(`❌ ${name} FAILED`);
        console.error(`   Expected: ${JSON.stringify(expected)}`);
        console.error(`   Got:      ${JSON.stringify(result)}`);
    }
}

const testCases: { name: string; ops: Operation[]; expected: number[] }[] = [
    {
        name: "Example 1",
        ops: [
            { type: 'ADD', timestamp: 10, userId: 'user1' },
            { type: 'ADD', timestamp: 20, userId: 'user2' },
            { type: 'QUERY', timestamp: 25, windowSize: 5 },
            { type: 'QUERY', timestamp: 25, windowSize: 15 },
            { type: 'ADD', timestamp: 30, userId: 'user1' },
            { type: 'QUERY', timestamp: 35, windowSize: 10 }
        ],
        expected: [1, 2, 1]
    },
    {
        name: "Example 2",
        ops: [
            { type: 'ADD', timestamp: 5, userId: 'A' },
            { type: 'ADD', timestamp: 5, userId: 'B' },
            { type: 'QUERY', timestamp: 5, windowSize: 0 },
            { type: 'ADD', timestamp: 10, userId: 'A' },
            { type: 'QUERY', timestamp: 10, windowSize: 2 }
        ],
        expected: [2, 1]
    },
    {
        name: "Edge Case: Overlapping timestamps",
        ops: [
            { type: 'ADD', timestamp: 10, userId: 'user1' },
            { type: 'ADD', timestamp: 10, userId: 'user1' },
            { type: 'QUERY', timestamp: 10, windowSize: 0 }
        ],
        expected: [1]
    }
];

for (const tc of testCases) {
    runTest(tc.name, tc.ops, tc.expected);
}
