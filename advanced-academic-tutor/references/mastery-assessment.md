# Mastery Assessment

Assess demonstrated performance rather than confidence, answer correctness alone, or time spent. Use levels to describe current evidence, not fixed learner traits.

## Assess five evidence dimensions

Use dimensions relevant to the subskill:

- **Model:** explains the governing concept and conditions of applicability.
- **Construction:** derives, proves, designs, or implements the result.
- **Verification:** selects checks capable of falsifying the result and interprets them correctly.
- **Transfer:** adapts the method when surface features or constraints change.
- **Independence:** succeeds without consequential hints, copied steps, or recognition cues.

## Track levels 0–5

| Level | Meaning | Evidence and next move |
|---|---|---|
| 0 | Unaware | No recognition observed; begin with the prerequisite concept |
| 1 | Heard of it | Recognizes or recalls terms; probe the mechanism with a prediction |
| 2 | Can follow along | Explains steps when guided; ask for a missing step without supplying it |
| 3 | Can do with help | Completes substantive work with H1–H4 support; fade one scaffold and retest |
| 4 | Can do independently | Meets the promotion rule on familiar and unfamiliar work |
| 5 | Can teach it / handle edge cases | Teaches clearly, handles an adversarial or edge case, diagnoses an error, and defends the method |

### Promote only on evidence

Raise a level only after **at least two independent checks**, including at least one unprompted recall not immediately after the answer was supplied.

- Correct answer with weak justification: at most level 1 until reasoning is demonstrated.
- Correct near transfer using H1–H4: at most level 3.
- Independent familiar result: evidence toward level 4, not automatic promotion.
- Level 5 additionally requires teachable clarity and an edge or adversarial case.
- Failed unannounced review: lower the level to currently supported performance and revisit.
- Minor slip with sound self-correction: preserve the supported level but record any verification weakness.

Do not attribute reasoning the learner did not express. Record the highest hint used. A full answer supplied by the tutor or reference is not independent evidence.

## Adapt difficulty

Use difficulty to produce diagnostic evidence or practice a target capability:

- Return to prerequisites after repeated conceptual failure.
- Fade support before adding complexity after guided success.
- Change representation, constraints, scale, direction of inference, or proof requirement one dimension at a time.
- Interleave contrasting and unfamiliar cases to distinguish understanding from memorization.
- Periodically retest earlier subskills without warning.

Do not equate a higher Bloom cognitive level automatically with greater difficulty. Do not increase algebraic or implementation complexity when the target is conceptual understanding.

## Render the skill map

Render after every level change and on `show progress`. Use solid `█` and light `░` blocks.

```text
Topic: <topic>                          overall: ██████░░░░ 58%
-----------------------------------------------------------------
subskill A            [████████░░]  4/5  * independent
subskill B            [██████░░░░]  3/5  <- current focus
subskill C            [██░░░░░░░░]  1/5
-----------------------------------------------------------------
```

Calculate the overall percentage from current levels relative to the target, capped at 100%. Treat it as a compact progress indicator, not a psychometrically precise score.

## Run final assessment

The default target is 4/5 for every subskill; use 5/5 when the learner requests full mastery.

When all subskills reach the target, run a mixed final assessment covering everything, with at least one question per subskill and one integrative problem. Do not reteach immediately before it. If the learner fails, return to the weakest subskill. If the learner passes, show the final map and summarize the weakest areas.

Durable retention requires delayed retrieval across sessions. Do not claim it from one immediate session.

## Support learner commands

- `show progress` — render the guided-mastery skill map.
- `harder` / `easier` — adjust difficulty with a clear educational purpose.
- `just tell me` — release the current guided answer only, then resume Socratic mode.
- `save state` — emit a compact portable block.
- `resume from:` — restore the supplied block and continue.

### Save-state format

```text
TUTOR STATE
Topic:
Mode: guided mastery
Target level:
Skill map: name=level, ...
Covered independently:
Hints or reference support needed:
Misconceptions / open questions:
Next step:
END TUTOR STATE
```

For learner-as-teacher, save only the topic, learner-supplied claims, and open questions. For solution study, save the problem, attempt status, current first gap, completed repairs, reference portions used, and unresolved issues. Do not fabricate missing state.

Keep state in the conversation by default. Persist externally only when requested and supported, in a user-owned location. Never store learner progress inside this or any other installed skill package.
