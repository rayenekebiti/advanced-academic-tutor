# Advanced Academic Tutor

A modular agent skill for rigorous, interactive tutoring in mathematics, physics, digital logic design, and data structures and algorithms. It emphasizes independent reasoning, explicit assumptions, verification, and transferable understanding rather than premature answer delivery.

## Interaction modes

| Mode | Typical request | Behavior |
|---|---|---|
| Guided mastery | “Teach me,” “quiz me,” or “help me master this” | Diagnostic placement, one-question Socratic turns, progressive hints, adaptive practice, skill maps, review, and final assessment |
| Learner-as-teacher | “Let me explain it to you” or “Act as a novice” | Short, non-leading questions based only on learner-supplied ideas, without corrections, hints, or endorsement |
| Solution study | “Compare my attempt with the released solution” | Attempt-first comparison, one substantive gap at a time, learner-led repair, and a withheld transfer variation |
| One-off answer | “What is X?” without a tutoring request | A normal concise answer without starting a tutoring course |

## Domain coverage

- **Mathematics and physics:** derivation ledgers, proof construction, assumptions, quantifiers, modeling, system boundaries, dimensional analysis, initial and boundary conditions, and limiting cases.
- **Digital logic:** Boolean algebra, truth tables, gates, Karnaugh maps, combinational and sequential circuits, FSMs, HDL reasoning, optimization, and correctness verification.
- **Data structures and algorithms:** ADT contracts, algorithm design, invariants, correctness proofs, complexity, memory, debugging, testing, trade-offs, and empirical performance evaluation.

## Repository structure

```text
.
├── README.md
└── advanced-academic-tutor/
    ├── SKILL.md
    └── references/
        ├── socratic-reasoning.md
        ├── first-principles.md
        ├── mastery-assessment.md
        ├── mathematics-physics.md
        ├── digital-logic.md
        └── dsa.md
```

The root `SKILL.md` coordinates module selection. Reference modules load only when needed, keeping routine interactions concise while preserving detailed workflows for guided learning.

## Installation

Copy the complete `advanced-academic-tutor/` directory into your agent's skills directory. Keep its internal folder structure intact so that `advanced-academic-tutor/SKILL.md` can resolve the files under `references/`.

No Python packages, external services, API keys, or runtime scripts are required by the tutoring skill itself.

## Example prompts

- “Teach me how to derive the Gaussian integral, and quiz me until I can reconstruct it independently.”
- “Act as a curious novice while I explain how an overlapping `101` sequence detector works.”
- “Here is my sliding-window solution and the released answer. Help me find the first gap without walking me through the whole solution.”
- “Guide me through proving this loop invariant, then give me an unfamiliar transfer problem.”

## Learner commands

Guided mastery supports:

- `show progress` — display the current skill map.
- `harder` / `easier` — adjust difficulty with an educational purpose.
- `just tell me` — reveal the current guided answer, then resume Socratic interaction.
- `save state` — emit a portable tutoring-state block.
- `resume from:` — restore a supplied state block and continue.

Progress remains in the conversation by default. The skill does not write learner state into its own package.

## Design principles

- Select exactly one interaction mode per session segment.
- Ask one main question per interactive tutoring turn.
- Build explanations from definitions, laws, axioms, or operational semantics.
- Localize the earliest substantive error before repairing downstream work.
- Promote mastery levels only from independent evidence, including unprompted recall and transfer.
- Treat tests, simulations, and correct final answers as evidence with explicit limits—not substitutes for reasoning.
- Never infer durable retention from a single immediate session.

## Validation and limitations

The packaged skill passed structural validation, archive integrity checks, and internal-link verification. Its workflows are specification-level teaching designs, not results from live learner studies. Optional tools such as a CAS, HDL simulator, formal prover, or profiler can strengthen verification but do not replace the relevant reasoning process.

## Design provenance

The interaction boundaries draw on these user-designated primary skills:

- [Jane Street `socratic-tutor`](https://github.com/janestreet/agent_skills/blob/master/socratic-tutor/SKILL.md)
- [`ai-novice`](https://github.com/bstellato/ai-teaching-skills/blob/main/ai-novice/SKILL.md)
- [`ai-solution-study`](https://github.com/bstellato/ai-teaching-skills/blob/main/ai-solution-study/SKILL.md)

This repository is a separate modular architecture and does not modify those projects.
