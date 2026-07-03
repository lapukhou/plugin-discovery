---
name: use-case-map
description: "Guides users through defining customer use cases using the Use Case Map framework (Problem, Persona, Alternative, Why, Frequency). This skill should be used whenever the user is brainstorming app ideas, defining a product concept, exploring who their customers are, thinking about product-market fit, analyzing retention strategy, mapping use cases, or doing any kind of product ideation. Also trigger when the user mentions customer problems, target personas, competitive alternatives, user motivations, usage frequency, or wants to validate whether an app idea solves a real problem. Even if the user just says 'I have an app idea' or 'help me think through this product concept,' use this skill to structure their thinking."
---

# Customer Use Case Expert

Guide users through defining customer use cases using the **Use Case Map** framework. A use case describes an **opportunity** — a problem worth solving for a specific audience — not a specific product. The framework captures who has the problem, how they cope today, why a better solution matters, and how often the problem recurs. This opportunity-first lens is the foundation of product strategy, retention, and growth.

## Opportunity-First Principle

A use case is always framed around the **opportunity** (the unmet need or underserved problem in the market), never around a particular product or solution. Products are one possible response to an opportunity; the opportunity exists independently of any product.

When a user provides a **specific product** as input (e.g., "I want to build an AI budget tracker"), do not describe the product — instead, extract the underlying opportunity or opportunities the product would address. A single product may map to multiple distinct opportunities. For each opportunity, walk through the full Use Case Map.

**How to extract opportunities from a product:**
1. Ask: "What problem does this product solve?" — the answer is the opportunity
2. If the product serves multiple personas with different behaviors, each persona-problem pair is a separate opportunity
3. Strip away the product's specific solution mechanism — what remains is the opportunity
4. Name the opportunity by the need, not the product (e.g., "Personal Expense Visibility" not "AI Budget Tracker")

**Examples:**
- Product input: "Scroll-breaking app" → Opportunity: "Reclaiming Attention from Compulsive Scrolling"
- Product input: "AI budget tracker" → Opportunity: "Personal Expense Visibility for Young Professionals"
- Product input: "Thumbtack" → Two opportunities: "Finding Reliable Home Service Professionals" (customer side) + "Acquiring Higher-Quality Customers for Home Services" (pro side)

## Language

Conduct the entire workflow in English — questions, discussion, and all generated artifacts (Use Case Map summaries, frontmatter). The Use Case Map framework uses English terminology and examples, and keeping everything in one language ensures consistency across the output. If the user writes in another language, respond in English and continue the framework in English.

## The Use Case Map

Every use case has five elements. Walk through each one, applying them to the user's specific app idea or product concept.

### 1. Problem

The specific issue users face, articulated in their own words.

Find the sweet spot — narrow enough to focus teams, broad enough not to miss the bigger picture.

- Too broad: "I want to be a better person" (Headspace) — pulls teams in every direction
- Too narrow: "I want to create playlists" (Spotify) — misses the real job of listening to music
- Just right: "I want to listen to music" (Spotify) — focused but expansive enough for strategy

Prompt the user with:
- "What problem does your product solve, in the user's own words?"
- "If your users didn't have your product, what would they struggle with?"

### 2. Persona

The demographic (B2C) or firmographic (B2B) characteristics of target users.

When multiple personas emerge, determine whether they differ in behavior:
- **Different behaviors** = separate use cases (e.g., HubSpot Sales Hub: Sales Reps vs Enterprise Teams have different alternatives and motivations)
- **Same behaviors** = single use case (e.g., Spotify: college students and working professionals use it the same way)

Prompt the user with:
- "Who specifically has this problem? Describe them."
- "Are there distinct user groups that would use this differently?"

### 3. Alternative

The other ways users solve the problem today — NOT just direct competitors.

This distinction is critical. Alternatives are often non-obvious and much larger than the competitor set:
- Slack's alternative was email, not HipChat
- Pinterest's alternative was cutting images from magazines, not other pinboard apps
- DocuSign's alternative was pen-and-ink signatures and FedEx, not HelloSign

Understanding alternatives reveals: (a) how to differentiate, (b) a much larger addressable market (10x-1000x vs competitors), (c) the natural frequency of the problem.

Prompt the user with:
- "If your product didn't exist, how would people solve this problem today?"
- "What did people do before products like yours existed?"

### 4. Why (Core Motivation + Differentiator)

**Core motivation** — the reason users choose the product. Falls into three categories:

| Category | Description | Sub-types |
|----------|-------------|-----------|
| **Personal** | Self-interested utility | Entertainment, Communication, Information, Flexibility, Time |
| **Financial** | Monetary value | More Transactions, Save Money, New Customers, Loss Prevention |
| **Social** | Emotional/status value | Recognition, Connection, Competition, Confidence |

**Differentiator** — how the product is specifically different from alternatives. Avoid generic claims ("we're better," "easier to use"). Articulate with contrast and specificity:
- HubSpot: "All-in-one vs. stringing together 10+ tools"
- Pinterest: "Most personalized visual content, powered by data at scale"
- Amazon: "Widest selection, fastest delivery, most competitive pricing"

Prompt the user with:
- "Why would someone choose your product over the alternative they use today?"
- "What is the one thing your product does that the alternative simply can't?"

### 5. Frequency

How often users encounter the problem — NOT how often they use the product.

**The Frequency Spectrum:**
- **Daily**: Slack, Instagram, Snapchat
- **Weekly**: Zoom, Figma, Miro
- **Monthly**: SurveyMonkey, Birchbox, Mint
- **Quarterly/Half-yearly**: Airbnb, Everlane, Allbirds
- **Yearly**: TurboTax
- **Multi-year**: Zillow (home buying), Carvana, Babylist

**Habit Zone vs Forgettable Zone:**
- Daily to monthly = **Habit Zone** — easier to build retention
- Less than monthly = **Forgettable Zone** — risk of re-acquiring users every time; consider layering higher-frequency use cases (e.g., Zillow added Zestimate score tracking to stay top of mind between home purchases)

Prompt the user with:
- "How often does someone experience this problem?"
- "Is your product in the habit zone or forgettable zone?"

## Managing Multiple Use Cases

When the product has or could have multiple use cases, guide prioritization:

- **Dominant use case**: Drives >75% of usage. Focus here first and deliver a 10x experience before expanding (e.g., Jira focused on developer project tracking before expanding to product management).
- **Anti-use cases**: Cases the product *could* serve but actively chooses not to. Defining these prevents dilution (e.g., Confluence choosing not to serve static documentation/wiki use case to protect their collaborative editing loop).
- **Evolving use cases**: Problems and personas shift over time. Plan for natural evolution (e.g., Uber: UberBlack high-end → UberPool daily commuters).

Three common reasons to add use cases:
1. **Market expansion** — tapping out on current market (Spotify: music → podcasts)
2. **Low frequency** — need higher-frequency hooks (Zillow: home buying → Zestimate tracking)
3. **User evolution** — personas naturally grow (Figma: individual → team → enterprise)

## Workflow

When a user brings an idea — whether a raw problem, a product concept, or a specific app — work through these steps:

1. **Capture the raw input** — let the user describe it freely
2. **Extract opportunities** — if the input is a specific product, decompose it into one or more underlying opportunities (see "Opportunity-First Principle" above). If it's already a problem/need, proceed directly.
3. **For each opportunity:**
   1. **Define the Problem** — refine into a well-scoped problem statement in the user's words
   2. **Identify the Persona** — who has this problem; do multiple personas with different behaviors warrant separate opportunities?
   3. **Map Alternatives** — brainstorm what users do today without any product solving this
   4. **Articulate the Why** — identify core motivation category and what a better solution would offer vs. alternatives
   5. **Estimate Frequency** — place on the spectrum, flag if in forgettable zone
4. **Synthesize the Use Case Map(s)** — present a clean summary of all five elements for each opportunity
5. **Stress test** — challenge assumptions, explore edge cases, identify risks

For detailed real-world examples (Figma, Thumbtack, HubSpot, Pinterest, Netflix, Zillow, and more), read `references/use-case-map-deep-dive.md`.

## Output Format

After working through the framework, produce a **Use Case Map Summary** as an MD file.

### Folder naming

Place each use case in its own folder named `<slug>`, where `<slug>` is a short kebab-case label derived from the use case title. Examples: `ai-budget`, `music-streaming`, `team-collaboration`. Name the MD file inside the folder **`use-case-map.md`**.

### Template

Template for `use-case-map.md`:
```
# Use Case Map: <slug>

## Problem
[Problem statement in the user's words — what they struggle with, independent of any product]

## Persona
[Target user description with key demographic/firmographic attributes]

## Alternatives
[List of alternative solutions users employ today — how they cope without a product solving this]

## Why
- **Core Motivation**: [Personal/Financial/Social] — [specific reason]
- **Differentiator**: [what a better solution would offer vs. the alternatives]

## Frequency
[Estimated frequency] — [Habit Zone / Forgettable Zone]
[If forgettable zone: suggestion for higher-frequency hooks]
```
