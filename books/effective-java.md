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