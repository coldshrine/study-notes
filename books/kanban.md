# [Kanban: Successful Evolutionary Change for Your Technology Business](https://www.goodreads.com/book/show/8086552-Kanban)

- [Solving an agile manager's dilemma](#solving-an-agile-managers-dilemma)
- [Kanban](#kanban)
- [Recipe for success](#recipe-for-success)
- [From the worst to the best in five quarters](#from-the-worst-to-the-best-in-five-quarters)
- [A continuous improvement culture](#a-continuous-improvement-culture)
- [Mapping the value stream](#mapping-the-value-stream)
- [Coordination with Kanban systems](#coordination-with-kanban-systems)
- [Establishing a delivery cadence](#establishing-a-delivery-cadence)
- [Establishing an input cadence](#establishing-an-input-cadence)
- [Setting work-in-progress limits](#setting-work-in-progress-limits)
- [Establishing service level agreements](#establishing-service-level-agreements)
- [Metrics and management](#metrics-and-management)
- [Operations review](#operations-review)
- [Starting a Kanban change initiative](#starting-a-kanban-change-initiative)
- [Bottlenecks and non-instant availability](#bottlenecks-and-non-instant-availability)
- [An economic model for Lean](#an-economic-model-for-lean)
- [Sources of variability](#sources-of-variability)
- [Issue management and escalation policies](#issue-management-and-escalation-policies)

## Solving an agile manager's dilemma

> Our deadlines were set by managers without regard to engineering complexity, risk, or project size.

> Changes suggested out of context would be rejected by the workers who lived and understood the project context.

Drum-Buffer-Rope is an example of a class of solutions known as pull systems. The side effect of pull systems is that they limit work-in-progress (WIP) to some agreed-upon quantity, thus preventing workers from becoming overloaded.

## Kanban

_Kan-ban_ is a Japanese word that literally means "signal card" in english. Cards are used as a signal to tell an upstream step in the process to produce more. Kanban is fundamental to the _kaizen_ (continuous improvement).

Workflow visualisation, work item types, cadence, classes of service, specific management reporting, and operation reviews is what defines the Kanban Method.

### Kanban system

A number of cards equivalent to the agreed capacity of a system are placed in circulation. One card attaches to one piece of work. Each card acts as a signalling mechanism. A new piece of work can be started only when a card is available. The free card is attached to a piece of work and follows it as it flows through the system. When there are no more free cards, no additional work can be started. Any new work must wait in a queue until a card becomes available. When some work is completed, its card is detached and recycled. With a card now free, a new piece of work in the queuing can be started.

This is known as a pull system because new work is pulled into the system when there is capacity to handle it, rather being pushed into the system based on demand. A pull system cannot be overloaded if capacity, as determined by the number of signal cards in circulation, has been set appropriately.

### Kanban in software development

In software development the cards do not actually function as signals to pull more work. They represent work items.

Card walls have become a popular visual control mechanism. These are not inherently Kanban systems, they are merely visual control systems. **If there is no explicit limit to work-in-progress and no signalling to pull new work through the system, it is not a Kanban system.**

### Why use Kanban

We use it in order to limit team's work-in-progress to a set capacity and to balance the demand on the team. By providing visibility onto quality and process problems, it makes obvious the impact of defects, bottlenecks, variability, and economic costs on flow and throughput.

Kanban facilitates emergence of a highly collaborative, high-trust, highly empowered, continuously improving organisation.

### Kanban and Lean

Kanban uses five core properties to create an emergent set of Lean behaviours in organisations:
* Visualise workflow
* Limit work-in-progress
* Measure and manage flow
* Make process policies explicit
* Use models to recognise improvement opportunities (like Theory of Constraints, Systems Thinking, _muda_)

---

Kanban is not a software development lifecycle methodology or an approach to project management. It requires that some process is already in place so that Kanban can be applied to incrementally change the underlying process.

Your situation is unique and you deserve to develop a unique process definition tailored and optimised to your domain.