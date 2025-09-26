# [The Art of Destroying Software](https://vimeo.com/108441214)

One of the beautiful things about deleting code is that it allows you to change your mind.

[Waterfall paper](http://www-scf.usc.edu/~csci201/lectures/Lecture11/royce1970.pdf), one of the biggest ironies in our industry; it basically describes agile.

[Big ball of mud paper](https://joeyoder.com/PDFs/mud.pdf). It argues that the big ball of mud is inevitable. The way to tackle it is to create pockets of smaller ball of muds. You have to write code for the purpose of deleting it.


What if you developed software with the purpose of deleting it.
Apply the lessons of Erlang to the rest of the software. Microservices help on this vision, if we have many services, I can delete and rewrite them.

The definition of refactor is to either change my test or my code. Refactor changing the code and the test at the same time is called *refucktor*. The whole point of TDD is to make one of the sides stable so you can modify the other. It's a measurement, I'm predicting what will happen. Many refactoring tools change both sides at the same time. Your tools affect the code you are building.

There is no way of having a 12 months project to refactor the `ls` program. The Unix way of doing things is the same as microservices, the same as the Erlang way. When we have small programs, we are not afraid anymore of deleting and rewriting them from scratch. We should optimise for their delete ability. Imagine how wonderful to know you could delete code without side-effects.