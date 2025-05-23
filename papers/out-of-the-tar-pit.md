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


#### Kinds of state

By "state" what is really meant is _mutable state_.

Language which do not support or discourage mutable state it is common to achieve somewhat similar effects by means of passing extra parameters to procedures (functions).

There is no reason why the functional style of programming cannot be adopted in stateful languages. Whatever the language being used, there are large benefits to be had from avoiding, implicit, mutable state.

#### State and modularity

State permits a particular kind of modularity, within a stateful framework it is possible to add state to any component without adjusting the components which invoke it. Within a functional framework the same effect can only be achieved by adjusting every single component that invokes it to carry the additional information around.

In a functional approach you are forced to make changes to every part of the program that could be affected, in the stateful you are not.

In a functional program _you can always tell exactly what will control the outcome of a procedure_ simply by looking at the arguments supplied where it is invoked. In a stateful program you can never tell what will control the outcome, and _potentially_ have a look at every single piece of code in the _entire system_ to determine this information.

The trade-off is between _complexity_ and _simplicity_.

The main weakness of functional programming is that problem arise when the system to be built must maintain state of some kind.

#### Summary

Functional programming goes along way towards voiding the problems of state-derived complexity.

### Logic programming

Together with functional programming _declarative_ style of programming places emphasis on _what_ needs to be done rather than exactly _how_ to do it.

#### State

Logic programming makes no use of mutable state, and for this reason profits from the same advantages as functional programming.

#### Control

Operational commitment ot _process_ the program is the same order as it read textually (depth first). Particular ways of writing down can lead to non-termination, which leads inevitably to the standard difficulty for informal reasoning caused by control flow.

#### Summary

Despite the limitations it offers the ability to escape from the complexity caused by control.

## Accidents and essence

Brooks defined difficulties of "essence" as those inherent in the nature of software and classified the rest as "accidents".

* **Essential complexity** is inherent in the _users problem_.
* **Accidental complexity** is complexity with which the development team would not have to deal in the ideal world.

Any real development _will_ need to contend with _some_ accidental complexity.

Complexity itself is not inherent (or essential) property of software. Much complexity that we do see in existing software is not essential (to the problem). The goal of software engineering must be both to eliminate as much of accidental complexity as possible and to assist with the essential complexity part of it.

## Recommended general approach

Complexity could not be _possibly_ avoided even in the ideal world.

### Ideal world

In the ideal world we would not be concerned about performance. Even in the ideal world, we would need to start with a set of _informal requirements_ from the prospective users. We would ultimately need something to _happen_, and we are going to need some _formality_.We are going to need to derive formal requirements from the informal ones.

The next step is simply to _execute_ these formal requirements directly.

Effectively what we have just described is in fact the very _essence_ of _declarative programming_, specify _what_ you require, not _how_ it must be achieved.

#### State in the ideal world

The aim for state is to get rid of it hoping that most will be _accidental state_.

All data will be provided (_input_) or _derived_.

**Input data** Included in the informal requirements and as such is deemed _essential_.
* If the system may be required to refer to the data in the future then it is _essential state_.
* If there is no such possibility and the data is designed to have some side-effect, the data need not to be maintained at all.

**Essential derived data (immutable)** Data can always be re-derived, we do _not_ need to store it in the ideal world (accidental state).

**Essential derived data (mutable)** This can be excluded and hence corresponds to _accidental state_.

**Accidental derived data** State that is _derived_ but _not_ in the users' requirements is _accidental state_.

As a summary, mutable state can be avoided, even in the ideal world we _are_ going to have _some_ essential state.

_Accidental state_ can be excluded from the ideal world (by re-deriving the data as required). The vast majority of state isn't needed. One effect of this is that _all_ the state int he system is _visible_ to the user.

#### Control in the ideal world

Control generally can be completely omitted, so is considered _accidental_.

We should not have to worry about the control flow. _Results_ should be independent of the actual control mechanism. This is what logic programming taught us.

#### Summary

It is clear that a lot of complexity is _accidental_.

### Theoretical and practical limitations

#### Formal specification languages

_Executable specifications_ would be ideal. Declarative programming paradigm proposed approaches have been proposed as approaches for executable specifications.

In the ideal world, specifications derived _directly_ from the users' informal requirement is critical.

Formal specification has been categorised in two main camps:
* **Property-based** approaches focus on _what_ is required rather than _how_ the requirements should be achieved (_algebraic_ approaches such as Larch and OBJ).
* **Model-based (or state-based)** approaches construct a model and specify how that model must behave. These approaches specify how a stateful, imperative language solution must behave to satisfy the requirements.

There have been arguments against the concept of executable specifications. The main objection is that requiring a specification language to be executable can directly restrict its expresiveness.

In response, a requirement for this kind of expressivity does not seem to be common in many problem domains. Secondly where such specifications _do_ occur they should be maintained in their natural form but supplemented with a _separate_ operational component.

_Property-based_ approaches have the greatest similarity to _executable specifications_ in the ideal world.

A second problem is that even when specifications _are_ directly executable, this can be impractical for efficiency reasons. It may require some accidental components.

##### Ease of expression

Immutable, derived data would correspond to _accidental state_ and could be omitted (you could derive data on-demand).

There are occasionally situations where (using on-demand derivation) does not give rise to the most natural modelling of the problem.

An example of this is the derived data representing the position state of an opponent in an interactive game. It is at all times _derivable_ by a function of both all prior movements and the initial starting positions, but this is not the way it is most naturally expressed.

##### Required accidental complexity

* **Performance** making use of accidental state and control can be required for efficiency.
* **Ease of expression** making use of accidental state can be the most natural way to express logic in some cases.

#### Recommendations

_Avoid_ state and control where they are not absolutely and truly essential. When needed, such complexity must be _separated_ out from the rest of the system.

##### Required accidental complexity

* **Performance** _avoid_ explicit management of the accidental state, restrict ourselves to simply _declaring_ what accidental state should be used, and leave it to a completely separate infrastructure to maintain. We can effectively forget that the _accidental state_ even exists.
* **Ease of expression** this problem arises when derived (_accidental_) state offers the most natural way to express part of the logic of the system.