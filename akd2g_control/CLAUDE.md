# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Code Organization

- No long files. If a file grows beyond ~150 lines or handles more than one responsibility, split it.
- Each file does one job: types, queries, mappers, fetch functions, and components all live in separate files.
- Group related files into folders. If a component has sub-components, extract them rather than stacking them in one file.
- New components, hooks, constants, and utilities each get their own file in the appropriate folder.
- Keep code lean — no unused abstractions, no premature generalization. Be flexible on adding folders to organize code. Yet keep it optimal.
- lib/mock-data/ — mock data for testing and development, if you need to add a new product, collection, or review use this folder.