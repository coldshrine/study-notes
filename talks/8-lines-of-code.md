# [8 Lines of Code](https://www.infoq.com/presentations/8-lines-code-refactoring)

Simplicity is good because
> I am stupid to work otherwise. Fancy code befuddles me.

The problem with magic: Things happen that I don't understand. Sometimes magic doesn't work, so I don't know how it works.

Annotations is an example of magic. Here is where simplicity goes out of window. This is not simple.

This _simple_ thing is actually increasing the complexity massively.

How do you explain all these magic to a person without much experience? How do you explain a _Dynamic Proxy_? With Dynamic Proxy you need to do _special things_ to make it work, like adding `virtual` to every method or avoiding returning `this`. People grow with these things and will start spreading this kind of behaviour without really understanding why they do it. This is actually cargo cult.

Some teams use frameworks and tools that have so much magic that they start looking for people that know about those things because teaching all that magic takes a lot of time.

With annotations those simple lines of code become way more complex than it should be.

Love platforms, hate frameworks. Frameworks have a tendency to introduce magic in your system.

> If you find you need an extension to your IDE to understand what's going on. It's probably not simple.

What's the core problem behind a problem (like wanting a _Dynamic Proxy_). **Can I change my problem so I no longer need those things?**

We can avoid the proxy entirely if we unify the interface for all of our methods (refactor parameters to objects, Commands), changing our problem to simplify the solution. Now that we have a common interface, we can do basic composition instead of proxying stuff at runtime.

From 

```c#
public void Deactivate(Guid id, string reason) {
    var item = repository.GetById(id);
    item.Deactivate();
}

public void Reactivate(Guid id, DateTime effective, string reason) {
    var item = repository.GetById(c.id);
    item.Reactivate();
}
```