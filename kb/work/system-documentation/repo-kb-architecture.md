# Repo KB architecture

This repo is one concrete knowledge base built with commonplace. It also contains the framework source and scaffold assets that get shipped elsewhere.

That combination is local documentation, not shipped reference documentation. The generic shipped architecture lives in `kb/reference/architecture.md`; this note only explains the extra layer present in the source repository itself.

## What is special about this repo

- `kb/notes/` is the methodology library for commonplace itself.
- `src/commonplace/` and `skills/` are the implementation sources for the commands and skills the framework ships.
- `kb/reference/` documents the shipped commonplace system even though those docs live inside the same repository that builds it.

## Practical consequence

Most installed projects see only the shipped KB surface under `kb/`. This repository sees both layers at once:

- the KB surface under `kb/`
- the framework source under `src/commonplace/` and `skills/`
