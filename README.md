# Advanced Academic Tutor

A modular agent skill for rigorous, interactive tutoring in mathematics, physics, digital logic design, and data structures and algorithms. It emphasizes independent reasoning, explicit assumptions, verification, and transferable understanding rather than premature answer delivery.

## Interaction modes

| Mode | Typical request | Behavior |
|---|---|---|
| Guided mastery | “Teach me,” “quiz me,” or “help me master this” | Diagnostic placement, one-question Socratic turns, progressive hints, adaptive practice, skill maps, review, and final assessment |
| Learner-as-teacher | “Let me explain it to you” or “Act as a novice” | Short, non-leading questions based only on learner-supplied ideas, without corrections, hints, or endorsement |
| Solution study | “Compare my attempt with the released solution” | Attempt-first comparison, one substantive gap at a time, learner-led repair, and a withheld transfer variation |
| One-off answer | “What is X?” without a tutoring request | A normal concise answer without starting a tutoring course |

Guided mastery also adapts to the learner: complete beginners start with faded worked examples, and frustration, time pressure (`exam mode`), and fatigue change the pace without loosening the evidence rules.

## Domain coverage

- **Mathematics and physics:** derivation ledgers, proof construction, assumptions, quantifiers, modeling, system boundaries, dimensional analysis, initial and boundary conditions, and limiting cases.
- **Digital logic:** Boolean algebra, truth tables, gates, Karnaugh maps, combinational and sequential circuits, FSMs, HDL reasoning, optimization, and correctness verification.
- **Data structures and algorithms:** ADT contracts, algorithm design, invariants, correctness proofs, complexity, memory, debugging, testing, trade-offs, and empirical performance evaluation.

## Repository structure

```text
.
├── README.md
├── CHANGELOG.md
├── LICENSE
├── evals/
│   └── evals.json
└── advanced-academic-tutor/
    ├── SKILL.md
    ├── references/
    │   ├── socratic-reasoning.md
    │   ├── first-principles.md
    │   ├── mastery-assessment.md
    │   ├── course-sources.md
    │   ├── mathematics-physics.md
    │   ├── digital-logic.md
    │   └── dsa.md
    └── scripts/
        └── extract_pages.py
```

The root `SKILL.md` coordinates module selection. Reference modules load only when needed, keeping routine interactions concise while preserving detailed workflows for guided learning.

## Installation

Copy the inner `advanced-academic-tutor/` directory (the one that contains `SKILL.md`) into your agent's skills directory. For Claude Code:

```bash
cp -r advanced-academic-tutor ~/.claude/skills/
```

Keep its internal folder structure intact so that `SKILL.md` can resolve the files under `references/`. The `evals/` folder is for testing and does not need to be installed.

No Python packages, external services, or API keys are required by the tutoring skill itself. The optional `scripts/extract_pages.py` helper needs Python 3 plus Poppler (`pdftotext`, `pdfinfo`) or `pip install pypdf`.

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
- `exam mode` — focus on the weakest high-yield subskills before a deadline, with faster direct explanations.
- `save state` — emit a portable tutoring-state block.
- `resume from:` — restore a supplied state block and continue.

Progress remains in the conversation by default. The skill does not write learner state into its own package.

## Course materials and citations

Give the tutor your course materials (a folder of PDFs or slides, files in a claude.ai Project, or pasted notes) and it grounds the session in them:

- **Index first:** on first use it lists the files, maps topics to pages or slides, and flags unreadable files. The index is saved in your course folder (`course-index.md`) or kept in the conversation, never inside the skill.
- **The course is the authority:** it teaches in the course's notation and definitions and flags any conflict with general knowledge instead of silently picking one.
- **Fixed citations:** course claims are cited as `[Lecture 4, slide 12]` or `[Notes.pdf p. 37, §2.3]`; anything else is labeled `(general knowledge)`.
- **No invented citations:** if the materials don't cover a topic, it says so rather than guessing a page.
- **Modes still apply:** a released solution in your materials stays withheld during guided mastery, and learner-as-teacher mode never cites or corrects from the sources.

Where the agent can run commands (for example Claude Code), `scripts/extract_pages.py` extracts PDF text page by page so citations point to real pages:

```bash
python3 advanced-academic-tutor/scripts/extract_pages.py Notes.pdf --out ~/course/extracted
```

Where it cannot (claude.ai Projects, pasted text), the tutor cites visible section or slide titles instead of computed page numbers.

## Design principles

- Select exactly one interaction mode per session segment.
- Ask one main question per interactive tutoring turn.
- Build explanations from definitions, laws, axioms, or operational semantics.
- Localize the earliest substantive error before repairing downstream work.
- Promote mastery levels only from independent evidence, including unprompted recall and transfer.
- Treat tests, simulations, and correct final answers as evidence with explicit limits—not substitutes for reasoning.
- Never infer durable retention from a single immediate session.

## Evaluation

`evals/evals.json` contains 15 behavioral test cases. Each has a prompt (multi-turn cases include the earlier context in brackets), the expected behavior, and checkable expectations. They cover:

- one-off questions that should not start tutoring;
- the one-question-per-turn rule in guided mastery;
- no corrections, facts, or endorsement in learner-as-teacher mode, including the end-of-session recap;
- solution study: requiring an attempt, and accepting a different valid route;
- the scope of `just tell me`, `exam mode`, and `save state`;
- refusing to promote a level on a single check;
- the faded worked-example path for beginners;
- course-material grounding: correct citations, no invented page numbers, flagged notation conflicts, and withheld released solutions.

Run them with the `skill-creator` skill's eval workflow, comparing runs with and without the skill installed.

## What's new in 1.1.0

- **Behavioral evals:** 15 test cases, described above.
- **Course materials and citations:** a Course Sources module that indexes your materials, cites them in a fixed format, flags conflicts, and never invents a citation, plus an optional page-extraction script.
- **Beginner path:** learners at level 0–1 get a worked example, then a problem with one step missing, then an independent problem, before regular Socratic questioning.
- **Learner-state adaptation:** guidance for frustration, time pressure (`exam mode`), and fatigue that changes the pace but not the evidence rules.
- **Less duplication:** one shared table defines what domain modules may do in each mode, replacing a repeated paragraph in each domain file.
- **Clearer cross-domain rule:** the lead domain owns the workflow, and a second domain is loaded only for a named check.
- **Quieter skill map:** shown at milestones and on `show progress`, not after every change.
- **Packaging:** MIT license, changelog, and an install command.

See [CHANGELOG.md](CHANGELOG.md) for details.

## Validation and limitations

The packaged skill passed structural validation, archive integrity checks, and internal-link verification. Its workflows are specification-level teaching designs, not results from live learner studies. Optional tools such as a CAS, HDL simulator, formal prover, or profiler can strengthen verification but do not replace the relevant reasoning process.

## Design provenance

The interaction boundaries draw on these user-designated primary skills:

- [Jane Street `socratic-tutor`](https://github.com/janestreet/agent_skills/blob/master/socratic-tutor/SKILL.md)
- [`ai-novice`](https://github.com/bstellato/ai-teaching-skills/blob/main/ai-novice/SKILL.md)
- [`ai-solution-study`](https://github.com/bstellato/ai-teaching-skills/blob/main/ai-solution-study/SKILL.md)

This repository is a separate modular architecture and does not modify those projects.

## License

[MIT](LICENSE)
