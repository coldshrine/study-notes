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

# Triple-stores and SPARQL

In a triple-store, all information is stored in the form of very simple three-part statements:  
**subject, predicate, object** (e.g., Jim, likes, bananas).  

A triple is equivalent to a vertex in a graph.

---

## The SPARQL Query Language

SPARQL is a query language for triple-stores using the RDF data model.

---

## The Foundation: Datalog

Datalog provides the foundation that later query languages build upon. Its model is similar to the triple-store model, but generalized a bit.  

Instead of writing a triple `(subject, predicate, object)`, we write it as `predicate(subject, object)`.

### Rules in Datalog
- Rules tell the database about new predicates.  
- Rules can refer to other rules, just like functions can call other functions or recursively call themselves.  
- Rules can be combined and reused in different queries.  

### Advantages
- Less convenient for simple one-off queries.  
- Better suited for complex data.  

---

## Storage and Retrieval

# Databases: Storage and Retrieval

Databases need to do two things: 
1. **Store the data**  
2. **Give the data back to you**  

---

## Data Structures That Power Your Database

Many databases use a **log**, which is an append-only data file. However, real databases also handle:
- Concurrency control  
- Reclaiming disk space to prevent unbounded log growth  
- Handling errors and partially written records  

### What Is a Log?  
A log is an append-only sequence of records.  

To efficiently find the value for a particular key, we need an additional structure: an **index**.  
- An index is derived from the primary data.  
- Well-chosen indexes speed up read queries but slow down writes.  
- Databases require manual index configuration based on typical query patterns.

---

## Hash Indexes

Key-value stores are similar to the dictionary type (hash map or hash table).

### Simplest Strategy:
- Use an **in-memory hash map** to map each key to a byte offset in the data file.  
- Append new key-value pairs to the file and update the hash map.  

#### Example: **Bitcask** (default storage engine in Riak)
- Keys must fit in available RAM.  
- Values can be loaded from disk if they exceed memory limits.  
- Suitable for frequent updates to values.  

---

### Managing Disk Space
1. **Segment Files**  
   - Split the log into segments when it reaches a certain size.  
   - Write subsequent data to a new segment.  

2. **Compaction**  
   - Remove duplicate keys and keep only the most recent update.  
   - Merge segments during compaction to reduce the number of segments.  

3. **Merged Segments**  
   - Written to a new file, ensuring old segments remain immutable.  
   - Read requests switch to the new segment after merging, and old segments are deleted.  

4. **In-Memory Hash Table**  
   - Each segment has its own hash table.  
   - Lookups start with the most recent segment and move backward as needed.  

---

## Important Considerations in Real Implementations

1. **File Format**  
   - Binary formats are simpler.  

2. **Deleting Records**  
   - Use a special deletion record ("tombstone") to mark entries for removal during merging.  

3. **Crash Recovery**  
   - Store snapshots of segment hash maps on disk to speed up recovery.  
   - Use checksums to detect and ignore corrupted parts of the log.  

4. **Concurrency Control**  
   - Sequential writes are handled by a single writer thread.  
   - Immutable segments enable concurrent reads by multiple threads.  

---

## Advantages of Append-Only Design

- Sequential writes (appending and merging) are faster than random writes, especially on magnetic spinning disks.  
- Simplifies concurrency and crash recovery.  
- Avoids file fragmentation over time.  

---

## Limitations of Hash Tables

1. **Memory Requirements**  
   - The hash table must fit in memory. On-disk hash maps are difficult to optimize.  

2. **Inefficient Range Queries**  
   - Hash tables are not suitable for range queries.  

# SSTables and LSM-Trees

We introduce a new requirement for segment files:  
The sequence of key-value pairs must be **sorted by key**.

---

## Sorted String Table (SSTable)

An SSTable requires:
1. Each key appears only once within a merged segment file (ensured by compaction).  

### Advantages of SSTables Over Log Segments with Hash Indexes:

1. **Efficient Merging**  
   - Merging segments is simple and efficient, leveraging algorithms like mergesort.  
   - When multiple segments contain the same key, the value from the most recent segment is kept, and older values are discarded.  

2. **Reduced Memory Usage**  
   - No need to keep an index of all keys in memory.  
   - For a key like `handiwork`, knowing the offsets for nearby keys (`handback` and `handsome`) allows a targeted search.  
   - You can jump to the offset for `handback` and scan until you find `handiwork`. If not found, the key is not present.  

3. **In-Memory Index Optimization**  
   - An in-memory index is still required to map some keys to offsets.  
   - Storing one key for every few kilobytes of the segment file is sufficient.  

4. **Compression**  
   - Records in the requested range can be grouped into blocks.  
   - Blocks are compressed before being written to disk.  
   
# How Do We Get the Data Sorted in the First Place?

With red-black trees or AVL trees, you can insert keys in any order and read them back in sorted order.

- When a write comes in, add it to an **in-memory balanced tree structure** (*memtable*).  
- When the memtable gets bigger than some threshold (megabytes), write it out to disk as an **SSTable file**. Writes can continue to a new memtable instance.  
- On a read request, try to find the key in the **memtable**, then in the most recent **on-disk segment**, then in the next-older segment, etc.  
- From time to time, run **merging and compaction** in the background to discard overwritten and deleted values.  

If the database crashes, the most recent writes are lost.  
To handle this:  
- Keep a separate **log on disk** where every write is immediately appended.  
  - The log is not in sorted order but helps restore the memtable after a crash.  
  - Every time the memtable is written out to an SSTable, the log can be discarded.  

---

# LSM-Structure Engines (Log Structured Merge-Tree)

Storage engines based on this principle of merging and compacting sorted files are often called **LSM structure engines**.

- **Lucene**, an indexing engine for full-text search used by Elasticsearch and Solr, uses a similar method for storing its term dictionary.  
- The **LSM-tree algorithm** can be slow when looking up keys that don't exist in the database.  

To optimize:  
- Use additional **Bloom filters** (a memory-efficient data structure for approximating the contents of a set).  

---

# Strategies for SSTable Compaction and Merging

There are different strategies to determine the order and timing of how SSTables are compacted and merged:  

1. **Size-Tiered Compaction**  
   - Newer and smaller SSTables are successively merged into older and larger SSTables.  
   - Used by **HBase**.  

2. **Leveled Compaction**  
   - The key range is split into smaller SSTables.  
   - Older data is moved into separate "levels", reducing disk space usage during compaction.  
   - Used by **LevelDB** and **RocksDB**.  

3. **Cassandra**  
   - Supports both size-tiered and leveled compaction.  

# B-Trees

The **B-tree** is the most widely used indexing structure.  

- **Key-value pairs** are sorted by key, enabling efficient key-value lookups and range queries.  
- The database is broken into **fixed-size blocks or pages**, traditionally 4KB, instead of variable-size segments as in log-structured indexes.  

---

## Structure and Operations

- **Root Page**: One page is designated as the root, and navigation starts from there.  
  - Contains keys and references to child pages.  

- **Updating an Existing Key**:  
  1. Search for the leaf page containing the key.  
  2. Update the value in that page.  
  3. Write the page back to disk.  

- **Adding a New Key**:  
  1. Find the appropriate page.  
  2. Add the key.  
  3. If the page is full, split it into two half-full pages.  
  4. Update the parent page to reflect the new subdivision of key ranges.  

- **Balancing**:  
  - B-trees remain balanced.  
  - A B-tree with *n* keys always has a depth of **O(log n)**.

---

## Write Operations

- **Overwrite-Based**:  
  - The basic operation overwrites a page on disk with new data.  
  - The location of the page remains unchanged, so references to the page remain intact.  
  - In contrast, **LSM-trees** (log-structured indexes) only append to files.  

- **Page Splits**:  
  - Some operations require multiple page overwrites.  
  - Example: When splitting a page, two pages are rewritten, and their parent page is also updated.  

- **Crash Scenarios**:  
  - If the database crashes after only some pages have been written, the index may be corrupted.  

---

## Write-Ahead Log (WAL)

- To ensure durability and consistency, an additional data structure, the **write-ahead log (WAL)** (also known as the redo log), is often used.  

---

## Concurrency Control

- If multiple threads access the B-tree:  
  - Careful concurrency control is required.  
  - Typically, **latches** (lightweight locks) protect the tree's internal data structures.  
  

# B-trees and LSM-trees

LSM-trees are typically faster for writes, whereas B-trees are thought to be faster for reads. Reads are typically slower on LSM-trees as they have to check several different data structures and SSTables at different stages of compaction.

## Advantages of LSM-trees:

- LSM-trees are typically able to sustain higher write throughput than B-trees, party because they sometimes have lower write amplification: a write to the database results in multiple writes to disk. The more a storage engine writes to disk, the fewer writes per second it can handle.  
- LSM-trees can be compressed better, and thus often produce smaller files on disk than B-trees. B-trees tend to leave disk space unused due to fragmentation.

## Downsides of LSM-trees:

- Compaction process can sometimes interfere with the performance of ongoing reads and writes. B-trees can be more predictable. The bigger the database, the more disk bandwidth is required for compaction. Compaction cannot keep up with the rate of incoming writes, if not configured properly you can run out of disk space.  
- On B-trees, each key exists in exactly one place in the index. This offers strong transactional semantics. Transaction isolation is implemented using locks on ranges of keys, and in a B-tree index, those locks can be directly attached to the tree.

# Other Indexing Structures

We've only discussed key-value indexes, which are like primary key index. There are also secondary indexes.

A secondary index can be easily constructed from a key-value index. The main difference is that in a secondary index, the indexed values are not necessarily unique. There are two ways of doing this: making each value in the index a list of matching row identifiers or by making a each entry unique by appending a row identifier to it.

# Full-text Search and Fuzzy Indexes

Indexes don't allow you to search for similar keys, such as misspelled words. Such fuzzy querying requires different techniques.

Full-text search engines allow synonyms, grammatical variations, occurrences of words near each other.

Lucene uses SSTable-like structure for its term dictionary. Lucene, the in-memory index is a finite state automaton, similar to a trie.

# Keeping Everything in Memory

Disks have two significant advantages: they are durable, and they have lower cost per gigabyte than RAM.

It's quite feasible to keep them entirely in memory, this has led to in-memory databases.

Key-value stores, such as Memcached, are intended for cache only; it's acceptable for data to be lost if the machine is restarted. Other in-memory databases aim for durability, with special hardware, writing a log of changes to disk, writing periodic snapshots to disk, or by replicating in-memory state to other machines.

When an in-memory database is restarted, it needs to reload its state, either from disk or over the network from a replica. The disk is merely used as an append-only log for durability, and reads are served entirely from memory.

Products such as VoltDB, MemSQL, and Oracle TimesTen are in-memory databases. Redis and Couchbase provide weak durability.

In-memory databases can be faster because they can avoid the overheads of encoding in-memory data structures in a form that can be written to disk.

Another interesting area is that in-memory databases may provide data models that are difficult to implement with disk-based indexes.

# Transaction Processing or Analytics?

A transaction is a group of reads and writes that form a logical unit. This pattern became known as **online transaction processing (OLTP)**.

Data analytics has very different access patterns. A query would need to scan over a huge number of records, only reading a few columns per record, and calculating aggregate statistics.

These queries are often written by business analysts and fed into reports. This pattern became known as **online analytics processing (OLAP)**.

# Data Warehousing

A data warehouse is a separate database that analysts can query to their heart's content without affecting OLTP operations. It contains a read-only copy of the data in all various OLTP systems in the company. Data is extracted out of OLTP databases (through periodic data dumps or a continuous stream of updates), transformed into an analysis-friendly schema, cleaned up, and then loaded into the data warehouse (process **Extract-Transform-Load** or **ETL**).

A data warehouse is most commonly relational, but the internals of the systems can look quite different.

- **Amazon RedShift** is a hosted version of ParAccel.  
- Other tools include **Apache Hive**, **Spark SQL**, **Cloudera Impala**, **Facebook Presto**, **Apache Tajo**, and **Apache Drill**. Some of them are based on ideas from Google's **Dremel**.

Data warehouses are used in a fairly formulaic style known as a **star schema**.

- **Facts** are captured as individual events, allowing maximum flexibility for analysis later. 
- The fact table can become extremely large.

Dimensions represent the who, what, where, when, how and why of the event.

The name "star schema" comes from the fact than when the table relationships are visualised, the fact table is in the middle, surrounded by its dimension tables, like the rays of a star.

Fact tables often have over 100 columns, sometimes several hundred. Dimension tables can also be very wide.

Column-oriented storage  
In a row-oriented storage engine, when you do a query that filters on a specific field, the engine will load all those rows with all their fields into memory, parse them and filter out the ones that don't meet the requirement. This can take a long time.

Column-oriented storage is simple: don't store all the values from one row together, but store all values from each column together instead. If each column is stored in a separate file, a query only needs to read and parse those columns that are used in a query, which can save a lot of work.

Column-oriented storage often lends itself very well to compression as the sequences of values for each column look quite repetitive, which is a good sign for compression. A technique that is particularly effective in data warehouses is bitmap encoding.

Bitmap indexes are well suited for all kinds of queries that are common in a data warehouse.

**Cassandra and HBase have a concept of column families, which they inherited from Bigtable.**

Besides reducing the volume of data that needs to be loaded from disk, column-oriented storage layouts are also good for making efficient use of CPU cycles (vectorised processing).

Column-oriented storage, compression, and sorting helps to make read queries faster and make sense in data warehouses, where most of the load consist on large read-only queries run by analysts. The downside is that writes are more difficult.

An update-in-place approach, like B-tree use, is not possible with compressed columns. If you insert a row in the middle of a sorted table, you would most likely have to rewrite all column files.

It's worth mentioning materialised aggregates as some cache of the counts ant the sums that queries use most often. A way of creating such a cache is with a materialised view, on a relational model this is usually called a virtual view: a table-like object whose contents are the results of some query. A materialised view is an actual copy of the query results, written in disk, whereas a virtual view is just a shortcut for writing queries.

When the underlying data changes, a materialised view needs to be updated, because it is denormalised copy of the data. Database can do it automatically, but writes would become more expensive.

A common special case of a materialised view is know as a data cube or OLAP cube, a grid of aggregates grouped by different dimensions.

Encoding and evolution  
Change to an application's features also requires a change to data it stores.

Relational databases conform to one schema although that schema can be changed, there is one schema in force at any point in time. Schema-on-read (or schemaless) contain a mixture of older and newer data formats.

In large applications changes don't happen instantaneously. You want to perform a rolling upgrade and deploy a new version to a few nodes at a time, gradually working your way through all the nodes without service downtime.

Old and new versions of the code, and old and new data formats, may potentially all coexist. We need to maintain compatibility in both directions:

- **Backward compatibility**: newer code can read data that was written by older code.  
- **Forward compatibility**: older code can read data that was written by newer code.

Formats for encoding data  
Two different representations:  

- **In memory**  
- When you want to write data to a file or send it over the network, you have to encode it  

Thus, you need a translation between the two representations. In-memory representation to byte sequence is called **encoding** (serialisation or marshalling), and the reverse is called **decoding** (parsing, deserialisation or unmarshalling).  

Programming languages come with built-in support for encoding in-memory objects into byte sequences, but it is usually a bad idea to use them. Precisely because of a few problems.

Often tied to a particular programming language.  
The decoding process needs to be able to instantiate arbitrary classes, and this is frequently a security hole.  

- **Versioning**  
- **Efficiency**  

Standardised encodings can be written and read by many programming languages.  

**JSON, XML, and CSV** are human-readable and popular, especially as data interchange formats, but they have some subtle problems:  

- Ambiguity around the encoding of numbers and dealing with large numbers.  
- Support for Unicode character strings, but no support for binary strings. People get around this by encoding binary data as Base64, which increases the data size by 33%.  
- There is optional schema support for both XML and JSON.  
- CSV does not have any schema.  

**Binary encoding**  
JSON is less verbose than XML, but both still use a lot of space compared to binary formats. There are binary encodings for JSON (MesagePack, BSON, BJSON, UBJSON, BISON, and Smile), and similar ones for XML (WBXML and Fast Infoset).  

**Apache Thrift and Protocol Buffers (protobuf)** are binary encoding libraries.  

- **Thrift offers two different protocols:**  
  - **BinaryProtocol:** There are no field names like `userName`, `favouriteNumber`. Instead, the data contains field tags, which are numbers (e.g., 1, 2).  
  - **CompactProtocol:** Equivalent to BinaryProtocol but packs the same information in less space. It combines the field type and the tag number into the same byte.  

- **Protocol Buffers:**  
  - Very similar to Thrift's CompactProtocol.  
  - Bit packing is slightly different, which might allow for smaller compression.  

**Schema evolution and compatibility:**  

Schemas inevitably need to change over time (schema evolution). How do Thrift and Protocol Buffers handle schema changes while keeping backward and forward compatibility?  

- **Forward compatible support:**  
  - When adding new fields, assign new tag numbers.  
  - Old code reading new data can simply ignore unrecognized tags.  

- **Backward compatible support:**  
  - As long as each field has a unique tag number, new code can always read old data.  
  - Every field added after the initial schema deployment must be optional or have a default value.  

- **Removing fields:**  
  - Removing a field is like adding one but with reversed backward and forward concerns.  
  - Only optional fields can be removed.  
  - Never reuse the same tag number after removal.  

- **Changing the data type of a field:**  
  - This carries the risk of values losing precision or getting truncated.  

**Avro**  
Apache Avro is another binary format that has two schema languages, one intended for human editing (Avro IDL), and one (based on JSON) that is more easily machine-readable.  

You go through the fields in the order they appear in the schema and use the schema to tell you the datatype of each field. Any mismatch in the schema between the reader and the writer would mean incorrectly decoded data.  

**Schema evolution:**  
- When an application wants to encode some data, it encodes the data using whatever version of the schema it knows (writer's schema).  
- When an application wants to decode some data, it expects the data to be in some schema (reader's schema).  

In Avro, the writer's schema and the reader's schema don't have to be the same. The Avro library resolves the differences by looking at the writer's schema and the reader's schema.  

- **Forward compatibility:**  
  - A new version of the schema as writer and an old version of the schema as reader.  
- **Backward compatibility:**  
  - A new version of the schema as reader and an old version as writer.  

To maintain compatibility, you may only add or remove a field that has a default value.  

- Adding a field without a default value: New readers wouldn't be able to read data written by old writers.  
- Changing the datatype of a field: Possible if Avro can convert the type.  
- Changing the name of a field: Backward compatible but not forward compatible.  

The schema is identified and encoded in the data.  
- In a large file with lots of records, the writer can include the schema at the beginning of the file.  
- In a database with individually written records, you cannot assume all the records will have the same schema, so you include a version number at the beginning of every encoded record.  
- While sending records over the network, you can negotiate the schema version on connection setup.  

Avro is friendlier to dynamically generated schemas (e.g., dumping into a file the database). You can easily generate an Avro schema in JSON.  

If the database schema changes, you can generate a new Avro schema for the updated database schema and export data in the new Avro schema.  

By contrast, with Thrift and Protocol Buffers, every time the database schema changes, you would have to manually update the mappings from database column names to field tags.  

Although textual formats such as JSON, XML, and CSV are widespread, binary encodings based on schemas are also a viable option as they have nice properties:  

- **Compactness:**  
  - Binary formats can be much more compact as they can omit field names from the encoded data.  

- **Schema as documentation:**  
  - The schema is a valuable form of documentation, required for decoding, ensuring it is always up to date.  

- **Compatibility checks:**  
  - A database of schemas allows you to verify forward and backward compatibility changes.  

- **Code generation:**  
  - Generating code from the schema is useful as it enables type checking at compile time.  

## Modes of Dataflow  

### Different Processes on How Data Flows Between Processes  

#### Via Databases  
- **Encoding and Decoding:**  
  - The process that writes to the database encodes the data, and the process that reads from the database decodes it.  

- **Version Compatibility:**  
  - A value in the database may be written by a newer version of the code and subsequently read by an older version still running.  

- **Code vs. Data Longevity:**  
  - When deploying a new version of your application, you may replace the old version with the new one within minutes. However, the same does not apply to databases. Data outlives code, and five-year-old data will still exist in its original encoding unless explicitly rewritten.  

- **Rewriting (Migration):**  
  - Rewriting data is expensive.  
  - Most relational databases support simple schema changes, like adding a new column with a `NULL` default value, without rewriting existing data.  
  - When an old row is read, the database fills in `NULL` values for missing columns.  

### Via Service Calls

You have processes that need to communicate over a network of clients and servers.

Services are similar to databases, each service should be owned by one team, and that team should be able to release versions of the service frequently, without having to coordinate with other teams. We should expect old and new versions of servers and clients to be running at the same time.

Remote procedure calls (RPC) try to make a request to a remote network service look the same as calling a function or method in your programming language. It seems convenient at first, but the approach is flawed:

- A network request is unpredictable.
- A network request may return without a result due to a timeout.
- Retrying will cause the action to be performed multiple times unless you build a mechanism for deduplication (idempotence).
- A network request is much slower than a function call, and its latency is wildly variable.
- Parameters need to be encoded into a sequence of bytes that can be sent over the network, which becomes problematic with larger objects.
- The RPC framework must translate datatypes from one language to another; not all languages have the same types.

There is no point trying to make a remote service look too much like a local object in your programming language because it's a fundamentally different thing.

New generations of RPC frameworks are more explicit about the fact that a remote request is different from a local function call. Frameworks like **Finagle** and **Rest.li** use features like promises to encapsulate asynchronous actions.

**RESTful API** has some significant advantages, such as being good for experimentation and debugging.

REST seems to be the predominant style for public APIs. The main focus of RPC frameworks is on requests between services owned by the same organization, typically within the same datacenter.

### Via Asynchronous Message Passing

In an asynchronous message-passing system, a client's request (usually called a message) is delivered to another process with low latency. The message goes via an intermediary called a **message broker** (message queue or message-oriented middleware), which stores the message temporarily. This approach has several advantages compared to direct RPC:

- It can act as a buffer if the recipient is unavailable or overloaded.
- It can automatically redeliver messages to a process that has crashed, preventing message loss.
- It avoids the sender needing to know the IP address and port number of the recipient (useful in a cloud environment).
- It allows one message to be sent to several recipients.
- It decouples the sender from the recipient.
- The communication happens in one direction: the sender sends the message and then forgets about it (asynchronous).

Open-source implementations for message brokers include **RabbitMQ**, **ActiveMQ**, **HornetQ**, **NATS**, and **Apache Kafka**.

One process sends a message to a named **queue** or **topic**, and the broker ensures the message is delivered to one or more consumers or subscribers to that queue or topic. Message brokers typically don't enforce a particular data model, so you can use any encoding format.

---

### Actor Model

The **actor model** is a programming model for concurrency in a single process. Instead of dealing with threads (and their complications), logic is encapsulated in **actors**. 

- Each actor typically represents one client or entity.
- An actor may have some local state and communicates with other actors by sending and receiving asynchronous messages.
- **Message delivery is not guaranteed**. 
- Since each actor processes only one message at a time, it doesn't need to worry about threads.

In **distributed actor frameworks**, this programming model scales applications across multiple nodes. It integrates a message broker and the actor model into a single framework.

---

### Examples of Distributed Actor Frameworks

- **Akka**:
  - Uses Java's built-in serialization by default, which does not provide forward or backward compatibility.
  - You can replace the default with something like **Protocol Buffers** to enable rolling upgrades.

- **Orleans**:
  - Uses a custom data encoding format by default, which does not support rolling upgrade deployments.

- **Erlang OTP**:
  - Making changes to record schemas is surprisingly difficult.

What happens if multiple machines are involved in storage and retrieval of data?

Reasons for distribute a database across multiple machines:

- Scalability  
- Fault tolerance/high availability  
- Latency, having servers at various locations worldwide  

Replication  
Reasons why you might want to replicate data:  

- To keep data geographically close to your users  
- Increase availability  
- Increase read throughput  

The difficulty in replication lies in handling changes to replicated data. Popular algorithms for replicating changes between nodes: single-leader, multi-leader, and leaderless replication.  

Leaders and followers  
Each node that stores a copy of the database is called a replica.  

Every write to the database needs to be processed by every replica. The most common solution for this is called leader-based replication (active/passive or master-slave replication).  

- One of the replicas is designated the leader (master or primary). Writes to the database must send requests to the leader.  
- Other replicas are known as followers (read replicas, slaves, secondaries or hot standbys). The leader sends the data change to all of its followers as part of a replication log or change stream.  
- Reads can be queried from the leader or any of the followers, while writes are only accepted on the leader.  

MySQL, Oracle Data Guard, SQL Server's AlwaysOn Availability Groups, MongoDB, RethinkDB, Espresso, Kafka, and RabbitMQ are examples of these kinds of databases.  


Synchronous vs asynchronous  
The advantage of synchronous replication is that the follower is guaranteed to have an up-to-date copy of the data that is consistent with the leader. The disadvantage is that if the synchronous follower doesn't respond, the write cannot be processed.  

It's impractical for all followers to be synchronous. If you enable synchronous replication on a database, it usually means that one of the followers is synchronous, and the others are asynchronous. This guarantees an up-to-date copy of the data on at least two nodes (this is sometimes called semi-synchronous).  

Often, leader-based replication is asynchronous. Writes are not guaranteed to be durable; the main advantage of this approach is that the leader can continue processing writes.  

Setting up new followers  
Copying data files from one node to another is typically not sufficient.  

Setting up a follower can usually be done without downtime. The process looks like:  
- Take a snapshot of the leader's database  
- Copy the snapshot to the follower node  
- Follower requests data changes that have happened since the snapshot was taken  
- Once the follower processes the backlog of data changes since the snapshot, it has caught up.  

Handling node outages  
How does high availability work with leader-based replication?  

**Follower failure: catchup recovery**  
- A follower can connect to the leader and request all the data changes that occurred during the time when the follower was disconnected.  

**Leader failure: failover**  
- One of the followers needs to be promoted to be the new leader.  
- Clients need to be reconfigured to send their writes to the new leader.  
- Followers need to start consuming data changes from the new leader.  

**Automatic failover consists of:**  
- **Determining that the leader has failed.** If a node does not respond in a period of time, it's considered dead.  
- **Choosing a new leader.** The best candidate for leadership is usually the replica with the most up-to-date changes from the old leader.  
- **Reconfiguring the system to use the new leader.** The system needs to ensure that the old leader becomes a follower and recognizes the new leader.  

**Things that could go wrong:**  
- If asynchronous replication is used, the new leader may have received conflicting writes in the meantime.  
- Discarding writes is especially dangerous if other storage systems outside of the database need to be coordinated with the database contents.  
- It could happen that two nodes both believe that they are the leader (split brain). Data is likely to be lost or corrupted.  
- What is the right time before the leader is declared dead?  

For these reasons, some operations teams prefer to perform failovers manually, even if the software supports automatic failover.  

Implementation of replication logs  
Statement-based replication  
The leader logs every statement and sends it to its followers (every INSERT, UPDATE or DELETE).  

This type of replication has some problems:  

- Non-deterministic functions such as NOW() or RAND() will generate different values on replicas.  
- Statements that depend on existing data, like auto-increments, must be executed in the same order in each replica.  
- Statements with side effects may result on different results on each replica.  

A solution to this is to replace any nondeterministic function with a fixed return value in the leader.  

# Write-ahead log (WAL) shipping

The log is an append-only sequence of bytes containing all writes to the database. The leader can send it to its followers. This way of replication is used in PostgresSQL and Oracle.

The main disadvantage is that the log describes the data at a very low level (like which bytes were changed in which disk blocks), coupling it to the storage engine.

Usually, it is not possible to run different versions of the database in leaders and followers. This can have a big operational impact, like making it impossible to have a zero-downtime upgrade of the database.

# Logical (row-based) log replication

Basically, a sequence of records describing writes to database tables at the granularity of a row:

- For an inserted row, the new values of all columns.
- For a deleted row, the information that uniquely identifies that row.
- For an updated row, the information to uniquely identify that row and all the new values of the columns.

A transaction that modifies several rows generates several such logs, followed by a record indicating that the transaction was committed. MySQL binlog uses this approach.

Since the logical log is decoupled from the storage engine internals, it's easier to make it backwards compatible.

Logical logs are also easier for external applications to parse, making them useful for data warehouses, custom indexes, and caches (change data capture).

# Trigger-based replication

There are some situations where you may need to move replication up to the application layer.

A trigger lets you register custom application code that is automatically executed when a data change occurs. This is a good opportunity to log this change into a separate table, from which it can be read by an external process.

The main disadvantages are that this approach has greater overhead, is more prone to bugs, but it may be useful due to its flexibility.

# Problems with replication lag

Node failures is just one reason for wanting replication. Other reasons are scalability and latency.

In a read-scaling architecture, you can increase the capacity for serving read-only requests simply by adding more followers. However, this only realistically works on asynchronous replication. The more nodes you have, the likelier is that one will be down, so a fully synchronous configuration would be unreliable.

With an asynchronous approach, a follower may fall behind, leading to inconsistencies in the database (eventual consistency).

The replication lag could be a fraction of a second or several seconds or even minutes.

The problems that may arise and how to solve them.

Reading your own writes  
Read-after-write consistency, also known as read-your-writes consistency is a guarantee that if the user reloads the page, they will always see any updates they submitted themselves.

How to implement it:

When reading something that the user may have modified, read it from the leader. For example, user profile information on a social network is normally only editable by the owner. A simple rule is always read the user's own profile from the leader.  
You could track the time of the latest update and, for one minute after the last update, make all reads from the leader.  
The client can remember the timestamp of the most recent write, then the system can ensure that the replica serving any reads for that user reflects updates at least until that timestamp.  
If your replicas are distributed across multiple datacenters, then any request needs to be routed to the datacenter that contains the leader.  
Another complication is that the same user is accessing your service from multiple devices, you may want to provide cross-device read-after-write consistency.

Some additional issues to consider:

Remembering the timestamp of the user's last update becomes more difficult. The metadata will need to be centralised.  
If replicas are distributed across datacenters, there is no guarantee that connections from different devices will be routed to the same datacenter. You may need to route requests from all of a user's devices to the same datacenter.

Monotonic reads  
Because of followers falling behind, it's possible for a user to see things moving backward in time.

When you read data, you may see an old value; monotonic reads only means that if one user makes several reads in sequence, they will not see time go backward.

Make sure that each user always makes their reads from the same replica. The replica can be chosen based on a hash of the user ID. If the replica fails, the user's queries will need to be rerouted to another replica.

# Consistent prefix reads  
If a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.

This is a particular problem in partitioned (sharded) databases as there is no global ordering of writes.

# Solutions for Replication Lag
A solution is to make sure any writes casually related to each other are written to the same partition.# Solutions for Replication Lag

Transactions exist so there is a way for a database to provide stronger guarantees so that the application can be simpler.

# Multi-Leader Replication

Leader-based replication has one major downside: there is only one leader, and all writes must go through it.

A natural extension is to allow more than one node to accept writes (multi-leader, master-master, or active/active replication) where each leader simultaneously acts as a follower to the other leaders.

# Use Cases for Multi-Leader Replication

## Multi-Datacenter Operation
You can have a leader in each datacenter. Within each datacenter, regular leader-follower replication is used. Between datacenters, each datacenter leader replicates its changes to the leaders in other datacenters.

Compared to a single-leader replication model in multi-datacenters:
- Performance: With single-leader, every write must go across the internet to wherever the leader is, adding significant latency. In multi-leader, every write is processed in the local datacenter and replicated asynchronously to other datacenters. The network delay is hidden from users, improving perceived performance.
- Tolerance of datacenter outages: In single-leader, if the datacenter with the leader fails, failover can promote a follower in another datacenter. In multi-leader, each datacenter can continue operating independently from others.
- Tolerance of network problems: Single-leader is very sensitive to problems in the inter-datacenter link as writes are made synchronously over this link. Multi-leader, with asynchronous replication, can tolerate network problems better.

Multi-leader replication is implemented with Tungsten Replicator for MySQL, BDR for PostgreSQL, or GoldenGate for Oracle. It's common to fall on subtle configuration pitfalls. Autoincrementing keys, triggers, and integrity constraints can be problematic. Multi-leader replication is often considered dangerous and avoided if possible.

## Clients with Offline Operation
If you have an application that needs to work while it is disconnected from the internet, every device that has a local database can act as a leader, and there will be some asynchronous multi-leader replication process (imagine, a Calendar application). CouchDB is designed for this mode of operation.

## Collaborative Editing
Real-time collaborative editing applications allow several people to edit a document simultaneously. Like Etherpad or Google Docs. The user edits a document, the changes are instantly applied to their local replica and asynchronously replicated to the server and any other user. If you want to avoid editing conflicts, you must lock the document before a user can edit it. For faster collaboration, you may want to make the unit of change very small (like a keystroke) and avoid locking.

# Handling Write Conflicts
The biggest problem with multi-leader replication is when conflict resolution is required. This problem does not happen in a single-leader database.

## Synchronous vs Asynchronous Conflict Detection
In single-leader, the second writer can be blocked and wait for the first one to complete, forcing the user to retry the write. On multi-leader, if both writes are successful, the conflict is only detected asynchronously later in time. If you want synchronous conflict detection, you might as well use single-leader replication.

## Conflict Avoidance
The simplest strategy for dealing with conflicts is to avoid them. If all writes for a particular record go through the same leader, then conflicts cannot occur. On an application where a user can edit their own data, you can ensure that requests from a particular user are always routed to the same datacenter and use the leader in that datacenter for reading and writing.

## Converging Toward a Consistent State
On single-leader, the last write determines the final value of the field. In multi-leader, it's not clear what the final value should be. The database must resolve the conflict in a convergent way, all replicas must arrive at the same final value when all changes have been replicated.

Different ways of achieving convergent conflict resolution:
1. Give each write a unique ID (timestamp, long random number, UUID, or a hash of the key and value), pick the write with the highest ID as the winner, and throw away the other writes. This is known as last write wins (LWW) and it is dangerously prone to data loss.
2. Give each replica a unique ID, writes that originated at a higher-numbered replica always take precedence. This approach also implies data loss.
3. Somehow merge the values together.
4. Record the conflict and write application code that resolves it at some later time (perhaps prompting the user).

## Custom Conflict Resolution
Multi-leader replication tools let you write conflict resolution logic using application code.  
On write: As soon as the database system detects a conflict in the log of replicated changes, it calls the conflict handler.  
On read: All the conflicting writes are stored. On read, multiple versions of the data are returned to the application. The application may prompt the user or automatically resolve the conflict. CouchDB works this way.

# Multi-Leader Replication Topologies
A replication topology describes the communication paths along which writes are propagated from one node to another.

The most general topology is all-to-all in which every leader sends its writes to every other leader. MySQL uses circular topology, where each node receives writes from one node and forwards those writes to another node. Another popular topology has the shape of a star, one designated node forwards writes to all of the other nodes.

In circular and star topologies, a write might need to pass through multiple nodes before they reach all replicas. To prevent infinite replication loops, each node is given a unique identifier and the replication log tags each write with the identifiers of the nodes it has passed through. When a node fails, it can interrupt the flow of replication messages.

In all-to-all topology, fault tolerance is better as messages can travel along different paths avoiding a single point of failure. It has some issues too, some network links may be faster than others, and some replication messages may "overtake" others. To order events correctly, there is a technique called version vectors. PostgreSQL BDR does not provide casual ordering of writes, and Tungsten Replicator for MySQL doesn't even try to detect conflicts.

# Leaderless Replication

Simply put, any replica can directly accept writes from clients. Databases like Amazon's in-house Dynamo datastore, Riak, Cassandra, and Voldemort follow the Dynamo style.

In a leaderless configuration, failover does not exist. Clients send the write to all replicas in parallel.

Read requests are also sent to several nodes in parallel. The client may get different responses. Version numbers are used to determine which value is newer.

Eventually, all the data is copied to every replica. After an unavailable node comes back online, it has two different mechanisms to catch up:

- **Read repair**: When a client detects any stale responses, it writes the newer value back to that replica.
- **Anti-entropy process**: A background process constantly looks for differences in data between replicas and copies any missing data from one replica to the other. It does not copy writes in any particular order.

# Quorums for Reading and Writing

If there are `n` replicas, every write must be confirmed by `w` nodes to be considered successful, and we must query at least `r` nodes for each read. As long as `w + r > n`, we expect to get an up-to-date value when reading. `r` and `w` values are called quorum reads and writes and are the minimum number of votes required for the read or write to be valid.

A common choice is to make `n` an odd number (typically 3 or 5) and to set `w = r = (n + 1)/2` (rounded up).

### Limitations:
- **Sloppy quorum**: The `w` writes may end up on different nodes than the `r` reads, so there is no longer a guaranteed overlap.
- If two writes occur concurrently and it is not clear which one happened first, the only safe solution is to merge them. Writes can be lost due to clock skew.
- If a write happens concurrently with a read, the write may be reflected on only some of the replicas.
- If a write succeeded on some replicas but failed on others, it is not rolled back on the replicas where it succeeded. Reads may or may not return the value from that write.
- If a node carrying a new value fails, and its data is restored from a replica carrying an old value, the number of replicas storing the new value may break the quorum condition.

Dynamo-style databases are generally optimised for use cases that can tolerate eventual consistency.

### Sloppy quorums and hinted handoff
Leaderless replication may be appealing for use cases that require high availability and low latency, and that can tolerate occasional stale reads.

It's likely that the client won't be able to connect to some database nodes during a network interruption.

- Is it better to return errors to all requests for which we cannot reach quorum of **w** or **r** nodes?  
- Or should we accept writes anyway, and write them to some nodes that are reachable but aren't among the **n** nodes on which the value usually lives?

The latter is known as **sloppy quorum**: writes and reads still require **w** and **r** successful responses, but those may include nodes that are not among the designated **n** "home" nodes for a value.

Once the network interruption is fixed, any writes are sent to the appropriate "home" nodes (**hinted handoff**).

Sloppy quorums are useful for increasing write availability: as long as any **w** nodes are available, the database can accept writes. This also means that you cannot be sure to read the latest value for a key, because it may have been temporarily written to some nodes outside of **n**.

### Multi-datacenter operation
Each write from a client is sent to all replicas, regardless of datacenter, but the client usually only waits for acknowledgement from a quorum of nodes within its local datacenter so that it is unaffected by delays and interruptions on cross-datacenter links.

---

### Detecting concurrent writes
In order to become eventually consistent, the replicas should converge toward the same value. If you want to avoid losing data, you, the application developer, need to know a lot about the internals of your database's conflict handling.

- **Last write wins (discarding concurrent writes):**  
  Even though the writes don't have a natural ordering, we can force an arbitrary order on them. We can attach a timestamp to each write and pick the most recent.  
  - There are some situations, such as caching, in which lost writes are acceptable.  
  - If losing data is not acceptable, **LWW** is a poor choice for conflict resolution.

- **The "happens-before" relationship and concurrency:**  
  Whether one operation happens before another operation is the key to defining what concurrency means.  
  - We can simply say that two operations are concurrent if neither happens before the other.  
  - Either **A happened before B**, or **B happened before A**, or **A and B are concurrent**.

### Capturing the happens-before relationship
The server can determine whether two operations are concurrent by looking at the version numbers.

- **Versioning mechanism:**  
  - The server maintains a version number for every key.  
  - It increments the version number every time that key is written.  
  - The new version number is stored along with the value written.

- **Client operations:**  
  - **Read:**  
    - When a client reads a key, the server returns all values that have not been overwritten, as well as the latest version number.  
    - A client must read a key before writing.  
  - **Write:**  
    - When a client writes a key, it must include the version number from the prior read.  
    - The client must merge together all values that it received in the prior read.

- **Server handling writes:**  
  - When the server receives a write with a particular version number:  
    - It can overwrite all values with that version number or below.  
    - It must keep all values with a higher version number.

Merging concurrently written values  
No data is silently dropped. It requires clients to do some extra work; they have to clean up afterward by merging the concurrently written values. Riak calls these concurrent values siblings.  

Merging sibling values is the same problem as conflict resolution in multi-leader replication. A simple approach is to just pick one of the values based on a version number or timestamp (last write wins). You may need to do something more intelligent in application code to avoid losing data.  

If you want to allow people to remove things, the union of siblings may not yield the right result. An item cannot simply be deleted from the database when it is removed; the system must leave a marker with an appropriate version number to indicate that the item has been removed when merging siblings (tombstone).  

Merging siblings in application code is complex and error-prone. There are efforts to design data structures that can perform this merging automatically (CRDTs).  

Version vectors  
We need a version number per replica as well as per key. Each replica increments its own version number when processing a write and also keeps track of the version numbers it has seen from each of the other replicas.  

The collection of version numbers from all the replicas is called a version vector.  

Version vectors are sent from the database replicas to clients when values are read and need to be sent back to the database when a value is subsequently written. Riak calls this causal context. Version vectors allow the database to distinguish between overwrites and concurrent writes.  

# Partitioning  
Replication, for very large datasets or very high query throughput is not sufficient, we need to break the data up into partitions (sharding).  

Basically, each partition is a small database of its own.  

The main reason for wanting to partition data is scalability, query load can be load cabe distributed across many processors. Throughput can be scaled by adding more nodes.  

---

## Partitioning and replication  
Each record belongs to exactly one partition, it may still be stored on several nodes for fault tolerance.  

A node may store more than one partition.  

---

## Partition of key-value data  
Our goal with partitioning is to spread the data and the query load evenly across nodes.  

If partition is unfair, we call it skewed. It makes partitioning much less effective. A partition with disproportionately high load is called a hot spot.  

The simplest approach is to assign records to nodes randomly. The main disadvantage is that if you are trying to read a particular item, you have no way of knowing which node it is on, so you have to query all nodes in parallel.  

---

## Partition by key range  
Assign a continuous range of keys, like the volumes of a paper encyclopaedia. Boundaries might be chose manually by an administrator, or the database can choose them automatically. On each partition, keys are in sorted order so scans are easy.  

The downside is that certain access patterns can lead to hot spots.  

---

## Partitioning by hash of key  
A good hash function takes skewed data and makes it uniformly distributed. There is no need to be cryptographically strong (MongoDB uses MD5 and Cassandra uses Murmur3). You can assign each partition a range of hashes. The boundaries can be evenly spaced or they can be chosen pseudorandomly (consistent hashing).  

Unfortunately we lose the ability to do efficient range queries. Keys that were once adjacent are now scattered across all the partitions. Any range query has to be sent to all partitions.  

---

## Skewed workloads and relieving hot spots  
You can't avoid hot spots entirely. For example, you may end up with large volume of writes to the same key.  

It's the responsibility of the application to reduce the skew. A simple technique is to add a random number to the beginning or end of the key.  

Splitting writes across different keys, makes reads now to do some extra work and combine them.  

# Partitioning and Secondary Indexes

The situation gets more complicated if **secondary indexes** are involved. A **secondary index** usually doesn't identify the record uniquely. They don't map neatly to partitions.

## Partitioning Secondary Indexes by Document

Each partition maintains its **secondary indexes**, covering only the documents in that partition (**local index**).

You need to send the query to all partitions and combine all the results you get back (**scatter/gather**). This is prone to **tail latency amplification** and is widely used in **MongoDB**, **Riak**, **Cassandra**, **Elasticsearch**, **SolrCloud**, and **VoltDB**.

## Partitioning Secondary Indexes by Term

We construct a **global index** that covers data in all partitions. The **global index** must also be partitioned so it doesn't become the bottleneck.

It is called **term-partitioned** because the term we're looking for determines the partition of the index.

Partitioning by term can be useful for **range scans**, whereas partitioning on a **hash of the term** gives a more even distribution load.

The advantage is that it can make reads more efficient: rather than doing **scatter/gather** over all partitions, a client only needs to make a request to the partition containing the term that it wants. The downside of a **global index** is that **writes are slower and complicated**.

# Rebalancing Partitions

The process of moving load from one node in the cluster to another.

## Strategies for Rebalancing

### How Not to Do It: Hash Mod N

The problem with **mod N** is that if the number of nodes **N** changes, most of the keys will need to be moved from one node to another.

### Fixed Number of Partitions

Create many more partitions than there are nodes and assign several partitions to each node. If a node is added to the cluster, we can steal a few partitions from every existing node until partitions are fairly distributed once again. 

- The number of partitions does not change, nor does the assignment of keys to partitions. 
- The only thing that changes is the assignment of partitions to nodes. 
- This is used in **Riak**, **Elasticsearch**, **Couchbase**, and **Voldemort**. 
- You need to choose a high enough number of partitions to accommodate future growth—neither too big nor too small.

### Dynamic Partitioning

The number of partitions adapts to the total data volume. 

- An empty database starts with an empty partition. 
- While the dataset is small, all writes have to be processed by a single node while the other nodes sit idle. 
- **HBase** and **MongoDB** allow an initial set of partitions to be configured (**pre-splitting**).

### Partitioning Proportionally to Nodes

**Cassandra** and **Ketama** make the number of partitions proportional to the number of nodes. 

- Have a fixed number of partitions per node. 
- This approach also keeps the size of each partition fairly stable.

## Automatic Versus Manual Rebalancing

Fully automated rebalancing may seem convenient, but the process can overload the network or the nodes and harm the performance of other requests while the rebalancing is in progress.

It can be good to have a human in the loop for rebalancing. You may avoid operational surprises.

# Request Routing

This problem is also called **service discovery**. There are different approaches:

1. **Allow clients to contact any node**  
   - The node handles the request directly or forwards it to the appropriate node.

2. **Use a routing tier**  
   - Send all requests from clients to a routing tier that acts as a partition-aware load balancer.

3. **Make clients aware of partitioning**  
   - Clients are informed about the partitioning and the assignment of partitions to nodes.

### Handling Changes in Partition Assignment

A common challenge is determining how the component making the routing decision learns about changes in the assignment of partitions to nodes.

- Many distributed data systems rely on a **separate coordination service** such as **ZooKeeper** to track cluster metadata:
  - Each node registers itself in ZooKeeper.
  - ZooKeeper maintains the authoritative mapping of partitions to nodes.
  - The routing tier or the partitioning-aware client can subscribe to this information in ZooKeeper.
  
- Examples of systems using ZooKeeper:
  - **HBase**, **SolrCloud**, and **Kafka**.

- Systems with alternative approaches:
  - **MongoDB** uses its own config server.
  - **Cassandra** and **Riak** use a **gossip protocol**.

---

# Parallel Query Execution

Massively Parallel Processing (**MPP**) relational database products are much more sophisticated in the types of queries they support.

# Transactions

Implementing fault-tolerant mechanisms is a significant challenge.

## The Slippery Concept of a Transaction

Transactions simplify fault tolerance and concurrency issues by grouping reads and writes into a single operation. Conceptually:

- **All reads and writes in a transaction are executed as one operation.**
  - Either the entire transaction succeeds (**commit**) or it fails (**abort/rollback**).
- Transactions allow applications to ignore certain potential error scenarios and concurrency issues while ensuring **safety guarantees**.

---

## ACID

The ACID properties describe the key guarantees of transactions:

1. **Atomicity**  
   - Not about concurrency but about handling partial writes.  
   - If a fault occurs after some writes have been processed, the transaction aborts, leaving no partial changes.  
   - **Better term:** Abortability.

2. **Consistency**  
   - Ensures that invariants on your data are always true.  
   - This depends on the **application's notion of invariants** (e.g., specific rules for valid data).  
   - While **atomicity, isolation, and durability** are properties of the database, **consistency** (in the ACID sense) is a property of the application.

3. **Isolation**  
   - Ensures that concurrently executing transactions are **isolated** from one another.  
   - Also known as **serializability**:  
     - Transactions behave as if they are running serially (one after another), even when they are executed concurrently.

4. **Durability**  
   - Guarantees that once a transaction successfully commits, its changes will not be lost, even in the event of:  
     - Hardware faults.  
     - Database crashes.  
   - In a **single-node database**, this means writing data to **nonvolatile storage**.  
   - In a **replicated database**, this means data is successfully copied to a required number of nodes.

Atomicity can be implemented using a log for crash recovery, and isolation can be implemented using a lock on each object, allowing only one thread to access an object at any one time.

# Transactions and Error Recovery

A key feature of transactions is their ability to be **aborted and safely retried** if an error occurs.

- In **datastores with leaderless replication**, it is the **application's responsibility** to handle error recovery.
- The purpose of aborts is to ensure **safe retries**, enabling the application to recover from transient issues.

---

## Weak Isolation Levels

Concurrency issues (e.g., race conditions) arise when:  
1. One transaction reads data that is concurrently modified by another transaction.  
2. Two transactions attempt to simultaneously modify the same data.

### Database Isolation and Concurrency

Databases provide **transaction isolation** to hide concurrency issues, but this comes with trade-offs:  

- **Serializable Isolation**:  
  - Provides the highest level of isolation, ensuring transactions behave as if executed one at a time.  
  - However, it incurs a significant **performance cost**.

- **Weaker Isolation Levels**:  
  - Common in practice to reduce performance overhead.  
  - These levels protect against **some** concurrency issues but not all.  
  - Applications must account for the remaining issues, potentially increasing complexity.

# Weak Isolation Levels in Practice

## Read Committed

The **Read Committed** isolation level provides two key guarantees:

1. **No Dirty Reads**  
   - When reading from the database, only **committed data** is visible.  
   - Writes by a transaction only become visible to others after the transaction **commits**.

2. **No Dirty Writes**  
   - Transactions will only overwrite committed data.  
   - Dirty writes are prevented by ensuring that:
     - A second write is delayed until the first write's transaction has either committed or aborted.

### Implementation of Read Committed

#### Preventing Dirty Writes
- Most databases use **row-level locks** to prevent dirty writes:
  - A lock is held by the transaction performing the write until it commits or aborts.
  - Only **one transaction** can hold the lock for any given object at a time.

#### Preventing Dirty Reads
- Requiring **read locks** is impractical in many cases:
  - A long-running write transaction can block multiple read-only transactions, leading to significant delays.
- Instead, databases handle dirty reads by:
  - Remembering both the **old committed value** and the **new value** set by the transaction holding the write lock.
  - While the transaction is ongoing:
    - Other transactions reading the object are given the **old committed value**.

Snapshot isolation and repeatable read  
There are still plenty of ways in which you can have concurrency bugs when using this isolation level.  

Nonrepeatable read or read skew, when you read at the same time you committed a change you may see temporal and inconsistent results.  

There are some situations that cannot tolerate such temporal inconsistencies:  

Backups. During the time that the backup process is running, writes will continue to be made to the database. If you need to restore from such a backup, inconsistencies can become permanent.  
Analytic queries and integrity checks. You may get nonsensical results if they observe parts of the database at different points in time.  

Snapshot isolation is the most common solution. Each transaction reads from a consistent snapshot of the database.  

The implementation of snapshots typically use write locks to prevent dirty writes.  

The database must potentially keep several different committed versions of an object (multi-version concurrency control or MVCC).  

Read committed uses a separate snapshot for each query, while snapshot isolation uses the same snapshot for an entire transaction.  

How do indexes work in a multi-version database? One option is to have the index simply point to all versions of an object and require an index query to filter out any object versions that are not visible to the current transaction.  

Snapshot isolation is called serializable in Oracle, and repeatable read in PostgreSQL and MySQL.  

## Preventing lost updates
This might happen if an application reads some value from the database, modifies it, and writes it back. If two transactions do this concurrently, one of the modifications can be lost (later write clobbers the earlier write).

##### Atomic write operations

A solution for this it to avoid the need to implement read-modify-write cycles and provide atomic operations such us

```sql
UPDATE counters SET value = value + 1 WHERE key = 'foo';
```

MongoDB provides atomic operations for making local modifications, and Redis provides atomic operations for modifying data structures.

##### Explicit locking

The application explicitly lock objects that are going to be updated.

##### Automatically detecting lost updates

Allow them to execute in parallel, if the transaction manager detects a lost update, abort the transaction and force it to retry its read-modify-write cycle.

MySQL/InnoDB's repeatable read does not detect lost updates.

##### Compare-and-set

If the current value does not match with what you previously read, the update has no effect.

```SQL
UPDATE wiki_pages SET content = 'new content'
  WHERE id = 1234 AND content = 'old content';
```

##### Conflict resolution and replication

With multi-leader or leaderless replication, compare-and-set do not apply.

A common approach in replicated databases is to allow concurrent writes to create several conflicting versions of a value (also know as _siblings_), and to use application code or special data structures to resolve and merge these versions after the fact.

#### Write skew and phantoms

Imagine Alice and Bob are two on-call doctors for a particular shift. Imagine both the request to leave because they are feeling unwell. Unfortunately they happen to click the button to go off call at approximately the same time.

    ALICE                                   BOB

    ┌─ BEGIN TRANSACTION                    ┌─ BEGIN TRANSACTION
    │                                       │
    ├─ currently_on_call = (                ├─ currently_on_call = (
    │   select count(*) from doctors        │    select count(*) from doctors
    │   where on_call = true                │    where on_call = true
    │   and shift_id = 1234                 │    and shift_id = 1234
    │  )                                    │  )
    │  // now currently_on_call = 2         │  // now currently_on_call = 2
    │                                       │
    ├─ if (currently_on_call  2) {          │
    │    update doctors                     │
    │    set on_call = false                │
    │    where name = 'Alice'               │
    │    and shift_id = 1234                ├─ if (currently_on_call >= 2) {
    │  }                                    │    update doctors
    │                                       │    set on_call = false
    └─ COMMIT TRANSACTION                   │    where name = 'Bob'  
                                            │    and shift_id = 1234
                                            │  }
                                            │
                                            └─ COMMIT TRANSACTION

Since database is using snapshot isolation, both checks return 2. Both transactions commit, and now no doctor is on call. The requirement of having at least one doctor has been violated.

Write skew can occur if two transactions read the same objects, and then update some of those objects. You get a dirty write or lost update anomaly.

Ways to prevent write skew are a bit more restricted:
* Atomic operations don't help as things involve more objects.
* Automatically prevent write skew requires true serializable isolation.
* The second-best option in this case is probably to explicitly lock the rows that the transaction depends on.
  ```sql
  BEGIN TRANSACTION;

  SELECT * FROM doctors
  WHERE on_call = true
  AND shift_id = 1234 FOR UPDATE;

  UPDATE doctors
  SET on_call = false
  WHERE name = 'Alice'
  AND shift_id = 1234;

  COMMIT;
  ```

### Serializability

This is the strongest isolation level. It guarantees that even though transactions may execute in parallel, the end result is the same as if they had executed one at a time, _serially_, without concurrency. Basically, the database prevents _all_ possible race conditions.

There are three techniques for achieving this:
* Executing transactions in serial order
* Two-phase locking
* Serializable snapshot isolation.

#### Actual serial execution

The simplest way of removing concurrency problems is to remove concurrency entirely and execute only one transaction at a time, in serial order, on a single thread. This approach is implemented by VoltDB/H-Store, Redis and Datomic.

##### Encapsulating transactions in stored procedures

With interactive style of transaction, a lot of time is spent in network communication between the application and the database.

For this reason, systems with single-threaded serial transaction processing don't allow interactive multi-statement transactions. The application must submit the entire transaction code to the database ahead of time, as a _stored procedure_, so all the data required by the transaction is in memory and the procedure can execute very fast.

There are a few pros and cons for stored procedures:
* Each database vendor has its own language for stored procedures. They usually look quite ugly and archaic from today's point of view, and they lack the ecosystem of libraries.
* It's harder to debug, more awkward to keep in version control and deploy, trickier to test, and difficult to integrate with monitoring.

Modern implementations of stored procedures include general-purpose programming languages instead: VoltDB uses Java or Groovy, Datomic uses Java or Clojure, and Redis uses Lua.

##### Partitioning

Executing all transactions serially limits the transaction throughput to the speed of a single CPU.

In order to scale to multiple CPU cores you can potentially partition your data and each partition can have its own transaction processing thread. You can give each CPU core its own partition.

For any transaction that needs to access multiple partitions, the database must coordinate the transaction across all the partitions. They will be vastly slower than single-partition transactions.

#### Two-phase locking (2PL)

> Two-phase locking (2PL) sounds similar to two-phase _commit_ (2PC) but be aware that they are completely different things.

Several transactions are allowed to concurrently read the same object as long as nobody is writing it. When somebody wants to write (modify or delete) an object, exclusive access is required.

Writers don't just block other writers; they also block readers and vice versa. It protects against all the race conditions discussed earlier.

Blocking readers and writers is implemented by a having lock on each object in the database. The lock is used as follows:
* if a transaction want sot read an object, it must first acquire a lock in shared mode.
* If a transaction wants to write to an object, it must first acquire the lock in exclusive mode.
* If a transaction first reads and then writes an object, it may upgrade its shared lock to an exclusive lock.
* After a transaction has acquired the lock, it must continue to hold the lock until the end of the transaction (commit or abort). **First phase is when the locks are acquired, second phase is when all the locks are released.**


It can happen that transaction A is stuck waiting for transaction B to release its lock, and vice versa (_deadlock_).

**The performance for transaction throughput and response time of queries are significantly worse under two-phase locking than under weak isolation.**

A transaction may have to wait for several others to complete before it can do anything.

Databases running 2PL can have unstable latencies, and they can be very slow at high percentiles. One slow transaction, or one transaction that accesses a lot of data and acquires many locks can cause the rest of the system to halt.

##### Predicate locks

With _phantoms_, one transaction may change the results of another transaction's search query.

In order to prevent phantoms, we need a _predicate lock_. Rather than a lock belonging to a particular object, it belongs to all objects that match some search condition.

Predicate locks applies even to objects that do not yet exist in the database, but which might be added in the future (phantoms).

##### Index-range locks

Predicate locks do not perform well. Checking for matching locks becomes time-consuming and for that reason most databases implement _index-range locking_.

It's safe to simplify a predicate by making it match a greater set of objects.

These locks are not as precise as predicate locks would be, but since they have much lower overheads, they are a good compromise.

#### Serializable snapshot isolation (SSI)

It provides full serializability and has a small performance penalty compared to snapshot isolation. SSI is fairly new and might become the new default in the future.

##### Pesimistic versus optimistic concurrency control

Two-phase locking is called _pessimistic_ concurrency control because if anything might possibly go wrong, it's better to wait.

Serial execution is also _pessimistic_ as is equivalent to each transaction having an exclusive lock on the entire database.

Serializable snapshot isolation is _optimistic_ concurrency control technique. Instead of blocking if something potentially dangerous happens, transactions continue anyway, in the hope that everything will turn out all right. The database is responsible for checking whether anything bad happened. If so, the transaction is aborted and has to be retried.

If there is enough spare capacity, and if contention between transactions is not too high, optimistic concurrency control techniques tend to perform better than pessimistic ones.

SSI is based on snapshot isolation, reads within a transaction are made from a consistent snapshot of the database. On top of snapshot isolation, SSI adds an algorithm for detecting serialization conflicts among writes and determining which transactions to abort.

The database knows which transactions may have acted on an outdated premise and need to be aborted by:
* **Detecting reads of a stale MVCC object version.** The database needs to track when a transaction ignores another transaction's writes due to MVCC visibility rules. When a transaction wants to commit, the database checks whether any of the ignored writes have now been committed. If so, the transaction must be aborted.
* **Detecting writes that affect prior reads.** As with two-phase locking, SSI uses index-range locks except that it does not block other transactions. When a transaction writes to the database, it must look in the indexes for any other transactions that have recently read the affected data. It simply notifies the transactions that the data they read may no longer be up to date.

##### Performance of serializable snapshot isolation

Compared to two-phase locking, the big advantage of SSI is that one transaction doesn't need to block waiting for locks held by another transaction. Writers don't block readers, and vice versa.

Compared to serial execution, SSI is not limited to the throughput of a single CPU core. Transactions can read and write data in multiple partitions while ensuring serializable isolation.

The rate of aborts significantly affects the overall performance of SSI. SSI requires that read-write transactions be fairly short (long-running read-only transactions may be okay).

## The trouble with distributed systems

### Faults and partial failures

A program on a single computer either works or it doesn't. There is no reason why software should be flaky (non deterministic).

In a distributed systems we have no choice but to confront the messy reality of the physical world. There will be parts that are broken in an unpredictable way, while others work. Partial failures are _nondeterministic_. Things will unpredicably fail.

We need to accept the possibility of partial failure and build fault-tolerant mechanism into the software. **We need to build a reliable system from unreliable components.**

### Unreliable networks

Focusing on _shared-nothing systems_ the network is the only way machines communicate.

The internet and most internal networks are _asynchronous packet networks_. A message is sent and the network gives no guarantees as to when it will arrive, or whether it will arrive at all. Things that could go wrong:
1. Request lost
2. Request waiting in a queue to be delivered later
3. Remote node may have failed
4. Remote node may have temporarily stoped responding
5. Response has been lost on the network
6. The response has been delayed and will be delivered later

If you send a request to another node and don't receive a response, it is _impossible_ to tell why.

**The usual way of handling this issue is a _timeout_**: after some time you give up waiting and assume that the response is not going to arrive.

Nobody is immune to network problems. You do need to know how your software reacts to network problems to ensure that the system can recover from them. It may make sense to deliberately trigger network problems and test the system's response.

If you want to be sure that a request was successful, you need a positive response from the application itself.

If something has gone wrong, you have to assume that you will get no response at all.

#### Timeouts and unbounded delays

A long timeout means a long wait until a node is declared dead. A short timeout detects faults faster, but carries a higher risk of incorrectly declaring a node dead (when it could be a slowdown).

Premature declaring a node is problematic, if the node is actually alive the action may end up being performed twice.

When a node is declared dead, its responsibilities need to be transferred to other nodes, which places additional load on other nodes and the network.

#### Network congestion and queueing

- Different nodes try to send packets simultaneously to the same destination, the network switch must queue them and feed them to the destination one by one. The switch will discard packets when filled up.
- If CPU cores are busy, the request is queued by the operative system, until applications are ready to handle it.
- In virtual environments, the operative system is often paused while another virtual machine uses a CPU core. The VM queues the incoming data.
- TCP performs _flow control_, in which a node limits its own rate of sending in order to avoid overloading a network link or the receiving node. This means additional queuing at the sender.

You can choose timeouts experimentally by measuring the distribution of network round-trip times over an extended period.

Systems can continually measure response times and their variability (_jitter_), and automatically adjust timeouts according to the observed response time distribution.

#### Synchronous vs ashynchronous networks

A telephone network estabilishes a _circuit_, we say is _synchronous_ even as the data passes through several routers as it does not suffer from queing. The maximum end-to-end latency of the network is fixed (_bounded delay_).

A circuit is a fixed amount of reserved bandwidth which nobody else can use while the circuit is established, whereas packets of a TCP connection opportunistically use whatever network bandwidth is available.

**Using circuits for bursty data transfers wastes network capacity and makes transfer unnecessary slow. By contrast, TCP dinamycally adapts the rate of data transfer to the available network capacity.**

We have to assume that network congestion, queueing, and unbounded delays will happen. Consequently, there's no "correct" value for timeouts, they need to be determined experimentally.