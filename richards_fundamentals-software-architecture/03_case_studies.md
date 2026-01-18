# Case Studies: Fundamentals of Software Architecture

## Overview

The book uses **Architecture Katas**—structured practice exercises—as its primary teaching vehicle for case studies. These are fictional but realistic business scenarios that allow readers to practice deriving architecture characteristics from requirements and making architectural decisions.

The concept was pioneered by Ted Neward, inspired by Dave Thomas's "Code Kata" (itself inspired by martial arts practice). Architecture Katas give nascent architects a way to practice architectural thinking in a safe environment.

---

## Primary Case Studies

### 1. Silicon Sandwiches

**Scenario**: A national sandwich shop wants to enable online ordering in addition to its call-in service.

**Requirements**:
- Users place orders and receive pickup times
- Integration with external mapping services (with traffic information)
- Directions to the shop
- Support for delivery where available
- Current user base: thousands
- Potential future scale: millions

**Derived Architecture Characteristics**:

| Characteristic | Rationale |
|----------------|-----------|
| **Scalability** | "Thousands, perhaps one day millions" of users |
| **Elasticity** | Handle bursts of requests (lunch rush, promotions) |
| **Availability** | Users expect ordering to work when they're hungry |
| **Reliability** | Site must stay up during ordering interactions |
| **Customizability** | Menu varies by location, promotions change frequently |

**Key Lessons**:
- Many important characteristics are implicit, not explicit in requirements
- "Thousands to millions" signals a scalability concern immediately
- Food ordering has predictable peak patterns requiring elasticity
- Architects must read between the lines of requirements

**Used Throughout Book For**:
- Component-Based Thinking (partitioning exercise)
- Monolith Case Study (architecture style selection)
- Extracting characteristics from requirements

---

### 2. Sysops Squad

**Scenario**: Penultimate Electronics, a large electronics retailer, has a support plan system where technology experts ("Sysops Squad") visit customers to fix electronic devices.

**Current State Problems**:
- Large monolithic application developed years ago
- Customers complain consultants don't show up (lost tickets)
- Wrong consultants often assigned (skill mismatch)
- Change is difficult and risky
- System frequently "freezes up" or crashes
- Modifications take too long and break other features

**Business Requirements**:
- Track trouble tickets from creation to resolution
- Route consultants based on skills and location
- Mobile-first experience for field consultants
- Graceful degradation when connectivity is poor

**Architecture Analysis**:

| Problem | Root Cause | Architectural Response |
|---------|------------|------------------------|
| Lost tickets | Monolith reliability issues | Distributed architecture with redundancy |
| Wrong consultant | No skill-based routing | Service to match skills to ticket types |
| Slow changes | Tight coupling | Decompose into services |
| Crashes | Single point of failure | Multiple deployment units |

**Key Lessons**:
- Modernizing legacy systems requires understanding current pain points
- Mobile-first and offline capability drive architecture decisions
- Location-based routing suggests geographic distribution
- Reliability problems often indicate over-coupled architecture

**Used For**:
- Architectural decomposition exercises
- Service-based architecture examples
- O'Reilly Architecture Kata competitions

---

### 3. Going, Going, Gone

**Scenario**: An online auction platform supporting both live and online bidding.

**Requirements**:
- Real-time bidding during live auctions
- Live-streamed auction events
- Video archives of past auctions
- Bidder reputation/history tracking
- Mixed participation (in-person + online simultaneous)

**Derived Architecture Characteristics**:

| Characteristic | Rationale |
|----------------|-----------|
| **Performance** | Real-time bidding requires sub-second response |
| **Scalability** | Major auctions attract many simultaneous bidders |
| **Reliability** | Missed bids mean lost revenue and angry customers |
| **Elasticity** | Traffic spikes during popular auctions |

**Key Lessons**:
- Real-time requirements significantly constrain architecture choices
- Streaming media adds complexity (different from transactional data)
- Hybrid online/in-person creates synchronization challenges
- Multiple "quanta" may be needed (bidding service vs. video streaming)

**Used For**:
- Architecture Quanta and Granularity discussions
- Component discovery exercises
- Multiple quantum identification

---

## Architecture Anti-Pattern Case Studies

### The Sinkhole Anti-Pattern (Layered Architecture)

**Definition**: Requests pass through layers without any business logic being performed—layers become mere pass-through conduits.

**Example Scenario**:
```
User Request → Presentation Layer → Business Layer → Persistence Layer → Database
                    (no logic)         (no logic)        (no logic)
```

**When It's Problematic**: If more than 50% of requests are simple pass-throughs, the architecture adds overhead without value.

**Why It Happens**:
- Over-engineering for "future flexibility"
- Strict layer separation rules applied dogmatically
- Copying patterns without understanding purpose

**Solution**: Allow selective layer bypassing for simple CRUD operations, or reconsider if layered architecture is appropriate.

---

### The Entity Trap Anti-Pattern

**Definition**: Mapping database entities directly to components, creating a data-centric rather than behavior-centric architecture.

**Example**:
```
Bad: Components mirror database tables
├── CustomerComponent
├── OrderComponent
├── ProductComponent
└── PaymentComponent

Better: Components encapsulate behavior
├── OrderPlacementService (handles orders, payments, inventory)
├── CustomerManagementService (handles customer lifecycle)
└── CatalogService (handles products, categories, search)
```

**Why It's Problematic**:
- Creates artificial boundaries based on data, not behavior
- Cross-cutting operations require coordinating many components
- Changes to data model ripple across architecture

**Key Lesson**: Components should be organized around behavior and business capability, not around data entities.

---

## Architecture Style Case Studies

### When to Use Layered Architecture

**Good Fit**:
- Small, simple applications
- Very tight budget and time constraints
- Teams familiar with the pattern
- Low scalability requirements

**Case Study Pattern**:
```
Presentation Layer
    ↓
Business Layer
    ↓
Persistence Layer
    ↓
Database
```

**Trade-offs Illustrated**:
| Advantage | Disadvantage |
|-----------|--------------|
| Simple to understand | Limited agility |
| Low cost | Business logic spread across layers |
| Familiar pattern | Doesn't support DDD well |
| Easy to staff | Difficult to scale parts independently |

---

### When to Use Microservices

**Good Fit**:
- High deployability requirements
- Team autonomy is important
- Different parts need different characteristics
- Bounded contexts are well-defined

**Illustrated Trade-offs**:
| Advantage | Disadvantage |
|-----------|--------------|
| Independent deployment | Network complexity |
| Team autonomy | Distributed transactions |
| Technology flexibility | Operational overhead |
| Granular scaling | Testing complexity |

---

## Architecture Katas Library

The book's companion website provides 22+ practice katas. Selected examples:

### High-Traffic Systems
| Kata | Key Challenge |
|------|---------------|
| Concert Comparison | Handling ticket sale demand spikes |
| All Stuff, No Cruft | Conference traffic bursts |
| Tales of a Fourth Grade | "Aggressive scalability" for school district |

### Real-Time Requirements
| Kata | Key Challenge |
|------|---------------|
| Going, Going, Gone | Live auction bidding |
| Am.I.Sck | Real-time nurse-patient chat |
| World of Webcraft | MMORPG with matchmaking |

### Integration-Heavy
| Kata | Key Challenge |
|------|---------------|
| Road Warrior | Aggregating airline/hotel/car data |
| E(xperimental) College | Legacy system integration |
| Gird the Grid | "Four nines" reliability for electrical grid |

### Compliance/Regulatory
| Kata | Key Challenge |
|------|---------------|
| Check Your Work | Audit trails for grading |
| Make the Grade | Multi-agency approval process |
| Tales of a Fourth Grade | FERPA compliance |

---

## Quotable Insights from Case Studies

> "One of the first details that should catch an architect's eye is the number of users: currently thousands, perhaps one day millions."
— On Silicon Sandwiches scalability

> "Many of the considerations an architect must make aren't explicitly expressed in requirements but rather by implicit knowledge of the problem domain."
— On reading between requirement lines

> "The architecture sinkhole anti-pattern occurs when requests move from layer to layer as simple pass-through processing with no business logic performed within each layer."
— On layered architecture pitfalls

---

## Key Takeaways from Case Studies

1. **Requirements rarely state architecture characteristics explicitly**—architects must infer them from domain knowledge

2. **Numbers matter**—user counts, transaction volumes, and growth projections drive scalability decisions

3. **Anti-patterns emerge from misapplied patterns**—understanding "why" prevents cargo-cult architecture

4. **Trade-offs are constant**—every case study demonstrates that gains in one characteristic come at the cost of another

5. **Practice matters**—architecture skills, like martial arts, improve through deliberate practice with katas

---

## Sources

- [Architecture Katas List](http://fundamentalsofsoftwarearchitecture.com/katas/list.html)
- [Architecture Katas Overview](http://fundamentalsofsoftwarearchitecture.com/katas/)
- [Sysops Squad Kata - GitHub](https://github.com/team7katas/sysopsquad)
- [Book Summary - Dan Lebrero](https://danlebrero.com/2021/11/17/fundamentals-of-software-architecture-summary/)
- [Knowledge Base Summary](https://yoan-thirion.gitbook.io/knowledge-base/software-architecture/fundamentals-of-software-architecture)
