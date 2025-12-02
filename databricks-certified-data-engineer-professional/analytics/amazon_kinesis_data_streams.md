# Amazon Kinesis Data Streams

Amazon Kinesis Data Streams (KDS) is a powerful, scalable service for capturing, processing, and analyzing large volumes of streaming data in real-time. It is designed to handle gigabytes of data per second from sources such as clickstreams, social media feeds, and application logs, enabling applications to process data almost immediately for analytics or decision-making. This section delves into essential components, operational modes, producer and consumer integrations, and best practices for scaling Kinesis Data Streams.

## Architecture

- **Shards and Partitioning**
  - **Shards** are the fundamental unit of capacity in Kinesis Data Streams, each capable of handling 1 MB/second of data input and 2 MB/second of data output. A stream consists of one or more shards, and the total throughput capacity of a stream is determined by the number of shards it contains.
  - Data is partitioned across shards using a **partition key** assigned when writing records to the stream. Records with the same partition key are assigned to the same shard, preserving the order of records within each shard.

- **Service Modes**
  - **Provisioned Mode**: Ideal for predictable workloads, allowing users to define the number of shards upfront. This mode supports auto-scaling within predefined limits and requires regular monitoring and management to ensure optimal performance without over-provisioning or throttling.
  - **On-Demand Mode**: Best for unpredictable workloads, dynamically adjusting capacity based on incoming data volume, freeing users from managing shard counts. This mode is convenient for applications with variable or unknown data traffic patterns.