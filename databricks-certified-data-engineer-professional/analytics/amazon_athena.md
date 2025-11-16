# Amazon Athena

Amazon Athena is a serverless interactive query service that simplifies data analysis by allowing users to run SQL queries directly on data stored in Amazon Simple Storage Service (S3). Athena is highly scalable and cost-effective, enabling querying of large datasets without the need for complex infrastructure or resource management.

Athena allows you to execute ad-hoc SQL queries on your S3 data using standard SQL syntax. By simply pointing Athena at your S3 data and running queries, you can quickly analyze large datasets and obtain results in seconds. Athena automatically scales based on data volume and query complexity, and you only pay for the data scanned.

A key feature of Athena is its integration with **AWS Glue**, which facilitates seamless data integration and metadata management. When data is cataloged by AWS Glue crawlers, metadata such as table definitions, schema, and location are stored in the AWS Glue Data Catalog. This enables Athena to understand the data's format (e.g., CSV, Parquet, ORC) and query it efficiently.

## Supported Data Formats

One of the strengths of Amazon Athena is its support for a wide variety of data formats. This flexibility allows users to analyze data in many forms, whether it’s structured, semi-structured, or unstructured. Below are the most commonly used formats supported by Athena: