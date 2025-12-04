# Amazon Kinesis Data Streams

Amazon Kinesis Data Streams (KDS) is a powerful, scalable service for capturing, processing, and analyzing large volumes of streaming data in real-time. It is designed to handle gigabytes of data per second from sources such as clickstreams, social media feeds, and application logs, enabling applications to process data almost immediately for analytics or decision-making. This section delves into essential components, operational modes, producer and consumer integrations, and best practices for scaling Kinesis Data Streams.

## Architecture

- **Shards and Partitioning**
  - **Shards** are the fundamental unit of capacity in Kinesis Data Streams, each capable of handling 1 MB/second of data input and 2 MB/second of data output. A stream consists of one or more shards, and the total throughput capacity of a stream is determined by the number of shards it contains.
  - Data is partitioned across shards using a **partition key** assigned when writing records to the stream. Records with the same partition key are assigned to the same shard, preserving the order of records within each shard.

- **Service Modes**
  - **Provisioned Mode**: Ideal for predictable workloads, allowing users to define the number of shards upfront. This mode supports auto-scaling within predefined limits and requires regular monitoring and management to ensure optimal performance without over-provisioning or throttling.
  - **On-Demand Mode**: Best for unpredictable workloads, dynamically adjusting capacity based on incoming data volume, freeing users from managing shard counts. This mode is convenient for applications with variable or unknown data traffic patterns.

## Producers

When integrating with Amazon Kinesis Data Streams, AWS provides several tools and libraries, including the AWS SDK, the Kinesis Producer Library (KPL), and the Kinesis Agent.

- **AWS Software Development Kit (SDK)**:
  The AWS SDK is a set of libraries and tools available for various programming languages and platforms, allowing developers to interact with AWS services programmatically. For Amazon Kinesis Data Streams, the AWS SDK enables direct creation, configuration, and management of streams, as well as sending and receiving data records from applications.

  To insert data into a stream, you typically use the `PutRecord` or `PutRecords` API operations. **PutRecords** supports batching, which improves throughput and reduces data ingestion costs by allowing up to 500 records or 5MB of data (whichever comes first) to be sent in a single API call.

- **Kinesis Producer Library (KPL)**:
  The Kinesis Producer Library (KPL) is a high-level, easy-to-use library designed specifically for efficient batch insertion of large volumes of data records into a Kinesis Data Stream. Written in Java (with a native C++ core for performance), KPL is best suited for applications that require high-throughput data ingestion, where manually managing batching, buffering, and retry logic would be inefficient.

  The KPL simplifies the data-sending process to Kinesis Data Streams by offering built-in capabilities for efficient data batching, asynchronous operations for enhanced throughput, and automatic retry mechanisms to handle transmission failures. This makes it ideal for streaming clickstream data and server logs from Java applications, ensuring reliable, efficient data collection with minimal development effort.

  - **Synchronous and Asynchronous Publishing**:
    In KPL, data can be published either synchronously or asynchronously, with asynchronous publishing being the default and recommended mode. The **RecordMaxBufferedTime** parameter controls how long a record will be buffered (in milliseconds) before transmission to the Kinesis Data Stream. This buffering allows KPL to aggregate records into larger requests, optimizing network and throughput performance.

    - For applications sensitive to latency, a lower buffered time may be preferred to ensure near real-time data processing.
    - For applications prioritizing maximum throughput, increasing the buffered time can allow more records to aggregate per request, reducing API calls and potentially decreasing costs.

- **Kinesis Agent**:
The Kinesis Agent is a pre-built, standalone Java application for Linux-based systems, providing a simple way to collect and send data to Kinesis Data Streams (and Kinesis Firehose) from files. The agent monitors files for changes, parses log entries, and automatically sends them to Kinesis Data Streams, handling tasks like file rotation, checkpointing, and retries. This setup simplifies the process of sending log data and metrics to Kinesis without requiring custom logging code.

## Consumers

Each data record in Kinesis Data Streams can be up to 1 MB in size. Each shard supports a read throughput of up to 2 MB per second, which is shared among all consumers accessing that shard. When multiple consumers access the same shard concurrently, they share this bandwidth, impacting data retrieval speed.

When retrieving data using the `GetRecords` API, a consumer can retrieve up to 10 MB of data in a single request from a shard. If a shard is polled less frequently, data accumulates in the shard, allowing larger batch retrievals (up to the 10 MB limit) per call. The **GetRecords call limit** is 5 calls per second per shard. Exceeding this rate triggers throttling and returns a `ProvisionedThroughputExceededException`. To avoid this, consider implementing a **backoff strategy**, where consumers pause and retry requests, especially during high-throughput periods.
