# Amazon Managed Streaming for Apache Kafka (Amazon MSK)

Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed AWS service designed to simplify the process of building and running applications that leverage Apache Kafka for streaming data. Apache Kafka is a widely used open-source platform for constructing real-time data pipelines and streaming applications, capable of high-throughput, low-latency data processing. With Amazon MSK, users can utilize Kafka’s APIs to seamlessly integrate with data lakes, synchronize databases, and power machine learning and analytics applications—offering an alternative to AWS Kinesis for streaming data solutions.

Amazon MSK uses Amazon EC2 instances to host Kafka brokers in a managed cluster. Each broker is a server responsible for maintaining Kafka topics and partitions, storing published data, and allowing consumers to read from these partitions. By using Amazon MSK, customers get a managed Kafka cluster that automates deployment, scaling, and maintenance while enabling users to work with Kafka's native APIs.

## Key Features and Capabilities

### 1. High Availability and Durability

Amazon MSK is architected to ensure high availability and durability:

- **Multi-AZ Data Replication:** Data is automatically replicated across multiple availability zones (AZs) within a region, ensuring resilience to hardware failures and supporting continuous operations.
- **Scalability:** Amazon MSK supports both vertical and horizontal scaling, allowing for changes in cluster size without causing downtime, making it highly adaptable to varying data processing demands.

### 2. Kafka Ecosystem Compatibility

Amazon MSK provides full compatibility with the open-source Apache Kafka ecosystem. It enables control-plane operations (like creating, updating, and deleting clusters) and supports native Kafka data-plane operations (such as producing and consuming data). The use of open-source Kafka versions allows for seamless integration with existing Kafka tools, plugins, and applications without requiring changes to existing code.

### 3. Flexible Message Size Configuration

By default, Amazon MSK sets a maximum message size of 1 MB, consistent with common Kafka configurations. However, users can adjust this limit if their applications require larger messages, making it suitable for use cases involving large data sets per message.

## Access Control and Security

Amazon MSK offers a granular permissions model using Apache Kafka’s Access Control Lists (ACLs). This system specifies which applications can read from or write to particular topics, providing a secure and precise mechanism for access control. Access control settings follow this format:

- **Principal P is [Allowed/Denied] Operation O From Host H on any Resource R matching ResourcePattern RP**

By default, Amazon MSK sets `allow.everyone.if.no.acl.found` to `true`, meaning that if no ACLs are set on a resource, all principals have access to it. However, ACLs can be customized to restrict access, particularly useful in scenarios where security policies or microservice architectures demand strict isolation between services.

For example, in cases where a microservice begins receiving unintended data from other services, ACLs can be configured to restrict access to each Amazon MSK topic, preventing unauthorized data access and ensuring a secure data flow for each microservice.

## MSK Connect

Amazon MSK includes **MSK Connect**, an extension that simplifies moving data in and out of Kafka clusters. Built on Kafka Connect (v2.7.1), MSK Connect allows users to deploy managed connectors that integrate Kafka with databases, file systems, and search indexes. Popular use cases include:

- **Amazon S3 and OpenSearch Integration:** MSK Connect includes connectors for moving data to/from Amazon S3 and Amazon OpenSearch Service.
- **Third-Party and Custom Connectors:** Supports connectors from partners, such as Debezium, which can capture database change logs for Kafka processing.