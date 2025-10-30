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

To

```c#
interface Handles<T> where T:Command
{
    void Handle(T command);
}
```
```c#
public static void Handle(DeactivatedCommand c) {
    var item = repository.GetById(c.id);
    item.Deactivate();
}

public static void Handle(ReactivateCommand c) {
    var item = repository.GetById(c.id);
    item.Reactivate();
}
```

Now that we have a common interface, would have Loggers, Transactions, etc. in the same way we had annotations.

```c#
class LoggingHandler<T> : Handles<T> where T:Command {
    private readonly Handles<T> next;

    public void LoggingHandler(Handles<T> next) {
        this.next = next;
    }

    public void Handle(T command) {
        myLoggingFramework.Log(command);
        next.Handle(command);
    }
}
```

The less magic I have, the faster I get onboard.

IoC container. Before having an injection container, we used to pass dependencies as parameters to constructors. Now we have all this boilerplate for injecting and passing parameters everywhere.

You can pass dependencies to handlers so we avoid having constructors.

```c#
public static void Deactivate(ItemRepository repository, DeactivatedCommand c) {
    var item = repository.GetById(c.id);
    item.Deactivate();
}
```

Now the problem we have is that we lost the common interface!

How can we do the equivalent of dependency injection inside a functional dependency

```c#
public static int Add(int a, int b) {
    return a + b;
}
```

We can close one of the parameters with a lambda (partial application).

```c#
var add5 => c => Add(5, x);
```

Now we can recover our common interface for our commands

```c#
public static void Deactivate(ItemRepository repository, DeactivatedCommand c) {
    var item = repository.GetById(c.id);
    item.Deactivate();
}
```

```c#
var nodepends => x => Deactivate(new ItemRepository(), x);
```

IoC containers solve a problem that maybe you don't have. If you had a UI program with lots of complex nested dependencies then maybe is the right tool. But for most cases IoC containers are too much.

```c#
void Bootstrap() {
    handlers.Add(x => Deactivate(new ItemRepository(), x));
    handlers.Add(x => Reactivate(new ItemRepository(), x));
    handlers.Add(x => CheckIn(new ItemRepository(), new BarService(), x));
}
```


How many use cases do you have? 15 lines of code could be completely fine. A junior person would totally understand.

Feel the pain of passing dependencies and setting up complex structures. A problem with IoC containers is that they make it very easy to do things that you shouldn't be doing.