# Core Framework: Fundamentals of Software Architecture

## The Big Idea

Software architecture is not just about structure—it's about making informed trade-offs across multiple dimensions while continuously evolving the system. The book reframes architecture as an engineering discipline with measurable characteristics, explicit decisions, and governance mechanisms.

> "Everything in software architecture is a trade-off." — First Law of Software Architecture

---

## The Two Laws of Software Architecture

### First Law: Everything is a Trade-off
Every architectural decision involves balancing competing concerns. There is no "best" architecture—only the "least worst" for a given context. Choosing one characteristic often diminishes another.

### Second Law: Why is More Important Than How
Understanding the rationale behind decisions matters more than the implementation details. Documentation should capture the "why" to enable future architects to make informed changes.

---

## The Four Dimensions of Software Architecture

The authors define software architecture as comprising four interrelated dimensions:

| Dimension | Description | Example |
|-----------|-------------|---------|
| **Structure** | The architecture style (organizational pattern) | Microservices, layered, event-driven |
| **Architecture Characteristics** | The "-ilities" that define success criteria | Scalability, availability, maintainability |
| **Architecture Decisions** | Hard rules constraining the system | "No direct database calls from presentation layer" |
| **Design Principles** | Soft guidelines (preferred, not mandated) | "Prefer asynchronous messaging between services" |

---

## Architecture Characteristics (The "-ilities")

Architecture characteristics are non-functional requirements that define system success orthogonal to domain functionality. They're not invented by architects—they're deduced from business requirements and domain concerns.

### Categories of Characteristics

**Operational Characteristics**
| Characteristic | Description |
|----------------|-------------|
| Availability | System uptime requirements |
| Reliability | Consistent behavior without failure |
| Scalability | Handling increased load |
| Elasticity | Dynamic scaling up/down |
| Performance | Response time and throughput |
| Recoverability | Ability to recover from failures |

**Structural Characteristics**
| Characteristic | Description |
|----------------|-------------|
| Maintainability | Ease of making changes |
| Testability | Ease of testing |
| Deployability | Ease and frequency of deployment |
| Configurability | End-user configuration options |
| Extensibility | Adding new functionality |
| Portability | Running on different platforms |

**Cross-Cutting Characteristics**
| Characteristic | Description |
|----------------|-------------|
| Security | Protection from threats |
| Accessibility | Usability for all users |
| Authentication | Identity verification |
| Authorization | Permission management |

### Classification Types

- **Explicit**: Directly stated in requirements
- **Implicit**: Necessary but unstated (e.g., security is rarely in requirements but always needed)

### Key Insight: Support Few Characteristics Well

> Most applications can only support a few architecture characteristics well.

Each supported characteristic requires design effort and often negatively impacts others. Never shoot for the "best" architecture—aim for the "least worst" that adequately supports the most critical characteristics.

---

## Architecture Quantum

One of the book's most important original concepts:

> An **architecture quantum** is "an independently deployable artifact with high functional cohesion and synchronous connascence."

### Three Defining Properties

1. **Independently deployable**: Contains all components needed to function independently
2. **High functional cohesion**: Does something purposeful and cohesive
3. **Synchronous connascence**: Has synchronous communication within its boundary

### Why It Matters

- A monolith has **one quantum** (one deployable unit)
- A microservices architecture has **multiple quanta** (many independent services)
- The database is part of the quantum if the system depends on it
- Different quanta can have different architecture characteristics

This concept helps architects identify natural boundaries for decomposition and understand where different characteristics can vary.

---

## Modularity and Metrics

### Cohesion
The degree to which elements within a module belong together. High cohesion is desirable.

### Coupling
The degree of interdependence between modules. Low coupling is desirable.

### Connascence
A more nuanced view of coupling—two components have connascence when a change in one requires a change in the other to maintain correctness.

**Static Connascence** (discoverable at compile time):
- Name → Type → Meaning → Position → Algorithm (weakest to strongest)

**Dynamic Connascence** (discoverable at runtime):
- Execution → Timing → Values → Identity (weakest to strongest)

### Key Metric: Distance from Main Sequence

**Formula: D = |A + I - 1|**

Where:
- **A** = Abstractness (ratio of abstract elements to total elements)
- **I** = Instability (ratio of efferent to total coupling)

Ideal: D approaches 0 (balanced abstraction and stability)

### Cyclomatic Complexity
Measures code complexity via decision points:
- Under 5: Preferred
- Under 10: Acceptable
- Over 10: Problematic

---

## Architecture Styles Catalog

The book provides a comprehensive catalog of architecture styles, comparing their characteristics:

### Monolithic Styles

| Style | Description | Best For |
|-------|-------------|----------|
| **Layered** | Traditional horizontal layers (presentation, business, data) | Simple applications, small teams |
| **Pipeline** | Filters connected by pipes | Data processing, ETL systems |
| **Microkernel** | Core system with plug-in components | Product-based applications |

### Distributed Styles

| Style | Description | Best For |
|-------|-------------|----------|
| **Service-Based** | 4-12 coarse-grained services, may share database | Pragmatic modernization |
| **Event-Driven** | Asynchronous event producers and consumers | High scalability, decoupling |
| **Space-Based** | In-memory data grids, virtualized middleware | Extreme elasticity requirements |
| **Service-Oriented (SOA)** | Enterprise services with orchestration layer | Large enterprises, reuse focus |
| **Microservices** | Fine-grained bounded contexts | High deployability, team autonomy |

### Style Comparison Matrix

| Style | Deployability | Elasticity | Scalability | Fault Tolerance | Overall Cost |
|-------|---------------|------------|-------------|-----------------|--------------|
| Layered | ★ | ★ | ★ | ★ | ★★★★★ |
| Microkernel | ★★★ | ★ | ★ | ★ | ★★★★★ |
| Service-Based | ★★★★ | ★★ | ★★★ | ★★★★ | ★★★★ |
| Event-Driven | ★★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★ |
| Microservices | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★ |

*(★ = Low/Poor, ★★★★★ = High/Excellent)*

---

## Event-Driven Architecture Topologies

### Broker Topology
- No central coordinator
- Events flow directly between processors
- **Pros**: High performance, scalability
- **Cons**: Difficult error handling, no workflow control

### Mediator Topology
- Central mediator coordinates workflow
- Better error handling and orchestration
- **Pros**: Workflow control, error recovery
- **Cons**: Single point of failure, lower performance

---

## Fitness Functions

Fitness functions provide objective integrity assessment of architecture characteristics:

> "Any mechanism that provides an objective integrity assessment of some architecture characteristic or combination of characteristics."

### Implementation Mechanisms
- Unit/integration tests
- Metrics and static analysis
- Monitoring and alerting
- Chaos engineering experiments
- Deployment pipeline gates

### Examples
| Characteristic | Fitness Function |
|----------------|------------------|
| Modularity | Cyclomatic complexity < 10 |
| Performance | Response time < 200ms (p95) |
| Availability | Uptime > 99.9% |
| Security | No critical vulnerabilities in scan |
| Testability | Code coverage > 80% |

---

## Component Determination

### Partitioning Approaches

**Technical Partitioning** (by layer)
```
├── presentation/
├── business/
├── services/
└── persistence/
```

**Domain Partitioning** (by business capability) — *Preferred*
```
├── catalog/
├── checkout/
├── inventory/
└── shipping/
```

### Anti-Pattern: The Entity Trap
Treating database entities as components creates data-centric rather than behavior-centric architecture. Components should encapsulate behavior, not just data.

---

## The Role of the Architect

### Eight Core Expectations

1. **Make architecture decisions** — Guide rather than specify technology
2. **Continually analyze architecture** — Assess viability against business needs
3. **Keep current with trends** — Track industry changes
4. **Ensure compliance** — Verify decisions are followed
5. **Gain diverse exposure** — Experience multiple technologies
6. **Have business domain knowledge** — Understand the problem space
7. **Possess interpersonal skills** — Collaborate effectively
8. **Navigate politics** — Work within organizational constraints

### Technical Breadth vs. Depth

| Role | Focus | Knowledge |
|------|-------|-----------|
| Developer | Depth | Deep expertise in few areas |
| Architect | Breadth | Broad understanding of many areas |

Architects must understand trade-offs across many solutions rather than mastering one.

---

## Architecture Decision Records (ADRs)

Structured documentation with five sections:

1. **Title**: Short descriptive name
2. **Status**: Proposed, Accepted, Deprecated, Superseded
3. **Context**: Forces at play, problem being addressed
4. **Decision**: The choice made and rationale
5. **Consequences**: Trade-offs and implications

---

## Risk Management

### Risk Assessment Formula
**Risk = Impact (1-3) × Likelihood (1-3)**

| Score | Risk Level |
|-------|------------|
| ≥ 6 | High |
| 3-5 | Medium |
| 1-2 | Low |

### Risk Storming
Collaborative technique for identifying architectural risks:
1. Individual identification (avoid groupthink)
2. Group consolidation
3. Prioritization
4. Mitigation planning

---

## Evolutionary Architecture

Architecture should support "guided, incremental change across multiple dimensions."

### Key Enablers
- Fitness functions protecting characteristics
- Continuous delivery practices
- Modular, decoupled architecture
- Architecture quantum boundaries

### Key Insight
The old "big design up front" is dead. Architecture is now iterative, evolving alongside development in a bidirectional partnership between architects and developers.

---

## Sources

- [Fundamentals of Software Architecture - O'Reilly](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/)
- [Book Companion Website](http://fundamentalsofsoftwarearchitecture.com/)
- [Dan Lebrero's Book Summary](https://danlebrero.com/2021/11/17/fundamentals-of-software-architecture-summary/)
- [Knowledge Base Summary](https://yoan-thirion.gitbook.io/knowledge-base/software-architecture/fundamentals-of-software-architecture)
- [GeeksforGeeks Summary](https://www.geeksforgeeks.org/software-engineering/fundamentals-of-software-architecture/)
