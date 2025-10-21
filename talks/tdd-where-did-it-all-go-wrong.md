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
  - TDD unit tests focus on a story. Use-case, scenario...
* Focusing on methods creates tests that are hard to maintain. We don't capture the behaviour we want to preserve.

A lot of issues with TDD is people misunderstanding _isolation_ as _class isolation_, replacing collaborators with test doubles.

### Red-green-refactor

1. **Red** Write a little test that doesn't work, and perhaps doesn't even compile at first.
2. **Green** Make the test work quickly, commiting whatever sins necessary in the process.
3. **Refactor** Eliminate all of the duplication, created in merely getting the test to work.

#### The simplest thing (green)

* Make it run. Quickly getting that bar to go green domintates everything else.
* The shift in aesthetics is hard for some experienced software engineers.
  - The only know how to follow the rules of good engineering.
  - Quick green excuses all sins.
  - This is not about accepting sin, its about being sinful.
  - Write sinful code!

This is difficult fir experienced engineers, we tend to think on how to engineer the problem, not how to solve it fast.

> We can commit any number of sins to get there, because speed trumps design, just for a brief moment. - Kent Beck

> Good design at good times. Make it run, make it right. - Kent Beck

#### Clean code now (refactor)

* The refactoring step is when we produce clean code.
  - It's when you apply patterns
  - It's when you remove duplication
  - It's when you sanitise the code smells
* **You do not write new unit tests here**
  - You are not introducing public classes
  - It is likely if you feel you need, you need collaborators to fulfill a role

If you add more tests at this point, you'll be coupling your tests to implementation details, making your tests fragile. Your API is your contract, your tests should test the API, not the implementation details. Coupling is the first problem in software.

* We need to eliminate dependency between our tests and our code
  - Tests should not depend on details, because then changing implementation breaks tests. Tests should depend on contracts or public interfaces.
  - This allows us to refactor implementations without changing tests.
  - Don't bake implementation details into tests
* Test behaviours not implementations

Counter argument: The setup of this may be too complex as we testing super high-level.

* Don't test internals
* Don't make everything public in order to test it
* Preserve implementation hiding by keeping a thin public API
* Refactor implementation details out, so that they do not need their own tests
* Continue to refactor implementation details over time, as you want
* Have expressive tests that you can read in the future

### Refactoring to patterns

Patterns emerge in refactoring step. You don't think on patterns first an implementations later.

References: TDD by Example (Kent Beck), Refactoring to Patterns (Joshua)

### Port and adapters

Testing ice-cream cone anti-pattern.

Testing piramid.

UI:
We are not testing the domain logic, we are testing the widgets.

Integration:
Tests cannot run in isolation if we have shared state fixtures like databases, etc. Here we do test that kind of stuff.

Unit:
To test the business logic. The tests are more valuable and less costly are unit tests.

#### Hexagonal architecture

We unit test the port, the use case. We test the behaviour, the contract to the world.

We don't test the implementation details (peg: the database).

Integraiton tests: Don't test things you don't own. Just test that you are using them correctly.

System tests: Tests that verify that everything works.

### Gears

We can be in the motorway driving in the fifth gear, that's may be the operational mode while developing, but sometimes we need to start changing down the gears.

Fifth gear is "obvious implementation", we can go straight to green. You may write unnecessary code.


Fourth gear is "we are writing code nicely", we start to think we don't know how to get to the solution so write some tests, some implementation details (drilling tests) to see how it may look. You need to think about behaviour. Maybe you want to remove those implementation tests once you finish with the behaviour.

You should test the ports, not implementation details.

You should be feel free to remove tests if necessary. The tests we need to keep are the tests that express the behaviour, the API of your system.

### Acceptance test-driven development

Customers should be available to write scenarios for tests. Getting the customer chain together for this is problematic.

Unit tests evolve into "programmer tests". ATDD is more about high-level communication.

**If customers do not participate, it does not make any sense**. Expensive to write, expensive to run (Fitness, Cucumber).

Maybe we should involve customers while writting unit tests and focus on unit tests. The problem is programmers making programmer driven tests instead of behaviour driven tests, so let's solve that.

### Behaviour-driven development

BDD starts with a similiar inisght, that we misunderstood TDD.

* It creates tools like RSpec and Jbehave
* It realises that specifying scenarios is the key to driving test-driven development
* It evolves into a methodology for facilitating the transmission of requirements from customer to developer through scenarios  that can be automated.

### Mocks

* Classic example is database
  - Long time to start
  - Difficult to keep "clean"
  - Tie tests to physical location on network
  - Write tests against something that acts like a DB

* Mocks can improve readability by making contents of read rows explicit (evident data)
* Mocks hinder the use of singletons