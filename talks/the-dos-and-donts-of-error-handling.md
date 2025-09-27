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