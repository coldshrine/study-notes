# [Effective Java](https://www.goodreads.com/book/show/105099.Effective_Java_Programming_Language_Guide)

- [Creating and destroying objects](#creating-and-destroying-objects)
- [Methods common to all objects](#methods-common-to-all-objects)
- [Classes and interfaces](#classes-and-interfaces)
- [Generics](#generics)
- [Enums and annotations](#enums-and-annotations)
- [Lambdas and streams](#lambdas-and-streams)
- [Methods](#methods)
- [General programming](#general-programming)
- [Exceptions](#exceptions)
- [Concurrency](#concurrency)
- [Serialisation](#serialisation)

## Creating and destroying objects

### Consider static factory methods instead of constructors

```java
public static Boolean valueOf(boolean b) {
  return b ? Boolean.TRUE : Boolean.FALSE;
}
```

Advantages:
* They have names.
* They are not required to create a new object each time they are invoked.
* They can return an object of any subtype of their return type.
* The class of the returned object can vary from call to call as a function of the input parameters.
* The class of the returned object need to exist when the class containing the method is written.