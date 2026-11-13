# Changelog

## 1.1.0 — 2026-11-13

### Added
- `evals/evals.json`: 15 behavioral test cases covering mode selection, the one-question rule, learner-as-teacher boundaries, solution-study rules, `just tell me`, promotion rules, the beginner path, `exam mode`, `save state`, and course-material citations.
- `references/course-sources.md`: grounding in provided course materials — indexing, course-as-authority with flagged conflicts, fixed citation formats, no invented citations, and per-mode rules.
- `scripts/extract_pages.py`: optional page-by-page PDF text extraction (Poppler or pypdf) for accurate page citations.
- `Sources:` line in the save-state format.
- "Course materials provided" routing row and Course Sources ownership line in `SKILL.md`.
- Faded worked-example path for learners at level 0–1 (First Principles), with an early exit from the diagnostic when the learner shows no recognition.
- "Adjust to learner state" section (Socratic Reasoning) for frustration, time pressure, and fatigue.
- `exam mode` learner command.
- "Domain modules in each mode" table (Socratic Reasoning), the single source for what domain modules may do in each mode.
- Cross-domain rule in `SKILL.md`: the lead domain owns the workflow; a second domain is loaded only for a named check.
- MIT `LICENSE` and this changelog.

### Changed
- The three domain modules point to the shared mode table instead of each restating mode rules.
- The skill map renders at milestones (target reached, level dropped, focus changed, `show progress`) instead of after every level change.
- Shorter, trigger-focused `SKILL.md` description that also mentions course materials and citations.

## 1.0.0

- Initial modular release: coordinator, three core modules, and three domain modules.
