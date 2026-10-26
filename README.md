# AI Annotation Examples

**Focus:** rubric-driven annotation of AI responses, structured labels, rationales, multi-reviewer agreement and adjudication.

## Problem statement
Annotations become useful for AI training only when the label taxonomy is clear, evidence accompanies each decision, and disagreements can be identified and resolved. This miniature workflow reproduces that process with **fictional data**.

## Annotation design
| Field | Purpose |
|---|---|
| `id`, `text` | Traceable unit of review |
| `source` | Synthetic ground-truth reference |
| `labels.factuality` | supported / unsupported / not_verifiable |
| `labels.tone` | professional / casual / inappropriate |
| `labels.safety` | safe / review / unsafe |
| `rationale` | Evidence-based explanation |
| `rater_a`, `rater_b` | Two independent factuality judgements |

The label names reflect **this demonstration taxonomy**, not any undisclosed employer guideline.

## Run
```bash
python -m src.annotation
python -m unittest discover -s tests -v
```

## Quality assurance workflow
1. Draft annotation instructions and allowed labels.
2. Independently label synthetic items without consulting another reviewer.
3. Validate schema and check for missing justifications.
4. Calculate **simple agreement** between raters; disagreement flags require adjudication.
5. Record the final decision and reason, especially for ambiguous cases.

## Research considerations
The included `agreement` function calculates raw agreement, **not** Cohen's kappa. Agreement alone can be inflated by imbalanced labels; a real benchmark would include chance-corrected agreement, calibration sessions, annotator training, blind rechecks, class distribution and drift monitoring.

## Portfolio value
Illustrates disciplined annotation rather than portraying annotation as mere tagging. Shows taxonomy design, human-in-the-loop escalation, traceable decisions and quality control.

## Skills demonstrated
Data annotation · Classification · Rubric design · Evaluator calibration · Label QA · Human-in-the-loop review · Python

# Scope and evidence

This is a **synthetic, independently developed demonstration**, not a reproduction of confidential employer data. All prompts, labels, examples, names and records are fabricated for demonstration. Sample counts and test outcomes are software demonstrations, **not historical workplace impact statistics**.

The repository demonstrates evaluation methodology and runnable code; it does not certify that the author achieved a specific result at a named client.

