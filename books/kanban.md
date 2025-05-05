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


## Recipe for success

Asking people to change their behaviour creates fear and lowers self-esteem, as it communicates that existing skills are clearly no longer valued.

The recipe for success presents guidelines for a new manager adopting a new existing team.
* **Focus on quality**: Excessive defects are the biggest waste in software development.
  - Both agile and traditional approaches to quality have merit
  - Code inspections improve quality
  - Collaborative analysis and design improve quality
  - The use of design patterns improves quality
  - The use of modern development tools improves quality
  - Reducing the quality of design-in-progress boosts software quality
* Reduce work-in-progress
* Deliver often
* Balance demand against throughput
* Prioritise
* Attack sources of variability to improve predictability

Working down the list, there is gradually less control and more collaboration required with other downstream and upstream groups. The final step it's the one that separates the truly great technical leaders from the merely competent managers.

### WIP, lead time, and defects

Longer lead times (from starting to done) seem to be associated with significantly poorer quality. In fact, an approximately 6.5x increase in average lead time resulted in greater than 30x in initial defects. Longer average lead times result from greater amounts of work-in-progress. Hence, the management leverage point for improving quality is to reduce the quantity of work-in-progress. **Shorter iterations will drive higher quality.**

### Frequent releases build trust

Reducing WIP shortens lead time and frequent releases build trust with external teams (social capital). Trust is event driven and that small, **frequent gestures or events enhance trust more than larger gestures made only occasionally.**

Small gestures often cost nothing but build more trust than large, expensive gestures bestowed occasionally.


### Tacit knowledge

Information discovery in software development is tacit in nature and is created during collaborative working sessions, face-to-face. Our minds have a limited capacity to store all this tacit knowledge. Knowledge depreciates with time, so shorter lead times are essential.

### Balance demand against throughput

By setting the rate at which we accept new requirements, we are effectively fixing our work-in-progress to a given size. As work is delivered, we will pull new work from the people creating demand.

### Create slack

Slack capacity created by the act of limiting work-in-progress enables improvement. **You need slack to enable continuous improvement.** You need to balance demand against throughput and limit the quantity of work-in-progress to enable slack.

In order to have slack, you must have an unbalanced value stream with a bottleneck resource. Optimising for utilisation is not desirable.

### Prioritise

At this point, management attention can turn to optimising the value delivered rather than merely the quantity of code delivered.

**Prioritisation should not be controlled by engineering.** Improving prioritisation requires the product owner, business sponsor, or marketing department. Engineering can seek only to influence how prioritisation is done.

### Building maturity

First, learn to build high-quality code. Then reduce the work-in-progress, shorten lead times, and release often. Next, balance demand against throughput, limit work-in-progress, and create slack to free up bandwidth, which enable improvements. Then, with a smoothly functioning and optimising software development capability, improve prioritisation to optimise value delivery.

### Attack sources of variability to improve predictability

Reducing variability in software development requires knowledge workers to change the way they work, to learn new techniques and change their personal behaviour. All of this is hard. Variability creates a greater need for slack.

## From the worst to the best in five quarters

### Adjusting policies

> So how prioritisation was facilitated? If something was important and valuable, it was selected for the input queue from the backlog; if it wasn't then it wasn't selected. Any item older than six months was purged from the backlog.

> The weekly meeting with product owners also disappeared, when a slot became available in the input queue. It would alert the product owners to pick again.

## A continuous improvement culture

Continually improving quality, productivity, and customer satisfaction is known as "kaizen culture".

Workforce is empowered. Individuals feel free to take action; free to do the right thing without fear. Management is tolerant with failure and individuals are free to self-organise around the work they do and how they do it. Everyone looks out for the performance of the team and the business above themselves.

A kaizen culture has a high level of social capital, a trusting culture where individuals respect each other. High-trust cultures tend to have flatter structures than lower-trust cultures. It is the degree of empowerment that enables a flatter structure to work effectively. Achieving kaizen culture may enable elimination of wasteful layers of management and reduce coordination costs as a result.

**Introducing a radical change is harder than incrementally improving an existing one.**

### Unanticipated effects of introducing Kanban

> The physical board had a huge psychological effect. By attending standup each day, team members were exposed to a sort of time-lapse photography of the flow work across the board.

### Sociological change

Kanban method appear to achieve a kaizen culture faster and more effectively than typical Agile software development teams. Kanban enables every stakeholder to see the effects of his or her actions or inactions.

## Mapping the value stream

Kanban drives change by optimising your existing process. The main change will be quantity of WIP and the interface to add interaction with upstream and downstream parts of your business. So you must work with your team to map the value stream as it exists. Map the process they actually use.

### Defining a start and end point for control

Define interface points with upstream and downstream partners.

### Work item types

Identify the types of work that arrive at that point in any others that exist within the workflow that will need to be limited. A few examples:
* Requirement
* Feature
* User story
* Use case
* Change request
* Production defect
* Maintenance
* Refactoring
* Bug
* Improvement suggestion
* Blocking issue

### Drawing a card wall

Once you have understood your workflow by sketching or modelling it, start to define a card wall by drawing columns on the board that represent the activities performed, in the order hey are performed.

Where to put buffers: do not try to second-guess the location of bottleneck that will require a buffer. Rather, implement a system and wait for the bottleneck to reveal itself, then make changes to introduce a buffer.

### Demand

For each type of work identified, you should make a study of the demand.

Decide to allocate capacity within the Kanban system to cope with that demand.

> The allocation is 60% change requests, 10% code refactorings, and 30% production text changes

### Anatomy of a work item card

The information on the cards must facilitate the pull system and empower individuals to make their own pull decisions.

Cards may include:
* Electronic tracking number as a link to the electronic card
* Title of the item
* Date the ticket entered the system. Facilitates first-in, first-out queuing for standard class of service
* Name of assigned person. Name tags, stickers or magnets are a good idea to represent members.

Basically sufficient information to facilitate project-management decisions without the intervention or direction of a manager.

### Electronic tracking

For teams that are distributed geographically, or those who have policies that allow team members to work from their homes, electronic tracking is essential. They allow you to visualise the work item tracking as if it were on a card wall.

### Coping with concurrency

Two or more activities can happen concurrently. There are two ways for coping with this.
* One is not to model it at all; just leave a single column where both activities can occur together. Using different colours or shapes of ticket to show the different activities.
* The other option is to split the board vertically into two (or more) sections
  ```
  ┌─────────────┬────────────────┬────────────────┬────────────┐
  │ INPUT QUEUE │   ANALYSIS     │ DEV & TEST DEV │ TEST READY │
  ├─────────────┼─────────┬──────┼─────────┬──────┼────────────┤
  │             │ IN PROG │ DONE │ IN PROG │ DONE │            │
  ·             ·         ·      ·         ·      ·            ·
  ```


### Coping with unordered activities

Usually happens in highly innovative and experimental work.

First, simply have a single column as a bucket for the activities and do not explicitly track on the board which of them is complete.
Second, tickets have to move vertically up and down the column they are pulled into each of the specific activities. When the activity is complete, the checkbox can be filled to visually signal that the item is ready to be pulled to another activity in the same column. If all the checkboxes are filled, the item is ready to be pulled to the next column on the board or it can be moved to "done".

    ┌──────────────────────────┐
    │ DEV & TEST DEV           │
    ├───────────────────┬──────┤
    │ IN PROGRESS       │ DONE │
    ├───────────────────┼──────┤
    │ ┌───────────────┐ │      │
    │ │ ☒ UI DESIGN   │ │      │
    │ │ ☒ SECURITY    │ │      │
    │ │ ☐ PERSISTENCE │ │      │
    │ │ ☐ BIZ LOGIC   │ │      │
    · └───────────────┘ ·      ·

## Coordination with Kanban systems

### Visual control and pull

You are likely to want to visually capture the assigned staff member, the start date, the electronic tracking number, the work item type, the class of service, and some status information, such as whether the item is late.

Visually communicate enough information to make the system self-organising and self-expediting ad the team level. It should enable team members to pull work without direction from their manager.

### Electronic tracking

As an alternative or as a supplement

### Daily standup meetings

In Agile a typical standup meeting is for a single team of up of twelve people, usually about six. Involving answering three questions: **What did you achieve yesterday? What will you do today? Are you blocked or do you need assistance?**

In Kanban, the wall contains all the information so the focus will be on the flow of work. The facilitator will "walk the board". Work backward, from right to left (in direction of the pull), through the tickets on the board. Making emphasis on items that are blocked, delayed due to defects or stuck for a few days. There will also a call for any other blocking issues that are not on the board and for anyone who needs help to speak up. Mature teams do not need to walk through every card. They will tend to focus only on the tickets that are blocked or have defects.

### The after meeting

Huddles of small groups of 2 or 3 people. Team members that want to discuss something on their minds. After meetings generate improvement ideas and result in process tailoring and innovation.

### Queue replenishment meetings

These serve the purpose of prioritisation in Kanban. They happen at regular intervals providing cadence for queue replenishment.
Ideally they will involve several product owners or business people from potentially competing groups. The tension becomes a positive influence.
Mature teams evolve towards demand-driven prioritisation where stakeholders can be available on demand.

### Release planning meetings

Basically plan downstream delivery.

### Triage

Triage is used to classify bugs that will be fixed, and their priority, versus bugs that will not be fixed.

The most useful application of triage is the backlog of items waiting to enter the system.

The purpose of triaging the backlog is to reduce its size. A good rule of thumb is to trim the backlog for anything more than 3 months of work.

There is a relationship between the size of the backlog, the volatility of the domain and the delivery velocity.

### Issue log review and escalation

When work items are impeded, an issue work item will be created. The issue will remain open until the impediment is removed and the original work item can progress through the system. Issues that are not progressing should be escalated.