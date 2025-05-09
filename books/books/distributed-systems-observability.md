# [Distributed Systems Observability](https://www.goodreads.com/book/show/40182805-distributed-systems-observability)

- [The need of observability](#the-need-of-observability)
- [Monitoring and observability](#monitoring-and-observability)
- [Coding and testing for observability](#coding-and-testing-for-observability)
  - [Testing for failure](#testing-for-failure)
- [The three pillars of observability](#the-three-pillars-of-observability)
  - [Event logs](#event-logs)
  - [Metrics](#metrics)
  - [Tracing](#tracing)

Most failures not addressed by application layers will arise from the complex interactions between various applications.

Observability isn't purely an operational concern.

## The need of observability

**Observability is not just about logs, metrics and traces it's about bringing better visibility into systems.**

Observability is a property of the system. It does acknowledge the following
- No complex system is ever fully healthy.
- Distributed systems are unpredictable.
- It's impossible to predict the state of different parts of the system.
- Failure needs to be embraced.
- Easy debugging is fundamental.

Observability is a feature that needs to be enshrined into a system.
- Lends itself well to being tested in a realistic manner (a degree of testing in production).
- Failure modes can be surfaced during the time of testing.
- Deployments can happen incrementally so the rollback can be triggered if a key of metrics deviate from the baseline.
- Report enough data points, so the system can be understood.
