# 🔗 Chains

## Overview

This folder contains my practice code for understanding Chains in LangChain.

Chains allow multiple components to work together by connecting prompts, language models, parsers, and other operations into a single workflow. Instead of executing one isolated task, chains enable the output of one step to become the input for the next.

Through these examples, I explored different ways of building sequential, parallel, and conditional workflows using LangChain.

---

## Files Included

- `main.py` – Entry point for running the examples
- `simple_chain.py` – Basic chain implementation
- `sequential_chain.py` – Executing multiple steps sequentially
- `parallel_chain.py` – Running independent tasks in parallel
- `conditional_chain.py` – Executing different chains based on conditions

---

## Concepts Practiced

- Simple Chains
- Sequential Chains
- Parallel Chains
- Conditional Chains
- Runnable Pipelines
- Multi-step Workflows

---

## What I Learned

- How LangChain connects multiple components into a single workflow.
- How the output of one step becomes the input for the next.
- When to use sequential workflows versus parallel execution.
- How conditional logic enables dynamic execution paths.
- Why chains improve code modularity and make AI applications easier to maintain.
