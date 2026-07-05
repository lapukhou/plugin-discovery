# ODI Framework Reference

Reference material for the JTBD Job Map Generator skill, extracted from "Jobs to Be Done: Theory to Practice" by Anthony W. Ulwick.

## Core Theory

**Jobs-to-be-Done Theory** defines a market as a group of people (end users) plus the core functional job(s) they are trying to get done — not a product category or industry. The job is the unit of analysis: stable over time, solution-agnostic, and universal.

**Outcome-Driven Innovation (ODI)** operationalizes JTBD Theory into a systematic process that achieves an 86% success rate by linking value creation to customer-defined performance metrics.

## Three Job Executor Types

ODI's first step is defining the customer — not one "customer" but three roles, each holding distinct insight (ch. 4):

| Role | Supplies |
|------|----------|
| **End user** | Functional desired outcomes on the core job, plus emotional/social jobs and related jobs |
| **Product lifecycle support team** | Consumption chain jobs (install, transport, maintain, dispose...) |
| **Purchase decision maker** | Financial desired outcomes (price, cost of ownership, risk of overpaying) |

In consumer products one person usually plays all three roles; in B2B they are often different people, and each role's outcomes must be captured separately.

## The Universal Job Map

All functional jobs consist of eight fundamental process steps. This framework is used to systematically capture desired outcomes at each stage of the job.

### Step Definitions

| Step | Actions | Example prompts for outcome elicitation |
|------|---------|----------------------------------------|
| **1. Define** | Plan, select, determine, map out, quantify goals | "What do you need to figure out or decide before you begin?" |
| **2. Locate** | Gather, access, collect, receive, retrieve | "What inputs, tools, or information do you need to find?" |
| **3. Prepare** | Set up, organize, arrange, examine, prioritize | "What do you need to arrange, set up, or get ready?" |
| **4. Confirm** | Validate, verify, ensure, check, confirm readiness | "What do you need to verify or confirm before proceeding?" |
| **5. Execute** | Perform, carry out, transact, implement, administer | "What is the core action you perform?" |
| **6. Monitor** | Track, verify, check, assess, ensure quality | "What do you watch, check, or track during the process?" |
| **7. Modify** | Update, adjust, maintain, correct, alter, improve | "What adjustments do you make when things aren't going as expected?" |
| **8. Conclude** | Store, finish, close, review, evaluate, clean up | "How do you wrap up? What do you check or store afterward?" |

### Application Rules

- Not every job uses all 8 steps equally — some may be minimal
- The steps are sequential in a typical execution but can loop (e.g., Monitor → Modify → back to Execute)
- Each step should be described from the user's perspective, not the product's
- Steps should be grounded in the specific context of the persona, not described generically

## Desired Outcome Statement Format

The precise format for capturing customer needs as measurable, solution-free metrics.

### Structure

```
[Direction] + the [metric] + [object of control] + [contextual clarifier]
```

### Components

| Component | Options / Description | Examples |
|-----------|----------------------|----------|
| **Direction** | Minimize, Maximize, Reduce, Increase | Always one of these four |
| **Metric** | time, likelihood, number, frequency, effort, degree, amount | What is being measured |
| **Object of control** | The specific thing being improved | "...of steps required to..." |
| **Contextual clarifier** | When, where, or under what conditions | "...when transitioning between activities" |

### Good vs Bad Outcomes

**Well-formed:**
- "Minimize the time it takes to identify the right playlist for a given mood"
- "Reduce the likelihood that the chosen method fails to produce the expected result"
- "Minimize the number of tools required to complete the task end-to-end"

**Poorly-formed (and why):**
- "I want a search bar" — solution, not outcome
- "Feel less frustrated" — emotional job, not functional outcome (capture separately)
- "Faster loading" — too vague, no object of control, no context
- "Be able to set a timer" — feature request, not outcome
- "Easy to use" — not measurable, not specific

### Validation Rules

Every outcome must be:
1. **Measurable** — could be scored on importance/satisfaction scales
2. **Controllable** — a product team could influence this metric
3. **Actionable** — knowing this is underserved suggests a direction for improvement
4. **Solution-free** — no mention of any specific product, feature, or technology
5. **Stable over time** — would have been true 10 years ago and will be true 10 years from now

## JTBD Needs Framework

A hierarchical model organizing ALL customer need types around the core functional job.

### Layer 1: Core Functional Job (End User)
- Decomposed via Job Map into 8 steps
- Each step yields desired outcome statements
- Typical total: 50-150 outcomes per core job
- Goal: get the core job done **better** and/or **more cheaply**

### Layer 2: Surrounding Need Types

**Related Jobs** (End User)
- 5-20 additional functional jobs the user performs alongside or in connection with the core job
- Format: same as core job (verb + object + context)
- Goal: help the user get more jobs done (platform expansion)
- Each related job could itself be decomposed into a full job map

**Emotional / Social Jobs** (End User)
- 5-25 feeling/perception needs
- Emotional: "Feel [emotion]" or "Avoid feeling [emotion]"
- Social: "Be perceived as [attribute]" or "Avoid being perceived as [attribute]"
- Goal: add emotional value to the solution
- These inform brand, messaging, visual design, and copy — rarely drive features directly

**Consumption Chain Jobs** (End User + Support)
- Jobs across the product lifecycle: discover, evaluate, purchase, onboard, learn, use, maintain, upgrade, troubleshoot, leave
- Each lifecycle stage has its own desired outcomes
- Goal: improve the full user experience, not just core functionality
- Friction at any stage is a differentiation opportunity

## Downstream: Scoring and Strategy

Prioritizing the captured outcomes — the Opportunity Algorithm (`Score = Importance + max(Importance - Satisfaction, 0)`) and the five-strategy Growth Strategy Matrix — is handled by the `opportunity-scoring` skill; see its `references/scoring-methodology.md` for the full treatment. The job map's task is to produce outcomes precise enough to be scored.

## Three Characteristics of a Well-Defined Functional Job

1. **Stable** — the job does not change over time; only solutions change. "Listen to music" persisted through vinyl → cassettes → CDs → MP3s → streaming.
2. **No geographical boundaries** — the same jobs exist globally; only solutions and satisfaction levels vary.
3. **Solution-agnostic** — the job does not prescribe hardware, software, or service.

## Job Altitude Guide

Finding the right level of abstraction for the core functional job:

| Level | Example | Problem |
|-------|---------|---------|
| Too narrow | "Boil water" | Misses the full job (prepare a hot beverage) |
| Too broad | "Maintain good health" | Cannot be mapped into actionable steps |
| Right | "Prepare a hot beverage for consumption" | Complete, mappable, solution-free |

**Calibration test:** Can you decompose this job into 5-8 meaningful steps using the Universal Job Map? If fewer than 5, too narrow. If more than 8 would each need their own sub-job-maps, too broad.

## Source

All frameworks from: Ulwick, A. W. (2016). *Jobs to Be Done: Theory to Practice*. IDEA BITE PRESS.
