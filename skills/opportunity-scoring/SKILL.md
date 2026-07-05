---
name: opportunity-scoring
description: "Scores every desired outcome in a job-map.md with the ODI Opportunity Algorithm (importance × satisfaction) against the use case's current alternatives to produce a ranked opportunity landscape — underserved / overserved / table-stakes zones, opportunity clusters, step-level analysis, a growth-strategy recommendation from the five-strategy JTBD Growth Strategy Matrix, and a self-contained opportunity brief. Outputs one file: opportunity-scores.md. Requires a finished job-map.md (produced by the job-map skill) plus its source use-case-map.md. Use whenever the user has a job map and wants prioritization — e.g. 'score the job map', 'run the opportunity algorithm', 'where's the white space', 'which outcomes are underserved'. Triggers on 'opportunity score', 'opportunity algorithm', 'importance vs satisfaction', 'underserved / overserved', 'opportunity landscape', 'growth strategy'. Do NOT use this to build the job map itself (that's the job-map skill), to generate app concepts from the scores (jtbd-to-concepts), to run the full discovery pipeline end-to-end (pp-discovery), or to define the use case (use-case-map)."
---

# Job Map → Opportunity Scores

Score the desired outcomes of a finished JTBD job map against current alternatives to reveal exactly **where to focus** — the underserved white space, the table stakes, the overserved fat. Takes the 40–80 precise, measurable outcomes a job map produces and ranks them.

## What this produces

One file, written in the same folder as the source job map:

- **`opportunity-scores.md`** — Alternative Capability Matrix, every outcome scored (Imp / Sat / Score / Zone / Reasoning), the opportunity landscape (distribution, underserved / overserved / table stakes), opportunity clusters, step-level analysis, a growth-strategy recommendation, and a self-contained opportunity brief.

## Input

Two files:

1. **`job-map.md`** — produced by the `job-map` skill.
2. **`use-case-map.md`** — the source use case in the same folder (for alternatives, persona, problem context).

Read both files fully before starting.

## Language

Conduct the entire workflow and produce all artifacts in English, regardless of the language the user writes in. The ODI framework uses English terminology.

## Core concept

The Opportunity Algorithm: `Score = Importance + max(Importance - Satisfaction, 0)`

- **Importance** (1-10): How critical this outcome is to the user when executing the job
- **Satisfaction** (1-10): How well current alternatives achieve this outcome
- **Opportunity Score**: The higher the score, the bigger the gap between what matters and what exists

| Score | Zone | Meaning |
|-------|------|---------|
| 15+ | Extreme opportunity | Users care deeply, nothing serves them — highest-value targets |
| 12-14.9 | High opportunity | Strong unmet needs — primary innovation zone |
| 10-11.9 | Moderate opportunity | Underserved — solid targets for differentiation |
| 6-9.9 | Appropriately served | Current alternatives handle these adequately |
| < 6 (Sat >> Imp) | Overserved | Users don't care much but solutions over-deliver — simplify here |

## Methodology grounding (JTBD RAG)

If the `rag-jtbd` plugin is installed (skill `rag-jtbd:jtbd` — a retrieval knowledge base over Ulwick's *Jobs to Be Done: Theory to Practice*), use it to ground judgment calls in the book instead of relying on memory:

- **When to query**: borderline zone classifications, growth-strategy calls the guardrails don't settle, definitional disputes (table stakes vs. unmet need, consumption chain scope, what counts as overserved), or when the user challenges a score's rationale.
- **How**: invoke the `rag-jtbd:jtbd` skill with the question; read the top retrieved pages and apply what the book actually says.
- **Cite** consulted chapters/pages in `Confidence & Limitations` (e.g., "growth-strategy call cross-checked against ch. 3 via the JTBD knowledge base").

If the plugin is not installed, proceed normally — this skill and `references/scoring-methodology.md` are self-contained.

## Analytical approach: Expert Surrogate Scoring

In a full ODI engagement, importance and satisfaction scores come from surveying 180-3,000 users. This skill uses an **expert surrogate** approach instead: systematically estimating scores by analyzing the use case's alternatives, persona behavior, and problem context.

This is less precise than a real survey but radically better than unstructured intuition because:
1. Every outcome gets explicit, comparable scores (not "this feels important")
2. Scoring is grounded in specific alternative analysis (not abstract guessing)
3. The reasoning is documented and auditable

**Critical rule:** Always document the reasoning behind each score. A score without reasoning is a guess. A score with reasoning is a hypothesis that can be validated.

### Step 0 (optional): Market reality check

**Off by default.** Run this step only when the user explicitly asks to ground the scoring in market data (e.g., "with market check", "validate the alternatives against real apps", "--market-check"). Never run it unprompted inside the pp-discovery pipeline.

When requested: use the `app-intelligence` skill (Appfigures Explorer) to scan the real competitive landscape for this job — the top apps in the relevant category/keywords, their traction, and what capabilities they actually ship. Use the findings to (a) extend or correct the use case's Alternatives list before building the capability matrix, and (b) calibrate Satisfaction scores against what shipping products actually deliver rather than what the use case author remembered. Cite what was scanned in the `Confidence & Limitations` section and raise the stated confidence level accordingly. If the scan fails or the skill is unavailable, say so and fall back to the standard expert-surrogate approach.

### Step 1: Build the Alternative Capability Matrix

Before scoring any outcomes, create a structured understanding of what current alternatives can and cannot do.

**Process:**
1. Read the Alternatives section of the use case
2. For each major alternative (typically 4-7), describe:
   - What it does well (which job steps it serves)
   - What it does poorly or not at all
   - Where it creates friction, failure, or frustration
   - Its inherent structural limitations (why it can't improve easily)
3. Create an Alternative Capability Matrix — a table mapping each alternative to the job map steps it addresses

**Output format:**

```markdown
## Alternative Capability Matrix

| Alternative | Define | Locate | Prepare | Confirm | Execute | Monitor | Modify | Conclude | Structural Limitation |
|-------------|--------|--------|---------|---------|---------|---------|--------|----------|-----------------------|
| [Alt 1]     | [0-2]  | [0-2]  | ...     | ...     | ...     | ...     | ...    | ...      | [why it can't improve] |
| [Alt 2]     | ...    | ...    | ...     | ...     | ...     | ...     | ...    | ...      | ...                    |
```

Score each cell 0 (not addressed), 1 (partially addressed), or 2 (well addressed). This matrix becomes the foundation for satisfaction scoring in Step 2.

### Step 2: Score Each Desired Outcome

For every desired outcome in the job map, assign Importance (1-10) and Satisfaction (1-10) scores. **This includes the consumption chain outcomes (CONS-*)** — they are scored with the same algorithm and appear in their own section of the output. Consumption chain gaps (e.g., nothing helps users evaluate or onboard) are real opportunities that feed directly into concept and onboarding design downstream.

**Importance scoring guide:**

| Score | Meaning | Signals to look for |
|-------|---------|---------------------|
| 9-10 | Critical — job fails without this | Mentioned in Problem section as core pain; affects every session; directly impacts the job's primary success metric |
| 7-8 | High — significantly impacts job success | Mentioned by persona as a frustration; affects most sessions; causes noticeable quality degradation when unmet |
| 5-6 | Moderate — matters but not decisive | Affects some sessions; persona would notice improvement but doesn't complain about current state |
| 3-4 | Low — nice to have | Rarely affects job success; peripheral to the core problem |
| 1-2 | Minimal — barely relevant | Theoretical concern only; persona wouldn't notice |

**Satisfaction scoring guide (based on alternative analysis):**

| Score | Meaning | Signals to look for |
|-------|---------|---------------------|
| 9-10 | Fully satisfied | Multiple alternatives solve this well; no complaints; mature solution space |
| 7-8 | Mostly satisfied | At least one alternative handles this adequately; minor friction remains |
| 5-6 | Partially satisfied | Alternatives attempt this but with significant limitations or workarounds |
| 3-4 | Poorly satisfied | Alternatives barely address this; users rely on willpower or manual effort |
| 1-2 | Not satisfied | No alternative addresses this; users have no real solution |

**Process for each outcome:**
1. Read the outcome statement
2. **Importance**: Judge based on how central this outcome is to the core problem and persona described in the use case
3. **Satisfaction**: Judge based on the Alternative Capability Matrix — how well do current alternatives collectively achieve this outcome?
4. **Calculate**: Score = Importance + max(Importance - Satisfaction, 0)
5. **Document reasoning**: 1-2 sentences explaining the scores, referencing specific alternatives or persona details

**Rules:**
- Do not default to high importance for everything — this destroys signal. Force-rank: no more than 30% of outcomes should score 9-10 on importance.
- Satisfaction should reflect the BEST available alternative for that specific outcome, not the average.
- When uncertain, bias satisfaction DOWN (toward underserved) — it's better to investigate a false positive than to miss a real opportunity.
- **Calibration anchor**: in real ODI surveys only a minority of outcomes turn out underserved — Bosch's circular-saw study found 14 of 75 (~19%) scoring above 10, and that was in a segment chosen *because* it was underserved. If more than ~1/3 of your outcomes score >= 10, you are almost certainly inflating importance or flooring satisfaction; recalibrate before proceeding.

### Step 3: Classify and Cluster Outcomes

Group scored outcomes into zones and identify clusters.

**Zone classification:**
- **Underserved** (Score >= 10): These are the opportunities. Sort by score descending.
- **Table Stakes** (Importance >= 7, Satisfaction >= 7): Must-match features — competitors handle these well, users expect them. Not a differentiation opportunity.
- **Overserved** (Satisfaction - Importance >= 3): Existing solutions over-deliver here. Opportunity for cost reduction or simplification.
- **Appropriately Served** (everything else): No urgent action needed.

**Cluster identification:**
Look for groups of 3-8 underserved outcomes that share a theme or job map step. These clusters represent addressable opportunity spaces — a product feature or capability that could serve multiple unmet needs simultaneously.

For each cluster:
1. Name it (2-4 words describing the theme)
2. List the outcomes it contains (by ID)
3. Sum the opportunity scores
4. Describe what a solution addressing this cluster would need to do (in outcome terms, not feature terms)

### Step 4: Analyze the Opportunity Landscape

Synthesize findings into a strategic picture.

**Assess the market condition:**
- If most outcomes are underserved → the market is ripe for a **differentiated** strategy (better, possibly more expensive)
- If outcomes split between underserved and overserved → opportunity for a **disruptive** strategy (simpler, cheaper for overserved; better for underserved)
- If many outcomes are table stakes with few underserved → market is mature; look for **niche segments** or **adjacent jobs**
- If underserved outcomes cluster around specific job steps → opportunity to **expand job coverage** (address steps competitors ignore)

**Segment-masking caveat**: this analysis scores against a single persona, which acts as a proxy for one outcome-based segment. Ulwick's Bosch case is the warning: the aggregate market showed *zero* unmet needs, while a segment covering 30% of the market had 14. A flat, "appropriately served" landscape may mean the persona is drawn too broadly — consider whether a sharper sub-persona would reveal a different landscape, and say so in Confidence & Limitations.

**Identify the recommended growth strategy** using the JTBD Growth Strategy Matrix (Ulwick, ch. 3) — a 2×2 of job performance (better/worse) × price (higher/lower), yielding five strategies:

| Strategy | Gets the job done | Price | When to recommend |
|----------|-------------------|-------|-------------------|
| **Differentiated** | Significantly better | Higher | Many underserved outcomes; users willing to pay for better; current alternatives are feature-poor. Can win outsized profit share on small market share (Nest: <10% share, >25% profit share at 7× competitors' price) |
| **Dominant** | ≥ ~20% better | ≥ ~20% cheaper | Technology enables both better AND cheaper; automation can replace manual alternatives — the most appealing strategy for a new entrant because incumbents cannot defend against it (ch. 3) |
| **Disruptive** | Worse (but good enough) | Cheaper | Overserved segment exists (paying for capability they don't need) or nonconsumers are locked out (for them even a "worse" product beats having nothing); simpler/cheaper solution viable |
| **Discrete** | Worse | Higher | Users are captive — legally, physically, emotionally, or circumstantially restricted with no alternatives (airport concessions, EpiPen). Rarely a recommendation for a new product; flag it if the data suggests it, and note it erodes as restrictions lift and risks reputational backlash (Mylan) |
| **Sustaining** | Slightly better (<5%) | Slightly cheaper | Almost never recommend for a new entrant — it defends an incumbent's share but wins no new customers ("stuck in the middle", per Porter) |

**Strategy-selection guardrails (from the book):**
- **The 20% rule**: customers rarely switch for less than a ~20% improvement in getting the job done (or in price). If the underserved clusters only support incremental gains, say so — a "slightly better" concept is stuck in the middle and will fail to convert users from alternatives.
- **Segmentation prerequisite**: a differentiated strategy fails without an underserved segment and a disruptive one fails without an overserved segment. Tie the recommendation explicitly to the zones found in Step 3 — never recommend a strategy the scored data doesn't evidence.
- Strategies apply at the **product level, not the company level** (Uber runs UberBLACK/differentiated, UberX/dominant, and UberPOOL/disruptive simultaneously). Differentiated often serves as a stepping stone to dominant as costs fall.

**Assess the competitive gap:**
- Which job map steps have the HIGHEST concentration of underserved outcomes? These are the steps where competitors are weakest.
- Which steps are table stakes? These must be matched but won't differentiate.
- Are there entire steps with NO alternative coverage? These are blue-ocean opportunities.

### Step 5: Generate Opportunity Brief

Synthesize everything into a concise strategic summary that bridges to solution ideation.

The brief should answer:
1. **Where are the biggest opportunities?** (top 3 clusters with scores)
2. **What strategy should a product pursue?** (growth strategy + reasoning)
3. **What must a minimum viable product address?** (table stakes + top underserved cluster)
4. **What should a product NOT try to do?** (overserved outcomes, appropriately served areas)
5. **What related jobs amplify the opportunity?** (from the job map's related jobs list, which ones align with underserved clusters)
6. **What is the outcome-based value proposition?** One sentence, phrased in the language of the top unmet outcomes — not features. Ulwick's Coloplast case is the model: segmentation showed 10 of the segment's top 15 unmet needs concerned preventing wounds from worsening, so repositioning from "heals wounds faster" to "we prevent complications" drove double-digit growth in under six months with no product or pricing changes. The unmet needs of today are the winning value propositions of the future.

### Write `opportunity-scores.md`

Produce an `opportunity-scores.md` file in the same folder as the job map.

**Document structure:**

```markdown
# Opportunity Scores: [Core Functional Job]

## Source
- **Use Case**: [title and id]
- **Job Map**: [title and id]
- **Persona**: [one-line summary]
- **Scoring Method**: Expert surrogate analysis based on [N] alternatives

## Alternative Capability Matrix

| Alternative | Define | Locate | Prepare | Confirm | Execute | Monitor | Modify | Conclude | Structural Limitation |
|-------------|--------|--------|---------|---------|---------|---------|--------|----------|-----------------------|
| ...         | ...    | ...    | ...     | ...     | ...     | ...     | ...    | ...      | ...                   |

## Scored Outcomes

### 1. Define

| ID | Desired Outcome | Imp | Sat | Score | Zone | Reasoning |
|----|----------------|-----|-----|-------|------|-----------|
| DEF-01 | [outcome] | [1-10] | [1-10] | [calc] | [zone] | [1-2 sentences] |
| ... | ... | ... | ... | ... | ... | ... |

### 2. Locate
[repeat pattern]

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

### Consumption Chain

| ID | Desired Outcome | Imp | Sat | Score | Zone | Reasoning |
|----|----------------|-----|-----|-------|------|-----------|
| CONS-01 | [outcome] | [1-10] | [1-10] | [calc] | [zone] | [1-2 sentences] |
| ... | ... | ... | ... | ... | ... | ... |

## Opportunity Landscape

### Distribution Summary

| Zone | Count | % of Total | Avg Score |
|------|-------|-----------|-----------|
| Extreme (15+) | [n] | [%] | [avg] |
| High (12-14.9) | [n] | [%] | [avg] |
| Moderate (10-11.9) | [n] | [%] | [avg] |
| Appropriately Served | [n] | [%] | [avg] |
| Table Stakes | [n] | [%] | — |
| Overserved | [n] | [%] | — |

### Underserved Outcomes (Score >= 10, ranked)

| Rank | ID | Desired Outcome | Score | Job Step |
|------|----|----------------|-------|----------|
| 1 | [id] | [outcome] | [score] | [step] |
| 2 | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

### Overserved Outcomes (Satisfaction >> Importance)

| ID | Desired Outcome | Imp | Sat | Gap | Job Step |
|----|----------------|-----|-----|-----|----------|
| [id] | [outcome] | [imp] | [sat] | [sat-imp] | [step] |

### Table Stakes (Imp >= 7, Sat >= 7)

| ID | Desired Outcome | Imp | Sat | Job Step |
|----|----------------|-----|-----|----------|
| [id] | [outcome] | [imp] | [sat] | [step] |

## Opportunity Clusters

### Cluster 1: [Name]
- **Outcomes**: [ID-01, ID-02, ID-03, ...]
- **Combined Score**: [sum]
- **Job Steps Involved**: [which steps]
- **Theme**: [what these outcomes have in common]
- **What a solution must do**: [description in outcome terms, not feature terms]

### Cluster 2: [Name]
[repeat pattern]

### Cluster 3: [Name]
[repeat pattern]

[additional clusters as needed]

## Step-Level Analysis

| Job Step | Underserved | Table Stakes | Overserved | Opportunity Density |
|----------|-------------|-------------|------------|---------------------|
| 1. Define | [n] | [n] | [n] | [high/medium/low] |
| 2. Locate | [n] | [n] | [n] | [high/medium/low] |
| 3. Prepare | [n] | [n] | [n] | [high/medium/low] |
| 4. Confirm | [n] | [n] | [n] | [high/medium/low] |
| 5. Execute | [n] | [n] | [n] | [high/medium/low] |
| 6. Monitor | [n] | [n] | [n] | [high/medium/low] |
| 7. Modify | [n] | [n] | [n] | [high/medium/low] |
| 8. Conclude | [n] | [n] | [n] | [high/medium/low] |
| Consumption Chain | [n] | [n] | [n] | [high/medium/low] |

## Growth Strategy Recommendation

**Recommended Strategy**: [Differentiated / Dominant / Disruptive / Discrete / Sustaining]

**Reasoning**: [3-5 sentences grounded in the scored data — which zones dominate, what the alternative landscape looks like, what the persona's willingness to pay/switch suggests. Confirm the 20% rule: would the addressed clusters make the job meaningfully (~20%+) better or cheaper than the best alternative?]

**Outcome-based value proposition**: [one sentence phrased in the language of the top unmet outcomes, not features — the Coloplast "we prevent complications" pattern]

**Implications for solution design:**
- **Must address** (table stakes): [list the table-stakes outcomes a product cannot skip]
- **Differentiate on** (top underserved clusters): [the clusters that create competitive advantage]
- **Simplify or skip** (overserved): [outcomes where current alternatives already over-deliver — do not invest here]
- **Expand into** (related jobs): [which related jobs from the job map align with the top opportunity clusters]
- **Path to address** (optional): [which of ODI's seven product-strategy actions fit the top clusters — borrow existing features, accelerate the pipeline, partner/license, acquire, devise new features, devise new subsystems/services, or conceptualize the ultimate single-platform solution (Ulwick ch. 4)]

## Opportunity Brief

[A concise 5-8 sentence strategic summary answering: What are the biggest opportunities? What strategy should a product pursue? What does an MVP need? What should it NOT do? This paragraph is the bridge to solution ideation — it should be self-contained enough that someone could read only this and understand what to build toward.]

## Confidence & Limitations

- **Scoring method**: Expert surrogate (AI analysis of alternatives and persona), not user survey
- **Confidence level**: [Low / Medium / High] — based on how detailed the use case's alternatives and persona sections are
- **To validate**: [2-3 specific suggestions for real-world validation — e.g., "survey N users on the top 10 underserved outcomes" or "test whether [specific outcome] resonates in user interviews"]
- **Known blind spots**: [any areas where the use case lacked detail, making scoring speculative]
- **Segment coverage**: [the persona scored here is a proxy for one outcome-based segment — note whether a broader or narrower persona could shift the landscape, per the segment-masking caveat]
```

## Quality Checklist

Before finalizing, verify:

- [ ] Every desired outcome from the job map has been scored, including the consumption chain (CONS-*) outcomes — none skipped
- [ ] Every score has documented reasoning (no naked numbers)
- [ ] Importance distribution is realistic (not >30% at 9-10)
- [ ] Underserved share is plausible (not more than ~1/3 of outcomes at score >= 10 — see the Bosch calibration anchor)
- [ ] Satisfaction scores reference specific alternatives
- [ ] Opportunity scores are calculated correctly: Imp + max(Imp - Sat, 0)
- [ ] Zone classifications are correct per the thresholds
- [ ] At least 2 opportunity clusters are identified with 3+ outcomes each
- [ ] Growth strategy recommendation is one of the five strategies, references the scored data, and checks the 20% rule
- [ ] An outcome-based value proposition is stated in outcome language, not feature language
- [ ] Table stakes are identified (products that ignore these will fail)
- [ ] Overserved outcomes are identified (products should not over-invest here)
- [ ] Confidence and limitations are honestly stated (including which chapters were consulted via the JTBD RAG, if it was used)
- [ ] The opportunity brief is self-contained and actionable

## References

- For the full opportunity algorithm, scoring guides, calibration anchors, and growth strategy matrix, see `references/scoring-methodology.md`.
- For book-grounded answers to methodology questions, use the `rag-jtbd:jtbd` skill if installed (see "Methodology grounding" above).
