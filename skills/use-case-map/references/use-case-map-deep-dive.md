# Use Case Deep Dive — Real-World Examples

This reference contains detailed real-world examples for each element of the Use Case Map. Load this when users need inspiration or want to see how established products defined their use cases.

## Table of Contents
1. [Use Case Examples by Company](#use-case-examples-by-company)
2. [Problem Definition — Pitfalls and Examples](#problem-definition)
3. [Persona Scenarios](#persona-scenarios)
4. [Alternatives vs. Competitors](#alternatives-vs-competitors)
5. [Core Motivations Taxonomy](#core-motivations-taxonomy)
6. [Differentiator Examples](#differentiator-examples)
7. [Frequency Spectrum Details](#frequency-spectrum-details)
8. [Multiple Use Case Strategies](#multiple-use-case-strategies)
9. [Common Pitfalls](#common-pitfalls)

---

## Use Case Examples by Company

### Pinterest
- **Use Case 1 — Browsing Interests**: Users who are bored and want to browse things they're interested in. Weekly frequency with a long lifetime. This is the **dominant use case**.
- **Use Case 2 — Planning a Project**: Users with a specific project (planning a wedding, decorating a home) looking for inspiration. Very high frequency during the project, then drops off.
- Pinterest chose to focus on the dominant browsing use case — it's far more popular and accounts for the bulk of activity.

### Airbnb
- **Guests**: Finding a place to stay when traveling. Quarterly/half-yearly frequency.
- **Hosts**: Looking for supplemental income, typically owners of a second home or home with extra space. Monthly frequency.

### Slack
- **First user**: Setting up a group chat and getting everything running. One-time onboarding frequency.
- **Second-plus user**: Solving communication problems, entering at a different lifecycle point. Daily frequency.
- Primary alternative was email, not competing chat products.

### Figma (B2B SaaS — Collaborative Design)

**Three use cases segmented by team size:**

| Element | Starter | Professional | Organization |
|---------|---------|-------------|-------------|
| **Problem** | "I want to collaborate with 1-2 others on a design project" | "I need to collaborate on visuals with my small team of 3-10" | "My large design team needs to collaborate securely using a robust design system" |
| **Persona** | Individual/freelance designer | Lead of a small design team | Lead of a larger design org (50+) |
| **Alternatives** | Email, Slack threads, design reviews | Same + Invision | Adobe XD, Static, annotated documents |
| **Core Motivation** | Personal: save time, collaborate flexibly | Personal: save time, flexibility | Personal: save time, flexibility |
| **Differentiator** | Much easier to collaborate than any other method | Easier collaboration with groups of 5-6 vs. review sessions | Per-editor pricing + enterprise features (SSO, design systems) |
| **Frequency** | Weekly | Weekly | Weekly |

Figma's use cases illustrate natural **user evolution** — a user starts on Starter, their team grows, they migrate to Professional, and eventually to Organization.

### Thumbtack (Marketplace — Home Services)

**Three use cases across two sides of the marketplace:**

**Pro side — Short-term Gig:**
- **Problem**: "I need more customers for my small business"
- **Persona**: Home service professionals (gardeners, plumbers) — low ticket size, weekly gigs
- **Alternatives**: Referrals, word of mouth, local ads, Google, Yelp, HomeAdvisor, Angie's List
- **Why**: Financial — more customers, more money. Differentiator: higher-quality customers who pay more and return
- **Frequency**: Weekly

**Pro side — Long-term Project** (later expansion):
- **Persona**: Architects, interior designers — high ticket size, year-long projects
- **Frequency**: Quarterly to yearly — fundamentally different from short-term gig pros

**Customer side:**
- **Problem**: "I need an easy way to find high-quality home professionals for a job for my home"
- **Persona**: Young working professionals in cities/suburbs
- **Alternatives**: Referrals, word of mouth, Google, Yelp, HomeAdvisor, Angie's List
- **Why**: Personal (easy, reputable) + Financial (compare bids, save money). Differentiator: easier and quicker to find pros with high-quality reviews
- **Frequency**: Monthly (~10 projects/year across categories)

Thumbtack first proved out short-term services before expanding to long-term projects. They actively chose NOT to serve adjacent use cases like property rentals, roommate finding, or secondhand sales (anti-use cases).

### HubSpot Sales Hub

**Problem**: "I spend countless hours on inefficient activities like CRM data entry, following up, rewriting emails"

Four personas with different behaviors → four separate use cases:
- **Sales Reps** (mid-size companies): Want to automate and save time
- **Sales Operations Executives**: Want full control and customization over toolsets
- **Enterprise Teams**: Value security features and existing system integrations
- **Individual Business Owners**: Limited budgets, need simple lead/customer management

The dominant use case targets Sales Reps in companies of 50-2,000 employees. Spreading across all four would dilute resources.

---

## Problem Definition

### Finding the Sweet Spot

The problem statement should be narrow enough to give teams clear direction, but broad enough that they don't miss the bigger picture and wider audience.

**Headspace example:**
- Too broad: "I want to be a better person" → could mean fitness, food, meditation — pulls in every direction
- Just right: "I want to reduce stress and anxiety through meditation" → clear focus

**Spotify example:**
- Too narrow: "I want to organize my music" / "I want to create playlists" → teams would only focus on playlist features, retention metrics around playlists, monetize playlists
- Just right: "I want to listen to music" → broader priorities and strategies

### Research Methods

Interview multiple user groups:
- **Existing healthy users**: These interviews form the use cases being served today
- **Target but unreached users**: These interviews reveal potential future use cases

Effective questions (open-ended, not "What problem does this product solve?"):
- "Why did you sign up for the product? What did you expect it to do for you?"
- "Did the product meet your expectations? When did you know?"
- "Before using this product, what did you use instead? What problem did that solve?"
- "When do you typically use this product? What motivates you before/after?"

---

## Persona Scenarios

### Scenario 1: Personas Differ in Behavior → Separate Use Cases

HubSpot: Sales Reps, Sales Ops Execs, Enterprise Teams, and Individual Business Owners all have the same problem (automate sales inefficiency) but very different alternatives and motivations. Each persona becomes a distinct use case.

### Scenario 2: Personas Don't Differ in Behavior → Single Use Case

Spotify: College students in small towns and 30-year-old urban professionals both want to listen to music. Their demographics differ but their usage patterns don't — one use case is sufficient.

**Key test**: Do the personas have different alternatives, motivations, or natural frequency? If yes, separate use cases. If no, keep them together.

---

## Alternatives vs. Competitors

Alternatives have 10x to 1000x the usage of direct competitors. Defining use cases around alternatives gives a much bigger market.

| Product | Direct Competitor View | True Alternative View |
|---------|----------------------|----------------------|
| Slack | HipChat, Flowdock | Email |
| Pinterest | iHeartThis, other pinboards | Cutting/pasting images from magazines, copying digital images into docs |
| DocuSign | HelloSign, e-sign products | Pen-and-ink signatures, FedEx-ing documents |
| Netflix | Hulu, Prime Video | Cable TV, movie theaters, "doing nothing" |
| Miro | Other whiteboards | Offline whiteboards, photographing drawings, Google Docs |

### How to Uncover Alternatives

Ask existing healthy users:
- "How did you solve this problem before our product?"
- "What behaviors have you stopped doing since using our product?"
- "What products have you stopped using?"

Ask target users:
- "When did you last experience this problem? How did you solve it?"
- "Tell me about a few more instances — what did you do?"

---

## Core Motivations Taxonomy

### Personal (Self-interested utility)
| Sub-type | Description | Example |
|----------|-------------|---------|
| Entertainment | More fun, avoid boredom | Netflix, gaming apps |
| Communication | Communicate with others (selfish reasons) | Messaging apps |
| Information | Gain knowledge or valuable information | News apps, Wikipedia |
| Flexibility | Gain flexibility of something valued | Calendly (scheduling flexibility) |
| Time | Save time or get time back | Automation tools, Calendly |

### Financial (Monetary value)
| Sub-type | Description | Example |
|----------|-------------|---------|
| More Transactions | More transactions from existing audience | Merchant tools |
| Save Money | Lower costs | Comparison shopping, coupons |
| New Customers | Gain access to new customers | Thumbtack for pros |
| Loss Prevention | Prevent loss of capital | Insurance products |

### Social (Emotional/status value)
| Sub-type | Description | Example |
|----------|-------------|---------|
| Recognition | Gain recognition, respect, reputation | Instagram posting |
| Connection | Greater sense of connection/belonging | Social networks |
| Competition | Feeling of winning or achievement | Fitness challenges, games |
| Confidence | Gain a sense of confidence | Fashion, personal development apps |

### Hidden Motivations

Users don't always understand or admit their true motivations, especially for social ones.

**Allbirds example**: On the surface, users think they buy for personal value (great quality, affordable). But there's a social element — wearing Allbirds sends a social message of brand recognition.

---

## Differentiator Examples

Good differentiators have **contrast and specificity**:

| Product | Differentiator | Why It Works |
|---------|---------------|-------------|
| HubSpot | All-in-one vs. stringing together 10+ tools | Specific contrast to the alternative |
| Pinterest | Most personalized visual content at scale | Specific capability, hard to replicate |
| Amazon | Widest selection + fastest delivery + most competitive pricing | Three concrete dimensions |
| Figma (Org) | Per-editor pricing with enterprise features (SSO, design systems) | Pricing model contrast vs. competitors |
| Thumbtack (Pro) | Higher-quality customers who pay more and return | Specific measurable advantage |

**Pitfall**: Listing product features instead of user needs. If you find yourself listing features, ask "why do customers find value from this?" to get to the real differentiator.

---

## Frequency Spectrum Details

| Frequency | Examples | Zone |
|-----------|----------|------|
| Daily | Slack, Instagram, Snapchat | Habit Zone |
| Weekly | Zoom, Figma, Miro, SaaS collaboration tools | Habit Zone |
| Monthly | SurveyMonkey, Birchbox, Ipsy, Mint, Credit Karma | Habit Zone (borderline) |
| Quarterly | Airbnb, VRBO, Everlane, Allbirds | Forgettable Zone |
| Yearly | TurboTax | Forgettable Zone |
| Multi-year | Zillow, Carvana, Babylist | Forgettable Zone |

### Determining Natural Frequency

Natural frequency = how often users encounter the **problem**, not how often they use the **product**.

- A user might use a product daily because it's not solving the problem well (more usage ≠ more value)
- A user might use a product rarely because it solves the problem poorly and they turn to alternatives

**Method**: Ask users about the last few times they experienced the problem and used alternatives:
- "When did you last experience this problem? What were you doing?"
- "How did you solve it? When was the time before that?"
- "When did you last use [alternative]? Why? And the time before that?"

### Escaping the Forgettable Zone

**Zillow's strategy**: Core use case (buying/selling a home) happens every 5-7 years. They layered on:
- Zestimate Score: Monitor your home's value and changes over time
- Zillow Content: Homes for sale in your area
- These higher-frequency hooks keep users engaged between the rare buying/selling events.

---

## Multiple Use Case Strategies

### Dominant Use Case
Focus resources on the use case that drives >75% of usage. Build a 10x experience before expanding.

- **Jira**: Years focused on developer project tracking before expanding to product management and engineering leadership
- **Pinterest**: Focused on browsing interests (dominant) over project planning

### Anti-Use Cases
Explicitly define what you choose NOT to serve to keep teams aligned and focused.

- **Confluence**: Could serve documentation/wiki (one publisher, many readers), but chose not to because it would require features (like turning off commenting) that would hurt the core collaborative editing viral loop.
- **Thumbtack**: Could serve property rentals, roommate matching, secondhand sales — actively chose not to, focusing solely on home services.

### Evolving Use Cases
- **Uber**: Started with UberBlack (high-end) → evolved to UberPool (21-40 year old urban commuters)
- **Netflix**: In 2012, alternative to cable/DVR. Today, competes with Hulu, Prime, Apple TV, Disney+ — changing why users choose Netflix
- **COVID impact**: Restaurants shifted from dine-in to delivery-first, fundamentally changing every element of the use case

---

## Common Pitfalls

1. **Defining the problem too broadly or too narrowly** — find the sweet spot
2. **Treating competitors as alternatives** — alternatives are how users solve the problem without your product, which is often non-digital or non-product
3. **Listing features instead of motivations for the "Why"** — ask "why do users find value from this feature?" to get to the real motivation
4. **Using product usage frequency as natural frequency** — measure how often the problem occurs, not how often the product is used
5. **Targeting too many use cases** — focus on the dominant one first, prove it out, then expand
6. **Not evolving use cases over time** — audiences, markets, and competition shift; use cases must shift with them
7. **Not defining anti-use cases** — without explicit anti-use cases, teams lack the ability to say no to distracting ideas
