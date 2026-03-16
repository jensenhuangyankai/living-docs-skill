---
name: setup-design-docs
description: Bootstrap a self-documenting living design documentation system for any repository. Creates docs/ folder structure, DESIGN.md index, feature/architecture/service templates with YAML frontmatter source_files linking, CHANGELOG.md, and an update instruction file for automated maintenance. Use when the user asks to set up design docs, create a documentation system, or bootstrap living documentation.
---

# Setup Design Documentation System

## Description

Bootstraps a complete living design documentation system in any repository. The system creates structured markdown docs with YAML frontmatter that link back to source code via glob patterns, enabling automated documentation updates.

This skill is **harness-agnostic** — the instructions work in any AI coding assistant (Cursor, Claude Code, Windsurf, Aider, etc.). Only the final installation path for the update instruction file varies by environment.

## When to Use

- Setting up documentation for a new or existing project
- User asks to "set up design docs", "create documentation system", or "bootstrap living docs"
- Migrating a project to self-documenting architecture

## Instructions

Follow these steps in order. Adapt all content to the actual project — never copy project-specific details from templates verbatim.

### Step 1: Analyze the Project

Before creating any files, you must deeply understand the project. **This is a large exploration task — use whatever parallel exploration capability your environment provides** (subagents, parallel tool calls, background tasks, etc.) to investigate the codebase thoroughly before writing anything.

Your exploration must cover all of the following areas. If your environment supports parallel execution, investigate independent areas concurrently (e.g. frontend, backend, and infrastructure in parallel):

1. **Project identity** — what is this project, what does it do, who is it for?
2. **Services** — list all deployable services (check docker-compose.yml, top-level directories with their own Dockerfile/package.json/go.mod/etc.). For each: name, language/framework, role, entry point, key modules with file paths.
3. **Features** — identify all major feature areas by scanning API routers, UI component directories, handler folders, route definitions. For each: name, summary, relevant source file glob patterns.
4. **Data model** — find database migrations, schemas, ORM models. List all tables with columns, relationships, enums, and stored procedures.
5. **Tech stack** — languages, frameworks, databases, auth providers, deployment tools with versions (read package.json, go.mod, requirements.txt, etc.).
6. **UI structure** — if there's a web frontend: routing approach, all pages/routes, component library, shared components.
7. **Auth approach** — how authentication and authorization work.
8. **Deployment** — Docker, CI/CD, environment configuration.
9. **Existing docs** — check if there are already docs that should be integrated rather than overwritten.

Read all config files (package.json, go.mod, docker-compose.yml, .env.example, Dockerfile, etc.), explore all top-level directories and their subdirectories, and produce a comprehensive structured analysis with exact file paths and glob patterns.

After exploration, collect the results into a mental model of:
- Project name and one-line description
- Services (name, tech, role)
- Features (name, summary, source file patterns)
- Data model approach (SQL migrations, ORM, etc.)

### Step 2: Plan the Document Tree

Based on the analysis, plan which documents to create. Use this standard structure, omitting categories that don't apply:

```
docs/
├── DESIGN.md              # Main index (always)
├── CHANGELOG.md           # Auto-maintained log (always)
├── BUILD_ORDER.md         # Phased dependency graph (optional)
├── architecture/          # Cross-cutting architectural docs
│   ├── system-overview.md
│   ├── data-model.md
│   ├── deployment.md
│   └── auth-and-security.md
├── services/              # One per deployable service (skip for monoliths)
│   ├── api.md
│   ├── worker.md
│   └── frontend.md
├── features/              # One per major feature area
│   ├── feature-name/
│   │   └── design.md
│   └── another-feature/
│       └── design.md
└── ui/                    # UI-specific docs (skip for non-UI projects)
    ├── pages.md
    └── components.md
```

**Rules for document tree planning:**
- Monoliths: skip `services/`, put service-level detail in `architecture/`
- CLI tools: skip `ui/`, may skip `features/` if simple
- Libraries: may only need `DESIGN.md` + `architecture/` + `CHANGELOG.md`
- APIs without UI: skip `ui/`

### Step 3: Create DESIGN.md (Main Index)

Use the template from [templates.md](templates.md) — "DESIGN.md Template" section.

This is the project's single entry point. It must contain:
1. **YAML frontmatter** with title, status, last_updated
2. **Project Identity** — what it is and why it exists (2-3 paragraphs)
3. **Architecture Summary** — Mermaid diagram + service table
4. **Tech Stack** — table of technologies with versions
5. **Feature Index** — grouped tables linking to feature docs
6. **Document Map** — table of every doc in the system with purpose

### Step 4: Create Architecture Documents

For each architecture doc, use the template from [templates.md](templates.md) — "Architecture Doc Template".

Key architecture docs and when to include them:

| Document | Include When |
|----------|-------------|
| `system-overview.md` | Always (even for monoliths) |
| `data-model.md` | Project has a database |
| `deployment.md` | Project has containerization, CI/CD, or cloud infra |
| `auth-and-security.md` | Project has authentication or authorization |

### Step 5: Create Service Documents

For multi-service projects, create one doc per deployable service using the template from [templates.md](templates.md) — "Service Doc Template".

### Step 6: Create Feature Documents

For each identified feature, create `docs/features/<feature-name>/design.md` using the template from [templates.md](templates.md) — "Feature Doc Template".

**This is the most important template.** Each feature doc must have:

1. **YAML frontmatter with `source_files`** — categorized glob patterns linking the doc to source code
2. **Standard sections**: Overview, Architecture, Data Model, Key Flows, Configuration, Related
3. **Mermaid diagrams** for architecture, data model, and key flows

The `source_files` frontmatter is what enables automated updates. Be thorough with glob patterns.

### Step 7: Create UI Documents (if applicable)

For projects with a UI, create:
- `docs/ui/pages.md` — route catalog
- `docs/ui/components.md` — component catalog

Use the templates from [templates.md](templates.md) — "UI Doc Templates".

### Step 8: Create CHANGELOG.md

Use the template from [templates.md](templates.md) — "CHANGELOG.md Template".

### Step 9: Install the Update Instructions

Create an update instruction file using the template from [update-skill-template.md](update-skill-template.md). This is what makes the system "living" — it automates doc updates at the end of each work session by:
1. Checking today's git changes
2. Matching changed files against `source_files` globs in doc frontmatter
3. Updating affected docs
4. Logging changes to CHANGELOG.md

**Install location depends on the AI coding environment:**

| Environment | Install Path |
|-------------|-------------|
| Cursor | `.cursor/skills/update-design-docs/SKILL.md` |
| Claude Code | `AGENTS.md` (append to root or create `docs/AGENTS.md`) |
| Windsurf | `.windsurfrules` (append) or `.windsurf/rules/update-design-docs.md` |
| Aider | `.aider/conventions.md` (append) |
| Generic / Unknown | `docs/UPDATE_INSTRUCTIONS.md` (referenced from DESIGN.md) |

If you cannot determine the environment, default to `docs/UPDATE_INSTRUCTIONS.md` and add a link to it from DESIGN.md's Document Map.

### Step 10: Verify and Report

After creating all documents:

1. Verify every doc has valid YAML frontmatter
2. Verify all `source_files` glob patterns match actual files (spot-check a few)
3. Verify all cross-references between docs resolve
4. Verify DESIGN.md's Document Map lists every created doc

Report a summary:

```
Documentation System Created
==============================
Total documents: X
  - DESIGN.md (main index)
  - CHANGELOG.md
  - Architecture docs: X
  - Service docs: X
  - Feature docs: X
  - UI docs: X
Update instructions installed: <path>

To maintain docs, run "update design docs" at the end of each work session.
```

## Provenance

Every `.md` file created by this skill MUST include a provenance header identifying the skill and the agent that ran it.

- **YAML frontmatter files**: Add `generated_by` as the **first field** after `---`:
  ```yaml
  ---
  generated_by: <agent> (setup-design-docs skill)
  title: Document Title
  ...
  ---
  ```
- **Files without frontmatter**: Add an HTML comment as the **first line**:
  ```markdown
  <!-- generated by: <agent> (setup-design-docs skill) | YYYY-MM-DD -->
  ```

Replace `<agent>` with the name of the AI coding agent running the skill (e.g., `cursor-agent`, `claude-code`, `windsurf`, `codex`).

## Important Notes

- **Adapt to the project** — templates are starting points, not rigid formats. Skip sections that don't apply.
- **Source file globs are critical** — these power the automated update system. Be thorough.
- **Mermaid diagrams** — include them for architecture, data model, and key flows. They're the most valuable part of the docs.
- **Don't over-document** — each doc should capture intent, architecture, and design decisions. Do NOT include API contract tables or UI component catalogs — these are derivable from `source_files` globs in frontmatter and go stale quickly.
- **Frontmatter consistency** — every doc needs `title`, `status`, `source_files`, `depends_on`, and `last_updated`.
