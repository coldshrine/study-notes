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
* **Organized around Business Capabilities.** Broad-stack implementation of software for that business area, including user-interface. Siloed funcional teams creating layered architectures (silos) vs cross-functional team and softwar organised vs capabilities (Conways law). Micro-services are cross-functioal. The necessarily more explicit separation makes it easier to keep the team boundaries clear.
* **Products not Projects.** A team should own a product over its full lifetime, you build it you run it. The product mentality, ties in with the linkage to business capabilities. Rather than looking at the software as a set of functionality to be completed.