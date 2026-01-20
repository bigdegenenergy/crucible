# Phase 3: The Pragmatist - Strategic Implementation Memo

## Book Information

- **Title:** Designing Data-Intensive Applications
- **Author:** Martin Kleppmann

## User Context

- **Role:** Senior Software Engineer / Tech Lead
- **Industry:** Technology / SaaS
- **Current Challenge:** Designing and scaling data systems that balance correctness, performance, and maintainability as the company grows

---

## 1. Define the "Job"

### JTBD Statement

> Help me **design data systems that handle growth without requiring rewrites** so that I can **deliver reliable features to users** while avoiding **premature complexity that slows down the team**.

### Job Dimensions

| Dimension      | Description                                                                                       |
| :------------- | :------------------------------------------------------------------------------------------------ |
| **Functional** | Make informed technical decisions about databases, replication, partitioning, and consistency     |
| **Social**     | Communicate architectural trade-offs to stakeholders; establish credibility as a systems thinker  |
| **Emotional**  | Feel confident that the system won't collapse under load; reduce anxiety about "unknown unknowns" |

---

## 2. The Translation Matrix

### Concept 1: The "Boring Technology" Default

| Abstract Principle                               | Industry-Specific Tactic                                                                                                                                                                                                                                 |
| :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Understand trade-offs before choosing technology | **Default to PostgreSQL** for new projects. Only consider specialized databases when you can articulate why Postgres can't handle the workload. Create a decision document that explicitly states: "We need X capability that Postgres lacks because Y." |

**Implementation:** Before any architectural discussion, ask: "Why can't we do this with a single Postgres instance and read replicas?" Make this the mandatory first question in design reviews.

### Concept 2: The Consistency Spectrum

| Abstract Principle                                    | Industry-Specific Tactic                                                                                                                                                                                                                                                                                                                                            |
| :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Different data has different consistency requirements | **Classify your data** into three tiers: (1) **Critical** - financial transactions, account balances (require strong consistency), (2) **Important** - user profiles, settings (read-your-writes consistency), (3) **Ephemeral** - analytics, recommendations, social feeds (eventual consistency acceptable). Design your architecture to treat these differently. |

**Implementation:** Create a data classification document. For each major entity, explicitly state the consistency tier and justify it. Review this quarterly as business requirements change.

### Concept 3: The Scalability Ladder

| Abstract Principle                            | Industry-Specific Tactic                                                                                                                                                                                                                                                                                |
| :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Scalability is not binary; it's a progression | **Define your scaling stages:** (1) Single instance with good indexes (0-100K users), (2) Read replicas for read-heavy workloads (100K-1M users), (3) Caching layer for hot data (1M-10M users), (4) Partitioning/sharding when single-master writes become bottleneck (10M+ users). Don't jump stages. |

**Implementation:** Document your current stage and the metrics that would trigger moving to the next stage. Resist pressure to "scale proactively" without evidence.

---

## 3. The "Monday Morning" Checklist

### Action 1: Audit Your Current Data Architecture

- [ ] **Verification:** Create a diagram showing all datastores, their purposes, and data flows
- **Success Metric:** Diagram exists and is understood by all senior engineers
- **Failure Mode:** Discovery that no one fully understands the current architecture (this is valuable information)

### Action 2: Define Consistency Requirements Per Entity

- [ ] **Verification:** Create a table mapping each major entity to its consistency tier with business justification
- **Success Metric:** Product and engineering agree on classification
- **Failure Mode:** Discovering that the business assumes strong consistency everywhere but the system provides eventual consistency

### Action 3: Identify Your Single Point of Failure

- [ ] **Verification:** Answer: "If this component fails, how long until users notice, and what's the blast radius?"
- **Success Metric:** Documented for the top 5 critical components
- **Failure Mode:** No clear answers; indicates monitoring/observability gaps

### Action 4: Establish a "Why Not Postgres?" Ritual

- [ ] **Verification:** Add to design review template: "Why can't the default technology handle this?"
- **Success Metric:** Every new component decision includes this justification
- **Failure Mode:** Team pushback reveals cultural preference for novelty over simplicity

### Action 5: Create a Scaling Roadmap

- [ ] **Verification:** Document current capacity, current usage, and the trigger metrics for each scaling stage
- **Success Metric:** Clear thresholds that would prompt architectural changes
- **Failure Mode:** Discovering you're already past a threshold without knowing it

---

## 4. The Learning Wager

Identify one specific belief or behavior I must "kill" to adopt this book's advice.

### The Belief/Behavior to Kill

> **"We need to design for scale from day one."**

This belief leads to premature complexity. The antidote is Kleppmann's message that you should understand trade-offs but not pay their costs until necessary.

### The Ante

> "I am willing to bet my time/energy on this idea because premature scaling has caused more project failures than insufficient scaling. The book cites evidence that companies like Amazon and LinkedIn started simple and evolved. If this is wrong, I will discover it through specific scaling pain, which is better than discovering I over-engineered through team velocity pain."

### The Experiment

| Element             | Details                                                    |
| :------------------ | :--------------------------------------------------------- |
| **Concept to Test** | "Boring technology by default"                             |
| **Duration**        | 30 Days                                                    |
| **If it works**     | I keep pushing back on complexity; document wins           |
| **If it fails**     | I adjust the "boring threshold" based on specific failures |

### The Prediction

> "I predict that applying the 'Why not Postgres?' question to the next 3 architectural decisions will result in at least 1 case where we avoid unnecessary complexity, saving engineering time."

_Learning happens in the gap between prediction and reality._

---

## Implementation Priority Matrix

| Action                               | Impact | Effort | Priority |
| :----------------------------------- | :----- | :----- | :------- |
| Audit current data architecture      | High   | Medium | **P0**   |
| Define consistency requirements      | High   | Low    | **P0**   |
| Establish "Why not Postgres?" ritual | High   | Low    | **P1**   |
| Identify single points of failure    | Medium | Medium | **P1**   |
| Create scaling roadmap               | Medium | Medium | **P2**   |

---

## Applied DDIA Decision Framework

When facing a data system design decision, apply this checklist:

### Before Adding Complexity

1. **What problem does this solve?** (Not "what could it solve someday")
2. **What's the simplest solution that works?** (Usually: better indexes, more RAM, read replicas)
3. **What's the operational cost?** (Monitoring, on-call, expertise required)
4. **What's the failure mode?** (How does this break, and what's the recovery path)
5. **Can we defer this decision?** (Building for current load + 10x is usually sufficient)

### When Evaluating Consistency Trade-offs

| Question                                  | If Yes               | If No                |
| :---------------------------------------- | :------------------- | :------------------- |
| Will incorrect data cause financial loss? | Strong consistency   | Consider eventual    |
| Will users notice stale data?             | Read-your-writes     | Eventual is fine     |
| Is this data used for compliance/audit?   | Strong consistency   | Depends on retention |
| Can we detect and repair inconsistency?   | Eventual might be OK | Strong consistency   |

### When Choosing Between Technologies

| Factor               | Weight | How to Evaluate                         |
| :------------------- | :----- | :-------------------------------------- |
| Team familiarity     | High   | Does anyone have production experience? |
| Operational maturity | High   | Is there a managed service option?      |
| Community support    | Medium | Stack Overflow answers, GitHub activity |
| Feature match        | Medium | Does it solve our actual problem?       |
| Performance          | Low\*  | Only matters after others are satisfied |

\*Performance is low weight because most systems never reach the scale where performance differences matter.

---

## Sources

- Kleppmann, M. (2017). _Designing Data-Intensive Applications_. O'Reilly Media.
- McKeown, G. (2014). _Essentialism: The Disciplined Pursuit of Less_. Crown Business.
- Christensen, C., et al. (2016). _Competing Against Luck: The Story of Innovation and Customer Choice_. Harper Business.
- McKinley, D. (2015). "Choose Boring Technology." boringtechnology.club.
