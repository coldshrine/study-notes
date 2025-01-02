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