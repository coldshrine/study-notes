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