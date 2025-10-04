![1756676813947](image/typescript/1756676813947.png)

# Interface vs Type

**What is an `interface`?**

An `interface` in TypeScript is used to  **define the shape of an object** , including:

* Properties
* Methods
* Optional or readonly fields

It’s mainly used for **object typing** and can be  **extended** .

**Example:**

```ts
interface User {
  id: number;
  name: string;
  email?: string; // optional
  readonly createdAt: Date;
}

const user: User = {
  id: 1,
  name: "Alice",
  createdAt: new Date(),
};

```

* `email` is optional
* `createdAt` is read-only (cannot be reassigned)

**What is a `type` alias?**

A `type` alias gives a name to  **any type** , not just objects. It can define:

* Objects
* Unions
* Intersections
* Tuples
* Primitives

**Example (object type):**

```ts
type User = {
  id: number;
  name: string;
  email?: string;
}

```

**Example (union type):**

```ts
type Status = "success" | "error" | "loading";

```

**Example (intersection type):**

```ts
type Person = { name: string };
type Employee = Person & { employeeId: number };
```

---

**Key Differences:**

| Feature                                             | `interface`                                        | `type`                                     |
| --------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------- |
| **Can extend**                                | Yes, can use `extends`                             | Yes, via intersections (`&`)               |
| **Can merge / reopen**                        | Yes, interface declarations with the same name merge | No, type aliases cannot be reopened          |
| **Can describe primitives / unions / tuples** | No                                                   | Yes                                          |
| **Readability / common use**                  | Often preferred for objects and classes              | More flexible, used for unions/intersections |

---

**When to use which?**

**Use `interface` when:**

* You’re defining an **object or class shape**
* You want to **take advantage of declaration merging** (extending interfaces across files)
* You want better readability for large object shapes

**Use `type` when:**

* You need **unions** or **intersections**
* You want to alias **primitive types** or **tuples**
* You want **more flexible type compositions**

---

**Examples in React**

**Typing props with `interface`:**

```ts
interface ButtonProps {
  label: string;
  onClick: () => void;
}

function Button({ label, onClick }: ButtonProps) {
  return <button onClick={onClick}>{label}</button>;
}
```

**Typing props with `type` (union example):**

```ts
type ButtonProps = {
  label: string;
  onClick: () => void;
  variant: "primary" | "secondary";
}
```

---

💡 **Analogy:**

* `interface` → blueprint for an object, can be extended or merged
* `type` → flexible alias, can describe almost anything

# Generics

Generics allow you to  **write reusable code that works with multiple types** , while still maintaining  **type safety** .

Think of them as **placeholders for types** that you define later when using the function, class, or interface.

**Why use Generics?**

Without generics:

```ts
function identity(value: any) {
  return value;
}

const num = identity(5);       // num is any
const str = identity("hello"); // str is any
```

* Problem: `any` removes type safety.
* You lose **autocomplete** and  **type checking** .

With generics:

```ts
function identity<T>(value: T): T {
  return value;
}

const num = identity<number>(5);       // num is number
const str = identity<string>("hello"); // str is string
```

* `T` is a  **type placeholder** .
* Type safety is preserved.

**Generic functions**

**Example 1 – Array utility:**

```ts
function firstElement<T>(arr: T[]): T | undefined {
  return arr[0];
}

const num = firstElement([1, 2, 3]);    // number
const str = firstElement(["a", "b"]);   // string
```

**Example 2 – Identity function:**

```ts
function wrapInArray<T>(value: T): T[] {
  return [value];
}

const wrappedNum = wrapInArray(42);     // number[]
const wrappedStr = wrapInArray("hi");   // string[]
```

Generic interfaces & types

```ts
interface Box<T> {
  content: T;
}

const numberBox: Box<number> = { content: 100 };
const stringBox: Box<string> = { content: "Hello" };
```

Generic type alias:

```ts
type Pair<T, U> = {
  first: T;
  second: U;
};

const pair: Pair<number, string> = { first: 1, second: "one" };
```

**Generics in React components**

**Typing props with generics:**

```ts
interface ListProps<T> {
  items: T[];
  render: (item: T) => JSX.Element;
}

function List<T>({ items, render }: ListProps<T>) {
  return <ul>{items.map(render)}</ul>;
}

// Usage
const users = [{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }];
<List items={users} render={(user) => <li key={user.id}>{user.name}</li>} />

```

* `T` allows the component to work with  **any type of items** .
* Maintains **type safety** across usage.

**Constraints on generics**

Sometimes you want to restrict what type `T` can be:

```ts
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

getLength("hello"); // 5
getLength([1, 2, 3]); // 3
// getLength(10); // ❌ Error: number doesn't have length

```

**Summary / Key Points**

* Generics = reusable, type-safe placeholders for types
* Can be used in **functions, interfaces, types, classes, React components**
* Keep code flexible **without losing type safety**
* Constraints (`extends`) allow limiting acceptable types

---

💡 **Analogy:**

Generics are like a  **blank label on a container** . You can fill it with anything (string, number, object), but the label ensures you **know exactly what type is inside** when you use it.

# **Utility types**

**Partial `<T>`**

`Partial` makes  **all properties of a type optional** .

**Use case:** Useful when you want to update an object partially.

```ts
interface User {
  id: number;
  name: string;
  email: string;
}

// Without Partial, all fields are required
const updateUser1: User = { id: 1 }; // ❌ Error

// With Partial
const updateUser2: Partial<User> = { name: "Alice" }; // ✅ OK

```

**Key point:** Does  **not remove properties** , just makes them optional.

**Pick<T, K>**

`Pick` allows you to **select a subset of properties** from a type.

**Use case:** Useful when you only need certain fields.

```ts
interface User {
  id: number;
  name: string;
  email: string;
}

type UserPreview = Pick<User, "id" | "name">;

const preview: UserPreview = { id: 1, name: "Alice" }; // ✅ OK
// email is not allowed here

```

**Key point:** You specify which keys you want to “pick” from the original type.

**Omit<T, K>**

`Omit` is the opposite of `Pick`: it **removes specified properties** from a type.

**Use case:** Useful when you want a type that  **excludes sensitive or unnecessary fields** .

```ts
interface User {
  id: number;
  name: string;
  email: string;
}

type UserWithoutEmail = Omit<User, "email">;

const user: UserWithoutEmail = { id: 1, name: "Alice" }; // ✅ OK
// email is not allowed

```

**Key point:** You remove keys instead of picking them.

**Record<K, T>**

`Record` creates a type with  **specific keys and values of a given type** .

**Use case:** Useful for mapping or dictionaries.

```ts
type Roles = "admin" | "editor" | "viewer";
type RolePermissions = Record<Roles, string[]>;

const permissions: RolePermissions = {
  admin: ["read", "write", "delete"],
  editor: ["read", "write"],
  viewer: ["read"],
};

```

`Record<K, T>` =  **keys of type K** , **values of type T**

**Quick Summary Table**

| Utility Type              | What it does              | Example Use Case                       |
| ------------------------- | ------------------------- | -------------------------------------- |
| **Partial `<T>`** | Makes all fields optional | Updating user info                     |
| **Pick<T, K>**      | Selects specific keys     | Returning only subset of object fields |
| **Omit<T, K>**      | Removes specific keys     | Excluding sensitive fields             |
| **Record<K, T>**    | Creates a key-value map   | Storing permissions or configs         |

💡 **Analogy:**

* `Partial` → like a  **flexible form** , you don’t need to fill everything
* `Pick` → like  **choosing items from a menu** , only what you want
* `Omit` → like **removing items from a set**
* `Record` → like a  **dictionary** , mapping keys to values

# Union vs intersection types

**Union Types (`|`)**

A **union type** means a variable can be  **one of several types** .

**Syntax:**

```ts
type A = string | number;
```

**Example:**

```ts
let value: string | number;

value = "hello"; // ✅ OK
value = 42;      // ✅ OK
// value = true; // ❌ Error, boolean not allowed
```

**Use case:** When a value could be  **one of multiple types** , like form inputs, API responses, or flexible function arguments.

**Function example:**

```ts
function printId(id: string | number) {
  console.log(`ID: ${id}`);
}

printId(101);      // ✅ OK
printId("ABC123"); // ✅ OK

```

**Key point:** Use unions when a value  **can be one type OR another** .

---

**Intersection Types (`&`)**

An **intersection type** means a variable must satisfy  **all combined types simultaneously** .

**Syntax:**

```ts
type A = { name: string } & { age: number };
```

**Example:**

```ts
type Person = { name: string } & { age: number };

const p: Person = {
  name: "Alice",
  age: 30,
}; // ✅ OK

// const p2: Person = { name: "Bob" }; // ❌ Error, missing 'age'

```

**Use case:** When you want to **combine multiple types** into one, e.g., merging props or data models.

**Function example:**

```ts
type Person = { name: string } & { age: number };

const p: Person = {
  name: "Alice",
  age: 30,
}; // ✅ OK

// const p2: Person = { name: "Bob" }; // ❌ Error, missing 'age'

```

**Key point:** Use intersections when a value  **must meet all criteria** .

---

**Comparison Table**

| Feature       | Union(`\|`)         | Intersection (`&`)               |
| ------------- | -------------------- | ---------------------------------- |
| Meaning       | One of the types     | All of the types combined          |
| Example Value | `string \| number`  | `{name: string} & {age: number}` |
| Use Case      | Flexible input types | Combining objects or props         |
| Key Idea      | OR                   | AND                                |

**Real-world analogy**

* **Union:** “I’ll eat **pizza OR pasta** for dinner.” (either works)
* **Intersection:** “I need a **pizza AND pasta** for dinner.” (must have both)

💡 **Tip for interviews:**

* If they ask about a union vs intersection, remember:  **union = flexibility, intersection = combination** .
* Be ready to give a small example with objects or function arguments.


# Any vs Unknown

These are both top types in typescript (meaning they can hold any value), but they behave verydifferently.

**🔹any**

* the "escape hatch" in Typescript
* Disables type checking, you can do anything with an `any` value.
* Useful temporary, but dangerous because it removes type satey

```ts
let value: any = "hello";
value = 123;       // okay
value.toUpperCase(); // okay (but may crash if value is not a string!)
```

👉 **Think of `any` as opting out of TypeScript.**


🔹**Unknown**

* Safer alternatives to any
* It can hold anything, but can't use it without first narrowing first
* Forces you to do type checks.

```ts
let value: unknown = "hello";
value = 123;       // okay

// Not allowed directly:
// value.toUpperCase(); ❌

// Need type check:
if (typeof value === "string") {
  console.log(value.toUpperCase()); // ✅ safe
}
```

**Interview takeaway:**

* Use `any` when you want to disable type checking (last resort).
* Use `unknown` when the type is dynamic but must be checked before use.


# **Optional Properties (`?`)**

* Marks a property as not required.
* Value can be the given type  **or undefined**.

```ts
interface User {
  id: number;
  name?: string; // optional
}

const u1: User = { id: 1 };          // ✅ valid
const u2: User = { id: 2, name: "A"} // ✅ valid
```

👉 Use `?` for props/configs where a field might not exist.


**`readonly` Properties**

* Prevents reassignment after initialization.
* Great for immutable data.

```ts
interface Car {
  readonly vin: string;
  model: string;
}

const car: Car = { vin: "123ABC", model: "Tesla" };
car.model = "Ford";   // ✅ allowed
car.vin = "999XYZ";   // ❌ Error: readonly
```

👉 Use readonly for things that should never change (IDs, constants).


✅ Quick Summary for Interview:

* **`any`** : do anything, unsafe.
* **`unknown`** : must check type before using, safer.
* **`?` (optional)** : property may be missing.
* **`readonly`** : property cannot be reassigned after set.
