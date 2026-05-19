# Align Mode

Use this mode when the user wants to clarify a feature, plan, or design before
implementation. The goal is shared understanding grounded in the repo's existing
language, code, and living docs.

This mode adapts the `grill-with-docs` workflow: interview the user one decision
at a time, challenge fuzzy terms, and capture only durable language or decisions
as docs.

## Workflow

1. Search for existing context docs:
   - `CONTEXT-MAP.md`
   - `CONTEXT.md`
   - `docs/adr/`
   - `docs/DESIGN.md`
   - relevant living docs found through [navigate.md](navigate.md)
2. If `CONTEXT-MAP.md` exists, use it to identify the bounded context. If the
   current topic spans or does not clearly match a context, ask before writing.
3. Read only the matching glossary, ADRs, living docs, and source files needed
   to ground the next question.
4. Interview the user one question at a time. For each question:
   - expose the decision dependency or ambiguity
   - provide a recommended answer with concise rationale
   - answer from code/docs directly when exploration can resolve it
5. When a domain term is resolved, update the relevant `CONTEXT.md` immediately.
6. Offer an ADR only when the decision passes the ADR threshold below.
7. After alignment, summarize resolved decisions, open questions, and docs
   changed.

## Context Docs

`CONTEXT.md` is a domain glossary. It is not a spec, scratch pad, design doc, or
implementation decision log.

Create context docs lazily:

- Single-context repo: create root `CONTEXT.md` only when the first domain term
  is resolved.
- Multi-context repo: use root `CONTEXT-MAP.md`; create context-local
  `CONTEXT.md` only when the first term for that context is resolved.

Use [context-format.md](align/context-format.md) when creating or editing a
context glossary.

## During the Interview

- **Challenge glossary conflicts**: if the user uses a term differently from
  `CONTEXT.md`, call out the mismatch immediately.
- **Sharpen fuzzy language**: when terms are vague or overloaded, propose one
  canonical term and aliases to avoid.
- **Probe concrete scenarios**: use edge cases, cardinality, lifecycle, deletion,
  ownership, state transitions, and cross-context flows to force precision.
- **Cross-reference code**: when the user says how the system works, check
  whether the code and living docs agree before accepting the premise.
- **Keep replies concise**: ask one question, give the recommendation, then wait.

## ADR Threshold

Create or offer an ADR only when all three are true:

- **Hard to reverse**: changing later has meaningful cost.
- **Surprising without context**: a future maintainer would wonder why.
- **Real trade-off**: reasonable alternatives existed and one was chosen.

Use [adr-format.md](align/adr-format.md) for placement, numbering, and content.

## Relationship To Living Docs

- `CONTEXT.md` captures project-specific language and relationships.
- `docs/adr/` captures non-obvious architectural decisions.
- Existing living docs capture source-linked implementation design.

Do not duplicate the same content across all three. If a resolved point is
domain vocabulary, write it in `CONTEXT.md`. If it is a lasting technical choice,
write an ADR. If it describes how code is structured or maintained, update the
source-linked living doc.
