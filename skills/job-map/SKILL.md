---
name: job-map
description: "Decomposes a single use-case-map.md into a complete JTBD Job Map using the Outcome-Driven Innovation (ODI) framework — core functional job, the 8-step Universal Job Map with desired outcome statements, related / emotional / social jobs (with Octalysis Core Drive mapping), and the consumption chain. Outputs one file: job-map.md. Use whenever the user has a use case and wants the jobs and measurable outcomes behind it — e.g. 'decompose this use case into a job map', 'run the ODI decomposition on this use case', 'what jobs and desired outcomes are behind this problem'. Triggers on 'job map', 'desired outcomes', 'ODI decomposition', 'universal job map', 'core functional job', 'JTBD decomposition'. Do NOT use this to score or prioritize the outcomes (that's the opportunity-scoring skill), to generate app concepts (jtbd-to-concepts), to run the full discovery pipeline end-to-end (pp-discovery), or to define the use case itself (use-case-map)."
---

# Use Case Map → JTBD Job Map

Transform a Use Case Map into a JTBD Job Map. The use case describes an **opportunity** (problem + persona + alternatives). This skill decomposes that opportunity into the **jobs** users are trying to get done and the **measurable outcomes** they use to judge success, using the Outcome-Driven Innovation (ODI) framework.

It turns one fuzzy problem into 40–80 precise, measurable points of intervention. Prioritizing them (importance × satisfaction scoring) is the job of the downstream `opportunity-scoring` skill.

## What this produces

One file, written in the same folder as the source use case:

- **`job-map.md`** — Core Functional Job, the 8-step Universal Job Map with desired outcome statements, Related Jobs, Emotional & Social Jobs (with Octalysis Core Drive mapping), and the Consumption Chain.

## Input

A `use-case-map.md` file following the Use Case Map format (Problem, Persona, Alternatives, Why, Frequency, Strategic Notes). Read the full file before starting.

## Language

Conduct the entire workflow and produce all artifacts in English, regardless of the language the user writes in. The ODI framework uses English terminology, and desired outcome statements must follow a precise English-language format.

---

## Workflow

### Step 1: Define the Core Functional Job

Read the use case's Problem and Persona sections. Extract the core functional job — the fundamental task the user is trying to accomplish.

The job executor plus the core functional job **defines the market** (Ulwick, ch. 8) — everything downstream (outcomes, scoring, strategy) is anchored to this statement, so get it right before proceeding.

**Rules for a well-defined job:**
- **Solution-agnostic** — no reference to any product, app, technology, or specific method, and phrased from the customer's perspective, not the company's ("prevent weeds from impacting crop yields", not "kill weeds")
- **Stable over time** — the job existed before smartphones and will exist after them ("listen to music" survived vinyl → cassette → CD → MP3 → streaming)
- **Right altitude** — not too narrow (a single action) and not too broad (an entire life domain)
- **One-dimensional (purely functional)** — no emotions, social aspirations, or desired outcomes mixed in ("cut wood in a straight line", not "accurately, safely and quickly cut wood")
- **A job, not a situation** — "long boring commute" is a situation; the job is what the user is trying to accomplish within it (e.g., "pass the time productively while commuting")
- **Format**: verb + object of the verb (noun) + contextual clarifier

**Altitude calibration:**
- Too narrow: "Put the phone down before bed" (one action, not the full job)
- Too broad: "Maintain good health" (too many sub-jobs, impossible to map)
- Right altitude: "Transition from daytime wakefulness to restful sleep" (complete job, solution-agnostic, mappable)

Defining the job too narrowly is not just an analytical error — it invites disruption. Ulwick's canonical example (ch. 4): the kettle maker who defines the job as "boil water" instead of "prepare a hot beverage for consumption" leaves the whole job open to Keurig.

**Process:**
1. Read the Problem section — identify what the user is ultimately trying to accomplish (not what they're struggling with)
2. Read the Persona section — understand the context and constraints
3. Draft the job statement
4. Validate: Is it solution-free? Stable? Right altitude? Purely functional?
5. Present the job statement and briefly explain why this altitude was chosen

### Step 2: Build the Universal Job Map

Decompose the core functional job into 8 process steps. For each step, describe what the user is trying to accomplish **in the context of the core job defined in Step 1**.

The 8 steps of the Universal Job Map:

| Step | What happens | Key question |
|------|-------------|--------------|
| **1. Define** | Plan, select, determine what's needed | What must the user determine, plan, or decide before starting? |
| **2. Locate** | Gather inputs, information, materials | What inputs, tools, or information must the user find or assemble? |
| **3. Prepare** | Set up, organize, arrange the environment | What setup, arrangement, or preparation is needed? |
| **4. Confirm** | Validate readiness, prioritize, make final decisions | What must the user verify or decide before executing? |
| **5. Execute** | Perform the core action | What is the central activity the user performs? |
| **6. Monitor** | Track progress, verify conditions | What does the user check, track, or watch during execution? |
| **7. Modify** | Make adjustments, corrections, handle exceptions | What adjustments or corrections does the user make? |
| **8. Conclude** | Finish, store results, evaluate success | How does the user finish, capture results, or assess outcomes? |

**Process:**
1. Walk through each step, asking: "In the context of [core job], what is the user doing at this stage?"
2. Write 2-4 sentences per step describing the activities
3. Not every job uses all 8 steps equally — some steps may be minimal. Note this, but still map them.
4. Ground each step in the specific persona and context from the use case — do not write generic descriptions

### Step 3: Generate Desired Outcome Statements

For each job map step, generate desired outcome statements — the metrics users use to judge success at that step.

**Desired Outcome Statement format (mandatory):**
```
[Direction] + the [metric] + [object of control] + [contextual clarifier]
```

**Direction** is always one of: Minimize, Maximize, Reduce, Increase
**Metric** is what is being measured: time, likelihood, number, frequency, effort, degree, amount — in Ulwick's studies the metric is *usually time or likelihood*; default to those two and reach for the others only when they genuinely fit better
**Object of control** describes what is being minimized/maximized
**Contextual clarifier** specifies when/where this matters

**Examples:**
- "Minimize the time it takes to determine the ideal sleep time given the next day's schedule"
- "Minimize the likelihood of encountering stimulating content that delays the transition to sleep"
- "Reduce the effort required to shift from active screen engagement to a passive wind-down activity"
- "Minimize the number of decisions required to start the sleep preparation routine"

**Anti-patterns (reject these):**
- "I want a dark mode" — this is a solution, not an outcome
- "Feel less anxious about tomorrow" — this is an emotional job, not a functional outcome
- "Faster app loading" — too vague, no object of control, no context
- "Be able to set a timer" — this is a feature, not an outcome

**Rules:**
- Generate 3-10 desired outcomes per job map step — density proportional to the step's complexity for this job, not a uniform quota. Padding a thin step to hit a number produces redundant outcomes, which the checklist forbids.
- Total across all steps: aim for 40-80 outcomes. (Full ODI engagements typically capture 50-150 per job — Bosch's study used 75, Arm & Hammer's 165. 40-80 is the right density for a single-persona expert-surrogate pass; going above it without survey data adds noise, not signal.)
- Each outcome must be measurable, controllable, actionable, solution-free, and stable over time
- Each outcome must be specific to the persona and context in the use case
- Outcomes must be mutually exclusive (no two say the same thing in different words)
- Assign a sequential ID to each outcome for traceability (e.g., DEF-01, LOC-01, PREP-01...)

### Step 4: Identify Related Jobs

From the use case's Problem, Persona, and Strategic Notes, identify 5-20 related functional jobs the user tries to accomplish alongside or in connection with the core job (Ulwick: typically 5-20 are on the end user's mind).

**Format**: verb + object + contextual clarifier (same as core job, but these are adjacent jobs, not sub-steps)

**Examples for a bedtime scroll use case:**
- "Plan the next day's schedule before sleeping"
- "Stay informed about news and social updates"
- "Decompress from the day's stress"
- "Connect with friends and family"
- "Manage alarm and wake-up settings"

**Why this matters:** Each related job is a potential feature expansion or integration point. Products that address related jobs alongside the core job become platforms.

### Step 5: Capture Emotional and Social Jobs

From the Persona and Why sections of the use case, extract:

**Emotional Jobs** — how the user wants to feel (or avoid feeling):
- Format: "Feel [emotion]" or "Avoid feeling [emotion]"
- Example: "Feel in control of my evening routine", "Avoid feeling guilty about wasted time"

**Social Jobs** — how the user wants to be perceived:
- Format: "Be perceived as [attribute]" or "Avoid being perceived as [attribute]"
- Example: "Be perceived as a disciplined person", "Avoid being perceived as phone-addicted"

Generate 5-15 emotional jobs and 3-8 social jobs.

**Core Drive Mapping** — For each emotional and social job, identify the primary Octalysis Core Drive it maps to. This makes the emotional dimension systematic and feeds into downstream motivation analysis (app concept generation).

| Emotional Job Pattern | Primary Core Drive |
|----------------------|-------------------|
| Feel in control, autonomous, empowered | CD3: Empowerment of Creativity & Feedback |
| Feel competent, progressing, achieving | CD2: Development & Accomplishment |
| Feel part of something meaningful, purposeful | CD1: Epic Meaning & Calling |
| Feel connected, belonging, accepted | CD5: Social Influence & Relatedness |
| Feel ownership, investment, personalization | CD4: Ownership & Possession |
| Avoid missing out, losing progress | CD8: Loss & Avoidance |
| Feel curious, surprised, engaged | CD7: Unpredictability & Curiosity |
| Feel exclusive, special, elite | CD6: Scarcity & Impatience |
| Avoid embarrassment, judgment | CD8 + CD5 |
| Feel proud, recognized for achievement | CD2 + CD1 |

Use this mapping table as a guide — some jobs may map to multiple Core Drives. Assign the single most dominant one as primary.

### Step 6: Map the Consumption Chain

ODI distinguishes three job-executor types, each holding distinct insight (Ulwick, ch. 4): the **end user** (functional outcomes, emotional/social jobs, related jobs — Steps 1-5 above), the **product lifecycle support team** (consumption chain jobs — this step), and the **purchase decision maker** (financial desired outcomes). In consumer products the same person usually plays all three roles, but capture each role's outcomes explicitly: the financial/purchase-decision outcomes (e.g., "Minimize the likelihood of paying for capabilities that go unused") belong in the **Evaluate** stage below. If the buyer is genuinely a different person (parent, employer, IT department), say so and give their outcomes their own weight.

Note on terminology: in the book, consumption chain jobs are covered by customer journey maps, not the job map proper — they are lifecycle jobs *around* solutions, so unlike core-job outcomes they are allowed to reference the solution's lifecycle (onboarding, troubleshooting), though still never a specific product or feature.

Define desired outcomes for the product lifecycle — how users interact with any solution to this job, from discovery to departure:

| Stage | Key question |
|-------|-------------|
| **Discover** | How do users find out a solution exists? |
| **Evaluate** | How do users decide whether to try it? |
| **Onboard** | What happens in the first session? |
| **Learn** | How do users learn to use it effectively? |
| **Use daily** | What is the recurring interaction? |
| **Troubleshoot** | What goes wrong and how do users fix it? |
| **Integrate** | How does it fit with other tools/habits? |
| **Leave** | What happens if they stop using it? |

For each stage, write 2-5 desired outcome statements using the same format as Step 3. Use prefix CONS- for IDs (e.g., CONS-01).

### Write `job-map.md`

Produce a `job-map.md` file in a folder alongside the source use case.

**Document structure:**

```markdown
# JTBD Job Map: [Core Functional Job]

## Source
- **Use Case**: [title and id from source]
- **Persona**: [one-line summary from source]
- **Problem**: [one-line summary from source]

## Core Functional Job

[Job statement from Step 1]

[2-3 sentences explaining the altitude choice and job boundaries — what's included and what's explicitly outside scope]

## Universal Job Map

### 1. Define
[Description of what the user does at this step]

| ID | Desired Outcome |
|----|----------------|
| DEF-01 | [outcome statement] |
| DEF-02 | [outcome statement] |
| ... | ... |

### 2. Locate
[Description]

| ID | Desired Outcome |
|----|----------------|
| LOC-01 | [outcome statement] |
| ... | ... |

### 3. Prepare
[repeat pattern]

### 4. Confirm
[repeat pattern]

### 5. Execute
[repeat pattern]

### 6. Monitor
[repeat pattern]

### 7. Modify
[repeat pattern]

### 8. Conclude
[repeat pattern]

## Related Jobs

| # | Related Job |
|---|------------|
| RJ-01 | [job statement] |
| RJ-02 | [job statement] |
| ... | ... |

## Emotional Jobs

| # | Emotional Job | Core Drive |
|---|--------------|-----------|
| EJ-01 | [statement] | [CD#: name] |
| ... | ... | ... |

## Social Jobs

| # | Social Job | Core Drive |
|---|-----------|-----------|
| SJ-01 | [statement] | [CD#: name] |
| ... | ... | ... |

## Consumption Chain

### Discover
| ID | Desired Outcome |
|----|----------------|
| CONS-01 | [outcome statement] |
| ... | ... |

### Evaluate
[repeat pattern]

### Onboard
[repeat pattern]

### Learn
[repeat pattern]

### Use Daily
[repeat pattern]

### Troubleshoot
[repeat pattern]

### Integrate
[repeat pattern]

### Leave
[repeat pattern]

## Summary

- **Core Job**: [job statement]
- **Total Desired Outcomes**: [count across all job map steps]
- **Total Consumption Chain Outcomes**: [count]
- **Related Jobs**: [count]
- **Emotional Jobs**: [count]
- **Social Jobs**: [count]
- **Steps with highest outcome density**: [list the 2-3 steps with the most outcomes — these are likely the most complex parts of the job]
```

## Quality Checklist

Before finalizing, verify:

- [ ] Core job is solution-agnostic, stable, right altitude, one-dimensional, and a job rather than a situation
- [ ] All 8 job map steps are addressed (even if some are thin)
- [ ] Every desired outcome follows the format: direction + metric + object of control + context
- [ ] No outcome contains a solution or feature reference
- [ ] No two outcomes are redundant
- [ ] Outcomes are grounded in the specific persona and context, not generic
- [ ] Related jobs are functional, not emotional or social
- [ ] Emotional/social jobs are separated from functional outcomes
- [ ] Every emotional and social job has a Core Drive mapping
- [ ] All IDs are sequential and unique
- [ ] Total desired outcomes are in the 40-80 range
- [ ] Consumption chain covers all 8 lifecycle stages

## Next step

The finished `job-map.md` is the input to the `opportunity-scoring` skill, which scores every outcome (importance × satisfaction) against the use case's alternatives and produces the ranked opportunity landscape.

## References

- For the full ODI methodology, job-map frameworks, and terminology, see `references/odi-framework-reference.md`.
