# Contributing Guide

Thanks for improving this repository. Keep changes small, focused, and aligned with the folder structure.

## Before You Start

- Check whether your change belongs in an existing topic folder.
- If you are adding a new example, place it in the most relevant top-level folder.
- If the change is a Python app, add or update a folder-level `requirements.txt`.

## Suggested Workflow

1. Create a new branch.
2. Make changes inside the relevant folder.
3. Add or update documentation if behavior changes.
4. Verify the folder runs correctly if it is a runnable example.
5. Open a pull request with a short summary of what changed.

## Folder Rules

- Keep topic-specific code inside the matching folder.
- Do not mix unrelated experiments in the same directory.
- Prefer local dependency files over a single root dependency list.
- Include a short README or notes file when a folder becomes non-trivial.

## Good Contributions

- new examples or demos
- bug fixes
- clearer documentation
- folder-specific setup files
- improved explanations or architecture notes

## Pull Request Tips

- Explain what the folder does.
- Mention how to run or verify it.
- Link to any relevant issue or context if available.