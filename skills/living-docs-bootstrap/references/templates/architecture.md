# Architecture Doc Template

Use this for `system-overview.md`, `data-model.md`, `deployment.md`, and
`auth-and-security.md`.

```markdown
---
generated_by: codex (living-docs-bootstrap skill)
title: <Document Title>
status: stable
source_files:
  <area>:
    - <glob>
depends_on: []
last_updated: YYYY-MM-DD
---

# <Document Title>

> One-line summary.

## Overview

[Explain the architectural concern and why it exists.]

## Diagram

\`\`\`mermaid
flowchart TD
    A["Component A"] --> B["Component B"]
\`\`\`

## Details

[Use tables for responsibilities, resources, or flows.]

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| <topic> | <choice> | <why> |
```
