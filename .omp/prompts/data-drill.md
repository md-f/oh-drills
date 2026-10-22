description: Generate a Data Engineering drill (5m, 15m, or 45m) in a Marimo notebook

Act as a senior data engineer. Generate a data transformation task based on the requested duration via $ARGUMENTS.

1. **Parse Input**:

- Identify Duration (5, 15, or 45).

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
  - Write `drill.py` inside the folder. This must be a **Marimo notebook** formatted as a Python file using `@mo.cell` decorators.
  - Structure Blueprint:

    ```python
    import marimo
    app = marimo.App(width="full")

    @app.cell
    def _():
        import marimo as mo
        import polars as pl
        return mo, pl

    @app.cell
    def _(mo, pl):
        # Generate a representative mock dataset
        df = pl.DataFrame(...)
        return df

    @app.cell
    def _(mo, pl):
        # TASK: Implement the transformation logic here
        def solve(df: pl.DataFrame) -> pl.DataFrame:
            return df
        return solve

    @app.cell
    def _(mo, pl):
        # To inspect the results, call the solve function:
        # mo.ui.table(solve(df))
        pass
    ```

1. **Output Format (for all modes)**:

# Data Engineering Problem Statement

## Requirements & Schema

## Expected Output Example

DO NOT provide hints or solutions in the chat.
