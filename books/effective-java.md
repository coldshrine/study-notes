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

Disadvantages:
* Classes that provide only static factory methods without public or protected constructors cannot be subclassed. This is preferable when using composition instead of inheritance.
* They are hard for programmers to find. Some conventions
  - `from`, as type-conversion method `Date d = Date.from(instant)`
  - `of`, an aggregation method `Set<Rank> faceCards = EnumSet.of(JACK, QUEEN, KING)`
  - `valueOf`, more verbose alternative than `from` and `of`, `BigInteger prime = BigInteger.valueOf(Integer.MAX_VALUE)`
  - `instance` or `getInstance`, returns and instance that cannot be said to have the same values, `StackWalker luke = StackWalker.getInstance(options)`
  - `create` or `newInstance` the method guarantees each call returns a new instance, `Object newArray = Array.newInstance(classObject, arrayLength)`
  - `get`**Type**, like `getInstance`but when factory method is in a different class `FileStore fs = Files.getFileStore(path)`
  - `new`**Type**, like `newInstance` but when factory method is in a different class `BufferedReader br = Files.newBufferedReader(path)`
  - **type**, a concise alternative to `get`_Type_ and `new`_Type_, `List<Compliant> litany = Collections.list(legacyLitany)`

### Consider builder when faced with many constructor parameters
```java
public class NutritionFacts {
    private final int servingSize;  // (mL)            required
    private final int servings;     // (per container) required
    private final int calories;     // (per serving)   optional
    private final int fat;          // (g/serving)     optional
    private final int sodium;       // (mg/serving)    optional
    private final int carbohydrate; // (g/serving)     optional

    public NutritionFacts(int servingSize, int servings) {
        this(servingSize, servings, 0);
    }

    public NutritionFacts(int servingSize, int servings, int calories) {
        this(servingSize, servings, calories, 0);
    }

    public NutritionFacts(int servingSize, int servings, int calories, int fat) {
        this(servingSize, servings, calories, fat, 0);
    }

    public NutritionFacts(int servingSize, int servings, int calories, int fat, int sodium) {
        this(servingSize, servings, calories, fat, sodium, 0);
    }

    public NutritionFacts(int servingSize, int servings, int calories, int fat, int sodium, int carbohydrate) {
        this.servingSize  = servingSize;
        this.servings     = servings;
        this.calories     = calories;
        this.fat          = fat;
        this.sodium       = sodium;
        this.carbohydrate = carbohydrate;
    }
}
```

The telescoping constructor pattern works, but it is hard to write client code when there are many parameters, and harder still to read it.

Avoid using JavaBeans pattern as it might leave the object in an inconsistent state partway through its construction. It does also precludes the possibility of making the class immutable.

```java
public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    private final int fat;
    private final int sodium;
    private final int carbohydrate;

    public static class Builder {
        private final int servingSize;
        private final int servings;

        private int calories      = 0;
        private int fat           = 0;
        private int sodium        = 0;
        private int carbohydrate  = 0;

        public Builder(int servingSize, int servings) {
            this.servingSize = servingSize;
            this.servings    = servings;
        }

        public Builder calories(int val)
            { calories = val;      return this; }
        public Builder fat(int val)
            { fat = val;           return this; }
        public Builder sodium(int val)
            { sodium = val;        return this; }
        public Builder carbohydrate(int val)
            { carbohydrate = val;  return this; }

        public NutritionFacts build() {
            return new NutritionFacts(this);
        }
    }

    private NutritionFacts(Builder builder) {
        servingSize  = builder.servingSize;
        servings     = builder.servings;
        calories     = builder.calories;
        fat          = builder.fat;
        sodium       = builder.sodium;
        carbohydrate = builder.carbohydrate;
    }
}
```

```java
NutritionFacts cocaCola = new NutritionFacts.Builder(240, 8)
    .calories(100).sodium(35).carbohydrate(27).build();
```

The Builder pattern simulates named optional parameters and it is well suited to class hierarchies. **It is good choice when designing classes whose constructors or static factories would have more than a handful of parameters.**

### Enforce the singleton property with a private constructor or an enum type

Beware that making a class a singleton can make it difficult to test its clients because it's impossible to substitute a mock implementation /

**Singleton with public final field**, this approach is simpler and it makes it clear that the class is a singleton.

```java
public class Elvis {
    public static final Elvis INSTANCE = new Elvis();
    private Elvis() { ... }

    public void leaveTheBuilding() { ... }
}
```

**Singleton with static factory**

```java
public class Elvis {
    private static final Elvis INSTANCE = new Elvis();
    private Elvis() { ... }
    public static Elvis getInstance() { return INSTANCE; }

    public void leaveTheBuilding() { ... }
}
```

**Enum singleton**, similar to public field approach but more concise. It provides serialisation machinery for free and provides guarantee against multiple instantiation even on serialisation and reflection attacks. **This is the best way of implementing a singleton.**

```java
public enum Elvis {
    INSTANCE;

    public void leaveTheBuilding() { ... }
}
```

### Enforce noninstantiability with a private constructor

Ocassionally you'll want to write a class that is a grouping of static methods. People abuse them in order to avoid thinking in terms of objects, but they have valud use cases.

Such _utility clases_ are not designed to be instantiated.

Attempting to enforce noninstantiability by making the class abstract does not work. **A class can be made noninstantiable by including a private constructor.**

```java
public class UtilityClass {
    // Suppress default constructor for noninstantiability
    private UtilityClass() {
        throw new AssertionError();
    }
    // Remainder omitted
}
```

### Prefer dependency injection to hardwiring resources

Innapropiate use of static utility, inflexible and untestable.

```java
public class SpellChecker {
    private static final Lexicon dictionary = ...;

    private SpellChecker() {} // Noninstantiable

    public static boolean isValid(String word) { ... }
    public static List<String> suggestions(String typo) { ... }
}
```

Dependency injection provides flexibility and testability

```java
public class SpellChecker {
    private final Lexicon dictionary;

    public SpellChecker(Lexicon dictionary) {
        this.dictionary = Objects.requireNonNull(dictionary);
    }

    public boolean isValid(String word) { ... }
    public List<String> suggestions(String typo) { ... }
}
```

A useful variant of the pattern is to pass a resource _factory_ to the constructor so the object can be called repeatedly to create instance of a type.

```java
Mosaic create(Supplier<? extends Tile> tileFactory) { ... }
```

### Avoid creating unnecessary objects

```java
String s = new String("bikini");
```
Performance can be greatly improved

```java
static boolean isRomanNumeral(String s) {
    return s.matches("^(?=.)M*(C[MD]|D?C{0,3})"
        + "(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$");
}
```

Reusing expensive object for improved performance

```java
public class RomanNumerals {
    private static final Pattern ROMAN = Pattern.compile(
        "^(?=.)M*(C[MD]|D?C{0,3})" +
        "(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$");

    static boolean isRomanNumeral(String s) {
        return ROMAN.matcher(s).matches();
    }
}
```

Be careful with autoboxing, as it blurs the distinction betwen primitive and boxed primitive types. The following code is hideously slow, can you spot object creation?

```java
private static long sum() {
    Long sum = 0L;
    for (long i = 0; i <= Integer.MAX_VALUE; i++)
        sum += i;

    return sum;
}
```

Prefer primitives to boxed primitives, and watch out for unintentional autoboxing.

### Eliminate obsolete object references

Can you find the _memory leak_?

```java
public class Stack {
    private Object[] elements;
    private int size = 0;
        private static final int DEFAULT_INITIAL_CAPACITY = 16;

    public Stack() {
        elements = new Object[DEFAULT_INITIAL_CAPACITY];
    }

    public void push(Object e) {
        ensureCapacity();
        elements[size++] = e;
    }

    public Object pop() {
        if (size == 0)
            throw new EmptyStackException();
        return elements[--size];
    }

    /**
     * Ensure space for at least one more element, roughly
     * doubling the capacity each time the array needs to grow.
     */
    private void ensureCapacity() {
        if (elements.length == size)
            elements = Arrays.copyOf(elements, 2 * size + 1);
    }
}
```

Don't forget to null out references once they become obsolete!

```java
public Object pop() {
    if (size == 0)
        throw new EmptyStackException();

    Object result = elements[--size];
    elements[size] = null; // Eliminate obsolete reference
    return result;

}
```

Be mindful about this, **nulling out object references should be the exception rather than the norm.** The best way to eliminate an obsolete reference is to let the variable that contained the reference fall out of scope.

Whenever a class manages its own memory, the programmer should be alert for memory leaks.

Common sources of memory leaks are caches, listeners and callbacks.

### Avoid finalisers and cleaners

Finalisers are unpredictable, often dangerous, and generally unnecessary. Cleaners are less dangerous than finalisers, but still unpredictable, slow, and generally unnecessary.

Never do anything time-critical in a finalisers or cleaners. There is no guarantee they'll be executed promptly.

Never depend on a finaliser or cleaner to update persistent state. The language specification provides no guarantee that finalisers or cleaners will run at all.

There is a sever performance penalty for using finalisers and cleaners.

Finalisers have a serious security problem: they open your class up to finaliser attacks. Throwing an exception from a constructor should be sufficient to prevent an object form coming into existence; in the presence of finalisers, it is not. To protect nonfinal classes from finaliser attacks, write a final `finalize` method that does nothing.

Instead of writing a finaliser or cleaner, just have your class implement `AutoCloseable`.

### Prefer `try`-with-resources to `try-finally`

`try-finally` is no longer the best way to close resources.

```java
static String firstLineOfFile(String path) throws IOException {
    BufferedReader br = new BufferedReader(new FileReader(path));
    try {
        return br.readLine();
    } finally {
        br.close();
    }
}
```

`try-finally` is ugly when used with more than one resource.

```java
static void copy(String src, String dst) throws IOException {
    InputStream in = new FileInputStream(src);
    try {
        OutputStream out = new FileOutputStream(dst);
        try {
            byte[] buf = new byte[BUFFER_SIZE];
            int n;
            while ((n = in.read(buf)) >= 0)
                out.write(buf, 0, n);
        } finally {
            out.close();
        }
    } finally {
        in.close();
    }
}
```


`try`-with-resources is the best way to close resources.

```
static String firstLineOfFile(String path) throws IOException {
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
       return br.readLine();
    }
}
```

`try`-with-resources on multiple resources, short and sweet.

```
static void copy(String src, String dst) throws IOException {
    try (InputStream   in = new FileInputStream(src);
         OutputStream out = new FileOutputStream(dst)) {
        byte[] buf = new byte[BUFFER_SIZE];
        int n;
        while ((n = in.read(buf)) >= 0)
            out.write(buf, 0, n);
    }
}
```


## Methods common to all objects

### Obey the general contract when overriding `equals`

* Each instance of the class is inherently unique
* there is no need for the class to provide a "logical equality" test
* A superclass has overriden `equals`, and the superclass behaviour is appropiate for this class
* The class is private or package-private, and you are certain that its `equals` method will never be invoked.

`equals` method implements _equivalence relation_ for any non-null reference values:
* **Reflexive**: `x.equals(x)` must return `true`
* **Symmetric**:  `x.equals(y)` returns `true` if `y.equals(x)` returns `true`
* **Transitive**:  `x.equals(y)` returns `true` and `y.equals(z)` returns `true`, then `x.equals(z)` must return `true`
* **Consistent**:  `x.equals(y)` should consistently return `true` or consistently return `false`
* `x.equals(null)` must return `false`

Do not write an `equals` method that depends on unreliable resources.

All objects objects must be unequal to `null`.
A few more caveats:
* Always override `hashCode` when you override `equals`.
* Don't try to be too clever
* Don't substitute another type for `Object` in the `equals` declaration.

### Always override `hashCode` when you override equals

Equal objects must have equal hash codes.

Do not be tempted to exclude significant fields from the hash code computation to improve performance.

Don't provide a detailed specification for the value returned by `hashCode`, so clients can't reasonably depend on it; this gives you the flexibility to change it.

### Always override `toString`

Providing a good `toString` implementation makes your class much more pleasant to use and makes systems using the class easier to debug.

When practical, the `toString` method should return all the interesting information in the object.

Whether or not you decide to specify the format, you should clearly document your intentions.

### Override `clone` judiciously

In practice, a class implementing `Cloneable` is expected to provide a properly functioning public `clone` method.

Immutable classes should never provide a `clone` method, because that would only encourage wasteful copying.

The `clone` method functions as a constructor; you must ensure that it does no harm to the original object and that it properly establishes invariants on the clone.

The `Cloneable` architecture is incompatible with normal use of final fields referring to mutable objects.

Public `clone` methods should omit the `throws` clause, as methods that don't throw checked exceptions are easier to use.

A better approach to object copying is to provide a copy constructor or copy factory.

```java
public Yum(Yum yum) { ... }
```

```java
public static Yum newInstance(Yum yum) { ... };
```

Advantages of using copy constructor or copy factory:
* They don't rely on a risk-prone extralinguistic object creation mechanism.
* They don't demand unenforceable adherence to thinly documented conventions.
* They don't conflict with the proper use of final fields.
* They don't throw unnecessary checked exceptions.
* They don't require casts.
* They can take an argument whose type is an interface implemented by the class.
* Interface-based copy constructors and factories (_conversion_ constructors and _conversion_ factories) allow the client to accept the implementation type of the original.

### Consider implementing `Comparable`

The notation `sgn`(expression) designates the mathematical _signum_ function, which is defined to return -1, 0, or 1

* The implementor must ensure that `sgn(x.compareTo(y)) == -sgn(y. compareTo(x))` for all `x` and `y`. Implies that `x.compareTo(y)` must throw an exception if and only if `y.compareTo(x)` throws an exception.
* Transitive: ``(x. compareTo(y) > 0 && y.compareTo(z) > 0)`` implies `x.compareTo(z) > 0`.
* `x.compareTo(y) == 0` implies that `sgn(x.compareTo(z)) == sgn(y.compareTo(z))`, for all `z`.
* It is strongly recommended, but not required, that `(x.compareTo(y) == 0) == (x.equals(y))`.

Use of the relational operators `<` and `>` in compareTo methods is verbose and error-prone and no longer recommended.

If a class has multiple significant fields, the order in which you compare them is critical. Start with the most significant field and work your way down.

The `Comparator` interface is outfitted with a set of comparator construction methods, which enable fluent construction of comparators. Many programmers prefer the conciseness of this approach, though it does come at a modest performance cost.

```java
private static final Comparator<PhoneNumber> COMPARATOR =
    comparingInt((PhoneNumber pn) -> pn.areaCode)
        .thenComparingInt(pn -> pn.prefix)
        .thenComparingInt(pn -> pn.lineNum);

public int compareTo(PhoneNumber pn) {
    return COMPARATOR.compare(this, pn);
}
```

**Avoid comparators based on differences, they violate transitivity**

```java
static Comparator<Object> hashCodeOrder = new Comparator<>() {
    public int compare(Object o1, Object o2) {
        return o1.hashCode() - o2.hashCode();
    }
};
```
## Classes and interfaces

### Minimise the accessibility of classes and members

A well-designed component hides all its implementation details, cleanly separating their API from its implementation.

Information hiding or _encapsulation_ is important because:
* _Decouples_ the component that comprise the system, allowing them to be developed, tested, optimised, used, understood and modified in isolation.
* Speeds up development because components can be developed in parallel.
* Eases the burden of maintenance because components can be understood more quickly and debugged or replaced with little fear or harming other components.
* Components can be optimised without affecting correctness of others.
* Increases software reuse because components that aren't tightly coupled often prove useful in other contexts.
* Decreases the risk in building large systems because individual components may prove successful even if the system does not.

Make each class or member as inaccessible as possible.

Instance fields of public classes should rarely be public. Classes with public mutable fields are generally thread-safe.

Nonzero-length array is always mutable, so it is wrong for a class to have a public static final array field, or accessor that returns such a field. It is a potential security hole.

```java
public static final Thing[] VALUES = { ... };
```

Alternatively, return a copy of a private array

```java
private static final Thing[] PRIVATE_VALUES = { ... };

public static final List<Thing> VALUES =
   Collections.unmodifiableList(Arrays.asList(PRIVATE_VALUES));
```

### In public classes, use accessor methods, not public fields

Degenerate classes like this should not be public

```java
class Point {
   public double x;
   public double y;
}
```

Because the data fields of such classes are accessed directly, these classes do not offer the benefits of _encapsulation_. You can't change the representation without changing the API, you can't enforce invariants, and you can't take auxiliary action when a field is accessed.

If a class is accessed outside its package, provide accessor methods.

If a class is package-private or is a private nested class, there is nothing inherently wrong with exposing its data fields.

### Minimise mutability

An immutable class is simply a class whose instances cannot be modified. **Immutable classes are easier to design, implement, and use than mutable classes. They are less prone to error and are more secure.**

1. Don't provide methods that modify the object's state (mutators).
2. Ensure that the class can't be extended.
3. Make all fields final.
4. Make all fields private.
5. Ensure exclusive access to any mutable components.

Returning new objects on operations is known as _functional approach_ because methods return the result of applying a function to their operand, without modifying it. Contrast it to the _procedural_ or _imperative_ approach in which methods apply a procedure to their operand, causing its state to change. **Method names in immutable objects are prepositions (such as `plus`) rather than names (such as `add`).**

Advantages of immutable objects:
* Simple.
* Inherently thread-safe; they require no synchronisation.
* Can be shared freely.
* Not only you can share immutable objects, but they can share their internals.
* Make great building blocks for other objects.
* Provide failure atomicity for free. There is no possibility of temporary inconsistency.

The main disadvantage immutable objects have is that they require a separate object for each distinct value.

Classes should be immutable unless there's a very good reason to make them mutable.

If a class cannot be made immutable, limit its mutability as much as possible. Declare every field `private final` unless there's a good reason to do otherwise.

Constructors should create fully initialised objects with all of their invariants established.

### Favour composition over inheritance

Using inheritance inappropriately lead to fragile software. It is safe to use inheritance within a package where programmers have classes and subclasses under control. It is safe to use inheritance when extending classes specifically designed and documented for extension.

Unlike method invocation, implementation inheritance violates encapsulation. Subclasses depend on the implementation details of its superclass for its proper function.

To avoid fragility use composition and forwarding instead of inheritance, especially if an appropriate interface to implement a wrapper exists. Wrapper classes are not only more robust than subclasses, they are also more powerful.

### Design and document for inheritance or else prohibit it

The class must document its self-use of overridable methods.

A class may have to provide hooks into its internal workings in the form of judiciously chosen protected methods.

**The only way to test a class designed for inheritance is to write subclasses.**

You must test your class by writing subclasses before you release it.

Constructors must not invoke overridable methods. Superclass constructor runs before the subclass constructor. If the overriding method depends on any initialisation performed by the subclass constructor, the method will not behave as expected.

```java
public class Super {
    // Broken - constructor invokes an overridable method
    public Super() {
        overrideMe();
    }

    public void overrideMe() {
    }
}

public final class Sub extends Super {
    // Blank final, set by constructor
    private final Instant instant;

    Sub() {
        instant = Instant.now();
    }

    // Overriding method invoked by superclass constructor
    @Override public void overrideMe() {
        System.out.println(instant);
    }

    public static void main(String[] args) {
        Sub sub = new Sub();//null
        sub.overrideMe();//instant
    }
}
```

Same restriction applies to `clone` and `readObject`, they should not invoke overridable methods, directly or indirectly.

Designing a class for inheritance requires great effort and places substantial limitations on the class.

The best solution to this problem is to prohibit subclassing in classes that are not designed and documented to be safely subclassed. There are two ways of doing this. Declare the class final or make all constructors private or package-private and to add public static factories instead of constructors.

### Prefer interfaces to abstract classes

Existing classes can easily be retrofitted to implement a new interface.

Interfaces are ideal for defining _mixings_, a type that a class can implement in addition to its "primary type". For example Comparable is a mixing that allows a class can be ordered.

Interfaces allow for the construction of nonhierarchical type frameworks.

Interfaces enable safe, powerful functionality enhancements via the wrapper class idiom. If you use abstract classes, you leave the programmer who wants to add functionality with no alternative than to use inheritance.

You can combine the advantages of interfaces and abstract classes by providing an abstract _skeletal implementation class_ to go with an interface. The interface defines the type, while the skeletal implementation class implements the primitive interface methods (_Template Method_ pattern).

Concrete implementation built on top of an skeletal implementation.

```java
static List<Integer> intArrayAsList(int[] a) {
    Objects.requireNonNull(a);

    // The diamond operator is only legal here in Java 9 and later
    // If you're using an earlier release, specify <Integer>
    return new AbstractList<>() {
        @Override public Integer get(int i) {
            return a[i];  // Autoboxing (Item 6)
        }

        @Override public Integer set(int i, Integer val) {
            int oldVal = a[i];
            a[i] = val;     // Auto-unboxing
            return oldVal;  // Autoboxing
        }

        @Override public int size() {
            return a.length;
        }
    };
}
```

Skeletal implementation classes provide implementation assistance of abstract classes without imposing constraints as type definitions.

Good documentation is essential in a skeletal implementation.

### Design interfaces for posterity

It is not always possible to write a default method that maintains all the invariants of every conceivable implementation.

In the presence of default methods, existing implementations of an interface may compile without error or warning but fail at runtime.

Is still of the utmost importance to design interfaces with great care. While it may be possible to correct some interface flaws after an interface is released, you cannot count on it.

### Use interfaces only to define types

Constant interface anti-pattern (only constants) are a poor use of interfaces. Implementing a constant interface causes this implementation detail to leak into the class's exported API.

```java
public interface PhysicalConstants {
    static final double AVOGADROS_NUMBER   = 6.022_140_857e23;
    static final double BOLTZMANN_CONSTANT = 1.380_648_52e-23;
    static final double ELECTRON_MASS      = 9.109_383_56e-31;
}
```