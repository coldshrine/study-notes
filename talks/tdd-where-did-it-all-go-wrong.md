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