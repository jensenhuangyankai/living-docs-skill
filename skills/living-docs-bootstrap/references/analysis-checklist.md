# Analysis Checklist

Read only enough of the repository to answer these questions before creating
docs:

## Project Identity

- What is the project?
- Who uses it?
- What core workflow does it enable?

## Services

- List deployable services or packages.
- Record language, framework, entry point, and main responsibility.

## Features

- Identify major feature areas from routes, handlers, pages, or modules.
- Capture the source file globs each feature should own.

## Data Model

- Find migrations, schemas, ORM models, or contracts.
- Record main entities and relationships.

## Tech Stack

- Read package manager files, lockfiles, Docker files, CI config, and env
  examples.
- Record notable versions when they are easy to obtain.

## Cross-Cutting Concerns

- Auth and authorization
- Background jobs or queues
- Deploy and runtime topology
- Existing docs worth preserving

## Minimum Output

Before writing docs, build a working summary of:

- project name and one-line purpose
- services and responsibilities
- major features and source globs
- data model approach
- deployment and auth notes
