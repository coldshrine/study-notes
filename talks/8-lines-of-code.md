# [8 Lines of Code](https://www.infoq.com/presentations/8-lines-code-refactoring)

Simplicity is good because
> I am stupid to work otherwise. Fancy code befuddles me.

The problem with magic: Things happen that I don't understand. Sometimes magic doesn't work, so I don't know how it works.

Annotations is an example of magic. Here is where simplicity goes out of window. This is not simple.

This _simple_ thing is actually increasing the complexity massively.

How do you explain all these magic to a person without much experience? How do you explain a _Dynamic Proxy_? With Dynamic Proxy you need to do _special things_ to make it work, like adding `virtual` to every method or avoiding returning `this`. People grow with these things and will start spreading this kind of behaviour without really understanding why they do it. This is actually cargo cult.