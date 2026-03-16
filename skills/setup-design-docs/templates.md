# Document Templates

Reference templates for the setup-design-docs skill. Adapt all content to the actual project.

---

## DESIGN.md Template

```markdown
---
generated_by: cursor-agent (setup-design-docs skill)
title: <Project Name> — Living Design Document
status: stable
last_updated: YYYY-MM-DD
---

# <Project Name>

> One-line description of what the project does and who it's for.

## Project Identity

**<Project Name>** is [what it is]. It [what it does] for [who uses it].

[2-3 paragraphs covering: purpose, key workflows, scale/scope, and what makes it interesting.]

## Architecture Summary

[Description of the overall architecture pattern.]

\`\`\`mermaid
flowchart LR
    subgraph Infra["Infrastructure"]
        ServiceA["Service A<br/>Tech"]
        ServiceB["Service B<br/>Tech"]
    end
    ExternalA["External Dep"]
    ExternalB["External Dep"]

    ServiceA -->|protocol| ExternalA
    ServiceB -->|protocol| ExternalB
\`\`\`

| Service | Tech | Role |
|---------|------|------|
| **Service A** | Framework, Language | What it does |
| **Service B** | Framework, Language | What it does |

**Database**: [Description]
**Auth**: [Description]
**Storage**: [Description]

→ [System Overview](architecture/system-overview.md) · [Data Model](architecture/data-model.md) · [Deployment](architecture/deployment.md)

## Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Frontend | Framework | X.Y |
| API | Framework | X.Y |
| Database | Engine | X.Y |
| Auth | Provider | — |
| Deployment | Platform | — |

## Feature Index

### Core Features

| # | Feature | Summary | Doc |
|---|---------|---------|-----|
| 1 | **Feature Name** | Brief summary | [design.md](features/feature-name/design.md) |

### Supporting Features

| # | Feature | Summary | Doc |
|---|---------|---------|-----|
| N | **Feature Name** | Brief summary | [design.md](features/feature-name/design.md) |

## Document Map

| Document | Purpose |
|----------|---------|
| **Top Level** | |
| [DESIGN.md](DESIGN.md) | This file — project index and architecture summary |
| [CHANGELOG.md](CHANGELOG.md) | Auto-maintained documentation change log |
| **Architecture** | |
| [architecture/system-overview.md](architecture/system-overview.md) | System architecture and service responsibilities |
| **Services** | |
| [services/service-name.md](services/service-name.md) | Service description |
| **Features** | |
| [features/feature-name/design.md](features/feature-name/design.md) | Feature description |
| **UI** | |
| [ui/pages.md](ui/pages.md) | Route catalog |
| [ui/components.md](ui/components.md) | Component catalog |
```

---

## CHANGELOG.md Template

```markdown
---
generated_by: cursor-agent (setup-design-docs skill)
title: Documentation Changelog
last_updated: YYYY-MM-DD
---

# Documentation Changelog

> Auto-maintained log of documentation changes. Updated by the update-design-docs instructions at the end of each work session.

## YYYY-MM-DD

### Initial Documentation Creation

- **All documents**: Created complete living design documentation system (N documents)
- **DESIGN.md**: Project index with architecture summary, tech stack, and feature index
- **Update instructions**: Installed for automated documentation maintenance
```

---

## Architecture Doc Template

```markdown
---
generated_by: cursor-agent (setup-design-docs skill)
title: <Document Title>
status: stable
source_files:
  <category>:
    - <glob pattern>
    - <glob pattern>
  <category>:
    - <glob pattern>
depends_on: []
last_updated: YYYY-MM-DD
---

# <Document Title>

> One-line summary.

## Overview

[2-3 paragraphs explaining the architectural concept, pattern, or subsystem.]

## Diagram

\`\`\`mermaid
flowchart TD
    A["Component A"] --> B["Component B"]
    B --> C["Component C"]
\`\`\`

## Details

[Tables, specifics, configuration, etc. — varies by topic.]

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| [Topic] | [What was chosen] | [Why] |
```

### Specific Architecture Docs

**system-overview.md** — Include: architecture diagram, service responsibility matrix, communication patterns, shared resources.

**data-model.md** — Include: full ER diagram (Mermaid erDiagram), table catalog with columns/types, enum types, stored procedures/functions, key indexes.

**deployment.md** — Include: deployment topology diagram, container/service definitions, environment variables catalog, health check endpoints, CI/CD pipeline.

**auth-and-security.md** — Include: auth flow diagram, provider config, role definitions, permission matrix, route protection rules, token/session handling.

---

## Service Doc Template

Use for multi-service projects. One doc per deployable unit.

```markdown
---
generated_by: cursor-agent (setup-design-docs skill)
title: <Service Name> Service
status: stable
source_files:
  <category>:
    - <glob pattern matching service source files>
  <category>:
    - <glob pattern>
depends_on:
  - architecture/data-model
  - architecture/system-overview
last_updated: YYYY-MM-DD
---

# <Service Name> Service

> One-line description of the service's role.

## Overview

[What this service does, what framework it uses, key patterns it follows.]

## Architecture

\`\`\`mermaid
flowchart TD
    Entry["Entry Point"] --> Handler["Handler Layer"]
    Handler --> Business["Business Logic"]
    Business --> Data["Data Layer"]
\`\`\`

## Key Modules

| Module | Path | Responsibility |
|--------|------|---------------|
| Entry point | `path/to/main` | Application bootstrap |
| Handlers | `path/to/handlers/` | Request handling |

## Configuration

| Variable | Purpose | Default |
|----------|---------|---------|
| `ENV_VAR` | Description | `default` |

## API Surface

[Endpoints, message types, job types — whatever this service exposes or consumes.]
```

---

## Feature Doc Template

The most important template. Each feature doc links to source code via `source_files` globs.

```markdown
---
generated_by: cursor-agent (setup-design-docs skill)
title: <Feature Name>
status: stable
source_files:
  components:
    - <glob for UI components, e.g. src/components/feature-name/*>
  routers:
    - <glob for API routes, e.g. src/server/api/routers/feature.ts>
  handlers:
    - <glob for backend handlers, e.g. services/worker/handlers/feature/*>
  migrations:
    - <glob for DB migrations, e.g. db/migrations/*feature_name*>
depends_on:
  - architecture/data-model
  - features/other-feature
last_updated: YYYY-MM-DD
---

# <Feature Name>

> One-line summary of what this feature does.

## Overview

[2-3 paragraphs: what problem it solves, key workflows, scope.]

## Architecture

\`\`\`mermaid
flowchart TD
    subgraph UI["UI Layer"]
        CompA["Component A"]
        CompB["Component B"]
    end

    subgraph API["API Layer"]
        EndpointA["endpoint.action"]
    end

    UI --> API
    API --> DB["Database"]
\`\`\`

## Data Model

\`\`\`mermaid
erDiagram
    table_name {
        uuid id PK
        text name
        uuid related_id FK
        timestamptz created_at
    }
    related_table {
        uuid id PK
        text value
    }
    table_name ||--o{ related_table : "relationship"
\`\`\`

## Key Flows

### Primary Flow

\`\`\`mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant API
    participant DB

    User->>Frontend: Action
    Frontend->>API: Request
    API->>DB: Query
    DB-->>API: Result
    API-->>Frontend: Response
    Frontend-->>User: Updated UI
\`\`\`

## Configuration

[Environment variables, feature flags, settings relevant to this feature.]

## Related

- [Related Feature](../related-feature/design.md) — How they interact
- [Architecture Doc](../../architecture/relevant.md) — Relevant context
```

### source_files Categories

Use whatever categories make sense for the project. Common ones:

| Category | Example Globs | When to Use |
|----------|--------------|-------------|
| `components` | `src/components/feature/*` | React/Vue/Svelte components |
| `routers` | `src/api/routers/feature.ts` | tRPC, Express, FastAPI routers |
| `routes` | `src/app/feature/**/*` | Next.js/Remix file-based routes |
| `handlers` | `services/worker/handlers/*` | Backend job/event handlers |
| `controllers` | `src/controllers/feature.ts` | MVC controllers |
| `models` | `src/models/feature.ts` | ORM models |
| `migrations` | `db/migrations/*feature*` | Database migrations |
| `services` | `src/services/feature.ts` | Business logic services |
| `hooks` | `src/hooks/useFeature.ts` | React hooks |
| `lib` | `src/lib/feature/*` | Utility/library code |
| `config` | `config/feature.yaml` | Configuration files |
| `orchestrator` | `orchestrator/internal/feature/*` | Orchestration logic |
| `tests` | `tests/feature/*` | Test files |

### Sections to Skip

Not every feature needs every section. Skip sections that don't apply:

- **No database tables?** Skip "Data Model"
- **Simple feature?** Skip "Key Flows" or reduce to one flow
- **No config?** Skip "Configuration"

### Sections NOT to Include

Do NOT include these sections in feature docs — they duplicate what's already in code and go stale quickly:

- **API Contracts** — The `source_files.routers` frontmatter already points to the source. Agents and humans can read the router file directly.
- **UI Components** (tables listing component names/files) — The `source_files.components` frontmatter already points to the source. The Architecture mermaid diagram captures the structural relationships.

---

## UI Doc Templates

### pages.md

```markdown
---
generated_by: cursor-agent (setup-design-docs skill)
title: UI Pages
status: stable
source_files:
  app:
    - <glob for route files, e.g. src/app/**/*>
  middleware:
    - <glob for middleware, e.g. src/middleware.ts>
depends_on:
  - architecture/auth-and-security
  - services/webapp
last_updated: YYYY-MM-DD
---

# UI Pages

> All routes with descriptions, layout groups, and auth requirements.

## Overview

[Brief description of routing approach — file-based routing, router config, etc.]

## Layout Hierarchy

\`\`\`mermaid
flowchart TD
    Root["Root Layout"]
    Root --> GroupA["Group A Layout"]
    Root --> GroupB["Group B Layout"]
    GroupA --> PageA1["/route-a"]
    GroupB --> PageB1["/route-b"]
\`\`\`

## Route Catalog

| Route | Layout | Auth | Description |
|-------|--------|------|-------------|
| `/` | Main | Required | Dashboard |
| `/login` | Auth | Public | Login page |
```

### components.md

```markdown
---
generated_by: cursor-agent (setup-design-docs skill)
title: UI Components
status: stable
source_files:
  components:
    - <glob for all components, e.g. src/components/**/*>
depends_on:
  - services/webapp
last_updated: YYYY-MM-DD
---

# UI Components

> Component catalog with hierarchy, shared components, and design system usage.

## Overview

[Component library used, design system, key patterns.]

## Component Hierarchy

\`\`\`mermaid
flowchart TD
    App["App"] --> Layout["Layout"]
    Layout --> Nav["Navigation"]
    Layout --> Content["Content Area"]
    Content --> FeatureA["Feature A Components"]
    Content --> FeatureB["Feature B Components"]
\`\`\`

## Shared Components

| Component | Path | Description |
|-----------|------|-------------|
| `Layout` | `components/layout.tsx` | Main application layout |
| `Nav` | `components/nav.tsx` | Navigation sidebar/header |

## Design System

[UI library, theme, key design tokens, dark mode support, etc.]
```

---

## BUILD_ORDER.md Template (Optional)

Use for complex projects where recreation order matters.

```markdown
---
generated_by: cursor-agent (setup-design-docs skill)
title: Build Order
status: stable
last_updated: YYYY-MM-DD
---

# Build Order

> Phased dependency graph for recreating this project from scratch.

## Phase 1: Foundation
- [ ] Project scaffolding and tooling
- [ ] Database schema (core tables)
- [ ] Authentication

## Phase 2: Core Features
- [ ] Feature A (depends on: Phase 1)
- [ ] Feature B (depends on: Phase 1)

## Phase 3: Workflow Features
- [ ] Feature C (depends on: Feature A, Feature B)

[Continue with logical phases...]
```
