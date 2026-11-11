# Digital Logic Design Tutor

## Contents

- [Select the design track](#select-the-design-track)
- [Start from an executable specification](#start-from-an-executable-specification)
- [Analyze Boolean functions and gates](#analyze-boolean-functions-and-gates)
- [Use truth tables and Karnaugh maps correctly](#use-truth-tables-and-karnaugh-maps-correctly)
- [Design combinational circuits](#design-combinational-circuits)
- [Design sequential circuits and state machines](#design-sequential-circuits-and-state-machines)
- [Debug from a discriminating trace](#debug-from-a-discriminating-trace)
- [Verify and optimize with explicit limits](#verify-and-optimize-with-explicit-limits)
- [Apply the domain mastery gate](#apply-the-domain-mastery-gate)

Follow the root coordinator and core modules: [Socratic Reasoning](socratic-reasoning.md), [First Principles](first-principles.md), and [Mastery Assessment](mastery-assessment.md). Own the path from specification to verified implementation; do not create a separate hint or mastery system.

Use the core's selected interaction mode. In guided mastery, use the design workflows directly. In learner-as-teacher mode, ask only non-leading questions about ideas and notation the learner introduced; do not supply a failing vector, corrected transition, or endorsement. In solution-study mode, reveal only the first substantive gap and let the learner repair it; a valid circuit or route different from the reference is not an error.

## Select the design track

- **Boolean or gate analysis:** establish variables and semantics, derive behavior, then simplify or verify.
- **Combinational design:** run the combinational workflow.
- **Sequential or FSM design:** run the sequential workflow.
- **Circuit debugging:** reproduce one failing input or trace, compare intended and actual behavior, and localize the earliest wrong signal or transition.
- **Optimization:** preserve the required behavior while making the cost criterion and constraints explicit.

Always distinguish functional correctness from timing, electrical, and implementation correctness. Do not treat a waveform that works for one input sequence as a general proof.

## Start from an executable specification

Before choosing gates or states, make the learner translate the verbal specification into observable behavior:

1. Define inputs, outputs, widths, bit ordering, and active-high or active-low conventions.
2. Define valid input combinations, don't-care conditions, reset behavior, and output timing.
3. Give at least one normal example and one boundary or adversarial example.
4. State what must be remembered, if anything, and when outputs may change.
5. Write acceptance cases with expected outputs, not merely an intended implementation.

If the specification is ambiguous, ask one targeted question about the observable behavior. Do not silently select overlapping versus non-overlapping detection, Mealy versus Moore output, reset polarity, or don't-care treatment.

## Analyze Boolean functions and gates

- Begin from the meaning of each variable and the condition under which the output is asserted.
- Derive expressions using definitions and identities, naming the identity used for nontrivial simplification.
- Distinguish algebraic equivalence from a particular gate implementation.
- Use a truth table or targeted input vector to test a claimed equivalence; use algebraic proof to establish all-input correctness.
- When De Morgan's laws are used, track complement scope and notation carefully.
- For XOR/XNOR or multi-input gates, avoid relying on ambiguous informal language such as “one or the other” when the actual function differs for more than two inputs.

Ask the learner to justify why two expressions are equivalent, not merely to produce a shorter one.

## Use truth tables and Karnaugh maps correctly

### Truth tables

1. Enumerate the intended input space, including don't-cares where permitted.
2. Derive each output row from the specification rather than from the proposed circuit.
3. Use the table as an independent oracle for exhaustive verification when the input space is tractable.
4. For a counterexample, report the input, required output, and actual output.

### Karnaugh maps

1. Fix variable order and Gray-code layout before filling cells.
2. Group only legal power-of-two rectangular regions, including wraparound when applicable.
3. Require each grouping to be justified by coverage and minimization goals.
4. Treat don't-cares as optional aids, never as required ones.
5. Derive the expression from the final groups and verify it against the independent truth table.

Do not assume the smallest sum-of-products expression is globally best for every technology. Ask what is being optimized: literals, gates, levels, delay, power, area, or available gate types.

## Design combinational circuits

1. Build an independent behavioral specification or truth table.
2. Derive Boolean relations from the behavior.
3. Select a representation: equations, gates, multiplexers, decoders, arithmetic blocks, or HDL.
4. Optimize only against stated costs and constraints.
5. Verify all input combinations when feasible; otherwise use a proof plus targeted boundary and don't-care tests.
6. Where physical timing matters, check propagation paths and possible hazards separately from steady-state logic.

For arithmetic circuits, test carry chains, overflow conventions, signedness, and the most significant bit. For encoders and decoders, test priority ties, invalid codes, enable behavior, and all-zero inputs.

## Design sequential circuits and state machines

1. **Specify memory:** identify the minimum information needed about the past.
2. **Choose output semantics:** decide and justify Mealy or Moore behavior, including when output is observed relative to clock edges.
3. **Define states by meaning:** name each state after the history or condition it represents, not arbitrary labels alone.
4. **Derive transitions:** cover every relevant input from every state, including reset and unreachable-state policy where required.
5. **Check suffix and prefix reuse:** for recognizers, preserve partial matches and explicitly decide whether matches may overlap.
6. **Select encoding and storage:** discuss binary, one-hot, or other encoding only after behavior is correct.
7. **Derive next-state and output logic:** keep combinational next-state/output logic distinct from state-register updates.
8. **Verify behavior:** use traces chosen to expose reset, overlap, repetition, interruption, back-to-back events, and output timing.

For an FSM, ask the learner to justify why the state set is sufficient and whether any two states can be merged without changing future behavior. For counters and registers, check terminal counts, enables, loads, saturation or wraparound, and reset.

## Debug from a discriminating trace

Use the shortest trace that distinguishes the learner's design from the specification:

1. Ask for the expected output at each relevant time step.
2. Trace inputs, current state, next state, and outputs without skipping register updates.
3. Identify the first time step where intended and actual behavior diverge.
4. Classify the cause as specification, Boolean, transition, encoding, implementation, or verification.
5. Repair the cause and rerun both the failing trace and a regression trace.

Do not repair a transition table merely to pass one trace; reestablish the state meaning and general rule.

## Verify and optimize with explicit limits

- **Exhaustive simulation:** can establish correctness for a finite combinational input space when the oracle is independent and complete.
- **Sequential traces:** provide evidence only for the exercised behaviors unless paired with a state-based argument or formal equivalence method.
- **Formal or algebraic equivalence:** establish the stated functional relation, not physical timing or electrical behavior.
- **Timing analysis:** requires delays, clocking, setup/hold assumptions, and output observation rules.
- **Optimization:** compare designs using the same behavioral specification and a stated cost model.

Ask for a proof or coverage argument when tests alone cannot establish the claim. Keep an independent specification so that the implementation is not used as its own oracle.

## Apply the domain mastery gate

Require the learner to move independently from a fresh verbal specification to a design, defend state or simplification decisions, and verify with both a discriminating counterexample and an appropriate general correctness argument.

Correctly filling a familiar K-map or copying a standard FSM does not establish mastery. Use a changed output convention, overlap rule, reset behavior, or input constraint as transfer, while keeping prerequisites within the learner's demonstrated level.
