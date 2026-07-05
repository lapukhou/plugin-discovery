# Scoring Methodology Reference

Reference material for the Opportunity Scorer skill, covering the Opportunity Algorithm, scoring heuristics, and growth strategy analysis.

## The Opportunity Algorithm

**Source**: Anthony W. Ulwick, "Jobs to Be Done: Theory to Practice", Chapters 4, 6, 7, 10.

### Formula

```
Opportunity Score = Importance + max(Importance - Satisfaction, 0)
```

- Both Importance and Satisfaction are rated on a 1-10 scale
- Maximum possible score: 20 (Importance = 10, Satisfaction = 0)
- Minimum possible score: 2 (Importance = 1, Satisfaction = 1)
- **Provenance**: ch. 4 states the formula as `importance + (importance − satisfaction)`; the `max(…, 0)` floor is Ulwick's standard practical form — when satisfaction exceeds importance the surplus is not subtracted, it instead flags the outcome as overserved (a cost-reduction target, and the precondition for a disruptive strategy)

### Score Interpretation

| Score Range | Zone | Strategic Action |
|-------------|------|-----------------|
| 15-20 | Extreme opportunity | Highest priority — users care deeply and nothing serves them. A product addressing these outcomes will win. |
| 12-14.9 | High opportunity | Strong unmet needs. Primary zone for feature investment and differentiation. |
| 10-11.9 | Moderate opportunity | Genuinely underserved. Solid targets for product improvement. |
| 6-9.9 | Appropriately served | Current alternatives handle these adequately. Improvement here adds marginal value. |
| < 6 with Sat >> Imp | Overserved | Existing solutions over-deliver on outcomes users don't value highly. Simplify or reduce cost. |

### Why This Formula Works

The formula asymmetrically weights underserved outcomes:
- When Importance > Satisfaction, the gap is added to Importance (double-counting the gap)
- When Satisfaction >= Importance, only Importance counts (no penalty for over-delivery)

This means a score of 10 genuinely indicates unmet need — the user cares about the outcome AND current solutions fail to deliver.

### Edge Cases

- **Imp = 10, Sat = 10** → Score = 10: Table stakes. Critically important and well-served. Must match but cannot differentiate.
- **Imp = 10, Sat = 1** → Score = 19: Extreme opportunity. Highest possible underservice.
- **Imp = 3, Sat = 9** → Score = 3: Overserved. Alternatives deliver far more than users need.
- **Imp = 5, Sat = 5** → Score = 5: Appropriately served. No action needed.

## Expert Surrogate Scoring Method

In a full ODI engagement, scores come from surveying 180-3,000 representative users. The expert surrogate method adapts this for contexts where a real survey isn't available.

### Principles

1. **Ground every score in evidence**, not intuition. Reference specific alternatives, persona details, or problem statements.
2. **Use the alternatives as satisfaction proxies.** If three alternatives all fail at a specific outcome, satisfaction is low. If even one alternative handles it well, satisfaction is moderate-to-high.
3. **Use the problem statement as importance calibration.** Outcomes directly tied to the core problem described in the use case get higher importance. Peripheral outcomes get lower importance.
4. **Force distribution.** In real surveys, importance scores naturally distribute across the range. When scoring synthetically, consciously avoid clustering everything at 8-10. Aim for:
   - 20-30% of outcomes at importance 8-10
   - 40-50% at importance 5-7
   - 20-30% at importance 1-4

### Importance Estimation Heuristics

| Signal | Importance Level | Reasoning |
|--------|-----------------|-----------|
| Mentioned in Problem section as core pain | 9-10 | The use case author identified this as the central issue |
| Directly affects the primary success metric of the job | 8-9 | Failure here means the job fails |
| Affects most sessions/occurrences | 7-8 | Consistent impact across uses |
| Causes noticeable frustration when unmet | 6-7 | Users feel it but can work around it |
| Affects only some sessions | 5-6 | Intermittent relevance |
| Relevant but peripheral to core pain | 3-4 | Nice to have, not need to have |
| Theoretical concern, not experienced pain | 1-2 | Unlikely to drive behavior change |

### Satisfaction Estimation Heuristics

| Signal | Satisfaction Level | Reasoning |
|--------|-------------------|-----------|
| Multiple alternatives handle this well | 9-10 | Solved problem — competitive to improve |
| At least one alternative handles this adequately | 7-8 | Users have a viable option |
| Alternatives attempt this but with major friction | 5-6 | Partial solutions exist with workarounds |
| Only willpower or manual effort addresses this | 3-4 | No real solution — users cope, not solve |
| No alternative even attempts this | 1-2 | Complete gap in the solution landscape |

### Calibration Anchor: The Bosch Benchmark

In Bosch's circular-saw study (270 respondents, 75 outcomes), only **14 outcomes (~19%) scored above 10** — and that was within a segment specifically chosen for being underserved. Real opportunity landscapes are mostly "appropriately served" with a minority of genuine gaps. If more than ~1/3 of scored outcomes land at score >= 10, the scoring is inflated (importance too high, or satisfaction floored) — recalibrate before drawing conclusions.

### Common Scoring Errors

1. **Importance inflation**: Rating everything 8-10 because the use case focuses on a real problem. Remember: not every outcome within the job is equally critical.
2. **Satisfaction floor**: Rating all satisfaction at 1-3 because "nothing works." Most alternatives solve some aspects well — that's why people use them. Satisfaction should vary across outcomes.
3. **Anchoring on the worst alternative**: Satisfaction should reflect the BEST available option for each specific outcome, not the worst or the average.
4. **Conflating related jobs with core outcomes**: Related jobs have their own importance independent of the core job. Don't score them on the same scale.
5. **Ignoring willpower as an alternative**: "Just stop scrolling" is a real alternative users attempt. It scores well on some outcomes (no cost, no setup) and terribly on others (no consistency, no external support).

## Alternative Analysis Method

### Building the Capability Matrix

For each alternative from the use case:

1. **List what it does** — specific capabilities, not vague descriptions
2. **Map to job steps** — which of the 8 Universal Job Map steps does it address?
3. **Rate coverage** — 0 (not addressed), 1 (partially), 2 (well addressed)
4. **Identify structural limitations** — why can't this alternative improve? (e.g., willpower is limited by decision fatigue at bedtime; iOS Bedtime mode can't block apps without breaking core phone functionality)

### Structural Limitations Matter

The most valuable insight from alternative analysis is understanding WHY alternatives fail. Structural limitations reveal outcomes that the entire category of existing solutions cannot address — these are the deepest opportunities.

Types of structural limitations:
- **Architectural** — the solution's core design prevents improvement (e.g., a screen dimmer can't address the behavioral problem of not stopping)
- **Motivational** — the alternative requires sustained willpower that depletes predictably (e.g., phone curfews that rely on self-discipline at the lowest-willpower moment of the day)
- **Scope** — the alternative only addresses one step of the job (e.g., sleep apps help with falling asleep but not with stopping scrolling)
- **Timing** — the alternative intervenes too late or too early (e.g., screen time reports show data the next day, when the scrolling has already happened)
- **Integration** — the alternative doesn't connect with the user's existing workflow (e.g., physical books require setup that competes with the zero-friction phone)

## Opportunity Clustering

### What Makes a Good Cluster

A cluster is a group of 3-8 underserved outcomes that:
1. Share a **thematic connection** (they all relate to the same aspect of the job)
2. Could plausibly be addressed by a **single product capability** or feature area
3. Span at least **2 job map steps** (clusters within a single step are too narrow; they're features, not opportunities)

### Cluster Naming

Name clusters with 2-4 words that describe the shared theme in outcome language, not solution language:
- Good: "Sleep transition friction" (describes the unmet need space)
- Bad: "Wind-down timer feature" (describes a solution)

### Cluster Scoring

Sum the opportunity scores of all outcomes in the cluster. Higher total = larger opportunity. But also consider:
- **Density**: A cluster of 3 outcomes scoring 15 each (total 45) is more focused than 8 outcomes scoring 6 each (total 48)
- **Span**: Clusters spanning multiple job steps suggest platform-level opportunities
- **Alignment with emotional jobs**: Clusters that also connect to emotional/social jobs have stronger user motivation

## Growth Strategy Matrix

### The Five Strategies

| Strategy | Performance | Cost | Target Segment | Key Requirement |
|----------|------------|------|----------------|-----------------|
| **Differentiated** | Much better | Same or higher | Underserved users | Many unmet needs to address; users willing to pay premium. Book example: Nest — <10% market share but >25% profit share at 7× competitors' price |
| **Dominant** | ≥ ~20% better | ≥ ~20% lower | All users | Technology/automation enables better AND cheaper. "Always the most appealing approach for a new market entrant because incumbents cannot defend against it" (ch. 3). Examples: Google Search, UberX, Netflix streaming, Bosch CS20 |
| **Disruptive** | Worse (but good enough) | Much lower | Overserved users / nonconsumers | Significant overserved segment exists, or nonconsumers for whom even a "worse" product beats having nothing; simpler solution viable. Examples: Google Docs, TurboTax, UberPOOL |
| **Discrete** | Worse | Higher | Restricted/captive users | Users have no alternatives in specific contexts (legally, physically, emotionally, or circumstantially restricted — airport concessions, check-cashing, EpiPen). Profitable but risks reputational backlash (Mylan), and erodes as restrictions lift |
| **Sustaining** | Slightly better (<5%) | Slightly lower | Existing users only | Incremental improvement — defends an incumbent's share but wins no new users ("stuck in the middle", per Porter) |

### Strategy Selection from Opportunity Data

| Opportunity Landscape Pattern | Recommended Strategy | Reasoning |
|-------------------------------|---------------------|-----------|
| Most outcomes underserved, few overserved | **Differentiated** | Large unmet need space; users will pay for a solution that works |
| Mix of underserved and overserved | **Disruptive** then **Dominant** | Enter cheap for overserved segment, iterate upward |
| Most outcomes are table stakes, few underserved | **Dominant** (if possible) or **Niche differentiated** | Market is mature; need tech advantage or narrow focus |
| Underserved outcomes cluster in ignored job steps | **Job expansion** (variant of differentiated) | Address steps competitors don't even try |
| Few alternatives exist at all | **Dominant** | Greenfield — build the comprehensive solution |

### Prerequisites and Scope

- A differentiated strategy fails without an underserved segment; a disruptive strategy fails without an overserved one — strategy selection must follow from the opportunity data, never from preference.
- Strategies apply at the **product level, not the company level**: Uber runs differentiated (UberBLACK), dominant (UberX), and disruptive (UberPOOL) simultaneously.
- Differentiated commonly serves as a stepping stone to dominant as costs fall (Apple iPhone line, Uber).

### From Strategy to Action (ODI steps 9-10, ch. 4)

Once a growth strategy is chosen, the book prescribes concrete follow-through. Use these lists when the opportunity brief needs to point beyond "what to build" toward "how to act on it":

**Market strategy — six activities:**
1. Target offerings to the segments they fit best
2. Communicate product strengths that are going un-messaged (Cordis grew share 1.5% → 5% this way, with no product change)
3. Build an outcome-based value proposition (the Coloplast pattern)
4. Build digital marketing around unmet-outcome keywords
5. Assign leads to outcome-based segments
6. Arm sales teams with outcome-based tools

**Product strategy — seven possible actions per underserved segment:**
1. Borrow features from other internal products
2. Accelerate the pipeline / R&D toward the unmet outcomes
3. Partner or license
4. Acquire a company that fills the gap (Arm & Hammer acquired Vi-COR for exactly this)
5. Devise new features
6. Devise new subsystems or services
7. Conceptualize the ultimate single-platform solution

### The Three Job Executor Types (ch. 4)

ODI recognizes three customer roles, each supplying different outcomes. When scoring, judge importance from the perspective of the executor who owns that outcome:

- **End user** — executes the core functional job; supplies the functional desired outcomes plus emotional and related jobs
- **Product life-cycle support team** — handles the consumption chain jobs (install, set up, learn, maintain, dispose); owns the CONS-* outcomes
- **Purchase decision maker** — supplies financial desired outcomes (may not be the end user at all)

### The 20% Rule

A product must get the job done at least 20% better OR 20% cheaper to compel users to switch from their current alternative. When evaluating whether opportunity clusters are large enough:
- Count the underserved outcomes the product would address
- Divide by total outcomes
- If addressing these outcomes would improve the overall job completion by ~20%, the product has a viable value proposition

## Confidence Calibration

### When Expert Surrogate Scoring Is Higher Confidence

- The use case has **detailed alternatives** (5+ alternatives with specific strengths/weaknesses described)
- The persona section describes **specific behaviors** (not just demographics)
- The problem section includes **quantitative signals** (e.g., "average 45-minute delay", "6-6.5 hours of sleep")
- The strategic notes section provides **market context** (evolution path, risks, anti-use-cases)

### When Expert Surrogate Scoring Is Lower Confidence

- The use case has **few or vague alternatives** ("competitors" without detail)
- The persona is **broad** ("adults 20-60 who...")
- The problem is **qualitative only** (no behavioral data)
- The job involves **highly personal variation** (emotional or social jobs dominate)

### Validation Recommendations

Always suggest concrete next steps for validating the highest-impact findings:
1. **Quick validation**: Show top 5 underserved outcomes to 5-10 target users; ask "How important is this to you? How well does your current approach handle it?"
2. **Medium validation**: In-app survey on the top 15 outcomes (importance + satisfaction, 1-5 scale) with 50-100 respondents
3. **Full validation**: ODI-standard survey (all outcomes, 1-10 scale, 180+ respondents, factor + cluster analysis for segmentation)

## Source

All frameworks from: Ulwick, A. W. (2016). *Jobs to Be Done: Theory to Practice*. IDEA BITE PRESS.

- Opportunity Algorithm and opportunity landscape: ch. 4, 8
- Growth Strategy Matrix and the five strategies: ch. 3 (full treatment), ch. 8 (glossary)
- Outcome-Based Segmentation and the segment-masking effect: ch. 3-5 (Bosch, Arm & Hammer)
- Market/product strategy actions: ch. 4 (ODI steps 9-10)
- Case studies: Bosch CS20 (ch. 2, 4, 5), Coloplast (ch. 4), Cordis (ch. 4)

For book-grounded answers beyond this summary, query the `rag-jtbd:jtbd` skill (if installed) — it retrieves from a chapter-by-chapter knowledge base of the book.
