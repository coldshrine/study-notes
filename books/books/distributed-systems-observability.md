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


## Monitoring and observability

**Observability is a superset of monitoring.** It provides highly granular insights into the implicit failure modes of the system. An observable system provides contexts about its inner workings.

**Monitoring reports the overall health of systems and derives alerts**

> ### Blackbox and whitebox monitoring
> _Blackbox monitoring_ refers to observing a system from the outside. Useful for identify the _symptoms_ of a problem like "error rate is up".
> _Whitebox monitoring_ refers to techniques of reporting data form inside a system.

Monitoring data should always provide a bird's-eye view of the overall health of a distributed system by recording and exposing high-level metrics over time across all components of the system.

**All alerts need to be _actionable_.**

A good set of metrics are the USE metrics and the RED metrics.
* USE methodology is for analysing system performance like utilisation, saturation, errors of resources, free memory, CPU or device errors.
* RED methodology is about application level metrics like request rate, error rate, and duration of the requests.

Debugging is often an iterative process and involves
* Start with a high-level metric
* Drill down observations
* Make the right deductions
* Testing the theory

Observability doesn't obviate the need for careful thought. The process of knowing what information to examine (observations), requires a good understanding of the system and domain, as well as a good sense of intuition.

## Coding and testing for observability

The idea of experimenting with live traffic is either seen as the preserve of operations engineers or is something that's met with alarm. Some amount of regression testing to post-production monitoring requires coding and testing for failure.

Acknowledging that systems will fail, being able to debug such failures is of paramount importance, and embedding debuggability into the system from the ground up.

Understanding service dependencies and abstractions better, allows you to improve reliability massively just by changing a single line of configuration.