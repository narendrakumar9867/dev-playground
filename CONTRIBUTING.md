# Contributing Guide

Thanks for improving this repository. Keep changes small, focused, and aligned with the folder structure.

## Before You Start

- Check whether your change belongs in an existing topic folder.
- If you are adding a new example, place it in the most relevant top-level folder.
- Each example folder should have its own `requirements.txt` and `README.md`.
- There is no root-level `requirements.txt` — every example manages its own dependencies.

## Suggested Workflow

1. Create a new branch.
2. Make changes inside the relevant folder.
3. Add or update the folder-level `README.md` if behavior changes.
4. Verify the folder runs correctly if it is a runnable example.
5. Open a pull request with a short summary of what changed.

## Folder Rules

- Keep topic-specific code inside the matching folder.
- Do not mix unrelated experiments in the same directory.
- Each runnable example must have its own `requirements.txt`.
- Each example folder should have a short `README.md` explaining what it does and how to run it.
- Do not add a root-level `requirements.txt` — dependencies stay inside each example folder.

## Good Contributions

- new examples or demos
- bug fixes
- clearer documentation
- improved explanations or architecture notes

## Pull Request Tips

- Explain what the example does.
- Mention how to run or verify it.
- Link to any relevant issue or context if available.