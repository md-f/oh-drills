# oh-drills

> **Note:** This repository provides specialized skills designed for use with the **oh-my-pi** LLM harness.

## Overview

`oh-drills` provides the automated generation of training drills designed to build "coding muscle memory" through high-frequency, timed
practice. Instead of solving massive, infrequent problems, this project focuses on mastering specific algorithmic patterns and data
transformation logic through disciplined, short-burst drills.

## Core Pillars

- **Algorithmic Fluency**: Rapid-fire logic and complexity training (Python/TypeScript).
- **Data Engineering**: Pipeline and transformation practice using Marimo notebooks (Python/Polars).
- **Time-Boxed Training**: Structured sessions in 5m, 15m, or 45m increments to match your cognitive load and goals.

## 1. Algorithmic Drills (`/algo-drill`)

Focuses on computational logic (Python/TypeScript) with durations of 5m (warm-up), 15m (standard), or 45m (deep).

```text
┌────────────────────────────────────────────────────────────────────────┐
│  Step 1: Trigger Algorithmic Drill                                     │
│  You type: /algo-drill 15 python                                       │
│                                                                        │
│  The LLM generates a problem and creates a new directory:              │
│  `drills/python/00X_15m_topic/` containing `drill.md` and              │
│  `drill_solution.py`.                                                  │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Step 2: 15-Minute Local Coding                                        │
│  Open the solution file in your editor and solve it.                   │
│  Run the solution to verify your logic.                                │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Step 3: Trigger Instant Review                                        │
│  You type: /review drills/python/00X_15m_topic/drill_solution.py       │
│                                                                        │
│  The LLM reviews complexity, edge cases, and provides an optimized     │
│  idiomatic version.                                                    │
└────────────────────────────────────────────────────────────────────────┘
```

## 2. Data Drills (`/data-drill`)

Focuses on data engineering (Marimo/Polars) using 5m (warm-up), 15m (standard), or 45m (deep) time-boxes.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  Step 1: Trigger Data Drill                                            │
│  You type: /data-drill 15                                              │
│                                                                        │
│  The LLM generates a problem and creates a new directory:              │
│  `drills/data/00X_15m_topic/` containing `drill.md` and                │
│  a Marimo notebook `drill.py`.                                         │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Step 2: Interactive Notebook Coding                                   │
│  Open `drill.py` in Marimo.                                            │
│  Fill in the `# TASK` cell and run the notebook to see results.        │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│  Step 3: Trigger Instant Review                                        │
│  You type: /review drills/data/00X_15m_topic/drill.py                  │
│                                                                        │
│  The LLM reviews your transformation logic and schema handling.        │
└────────────────────────────────────────────────────────────────────────┘
```

## Tips

### Non-LLM Local Timer

To avoid consuming tokens for a countdown, you can ask the LLM to trigger a background bash alarm when generating a drill:

```bash
# Non-blocking terminal alarm (e.g., 15 minutes)
(sleep 900 && notify-send "Drill Alert" "Timer is UP! Time to /review") &
```

### TypeScript Environment

If running TypeScript drills via `bun`:

```bash
# Setup types and dependencies
bun add -d typescript @types/node
bun add <my-library> 
# Run a file
bun run drills/ts/001/drill_solution.ts 
```
