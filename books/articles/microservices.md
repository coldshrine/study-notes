# [Microservices by Martin Fowler](https://www.martinfowler.com/articles/microservices.html)

Microservice architectural style is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API.

Built around business capabilities.

## Monolith
- A monolithic application built as a single unit. All your logic for handling a request runs in a single process.
- A change made to a small part of the application, requires the entire monolith to be rebuilt and deployed.
- It's often hard to keep a good modular structure.
- Scaling requires scaling of the entire application rather than parts.

## Microservice
As well as the fact that services are independently deployable and scalable, each service also provides a firm module boundary.

### Characteristics

* **Componentization via Services.** Component is a unit of software that is independently replaceable and upgradeable. Libraries in-memory function calls, while services are out-of-process communicate via RPC or web requests. services are independently deployable. More explicit components. Services map to runtime processes, but that is only a first approximation. Downsides: Remote calls are more expensive than in-process calls.