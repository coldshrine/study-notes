# [The Do's and Don'ts of Error Handling](https://www.youtube.com/watch?v=TTM_b7EJg5E)

> A system is fault-tolerant if it continues working even if something is wrong

> Work like this is never finished, it's always in-progress

* Hardware can fail (relatively uncommon)
* Software can fail (common)

## Overview

* Fault-tolerance cannot be achieved using a single computer – it may fail
* We have to use several computers
    * Concurrency
    * Parallel programming
    * Distributed programming
    * Physics – time to propagate messages
    * Engineering
    * **Message passing is inevitable** – the basis of Object-Oriented Programming
* Programming languages should make this ~easy~ doable

We are never going to eliminate failure, systems will be inconsistent. We have to deal with it.

* How individual computers work is the smaller problem. How the system works as a whole is important.
* How the computers are interconnected and the protocols used between computers is the significant problem.
* We want the same way to program large and small scale systems.

Why do we have to program differently for local programs to communicate (memory) versus distributed systems (message bus)?

In Object-Oriented Programming, Alan Kay said that the big idea behind Object-Oriented Programming was "messaging"

## Erlang

* Derived from Smalltalk and Prolog (influenced by ideas from CSP)
* Unifies ideas on concurrent and functional programming
* Follows laws of physics (asynchronous messaging)
* Designed for programming fault-tolerant systems
