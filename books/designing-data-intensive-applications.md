# Reliable, Scalable, and Maintainable Applications

A data-intensive application is typically built from standard building blocks. They usually need to:

- Store data (databases)
- Speed up reads (caches)
- Search data (search indexes)
- Send a message to another process asynchronously (stream processing)
- Periodically crunch data (batch processing)

## Key Goals

1. **Reliability**: To work correctly even in the face of adversity.
2. **Scalability**: Reasonable ways of dealing with growth.
3. **Maintainability**: Be able to work on it productively.

---

## Reliability

### Typical Expectations:

- Application performs the function the user expected.
- Tolerates the user making mistakes.
- Its performance is good.
- The system prevents abuse.

Systems that anticipate faults and can cope with them are called **fault-tolerant** or **resilient**.

- A **fault** is usually defined as one component of the system deviating from its spec, whereas a **failure** is when the system as a whole stops providing the required service to the user.
- You should generally prefer **tolerating faults** over **preventing faults**.

### Types of Faults

1. **Hardware Faults**:
   - Until recently, redundancy of hardware components was sufficient for most applications.
   - As data volumes increase, more applications use a larger number of machines, proportionally increasing the rate of hardware faults.
   - There is a move towards systems that tolerate the loss of entire machines. A system that tolerates machine failure can be patched one node at a time, without downtime of the entire system (**rolling upgrade**).

2. **Software Errors**:
   - Unlike hardware, software errors are systematic and tend to cause many more system failures.
   
3. **Human Errors**:
   - Humans are known to be unreliable. Configuration errors by operators are a leading cause of outages.
   - Ways to make systems more reliable:
     - Minimize opportunities for error, e.g., admin interfaces that make it easy to do the "right thing" and discourage the "wrong thing".
     - Provide fully featured non-production sandbox environments where people can explore and experiment safely.
     - Automated testing.
     - Quick and easy recovery from human error:
       - Fast rollback of configuration changes.
       - Gradual rollout of new code.
       - Tools to recompute data.
     - Detailed and clear monitoring, such as performance metrics and error rates (**telemetry**).
     - Implement good management practices and training.

---

## Scalability

This is how to cope with increased load. First, succinctly describe the current load on the system; only then can growth questions be discussed.

### Twitter Example

#### Twitter Main Operations

1. **Post Tweet**: A user can publish a new message to their followers (4.6k req/sec, over 12k req/sec peak).
2. **Home Timeline**: A user can view tweets posted by the people they follow (300k req/sec).

#### Two Ways of Implementing Operations:

1. **Approach 1**:
   - Posting a tweet simply inserts the new tweet into a global collection of tweets.
   - When a user requests their home timeline, look up all the people they follow, find all the tweets for those users, and merge them (sorted by time). This could be done with a SQL JOIN.

2. **Approach 2**:
   - Maintain a cache for each user's home timeline.
   - When a user posts a tweet, look up all the people who follow that user, and insert the new tweet into each of their home timeline caches.

**Downside of Approach 2**:
- Posting a tweet now requires a lot of extra work. Some users have over 30 million followers, resulting in over 30 million writes to home timelines.

#### Hybrid Approach

- Tweets continue to be fanned out to home timelines, but a small number of users with a very large number of followers are fetched separately and merged with that user's home timeline when it is read, like in Approach 1.

---

### Describing Performance

#### What Happens When Load Increases?

- How is the performance affected?
- How much do you need to increase your resources?

In a batch processing system such as Hadoop, we usually care about **throughput**, or the number of records we can process per second.

#### Latency and Response Time

- **Response Time**: What the client sees.
- **Latency**: The duration a request is waiting to be handled.

##### Percentiles

- **Median (50th percentile or p50)**: Half of user requests are served in less than the median response time, and the other half take longer.
- **Percentiles 95th, 99th, and 99.9th (p95, p99, and p999)**: Indicate how bad the outliers are.

---

## Maintainability

The majority of the cost of software is in its ongoing maintenance. There are three design principles for software systems:

1. **Operability**: Make it easy for operation teams to keep the system running.
2. **Simplicity**: Easy for new engineers to understand the system by removing as much complexity as possible.
3. **Evolvability**: Make it easy for engineers to make changes to the system in the future.

---

### Operability: Making Life Easy for Operations

A good operations team is responsible for:

- Monitoring and quickly restoring service if it goes into a bad state.
- Tracking down the cause of problems.
- Keeping software and platforms up to date.
- Keeping tabs on how different systems affect each other.
- Anticipating future problems.
- Establishing good practices and tools for development.
- Performing complex maintenance tasks, like platform migration.
- Maintaining the security of the system.
- Defining processes that make operations predictable.
- Preserving the organization’s knowledge about the system.

Good operability means making routine tasks easy.

---

### Simplicity: Managing Complexity

When complexity makes maintenance hard, budget and schedules are often overrun. There is a greater risk of introducing bugs.

- Making a system simpler means removing **accidental complexity**, which is not inherent in the problem that the software solves (as seen by users).
- One of the best tools we have for removing accidental complexity is **abstraction**, which hides the implementation details behind clean and simple-to-understand APIs and facades.

---

### Evolvability: Making Change Easy

- Agile working patterns provide a framework for adapting to change.
- **Functional Requirements**: What the application should do.
- **Nonfunctional Requirements**: General properties like security, reliability, compliance, scalability, compatibility, and maintainability.
"""


# Data Models and Query Language

Most applications are built by layering one data model on top of another. Each layer hides the complexity of the layers below by providing a clean data model. These abstractions allow different groups of people to work effectively.

## Relational Model vs Document Model

The roots of relational databases lie in business data processing, transaction processing, and batch processing.

The goal was to hide the implementation details behind a cleaner interface.

Not Only SQL has a few driving forces:

- Greater scalability
- Preference for free and open source software
- Specialized query optimizations
- Desire for a more dynamic and expressive data model

With a SQL model, if data is stored in relational tables, an awkward translation layer is introduced. This is called impedance mismatch.

The JSON model reduces the impedance mismatch, and the lack of schema is often cited as an advantage.

JSON representation has better locality than the multi-table SQL schema. All the relevant information is in one place, and one query is sufficient.

In relational databases, it's normal to refer to rows in other tables by ID, because joins are easy. In document databases, joins are not needed for one-to-many tree structures, and support for joins is often weak.

If the database itself does not support joins, you have to emulate a join in application code by making multiple queries.

The most popular database for business data processing in the 1970s was IBM's Information Management System (IMS).

IMS used a hierarchical model and, like document databases, worked well for one-to-many relationships. However, it made many-to-many relationships difficult and didn't support joins.

## The Network Model

Standardized by a committee called the Conference on Data Systems Languages (CODASYL), the network model was a generalization of the hierarchical model. In the tree structure of the hierarchical model, every record has exactly one parent, while in the network model, a record could have multiple parents.

The links between records are like pointers in a programming language. The only way of accessing a record was to follow a path from a root record, called the access path.

A query in CODASYL was performed by moving a cursor through the database by iterating over a list of records. If you didn't have a path to the data you wanted, you were in a difficult situation, as it was hard to make changes to an application's data model.

## The Relational Model

By contrast, the relational model was a way to lay out all the data "in the open." A relation (table) is simply a collection of tuples (rows), and that's it.

The query optimizer automatically decides which parts of the query to execute in which order and which indexes to use (the access path).

The relational model thus made it much easier to add new features to applications.

The main arguments in favor of the document data model are schema flexibility, better performance due to locality, and sometimes closer data structures to those used by the applications. The relational model counters by providing better support for joins and many-to-one and many-to-many relationships.

If the data in your application has a document-like structure, then it's probably a good idea to use a document model. The relational technique of shredding can lead to unnecessarily complicated application code.

The poor support for joins in document databases may or may not be a problem.

If your application does use many-to-many relationships, the document model becomes less appealing. Joins can be emulated in application code by making multiple requests. Using the document model can lead to significantly more complex application code and worse performance.

## Schema Flexibility

Most document databases do not enforce any schema on the data in documents. Arbitrary keys and values can be added to a document, but when reading, clients have no guarantees as to what fields the documents may contain.

Document databases are sometimes called schemaless, but maybe a more appropriate term is schema-on-read, in contrast to schema-on-write.

- Schema-on-read is similar to dynamic (runtime) type checking, whereas schema-on-write is similar to static (compile-time) type checking.
- The schema-on-read approach is useful if the items in the collection don't have the same structure (heterogeneous data).

### Many Different Types of Objects

- Data determined by external systems

### Data Locality for Queries

If your application often needs to access the entire document, there is a performance advantage to this storage locality.

The database typically needs to load the entire document, even if you access only a small portion of it. On updates, the entire document usually needs to be rewritten, so it is recommended that you keep documents fairly small.

## Convergence of Document and Relational Databases

- PostgreSQL supports JSON documents.
- RethinkDB supports relational-like joins in its query language.
- Some MongoDB drivers automatically resolve database references.

Relational and document databases are becoming more similar over time.

## Query Languages for Data

SQL is a declarative query language. In an imperative language, you tell the computer to perform certain operations in order.

In a declarative query language, you just specify the pattern of the data you want, but not how to achieve that goal.

A declarative query language hides the implementation details of the database engine, making it possible for the database system to introduce performance improvements without requiring any changes to queries.

Declarative languages often lend themselves to parallel execution, while imperative code is very hard to parallelize across multiple cores because it specifies instructions that must be performed in a particular order. Declarative languages specify only the pattern of the results, not the algorithm used to determine results.

## Declarative Queries on the Web

In a web browser, using declarative CSS styling is much better than manipulating styles imperatively in JavaScript. Declarative languages like SQL turned out to be much better than imperative query APIs.

 # MapReduce Querying

MapReduce is a programming model for processing large amounts of data in bulk across many machines, popularized by Google.

Mongo offers a MapReduce solution:

```javascript
db.observations.mapReduce(
    function map() { // 2
        var year  = this.observationTimestamp.getFullYear();
        var month = this.observationTimestamp.getMonth() + 1;
        emit(year + "-" + month, this.numAnimals); // 3
    },
    function reduce(key, values) { // 4
        return Array.sum(values); // 5
    },
    {
        query: { family: "Sharks" }, // 1
        out: "monthlySharkReport" // 6
    }
);

The map and reduce functions must be pure functions. They cannot perform additional database queries and must not have any side effects. These restrictions allow the database to run the functions anywhere, in any order, and rerun them on failure.

A usability problem with MapReduce is that you have to write two carefully coordinated functions. A declarative language offers more opportunities for a query optimizer to improve the performance of a query. For these reasons, MongoDB 2.2 added support for a declarative query language called the aggregation pipeline:

db.observations.aggregate([
    { $match: { family: "Sharks" } },
    { $group: {
        _id: {
            year:  { $year:  "$observationTimestamp" },
            month: { $month: "$observationTimestamp" }
        },
        totalAnimals: { $sum: "$numAnimals" }
    } }
]);

# Graph-like Data Models

If many-to-many relationships are very common in your application, it becomes more natural to start modeling your data as a graph.

A graph consists of:
- **Vertices** (nodes or entities)  
- **Edges** (relationships or arcs)  

Well-known algorithms can operate on these graphs, like the shortest path between two points or the popularity of a web page.

There are several ways of structuring and querying the data:
- The **property graph model** (implemented by Neo4j, Titan, and Infinite Graph)  
- The **triple-store model** (implemented by Datomic, AllegroGraph, and others)  

There are also three declarative query languages for graphs:
- Cypher  
- SPARQL  
- Datalog  

---

## Property Graphs

Each **vertex** consists of:
- Unique identifier  
- Outgoing edges  
- Incoming edges  
- Collection of properties (key-value pairs)  

Each **edge** consists of:
- Unique identifier  
- Vertex at which the edge starts (tail vertex)  
- Vertex at which the edge ends (head vertex)  
- Label to describe the kind of relationship between the two vertices  
- A collection of properties (key-value pairs)  

Graphs provide a great deal of flexibility for data modeling and are good for evolvability.

---

### Cypher

Cypher is a declarative language for property graphs created by Neo4j.

---

### Graph Queries in SQL

In a relational database, you usually know in advance which joins you need in your query. In a graph query, the number of joins is not fixed in advance.

In Cypher, `:WITHIN*0...` expresses "follow a WITHIN edge, zero or more times" (like the `*` operator in a regular expression). 

This idea of variable-length traversal paths in a query can be expressed using something called **recursive common table expressions** (the `WITH RECURSIVE` syntax).

