# ADR Format

ADRs live in `docs/adr/` and use sequential numbering:

```text
docs/adr/0001-short-slug.md
docs/adr/0002-short-slug.md
```

Create `docs/adr/` lazily, only when the first ADR is needed. Number by scanning
for the highest existing ADR number and incrementing by one.

## Minimal Template

```markdown
# <Short Title>

<One to three sentences explaining the context, the decision, and why this
choice was made.>
```

## Optional Sections

Use these only when they add value:

- `Status` frontmatter: `proposed`, `accepted`, `deprecated`, or
  `superseded by ADR-NNNN`.
- `## Considered Options`: when rejected alternatives are worth remembering.
- `## Consequences`: when downstream effects are not obvious from the code.

## Good ADR Topics

- Architectural shape and service boundaries.
- Integration patterns between contexts.
- Technology choices that carry real lock-in.
- Boundary, ownership, or scope decisions.
- Deliberate deviations from the obvious path.
- Constraints not visible in the code.
- Rejected alternatives likely to be proposed again later.

Skip ADRs for easy-to-reverse choices, obvious implementation details, and
routine library choices.
