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
