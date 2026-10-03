# Autonomous Multi-Agent Task Orchestrator

An autonomous multi-agent system that breaks complex goals into smaller tasks, assigns them to specialized agents, manages dependencies, handles failures and retries, persists task state, and recovers incomplete tasks after a restart.

## Project Overview

The Autonomous Multi-Agent Task Orchestrator demonstrates how multiple specialized agents can collaborate to solve complex tasks through a structured execution workflow.

Instead of executing a task as one large operation, the system:

1. Receives a user goal
2. Creates an execution plan
3. Breaks the goal into subtasks
4. Assigns subtasks to specialized agents
5. Manages task dependencies
6. Passes results between agents
7. Handles failures and retries
8. Verifies task results
9. Synthesizes the final result
10. Persists task state
11. Recovers incomplete tasks after a restart

## Architecture

```text
                         User Goal
                             |
                             v
                      +--------------+
                      |    Planner   |
                      +------+-------+
                             |
                             v
                      +--------------+
                      | Task Manager |
                      +------+-------+
                             |
             +---------------+---------------+
             |               |               |
             v               v               v
        +---------+     +---------+     +-------------+
        | Research|     | Analysis|     | Verification|
        |  Agent  |     |  Agent  |     |    Agent    |
        +----+----+     +----+----+     +------+------+
             |               |                  |
             +---------------+------------------+
                             |
                             v
                      +--------------+
                      |   Synthesis  |
                      |     Agent    |
                      +------+-------+
                             |
                             v
                       Final Result


                 +-------------------------+
                 | Memory / Persistent     |
                 | State                   |
                 |                         |
                 | - Results               |
                 | - Task Status           |
                 | - Attempts              |
                 | - Dependencies          |
                 | - Execution History     |
                 +-------------------------+