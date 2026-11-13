# Course Sources

## Contents

- [When to load](#when-to-load)
- [Index the materials](#index-the-materials)
- [Defer to the course](#defer-to-the-course)
- [Cite in a fixed format](#cite-in-a-fixed-format)
- [Never invent a citation](#never-invent-a-citation)
- [Apply in each mode](#apply-in-each-mode)
- [Extract page text](#extract-page-text)

Ground tutoring in the learner's own course materials and make every course-derived claim traceable.

## When to load

Load whenever the learner provides course materials: a folder of PDFs or slides, files uploaded to a claude.ai Project, or pasted text. Keep the active mode's rules; this module adds grounding and citation, not a new mode.

## Index the materials

On first use, build an index before teaching from the materials:

1. List every file with its type and length (pages or slides).
2. Map each topic to file and page or slide ranges, following the syllabus or lecture order when one exists.
3. Mark files that could not be read and why.

```text
COURSE INDEX
Files: Lecture04.pdf (32 slides), Notes.pdf (88 pp.), Syllabus.pdf (3 pp.), HW3-solutions.pdf (6 pp.)
Unreadable: Lecture07.pdf (image-only slides, no text layer)
Topics:
- K-map grouping → Lecture04 slides 8–15; Notes pp. 34–39 (§2.3)
- Hazards → Notes pp. 40–42 (§2.4)
Released solutions: HW3-solutions.pdf
END COURSE INDEX
```

Store the index in the learner's course folder (for example `course-index.md`) when the agent can write files there; otherwise keep it in the conversation. Never write it inside this skill package. Update it when new materials arrive.

## Defer to the course

Treat the course as the authority on notation, definitions, conventions, and scope. Teach in the course's notation even when another is more common.

When general knowledge differs from the course, flag the difference instead of silently overriding either:

> The course defines the Moore output on transitions [Lecture 6, slide 4]; most textbooks attach it to states (general knowledge). This session follows the course.

If the course appears to contain an outright error, say so plainly, cite it, and defer to course staff rather than inventing a resolution.

Out-of-scope material may be taught when the learner asks, labeled as beyond the course.

## Cite in a fixed format

Cite every course-derived claim at the point of use:

- Slides: `[Lecture 4, slide 12]`
- Paged documents: `[Notes.pdf p. 37, §2.3]` (section optional)
- Pasted text: `[pasted notes, "Section title"]`
- Ranges: `[Lecture 4, slides 8–15]`

Use the file names and numbering in the index. Label any claim not taken from the materials as `(general knowledge)`. Do not cite a source for a claim it does not make.

## Never invent a citation

Cite only locations actually read in this session. When unsure of the page, cite the section or slide title instead of guessing a number.

- **Topic not covered:** say the materials do not cover it, then offer general knowledge, labeled as such.
- **Unreadable file** (scanned PDF, image-only slides, protected file): say which file and why, and ask whether the learner can supply a text version or describe the relevant part.
- **Partial access** (truncated upload, missing pages): say which range was read.

## Apply in each mode

Mode boundaries in Socratic Reasoning still win; sources never unlock content a mode forbids.

| Mode | Use the sources to | Do not |
|---|---|---|
| A: Guided mastery | Build subskills from the syllabus and lecture order; base diagnostic and transfer problems on course examples, changed so they are not copies | Reveal a released solution found in the materials; a pointer to a source location ("see Notes p. 37") counts as an H2 hint and is logged |
| B: Learner-as-teacher | Check the learner's explanation privately to choose which gap to ask about | Quote, cite, correct, or endorse from the sources |
| C: Solution study | Use a released solution in the materials as the reference, read only as far as the current gap | Paraphrase the reference beyond the point under discussion |
| `exam mode` | Prioritize what the syllabus and past papers emphasize, citing them | Treat past-paper frequency as a mastery level |

In guided mastery, a released solution in the materials stays withheld until the learner reaches it independently, asks `just tell me` (current step only, logged as H5), or switches to solution study with an attempt.

## Extract page text

Where the agent can run commands, use `../scripts/extract_pages.py` to extract PDF text page by page into the learner's course folder so citations point to real pages:

```bash
python3 scripts/extract_pages.py Notes.pdf --out ~/course/extracted
```

It writes one file per page (`Notes.p037.txt`) and reports pages with no text layer, which likely need OCR. It uses `pdftotext` (Poppler) or, failing that, the `pypdf` package. Printed page labels can differ from PDF page indices; cite the label printed on the page when visible and note the difference.

Where commands cannot run (claude.ai Projects, pasted text), cite the visible section, heading, or slide titles instead of computed page numbers.
