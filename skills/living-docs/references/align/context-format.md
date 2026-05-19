# Context Format

`CONTEXT.md` records shared project language for one bounded context.

## Template

```markdown
# <Context Name>

<One or two sentences describing what this context is and why it exists.>

## Language

**<Term>**: <One-sentence definition of what the concept is.>
_Avoid_: <ambiguous alias>, <misleading synonym>

**<Term>**: <One-sentence definition of what the concept is.>

## Relationships

- A **<Term>** has zero or more **<Other Terms>**
- A **<Term>** belongs to exactly one **<Other Term>**

## Example Dialogue

> **Dev:** "When a **<Term>** changes, should we update the **<Other Term>**?"
> **Domain expert:** "No. The **<Other Term>** only changes after..."

## Flagged Ambiguities

- "`<word>`" was used to mean both **<Term A>** and **<Term B>**; resolved:
  <short resolution>.
```

## Rules

- Include only domain concepts specific to this project or bounded context.
- Exclude general programming, framework, infrastructure, or utility concepts.
- Pick one canonical term when multiple words exist for the same concept.
- List misleading aliases with `_Avoid_` when useful.
- Keep definitions to one sentence. Define what the thing is, not everything it
  does.
- Use relationships for cardinality, ownership, lifecycle boundaries, and
  context boundaries.
- Include an example dialogue when it clarifies how terms interact.
- Flag conflicts explicitly with their resolution.
- Group terms under subheadings only when natural clusters emerge.

## Context Maps

For multi-context repos, root `CONTEXT-MAP.md` should list contexts and their
relationships:

```markdown
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) - receives and tracks customer orders
- [Billing](./src/billing/CONTEXT.md) - generates invoices and processes
  payments

## Relationships

- **Ordering -> Billing**: Ordering emits `OrderPlaced`; Billing consumes it to
  prepare an invoice.
```
