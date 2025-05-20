# [Out of the Tar Pit](http://curtclifton.net/papers/MoseleyMarks06a.pdf)

- [Complexity](#complexity)
  - [Simplicity is hard](#simplicity-is-hard)
- [Approaches to understanding](#approaches-to-understanding)
- [Causes of complexity](#causes-of-complexity)
  - [Complexity caused by state](#complexity-caused-by-state)
  - [Complexity caused by control](#complexity-caused-by-control)
  - [Complexity caused by code volume](#complexity-caused-by-code-volume)
  - [Other causes of complexity](#other-causes-of-complexity)
- [Classical approaches to managing complexity](#classical-approaches-to-managing-complexity)
  - [Object-orientation](#object-orientation)
  - [Functional programming](#functional-programming)
  - [Logic programming](#logic-programming)
- [Accidents and essence](#accidents-and-essence)
- [Recommended general approach](#recommended-general-approach)
  - [Ideal world](#ideal-world)
  - [Theoretical and practical limitations](#theoretical-and-practical-limitations)
- [The relational model](#the-relational-model)
  - [Structure](#structure)
  - [Manipulation](#manipulation)
  - [Integrity](#integrity)
  - [Data independence](#data-independence)
  - [Extensions](#extensions)
- [Functional relational programming](#functional-relational-programming)
  - [Architecture](#architecture)
  - [Benefits of this approach](#benefits-of-this-approach)
  - [Types](#types)

The biggest problem in the development and maintenance of large-scale software systems is complexity. The major contributor to this complexity is the handling of _state_. Other closely related are _code volume_, and explicit _flow of control_.

Object-oriented programming tightly couples state with related behaviour, and functional programming eschews state and side-effects all together.

## Complexity

In the ["No Silver Bullet" paper](http://worrydream.com/refs/Brooks-NoSilverBullet.pdf) Brooks identified four properties of software which make software hard: Complexity, Conformity, Changeability and Invisibility.

Complexity is _the_ root of the vast majority of problems with software today, like the ones about unreliability, late delivery or lack of security.


### Simplicity is hard

The type of complexity we are discussing in this paper is the one which makes large systems _hard to understand_. The one that causes huge resources in _creating and maintaining_ such systems. This type complexity has nothing to do with the complexity related with a _machine executing a program_.

## Approaches to understanding

* **Testing**: Attempting to understand the system from the outside with observations about how it behaves. Performed either by a human or by a machine.
* **Informal reasoning**: Understand the system by examining it from the inside.

Reasoning is the most important by far, mainly because there are limits to what can be achieved by testing, and because informal reasoning is _always_ used.

The key problem with testing is that tells you _nothing at all_ when it is given a different set of inputs.

> Testing can be used very effectively to show the presence of bugs but never to show their absence – Dijkstra

_Informal reasoning_ is limited in scope, imprecise and hence prone to error, as well as _formal reasoning, which is dependant upon the accuracy of specification. It may often be prudent to employ testing _and_ reasoning together.

Is because of the limitations of these approaches that _simplicity_ is vital.

## Causes of complexity

### Complexity caused by state

#### Impact of state in testing

State affects all types of testing. The common approach to testing a stateful system is to start up such that it is in some kind of "clean" or "initial" state, perform the desired tests upon the assumption that the system would perform in the same way every time the test is run. Sweeping the problem of state under the carpet.

It's not _always_ possible to "get away with it", some sequence of events can cause the system to "get into a bad _state_", then thing can go wrong.

Even though the number of _inputs_ may be very large, the number of possible _states_ the system can be is often even larger.

#### Impact of state in informal reasoning

The mental processes which are used to do this informal reasoning often revolve around a case-by-case mental simulation of behaviour. As the number of states grows, the effectiveness of this mental approach buckles quickly.

Another issue for informal reasoning is _contamination_.

Consider a system made up of procedures, some of which are stateful and others which aren't. If the procedure makes use of any procedure which _is_ stateful, _even indirectly_, the procedure becomes _contaminated_.

The more we can do to _limit_ and _manage_ state, the better.

### Complexity caused by control

Control is about _order_ in which things happen. We do not want to have to concerned about this.

When control is an implicit part of the language, every single piece of program must be understood in that context. When a programmer is forced to specify the control, he or she is being forced to specify an aspect of _how_ the system should work rather than simply _what_ is desired. They are being forced to _over-specify_ the problem.

A control-related problem is concurrency, which affects _testing_ as well.

Concurrency is normally specified _explicitly_ in most languages. The most common model is "shared-state concurrency" in which explicit synchronisation is provided. The difficulty for informal reasoning comes from adding further the _number of scenarios_ that must mentally be considered as the program is read.

Running a test in the presence of concurrency tells you _nothing at all_ about what will happen the next time you run that very same test.

### Complexity caused by code volume

This is a secondary effect. Much code is simply concerned with managing _state_ or specifying _control_. It is the easiest form of complexity to _measure_, and it interacts badly with the other causes of complexity.

Complexity definitively _does_ exhibit nonlinear increase with size (of the code) so it's vital to reduce the amount of code to an absolute minimum.

### Other causes of complexity

There are other causes like: duplicated code, dead code, unnecessary abstraction, missed abstraction, poor modularity, poor documentation...

All these come down to the following principles

* **Complexity breeds complexity**. Complexity introduced as a _result of_ not being able to clearly understand a system, like _Duplication_. This is particularly common in the presence of time pressures.
* **Simplicity is hard**. Simplicity can only be attained if it is recognised, sought and priced.
* **Power corrupts**. In the absence of language-enforced guarantees mistakes (and abuses) _will_ happen. We need to be very wary of any language that even _permits_ state, regardless of how much it discourages its use, the more _powerful_ a language, the harder it is to _understand_ systems constructed in it.

## Classical approaches to managing complexity

### Object-orientation

Imperative approach to programming.

#### State

An object is seen as consisting of some state together with a set of procedures for accessing and manipulating that state.

_Encapsulation_ allows the enforcement of integrity constraints over an object's state by regulating access to that state through access procedures ("methods").

One problem is that if several of the access procedures access or manipulate the same bit of state, then there may be several places where a given constraint must be enforced. Another major problem is that encapsulation-based integrity constraint enforcement is strongly biased toward single-object constraints, and it's awkward to enforce more complicated constraints involving multiple objects.

##### Identity and state

Each object is seen as being uniquely identifiable entity regardless of its attributes. This is known as _intentional_ identity (in contrast with _extensional_ identity in which things are considered the same if their attributes are the same).

Object identity _does_ make sense when objects are used to provide a (mutable) stateful abstraction.

However, where mutability is _not_ required, the OOP approach is the creation of "Value Objects". It is common to start using custom access procedures to determine whether two objects are equivalent. There is no guarantee that such domain-specific equivalence concepts conform to the standard idea of an equivalence relation (peg: no guarantee of transitivity).

The concept of _object identity_ adds complexity to the task of reasoning about systems developed in OOP.


##### State in OOP

All forms of OOP rely on state, and general behaviour is affected by this state. OOP does not provide an adequate foundation for avoiding complexity.

#### Control

Standard sequentual control flow and explicit classical "shared-state concurrency" cause standard complexity errors. A slight variation of "message-passing" Actor model canis not lead to easier informal reasoning but is not widespread.

#### Summary

Conventional imperative and object-oriented programs suffer greatly from both state-derived and control-derived complexity.

### Functional programming

It has its roots in the completely stateless lambda calculus of Church.

#### State

Functional programming languages are often classified as "pure" which shun state and side-effects completely, and "impure", whilst advocating the avoidance of state and side-effects in general, do permit their use.

By avoiding state (and side-effects) the entire system gains the property of _referential transparency_, a function will _always_ return exactly the same result. Because of this, testing does become far more effective.

By avoiding state, informal reasoning becomes much more effective.

#### Control

Functional languages do derive one slight benefit when it comes to control because they encourage a more abstract use of control functionals (such as `fold` / `map`) rather than explicit looping. There are also concurrent versions.
