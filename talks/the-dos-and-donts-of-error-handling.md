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

Invented Erlang to solve a problem, not the language to find a problem to be solved with it.

Building fault-tolerant software boils down to detecting errors and doing something when errors are detected.

> We can't fix our own errors in the same way if I'm having a heart attack, I'll need someone to help me out

## Types of errors

* Errors that can be detected at compile time
* Errors that can be detected at run-time
* Errors that can be inferred
* Reproducible errors
* Non-reproducible errors

## Philosophy

* Find methods to prove Software correct at compile-time
* Assume software is incorrect and will fail at run-time then do something about it at run-time

## Evidence for software failure is all around us

Proving the self-consistency of small programs will not help. Testing a system will tell us that is self-consistent, not that it is correct.

## Conclusion

* Some small things can be proven to be self-consistent.
* Large assemblies of small things are possible to prove correct.

---

1980 - Erlang model of computation rejected. Shared memory systems ruled the world.
1985 - Ericsson started working on "a replacement of PLEX", started thinking about errors. "errors must be corrected somewhere else", "shared memory is evil", "pure message passing"
1986 - Erlang, unification of OO with FP
1998 - Several products in Erlang, Erlang gets banned and moved to Open Source
2004 - Erlang model of computation widely adopted in many different languages.

## Types of system

* Highly reliable (nuclear power plant control, air-traffic), satellite (very expensive if they fail)
* Reliable (driverless cars) (moderately expensive if they fail. Kills people if they fail)
* Reliable (annoys people if they fail), banks, telephone
* Dodgy (cross if they fail), Internet, HBO, Netflix
* Crap (very cross if they fail), free apps

Different technologies are used to build and validate the systems.

How can we make software that works reasonably well even if there are errors in the software? "Making reliable distributed systems in the presence of software errors" book by Joe Armstrong