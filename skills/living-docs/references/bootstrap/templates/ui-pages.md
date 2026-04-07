# UI Pages Template

```markdown
---
generated_by: codex (living-docs skill)
title: UI Pages
status: stable
source_files:
  routes:
    - <glob>
depends_on:
  - architecture/system-overview
last_updated: YYYY-MM-DD
---

# UI Pages

> Route catalog and page responsibilities.

## Overview

[Describe routing strategy and layout boundaries.]

## Layout Hierarchy

\`\`\`mermaid
flowchart TD
    Root["Root"] --> Public["Public"]
    Root --> Auth["Authenticated"]
\`\`\`

## Route Catalog

| Route | File | Purpose | Access |
|-------|------|---------|--------|
| `/` | `<path>` | <purpose> | Public |
```
