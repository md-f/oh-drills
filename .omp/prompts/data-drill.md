description: Generate a Data Engineering drill (5m, 15m, or 45m) in a Marimo notebook

Act as a senior data engineer. Generate a data transformation task based on the requested duration and language (Python/Polars recommended) via $ARGUMENTS.

1. **Parse Input**:

- Identify Duration (5, 15, or 45).
- Assume Python if unspecified.

1. **Branching Logic**:

#### IF DURATION IS 5m (Warm-up Mode)

- **Goal**: Basic data cleaning/manipulation.
- **Content**: Simple filtering, column renaming, or basic type casting on a small dataset.
- **Output**: Print the problem statement (Statement, Signature, Examples) directly to the chat.
- **Constraint**: **DO NOT** create any directories or files.

#### IF DURATION IS 15m or 45m (Drill Mode)

- **Complexity Guide**:
  - **15m (Standard)**: Intermediate transformations: Joins, Group-bys, aggregations, or multi-column logic.
  - **45m (Deep)**: Complex ETL: Window functions, pivoting/unpivoting, handling schema evolution, or complex nested JSON parsing.
- **Indexing**:
  - List `drills/data` to find the highest 3-digit zero-padded index (e.g., `001`).
  - Determine next index (e.g., `002`).
- **Directory Creation**:
  - Create a new directory: `drills/data/<index>_<duration>m_<slug>/`.
- **File Writing**:
  - Write `drill.md` inside the folder containing the problem statement and requirements.
  - Write `drill.py` inside the folder. This must be a **Marimo notebook** formatted as a Python file.
    - It MUST include:
      1. `import marimo as mo` and `import polars as pl`.
      2. A cell that generates a representative mock dataset (e.g., a dictionary converted to a Polars DataFrame).
      3. A cell clearly marked with `# TASK` containing a placeholder function for the user to implement.
      4. A cell that uses `mo.ui.table(df)` or `print(df)` to inspect the results.

1. **Output Format (for all modes)**:

# Data Engineering Problem Statement

## Requirements & Schema

## Expected Output Example

DO NOT provide hints or solutions in the chat.
