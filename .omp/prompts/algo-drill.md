description: Generate a CodeSignal drill (5m, 15m, or 45m)

Act as a strict technical interviewer. Generate a single CodeSignal-style problem based on the requested duration and language ($ARGUMENTS).

1. **Parse Input**:

- Identify Duration (5, 15, or 45).
- Determine if $ARGUMENTS is Python or TypeScript. **If unspecified, assume Python**.

1. **Branching Logic**:

#### IF DURATION IS 5m (Warm-up Mode)

- **Goal**: Rapid-fire syntax and basic logic check.
- **Content**: Completely random, simple array/string manipulation, or single-pass logic. No complex state.
- **Output**: Print the problem statement (Statement, Signature, Examples) directly to the chat.
- **Constraint**: **DO NOT** create any directories or files. This is an ephemeral warm-up.

#### IF DURATION IS 15m or 45m (Drill Mode)

- **Complexity Guide**:
  - **15m (Standard)**: Stateful structures (TTL, buffers), sliding windows, pattern matching, or prefix sums.
  - **45m (Deep)**: Algorithmic depth, advanced data structures (Heaps, Trees), multi-stage logic, or complex simulations.
- **Indexing**:
  - List `drills/<lang>/` to find the highest 3-digit zero-padded index (e.g., `001`).
  - Determine next index (e.g., `002`).
- **Directory Creation**:
  - Create a new directory: `drills/<lang>/<index>_<duration>m_<short_name>/` (where `short_name` is a slug of the topic).
- **File Writing**:
  - Write `drill.md` inside that directory containing the full problem text.
  - Write `drill_solution.<ext>` inside that directory containing the function signature and a main execution block running the example cases.

1. **Output Format (for all modes)**:

# Problem Statement & Constraints

## Function Signature

## Examples

DO NOT provide hints or solutions in the chat.
