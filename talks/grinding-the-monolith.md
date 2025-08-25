# [Grinding the monolith](https://www.youtube.com/watch?v=xxW_c_8AHiE)

## Monolith

Pros:
* Easier to deploy
* Easier to place and find stuff in

## Microservices

Cons:
* Operational complexity
* Partial failure

Pros:
* Independence of development
* Independence of scalability
* Building in smaller and simpler pieces

### We have heard the story before

Java Beans, COMM, COBRA
* Independent components, you can just buy and connectcomponents
* Decoupled and simple pieces

We can have software that works like Lego. But this hypothesis does not work in reality as there are many more dimensions (connections between components). Components may have hundreds or thousands of collaborators, we would need to have to have nth dimensional Lego bricks!

Maybe a better model would be Mycelium, a fungus where fractal roots communicate to each other in a way more complex way.
