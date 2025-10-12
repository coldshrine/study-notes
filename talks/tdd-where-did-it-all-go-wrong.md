# [TDD, where did it all go wrong](https://vimeo.com/68375232)

### Frustrations with TDD

Didn't refactoring promise change without breaking tests?

If we change the implementation details, non of our tests should break.

More test code than implementation code.

Programming Anarchy and Lean Software Development drop tests first.

Duct tape programmer, delivers functionality faster, quickly abandoning tests as "slowing them down'

Difficult to understand test intent, why tests fail.

ATDD suites:
- much of their life in red
- Customers don't engange with the suite
- slow to run and increasing cost.
    - devs ignoring red results
    - we need tools to fix them
    - devs don't want to write them

## Where did it all go wrong?

- Writing tests against operations instead of writing them against behaviour (BDD).
- Coupling our tests to implementation details.

### TDD rebooted

#### The Zen of TDD

* Avoid testing implementation details, test behaviours. Test intent has to be explicit about this, high-level details.
  - Adding a new class is not the trigger for writing tests. The trigger is implementing a requirement.
  - Test outside-in, writing tests to cover then the use cases, scenarios. You have to test the domain, if you test through forms (MVC), the moment you change your delivery mechanism you break all the tests. You should test the surface. Don't test the internals, you'd be coupling your test to internal details.
  - Only writing test to cover the implementation details as a way to understand the refactoring of the simple implementation we start with.

BDD (Dan North), we should test behaviours, not tests. People misunderstand what TDD is all about.

Kent explicitly talks about behaviours, with examples. Testing the perimeter surface, not the implementation details.

#### What is a unit test

* For Kent Beck, it is a test that _runs in isolation_ from other tests.
  - Nothing more, nothing less.
  - It is NOT to be confused with the classical unit test definition of targeting a module.
  - We don't touch file system, database, because these _shared fixture_ elements prevent us running in isolation from other tests (side-effects.)
* Explicitly writing tests that target a method on a clas, is not a TDD unit tests