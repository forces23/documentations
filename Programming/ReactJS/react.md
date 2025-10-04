sl![1756594516638](image/react/1756594516638.png)

# Prop Vs State

## Why Use State?

* props are immutable
* value which can change dynamically

## What is State?

* State is nothing but a object which holds information to control the behavior of the component

| Props                                 | State                                   |
| ------------------------------------- | --------------------------------------- |
| passed to the component               | contained in the component              |
| immutable<br />(Cannot be changed)    | mutable<br />(can be changed)           |
| like params passed to a function      | like a variable declared in a function  |
| provides external data to a component | provides internal data to the component |

**Note:** You can pass a state from the parent to the child component if you declare the state in the parent and pass the state as a prop. The only catch with this is that the state passed can not be changes UNLESS you pass along the state updater function (setState), so the child may use this.

**Note:** This whole concept is the key to components being reusable

# React Hooks

## useState

when you call useState it returns 2 things:

1. value
2. function
   * This function is what triggers a re-render the DOM so that changes reflect on on the page

🔹 `useState` Syntax

```
const [state, setState] = useState(initialValue);
```

* **`state`** → current value.
* **`setState`** → function to update the value.
* **`initialValue`** → the starting value of the state.

Example:

```ts
// Typescript
import {useState} from 'react'

const = [state, setState] = useState<string>("Hello, World")
```

**Note:** Console.logs will always be behind. so if you were console.log-ing a number like this :

```ts

export const StateExample() {
     const [count, setCount] = useState<number>(0);

     const increment() {
          setCount(prev => prev+1);
          console.log(count);
     }

     return (
          <h1> {count} </h1>
	  <button onClick={increment}> Click Me! </button>
     )
}
```

when it console logs you would think that it would be 1 since it already starts at 0 but when you click the button it will show 0 in the browser console. This is because the re-render happens after the the function runs. so keep that in mind...

## useEffect

Uses of a useEffect:

* run a function eveytime a specific state changes
* run a function everytime the page loads
* run a function on ever re-render of the UI

It is important to always use a dependency list bracket even if empty.

If you **dont put a dependency** list bracket then the useEffect will **trigger** whenever **ANY state changes.**

If you leave the **dependency bracket empty** then it will **trigger only on the inital load** of the page

If you **add a dependency to the brackets** then that useEffect will only **trigger if that dependency changes**.

🔹 `useEffect` Syntax

```ts
useEffect(() => {
  // side effect code (runs after render)  return () => {
    // optional cleanup code (runs before unmount or before next effect)
  };
}, [dependencies])
```

* **Effect function** → runs after the component renders.
* **Cleanup function** (optional) → useful for timers, subscriptions, event listeners.
* **Dependency array** → controls *when* the effect runs:
  * `[]` → runs **only once** after initial render.
  * `[value]` → runs whenever `value` changes.
  * *(no array)* → runs  **after every render** .

Example:

```ts

export const EffectExample() {
     const [data, setData] = useState([]);
     const [test, setTest] = useState(false);

     // useEffect eith empty dependency will ONLY trigger whenever the page the page loads
     useEffect(() => {
          fetch("jsonplaceholder.typicode.com/posts")
               .then((response) => response.json())
               .then((json) => setData(json));
     },[]);

     // useEffect with something in the dependency brackets means that the function will get triggered everytime the dependency changes (in this example everytime you click on toggle button)
     useEffect(() => {
          console.log(test);
     },[test]);

     return (
          <div>
               <button onClick={() => setTest((prev) => !prev)}> Toggle </button>
               <h1> Post</h1>
               <ul>
                    {jsonData.map((item, index) => (
                         <li>{item.title} </li>
                    ))}
               </ul>
          </div>
     );
}
```

N**ote:** Can use jsonplaceholder.typicode.com/posts as a easy way to test fetching from an API

**Note:** more effective way of fetching data is **React Query**

Advanced:

* subscribing to events

## useContext

The **Context API** is React’s simplest form of global state management. It allows you to create a **context** and then wrap a **provider** around components. Any component inside that provider (the children) can access the data in the context, without needing to pass props manually through multiple levels. using something like can help prevent prop drilling

There are libraries also that you can you :

* Redux
* Zustand
* React Query

How to create the context:

```ts
import React, { createContext, useContext, useState, ReactNode } from "react";

// 1. Create a context with default values
type AppContextType = {
  theme: string;
  user: string;
  setTheme: (theme: string) => void;
  setUser: (user: string) => void;
};

const AppContext = createContext<AppContextType | undefined>(undefined);

// 2. Create a Provider component
const AppProvider = ({ children }: { children: ReactNode }) => {
  const [theme, setTheme] = useState("light");
  const [user, setUser] = useState("Guest");

  return (
    <AppContext.Provider value={{ theme, user, setTheme, setUser }}>
      {children}
    </AppContext.Provider>
  );
};

// 3. Custom hook for easier usage
const useAppContext = () => {
  const context = useContext(AppContext);
  if (!context) throw new Error("useAppContext must be used inside AppProvider");
  return context;
};
```

```ts
import React, { useState } from "react";
// import useAppContext

// 4. Example component that consumes the context
const Profile = () => {
  const { user, setUser } = useAppContext();

  return (
    <div>
      <h2>Current User: {user}</h2>
      <button onClick={() => setUser("Bobby")}>Change User</button>
    </div>
  );
};

const ThemeSwitcher = () => {
  const { theme, setTheme } = useAppContext();

  return (
    <div>
      <h2>Theme: {theme}</h2>
      <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
        Toggle Theme
      </button>
    </div>
  );
};

// 5. Wrap components with provider
const App = () => {
  return (
    <AppProvider>
      <h1>React Context Example</h1>
      <Profile />
      <ThemeSwitcher />
    </AppProvider>
  );
};

export default App;
```

## useReducer

* `useReducer` is a React  **hook for managing state** .
* It’s an  **alternative to `useState`** , especially when state logic is **complex** or involves **multiple values** that change together.
* Instead of updating state directly with a setter (like `setState`), you **dispatch actions** to a reducer function, which decides how the state should change.

👉 Think of it like a  **mini Redux inside your component** .

🔹 Syntax

```ts
const [state, dispatch] = useReducer(reducer, initialState);
```

* **`reducer`** → A function `(state, action) => newState` that defines how the state changes.
* **`initialState`** → The starting state.
* **`dispatch`** → A function you call with an `action` to update the state.

Example: Counter with `useReducer`

Here’s a simple counter that increments, decrements, and resets:

```ts
import React, { useReducer } from "react";

// 1. Define the state type
type State = {
  count: number;
};

// 2. Define possible action types
type Action =
  | { type: "INCREMENT" }
  | { type: "DECREMENT" }
  | { type: "RESET" }
  | { type: "SET"; payload: number };

// 3. Create the reducer function
const reducer = (state: State, action: Action): State => {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + 1 };
    case "DECREMENT":
      return { count: state.count - 1 };
    case "RESET":
      return { count: 0 };
    case "SET":
      return { count: action.payload };
    default:
      return state;
  }
};

// 4. Use it inside a component
const Counter = () => {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
         <h1>Count: {state.count}</h1>
         <button onClick={() => dispatch({ type: "INCREMENT" })}>+</button>
         <button onClick={() => dispatch({ type: "DECREMENT" })}>-</button>
         <button onClick={() => dispatch({ type: "RESET" })}>Reset</button>
         <button onClick={() => dispatch({ type: "SET", payload: 10 })}>Set to 10</button>
    </div>
  );
};

export default Counter;

```

🔹 Key Takeaways

1. `useState` is simpler and great for small state updates.
2. `useReducer` is better when:
   * State has  **multiple sub-values** .
   * Updates are  **dependent on action types** .
   * You want a **clearer, more predictable state transition** (like Redux).

## UseRef

`useRef` is a React hook that gives you a **mutable object** with a `.current` property.

```ts
const myRef = useRef(initialValue); 
```

* `myRef.current` → holds the value (starts as `initialValue`).
* Unlike state (`useState`), changing `myRef.current`  **does NOT cause a re-render** .
* A ref object stays the **same** between re-renders (it doesn’t get reset).

👉 Think of it like a **“box”** that React gives you to store a value that you want to  **persist between renders** , but  **without triggering re-renders** .

---

🔹 2 Main Uses of `useRef`

1. Accessing DOM Elements

Refs are often used to directly access a DOM element.

Example: Focusing an input field.

```ts
import React, { useRef } from "react";

const InputFocus = () => {
  const inputRef = useRef<HTMLInputElement>(null);

  const focusInput = () => {
    inputRef.current?.focus(); // directly access the input element
  };

  return (
    <div>
      <input ref={inputRef} type="text" placeholder="Type here..." />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
};

export default InputFocus;

```

✔ Here, `inputRef.current` points to the `<input>` element.

---

2. Storing Mutable Values (like instance variables)

You can use `useRef` to keep values between renders  **without re-rendering** .

Example: Keeping track of a render count.

```ts
import React, { useRef, useState, useEffect } from "react";

const RenderCounter = () => {
  const [text, setText] = useState("");
  const renderCount = useRef(0);

  useEffect(() => {
    renderCount.current += 1; // update without re-rendering
  });

  return (
    <div>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <p>Renders: {renderCount.current}</p>
    </div>
  );
};

export default RenderCounter;

```

✔ `renderCount` increases every render, but updating it doesn’t trigger another render (unlike `useState`).

---

🔹 Key Differences vs `useState`

| Feature            | `useState`    | `useRef`                       |
| ------------------ | --------------- | -------------------------------- |
| Triggers re-render | ✅ Yes          | ❌ No                            |
| Persists value     | ✅ Yes          | ✅ Yes                           |
| Common use         | State UI values | Access DOM, store mutable values |

---

🔹 Summary

* `useRef(initialValue)` → returns an object `{ current: initialValue }`.
* The `.current` value  **persists across renders** .
* Updating `.current` does **not** re-render the component.
* Used for:
  1. Accessing/manipulating DOM elements (`ref={myRef}`).
  2. Storing values that survive re-renders but don’t need to trigger UI updates.

## useImperativeHandle

`useImperativeHandle` is a React hook that lets you **customize the instance value** that is exposed to a parent component when using  **`ref` with `forwardRef`** .

In plain English: It lets a parent call **functions inside a child component** through a ref.

example would be that this would be useful if you did not want to move a state up into the parent just to use the updater for a state from a child

⚡A good real-world use case:

* A reusable **custom input** component that has methods like `.focus()`, `.clear()`, or `.validate()`.
* Parent doesn’t need to manage all those internal details — it just calls the methods when needed.

👉 Normally, refs are just used to access  **DOM elements** .

👉 With `useImperativeHandle`, you can **expose specific functions or values** from a child component to the parent.

---

🔹 Syntax

```ts
useImperativeHandle(ref, () => ({
  // values or methods exposed to parent
}));
```

* **`ref`** → the ref forwarded from the parent.
* **`()=>({...})`** → returns an object of methods/values you want the parent to access.

⚠️ Must be used inside a component that is wrapped with `forwardRef`.

---

🔹 Example: Exposing a Child Method to Parent

Let’s say we want a parent to be able to  **focus an input inside a child** .

```ts
import React, { useRef, forwardRef, useImperativeHandle } from "react";

// 1. Child component
const CustomInput = forwardRef((props, ref) => {
  const inputRef = useRef<HTMLInputElement>(null);

  // Expose methods to parent
  useImperativeHandle(ref, () => ({
    focusInput: () => {
      inputRef.current?.focus();
    },
    clearInput: () => {
      if (inputRef.current) inputRef.current.value = "";
    }
  }));

  return <input ref={inputRef} type="text" placeholder="Type something..." />;
});

// 2. Parent component
const App = () => {
  const inputRef = useRef<{ focusInput: () => void; clearInput: () => void }>(null);

  return (
    <div>
      <CustomInput ref={inputRef} />
      <button onClick={() => inputRef.current?.focusInput()}>Focus Input</button>
      <button onClick={() => inputRef.current?.clearInput()}>Clear Input</button>
    </div>
  );
};

export default App;

```

---

🔹 Breakdown

1. **`forwardRef`**
   * Wraps the child so it can accept a `ref` from the parent.
2. **Inside child (`CustomInput`)**
   * We make a regular `inputRef` to access the DOM input.
   * `useImperativeHandle(ref, () => ({ ... }))` decides what the parent can call.
   * We expose `focusInput` and `clearInput`.
3. **Parent (`App`)**
   * Creates a `ref`.
   * Calls `inputRef.current.focusInput()` or `inputRef.current.clearInput()`.

---

🔹 Why use it?

* Encapsulation: The parent doesn’t need to know about the child’s internal refs.
* Control: The child decides **which methods/values** are exposed.
* Real-world uses:
  * Custom form inputs (`.focus()`, `.clear()`, `.validate()`).
  * Media players (`.play()`, `.pause()`).
  * Animation triggers (`.startAnimation()`).

---

✅ **Rule of thumb:**

* Use normal `ref` for DOM access.
* Use `useImperativeHandle` when you want to expose **custom methods** from a child component.

## useMemo

🔹 **What is `useMemo`?**

* `useMemo` is a React hook that  **memoizes the result of a computation** .
* In other words, it **remembers the result of a function** until its dependencies change.
* Helps **avoid recalculating expensive operations** on every render.

---

🔹 **Syntax**

```ts
const memoizedValue = useMemo(() => {
  // expensive calculation
  return computeSomething(a, b);
}, [a, b]);

```

* First argument: a function that returns the value you want to memoize.
* Second argument: dependency array — the value is recalculated  **only when dependencies change** .

---

🔹 **Example 1: Expensive Calculation**

```ts
import React, { useState, useMemo } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [number, setNumber] = useState(0);

  // Expensive calculation: only recomputed when 'number' changes
  const factorial = useMemo(() => {
    console.log("Calculating factorial...");
    let result = 1;
    for (let i = 1; i <= number; i++) {
      result *= i;
    }
    return result;
  }, [number]);

  return (
    <div>
      <input
        type="number"
        value={number}
        onChange={(e) => setNumber(+e.target.value)}
      />
      <p>Factorial: {factorial}</p>

      <button onClick={() => setCount(count + 1)}>Re-render</button>
      <p>Count: {count}</p>
    </div>
  );
}

export default App;

```

**What happens here:**

* When you change `number`, `factorial` is recalculated. ✅
* When you change `count`, `factorial` is **not recalculated** because it’s memoized. ✅
* Console shows `"Calculating factorial..."`  **only when necessary** .

---

🔹 **When to Use `useMemo`**

1. **Expensive calculations**
   * Large loops, heavy math, sorting big arrays.
2. **Derived data from props/state**
   * Example: filtered or sorted lists.
3. **Referential equality for dependencies**
   * When you want stable object/array references to prevent child components from unnecessary re-renders.

---

**🔹 Common Mistakes**

* ❌ Using `useMemo` everywhere — it has some memory & computation overhead. Only use for  **expensive calculations** .
* ❌ Forgetting dependencies — if dependencies are missing, React might return  **stale values** .
* ❌ Confusing it with `useCallback` — `useMemo` memoizes  **values** , `useCallback` memoizes  **functions** .

---

**Quick Comparison**

| Hook            | Memoizes                     | Returns              |
| --------------- | ---------------------------- | -------------------- |
| `useMemo`     | Computed**value**      | `memoizedValue`    |
| `useCallback` | **Function reference** | `memoizedFunction` |

## useCallback

**🔹 What is `useCallback`?**

* `useCallback` is a React hook that  **memoizes a function reference** .
* It **returns the same function instance** across renders  **until dependencies change** .
* This is useful because in React, passing a new function every render can cause **unnecessary re-renders** of child components that rely on reference equality.

---

🔹 **Syntax**

```ts
const memoizedFunction = useCallback(() => {
  // function logic here
}, [dependencies]);
```

* **First argument:** the function you want to memoize.
* **Second argument:** dependency array — function is recreated  **only if dependencies change** .

---

**🔹 Why it matters**

1. **Child component re-renders**
   * If a child component uses `React.memo` to avoid re-rendering unnecessarily, passing a new function each time will break memoization.
   * `useCallback` keeps the function the **same instance** until dependencies change.
2. **Performance**
   * Useful when you pass functions to components or hooks that rely on **stable function references** (like `useEffect`, `useMemo`, or event listeners).

---

**🔹 Example 1: Prevent unnecessary re-renders**

```ts
import React, { useState, useCallback } from "react";

const Button = React.memo(({ onClick, label }) => {
  console.log("Button re-rendered:", label);
  return <button onClick={onClick}>{label}</button>;
});

export default function App() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState("");

  // Without useCallback, this function is recreated every render
  const increment = useCallback(() => {
    setCount((c) => c + 1);
  }, []); // No dependencies → always same function instance

  return (
    <div>
      <Button onClick={increment} label="Increment" />
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type something"
      />
      <p>Count: {count}</p>
      <p>Text: {text}</p>
    </div>
  );
}

```

**What happens here:**

* `Button` is wrapped with `React.memo`.
* Without `useCallback`, typing in the input creates a **new `increment` function** → `Button` re-renders every time.
* With `useCallback`, `increment` is stable → `Button` does **not re-render** when input changes. ✅

---

🔹 **Comparison with `useMemo`**

| Hook            | Memoizes                   | Returns              |
| --------------- | -------------------------- | -------------------- |
| `useMemo`     | Value (calculation result) | `memoizedValue`    |
| `useCallback` | Function reference         | `memoizedFunction` |

Think of `useCallback(fn, deps)` as a shortcut for:

```ts
const memoizedFn = useMemo(() => fn, deps);
```

🔹 Common Mistakes
❌ Using useCallback everywhere → can add overhead; only use for stable references needed by children or hooks.

❌ Wrong dependencies → function may have stale closure values. Always include any variables used inside the function.

❌ Confusing useCallback with preventing all re-renders — it only stabilizes the function reference, not the component.

✅ **Rule of thumb:**

* `useCallback` = “Keep the function the same between renders unless dependencies change.”
* Useful for **memoized child components** or  **performance-critical situations** .
* Think of it as  **useMemo for functions** .

## useLayoutEffect

`useLayoutEffect` works almost the same as `useEffect`.

The **difference** is **when it runs** in the React render lifecycle.

👉 **`useEffect`** runs **after paint** (browser paints the screen, then the effect runs asynchronously).

👉 **`useLayoutEffect`** runs  **synchronously after DOM mutations but before the browser paints** .

So:

* `useLayoutEffect` → runs  **right after React updates the DOM** , but before the user actually sees anything.
* `useEffect` → runs  **after the user sees the updated UI** .

---

🔹 **Syntax**

```ts
useLayoutEffect(() => {
  // side effect code (runs synchronously before paint)

  return () => {
    // cleanup runs before next layout effect or on unmount
  };
}, [dependencies]);

```

🔹 **Why is this important?**

Because `useLayoutEffect` lets you **measure the DOM and synchronously make adjustments** before the browser paints.

* If you need to **read layout values** (like element width/height, scroll position, bounding boxes).
* If you need to **apply styles or scroll corrections** to avoid visible flicker.

---

**🔹 Example 1: Measuring an Element’s Size**

```ts
import React, { useLayoutEffect, useRef, useState } from "react";

const Box = () => {
  const boxRef = useRef<HTMLDivElement>(null);
  const [boxWidth, setBoxWidth] = useState(0);

  useLayoutEffect(() => {
    if (boxRef.current) {
      setBoxWidth(boxRef.current.getBoundingClientRect().width);
    }
  }, []);

  return (
    <div>
      <div
        ref={boxRef}
        style={{ width: "200px", height: "100px", background: "lightblue" }}
      >
        Box
      </div>
      <p>Measured width: {boxWidth}px</p>
    </div>
  );
};

export default Box;

```

✔ Here, `useLayoutEffect` ensures we measure the width  **before paint** , so the user won’t see a “flash” where the width is `0` before updating.

**🔹 Example 2: Preventing Flicker with Scroll**

```ts
import React, { useLayoutEffect, useRef } from "react";

const ChatWindow = () => {
  const containerRef = useRef<HTMLDivElement>(null);

  // Always scroll to bottom when messages change
  useLayoutEffect(() => {
    containerRef.current?.scrollTo(0, containerRef.current.scrollHeight);
  });

  return (
    <div
      ref={containerRef}
      style={{ height: "150px", overflowY: "auto", border: "1px solid black" }}
    >
      <p>Message 1</p>
      <p>Message 2</p>
      <p>Message 3</p>
      <p>Message 4</p>
      <p>Message 5</p>
    </div>
  );
};

export default ChatWindow;

```

✔ Using `useLayoutEffect` ensures the scroll jump happens  **before paint** , so the user never sees the wrong scroll position.

**🔹 Key Differences: `useEffect` vs **`b`

| Feature            | `useEffect`                         | `useLayoutEffect`                   |
| ------------------ | ------------------------------------- | ------------------------------------- |
| Runs after paint?  | ✅ Yes                                | ❌ No (before paint)                  |
| Async vs Sync      | Async (non-blocking)                  | Sync (blocking render)                |
| Good for           | Data fetching, subscriptions, logging | DOM measurements, preventing flicker  |
| Performance impact | Lighter (doesn’t block UI)           | Heavier (can block paint if overused) |

🔹 **Rule of Thumb**

* **Default to `useEffect`** → it’s safer, doesn’t block UI.
* Use **`useLayoutEffect` only when you need DOM measurements or synchronous layout adjustments** (like avoiding flickers, scrolling, animations).

## useInsertionEffect

 `useInsertionEffect` is like `useLayoutEffect`, but it’s designed specifically for **inserting styles into the DOM** before any layout calculations or paints happen.

It runs  **synchronously before DOM mutations are flushed** .

This means it happens  **even earlier than `useLayoutEffect`** , giving you a chance to inject styles before the browser starts calculating layout.

👉 In practice, it’s almost never needed unless you are **building a styling library** (like styled-components, emotion, or JSS).

---

**🔹 Syntax**

```ts
useInsertionEffect(() => {
  // insert styles into the DOM here
}, [dependencies]);

```

✔ Just like `useEffect`/`useLayoutEffect`, it supports a cleanup function and dependency array.

**🔹 When to Use It**

* **NOT for normal app code** → React docs explicitly say:
  > “`useInsertionEffect` should only be used by CSS-in-JS libraries to inject styles.”
  >
* Use it if:
  * You are writing a **custom styling system** that dynamically creates CSS rules.
  * You need styles to exist **before layout effects** to prevent  **flash of unstyled content (FOUC)** .

---

**🔹 Example: Injecting Styles**

Here’s a contrived example to show how it works:

```ts
import React, { useInsertionEffect } from "react";

const DynamicStyleBox = ({ color }: { color: string }) => {
  useInsertionEffect(() => {
    const styleTag = document.createElement("style");
    styleTag.innerHTML = `
      .dynamic-box {
        width: 100px;
        height: 100px;
        background-color: ${color};
      }
    `;
    document.head.appendChild(styleTag);

    return () => {
      document.head.removeChild(styleTag);
    };
  }, [color]);

  return <div className="dynamic-box"></div>;
};

export default DynamicStyleBox;

```

✔ Here, the `<style>` is injected into the DOM  **before the browser calculates layout** , so the box shows up styled immediately.

🔹 **Comparison with Other Hooks**

| Hook                   | When it runs                                      | Typical Use                           |
| ---------------------- | ------------------------------------------------- | ------------------------------------- |
| `useEffect`          | After paint                                       | Data fetching, subscriptions, logging |
| `useLayoutEffect`    | After DOM mutations, before paint                 | DOM measurements, scroll adjustments  |
| `useInsertionEffect` | Before DOM mutations are flushed (earliest point) | Injecting CSS to avoid FOUC           |

---

**🔹 Rule of Thumb**

* ✅ Use `useEffect` for almost everything.
* ✅ Use `useLayoutEffect` if you need DOM measurements or sync UI adjustments.
* ⚠️ Use `useInsertionEffect`  **only if you’re building a CSS-in-JS library or handling styles at a very low level** .

## useId

 `useId` is a **React hook for generating unique IDs** that are stable across server and client rendering.

This is especially important for **accessibility attributes** (`id`, `htmlFor`, `aria-*`) and when you need consistent IDs in a component tree.

Unlike generating IDs manually (like using `Math.random()`), `useId` ensures the IDs  **match between SSR (server-side rendering) and CSR (client-side rendering)** , preventing React hydration issues.

---

**🔹 Syntax**

```ts
const id = useId();

```

* Returns a **unique string** (not a number).
* The string is guaranteed to be  **unique within the app** .

---

**🔹 Example 1: Label + Input**

Let’s say you have a form with a label and input. Normally, you’d need an `id` to connect the label to the input with `htmlFor`.

```ts
import { useId } from "react";

export default function NameField() {
  const id = useId();

  return (
    <div>
      <label htmlFor={id}>Name:</label>
      <input id={id} type="text" />
    </div>
  );
}

```

✅ The `label` is linked to the `input` using the **same unique ID** from `useId`.

---

**🔹 Example 2: Multiple Instances**

Each instance of the component gets its  **own unique IDs** , so they don’t collide:

```ts
function EmailField() {
  const id = useId();

  return (
    <div>
      <label htmlFor={id}>Email:</label>
      <input id={id} type="email" />
    </div>
  );
}

export default function Form() {
  return (
    <>
      <EmailField />
      <EmailField />
    </>
  );
}

```

➡️ Each `EmailField` gets a different ID like `:r1:` and `:r2:`, so the labels stay connected to the right input.

---

**🔹 Example 3: Prefixing IDs**

You can combine `useId` with a string if you want to make it more descriptive:

```ts
function Checkbox() {
  const id = useId();

  return (
    <div>
      <input type="checkbox" id={`accept-${id}`} />
      <label htmlFor={`accept-${id}`}>Accept Terms</label>
    </div>
  );
}

```

**🔹 Key Points**

1. ✅ Guarantees  **unique IDs per component** .
2. ✅ Works with **SSR + hydration** without mismatch issues.
3. ✅ Great for **accessibility** (labels, ARIA attributes).
4. ⚠️ Don’t use it for keys in lists — use array indexes or real unique data for that.

---

👉 So in short: `useId` = **React’s built-in way to safely generate unique, stable IDs for accessibility and form elements.**

**My question to understand this:**

* so when creating inputs and etc for forms you should be using this instead of creating your own because its more efficient?

**Response:**

Good question 👍

Not exactly because of  *efficiency in performance* , but because of  **correctness and accessibility** . Let’s break it down:

---

**Why `useId` is useful in forms**

* **Unique IDs**

  * In HTML, labels and inputs are linked by `for` (or `htmlFor` in React) and `id`.
  * If you hardcode IDs like `"username"`, `"email"`, etc., and then render multiple copies of that form (like inside a list or modal), you’ll have  **duplicate IDs** , which is invalid HTML and breaks accessibility.

  ```ts
  <label htmlFor="username">Username</label>
  <input id="username" />

  ```

  If you render this twice, both inputs share the same `"username"` ID → 🚫 bad.
* **Server + Client consistency**

  * In SSR (Next.js, Remix, etc.), `useId` guarantees the same ID is generated on the server and the client.
  * If you generate random IDs yourself (like with `Math.random()`), React will throw hydration warnings.
* **Accessibility**

  * Screen readers rely on these unique IDs to correctly associate labels, inputs, error messages, and descriptions.
  * Using `useId` ensures your form is  **accessible by default** .

**Example with `useId`**

```ts
import { useId } from "react";

function LoginForm() {
  const usernameId = useId();
  const passwordId = useId();

  return (
    <form>
      <div>
        <label htmlFor={usernameId}>Username</label>
        <input id={usernameId} type="text" />
      </div>

      <div>
        <label htmlFor={passwordId}>Password</label>
        <input id={passwordId} type="password" />
      </div>
    </form>
  );
}

```

✔ Each render has unique IDs.

✔ Multiple `<LoginForm />` instances won’t conflict.

✔ Accessible and SSR-safe.

✅ So to answer your question:

Yes — for **inputs, forms, and anything needing unique `id` attributes** (labels, aria-describedby, error messages, etc.), you should use `useId` instead of manually hardcoding or generating your own IDs.

## useTransition

**The Problem It Solves**

Normally in React,  **all state updates are treated as urgent** .

* Example: typing into an input or clicking a button → React rerenders immediately.
* But sometimes, updates are **slow** (e.g., filtering a big list, rendering charts, or fetching data).
* If React treats these as urgent, the UI can **feel laggy** — typing freezes, clicks are delayed.

👉 `useTransition` helps separate **urgent updates** (like typing) from **non-urgent updates** (like filtering a big list).

**What `useTransition` Does**

* It lets you mark a state update as **“non-urgent”** (called a  **transition** ).
* Urgent updates (like typing) happen right away.
* Transition updates (like rendering a large list) can  **wait until React is less busy** , so the UI stays responsive.

**The Syntax**

```ts
const [isPending, startTransition] = useTransition();
```

* `isPending` → `true` while the transition update is running (good for showing a spinner/loader).
* `startTransition` → a function you wrap around non-urgent updates.

**Example: Without vs With** `b`

❌ Without `useTransition` (laggy UI)

```ts
function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  function handleChange(e) {
    setQuery(e.target.value);
    // Big expensive update
    setResults(expensiveSearch(e.target.value));
  }

  return (
    <>
      <input value={query} onChange={handleChange} />
      <ResultsList items={results} />
    </>
  );
}

```

Typing into the input feels **slow** if `expensiveSearch` is heavy.

---

✅ With `useTransition` (smooth UI)

```TS
function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [isPending, startTransition] = useTransition();

  function handleChange(e) {
    const value = e.target.value;
    setQuery(value); // urgent → update input immediately

    startTransition(() => {
      // non-urgent → can be delayed
      setResults(expensiveSearch(value));
    });
  }

  return (
    <>
      <input value={query} onChange={handleChange} />
      {isPending && <p>Loading results...</p>}
      <ResultsList items={results} />
    </>
  );
}

```

* Typing stays fast (React updates the input immediately).
* The expensive search updates in the background.
* `isPending` lets you show “Loading…” while React updates results.

**When to Use `useTransition`**

Use it when you have:

* ✅ Large lists or expensive calculations after a state change.
* ✅ Slow updates that make the UI lag.
* ✅ Data fetching (filter, search, sort, pagination).
* ✅ Smooth user experiences where “instant feedback” matters (typing, clicking).

❌ Don’t use it for everything — only when performance or responsiveness is an issue.

Analogy

Think of React updates as  **lines at a grocery store** :

* Urgent updates (like typing) = “express checkout lane.”
* Non-urgent updates (like filtering a big list) = “big shopping cart lane.”

  `useTransition` makes sure express checkout customers (urgent updates) don’t get stuck behind giant carts.

👉 **So in short:**

`useTransition` = **Keep UI snappy by telling React which updates can wait.**

## useDeferredValue

`useDeferredValue` is a React Hook that lets you **defer updating a value** until React has time.

* You give it a value (like search text).
* React immediately gives you back a **deferred version** of that value.
* The deferred value may "lag behind" temporarily, while React prioritizes more urgent updates.

Think of it as saying:

👉 “This value isn’t urgent. Update it *later* when React is free.”

---

**🔹 Syntax**

```ts
const deferredValue = useDeferredValue(value);
```

* `value` → the value you want to “slow down.”
* `deferredValue` → a lagging copy of `value` that updates later.

**🔹 Example: Search Input + Heavy List**

```ts
import React, { useState, useDeferredValue } from "react";

export default function SearchApp() {
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query); // lagging version of query

  const items = Array.from({ length: 5000 }, (_, i) => `Item ${i + 1}`);

  // Only filter with deferredQuery (not the live query)
  const filteredItems = items.filter(item =>
    item.toLowerCase().includes(deferredQuery.toLowerCase())
  );

  return (
    <div>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <p>Typing: {query}</p>
      <p>Filtering with: {deferredQuery}</p>

      <ul>
        {filteredItems.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

```

**What Happens Here?**

* **`query`** updates immediately → so typing feels instant.
* **`deferredQuery`** lags behind → React takes its time to update it, avoiding UI freezes while filtering thousands of items.
* The UI feels  **responsive** , even if filtering is slow.

---

**🔹 Difference Between `useDeferredValue` and `useTransition`**

| Feature | `useTransition`                                  | `useDeferredValue`                                 |
| ------- | -------------------------------------------------- | ---------------------------------------------------- |
| Usage   | Wraps state updates in `startTransition`         | Wraps a value directly                               |
| Control | Lets you decide which updates are “low priority” | Lets React decide when to update the deferred value  |
| Example | Updating a big list when search changes            | Filtering with a lagging version of the search input |

👉 You often use `useDeferredValue` **inside child components** that receive props, while `useTransition` is more about  **marking updates as low-priority at the source** .

---

✅  **Summary** :

* `useDeferredValue` = gives you a lagging copy of a value so expensive renders don’t block urgent updates.
* Best used in  **search inputs, autocomplete, live filters, or any situation where input speed matters but rendering can wait** .

## useSyncExternalStore

**🔹What is `useSyncExternalStore`?**

* It’s a hook designed to let React components  **safely read from an external store** .
* Unlike `useState` or `useReducer`, which store data inside React, this is for when your data **lives outside React** (e.g., Redux store, localStorage, global event listeners).
* It ensures React components stay  **consistent across concurrent renders** , which wasn’t always guaranteed with older hacks like `useEffect` subscriptions.

---

🔹**Syntax**

```ts
const state = useSyncExternalStore(
  subscribe,       // How to subscribe to the store (e.g., addEventListener)
  getSnapshot,     // How to read the current value from the store
  getServerSnapshot? // (optional) for SSR, what value to use on the server
);

```

* **`subscribe`** : A function that tells React how to listen for changes.
* **`getSnapshot`** : A function that returns the current value of the store.
* **`getServerSnapshot`** : (optional) Used for server-side rendering fallback.

**🔹Example 1: Window Resize Listener**

Imagine you want your component to re-render when the window is resized:

```ts
import React, { useSyncExternalStore } from "react";

function useWindowWidth() {
  return useSyncExternalStore(
    // Subscribe: tell React how to listen for changes
    (callback) => {
      window.addEventListener("resize", callback);
      return () => window.removeEventListener("resize", callback);
    },
    // Get snapshot: read current value
    () => window.innerWidth,
    // Server snapshot (for SSR)
    () => 1024
  );
}

export default function App() {
  const width = useWindowWidth();

  return <h1>Window width: {width}px</h1>;
}

```

✅ Every time the window resizes, React re-renders with the new width.

**🔹Example 2: Reading From a Global Store (like Redux-lite)**

```ts
// Fake store
let store = { count: 0 };
let listeners: (() => void)[] = [];

function increment() {
  store.count++;
  listeners.forEach((l) => l());
}

function subscribe(callback: () => void) {
  listeners.push(callback);
  return () => {
    listeners = listeners.filter((l) => l !== callback);
  };
}

function getSnapshot() {
  return store.count;
}

export default function Counter() {
  const count = useSyncExternalStore(subscribe, getSnapshot);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}

```

✅ `useSyncExternalStore` ensures the count is always consistent with React’s concurrent rendering.

---

**When to Use It**

* ✅ When working with **external state** (Redux, Zustand, MobX, browser APIs).
* ✅ When you need **safe concurrent rendering** (no tearing / inconsistent UI).
* ❌ Not needed for regular component state (`useState`, `useReducer` are better).

---

**👉 In short:**

`useSyncExternalStore` is the **official React way** to subscribe to external stores safely, especially in concurrent React (React 18+).

## React Hooks Cheat Sheet

| Hook                           | What it Does                                         | When to Use                                          | Common Mistakes / Notes                                                           |
| ------------------------------ | ---------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------- |
| **useState**             | Stores state in a component                          | Any component state that changes over time           | Don’t directly mutate state; always use setter                                   |
| **useEffect**            | Runs side effects after render                       | Data fetching, subscriptions, timers, DOM updates    | Avoid missing dependency array; can cause infinite loops                          |
| **useContext**           | Access context value                                 | When you need shared state across components         | Don’t overuse context for every piece of state; can cause unnecessary re-renders |
| **useReducer**           | Manages complex state with reducer pattern           | Complex state logic, forms, counters                 | Don’t forget to return new state object; immutable updates only                  |
| **useRef**               | Holds mutable values or DOM refs                     | Access DOM elements, store timers, persistent values | Mutating `.current`doesn’t trigger re-render                                   |
| **useMemo**              | Memoizes expensive calculations                      | Heavy computations, derived state                    | Don’t overuse; use only when performance matters                                 |
| **useCallback**          | Memoizes function references                         | Pass functions to children to prevent re-renders     | Only necessary if child components rely on reference equality                     |
| **useLayoutEffect**      | Runs synchronously after DOM mutations, before paint | Measure DOM elements, avoid layout flicker           | Blocking render if overused; usually `useEffect`is enough                       |
| **useImperativeHandle**  | Customize ref value exposed to parent                | Wrapping child components, exposing specific methods | Don’t overuse; breaks declarative model if misused                               |
| **useDebugValue**        | Adds labels in React DevTools for custom hooks       | Custom hooks                                         | Doesn’t affect behavior; purely for dev tools                                    |
| **useTransition**        | Marks state updates as non-urgent                    | Large lists, filtering, slow rendering               | Don’t mark urgent updates; use for background rendering                          |
| **useDeferredValue**     | Provides a lagging version of a value                | Filtering, autocomplete, UI smoothing                | Only useful when rendering heavy components                                       |
| **useId**                | Generates unique IDs                                 | Form elements, accessibility, SSR-safe IDs           | Don’t use for keys in lists; IDs only                                            |
| **useSyncExternalStore** | Subscribes to external stores safely                 | Zustand, Redux, custom stores                        | Not needed for local state; only for external state                               |
| **useInsertionEffect**   | Injects styles into DOM before paint                 | CSS-in-JS libraries                                  | Very rare for app developers; avoid for normal components                         |

# Local vs Global State Managment

**What is state management?**

State Management is how your application **stores, updates, and sharess data** that determines how it behaves and what the user sees.

Key Concepts

* **Application State:**

  * Data the determines the nehavior and apperance of your application
  * Example:
    * whether a modal is open
    * what page is selectec
    * form inputs
    * etc.
* **Shared Data:**

  * Data that multiple components nee to read or update
  * Example:
    * current user information
    * theme
    * shopping cart items


**Local State**

* **Managed inside a component** using `useState` or `useReducer`.
* **Scope:** only the component itself (or its children if passed via props).
* **When to use:**
  * Form inputs
  * Toggle buttons
  * Component-specific UI state

**Example: Local state with `useState`**

```ts
funtion Counter() {
    const [count, setCount] = useState(0);

     return (
          <div>
               <p>Count: {count}</p>
               <button onClick={() => setCount(count + 1)}> Increment </button>
          </div>
     );
}
```

✅ Simple, fast, and does not require extra libraries


**Global State**

* **Managed outside of a single component** and can be accessed by multiple components.
* **Scope:** entire app (or a large part of it).
* **When to use:**

  * User authentication info
  * Theme (dark/light mode)
  * Shopping cart
  * Data fetched from API shared across pages


Different State Libraries

| Library               | Approach            | Key Concepts                         | Best Use Case                                                            |
| --------------------- | ------------------- | ------------------------------------ | ------------------------------------------------------------------------ |
| **Redux**       | Flux pattern        | Actions, Reducers, Store             | Large apps with complex state logic, predictable updates                 |
| **Zustand**     | Minimal, hook-based | Store, setState                      | Medium apps, simpler syntax, easy integration                            |
| **Context API** | React built-in      | Provider, useContext                 | Sharing simple state, theming, auth info, small-medium apps              |
| **MobX**        | Observable-based    | Observable state, actions, reactions | Apps that benefit from automatic reactivity, less boilerplate than Redux |

**When to Use Each**

**Local State**

* Use for  **isolated, component-specific state** .
* Avoid putting **global state** here to prevent “prop drilling” (passing props multiple levels).

**Context API**

* Use for  **lightweight global state** .
* Best for **themes, auth, settings** — not for frequent updates of large data.

**Zustand**

* Simple, minimalistic global state.
* Great when you want  **global state without Redux boilerplate** .

**Redux**

* Use for **large, complex apps** with multiple sources of truth.
* Predictable state updates via  **actions and reducers** .
* Works well with DevTools and middleware.

**MobX**

* Reactive, less boilerplate than Redux.
* Best when you want  **automatic updates without manually dispatching actions** .


**Key Takeaways**

* **Local state** : simple, component-specific, use `useState` or `useReducer`.
* **Global state** : needed when multiple components rely on the same data.
* **Choose the right tool** :
* Simple sharing → Context API
* Minimal but global → Zustand
* Large & complex → Redux
* Reactive & automatic → MobX
* Avoid overcomplicating —  **don’t use global state if local state suffices** .
* Keep state  **predictable, minimal, and maintainable**


# Controlled vs Uncontrolled 

When working with **form inputs** in React, it’s important to understand  **how the component’s value is managed** .

---

**Controlled Components**

A controlled component is a form element whose  **value is fully controlled by React state** . The React component  **owns the state** , and the form input reflects that state.

**Key Points:**

* React state is the  **single source of truth** .
* Any change to the input must update the state via `onChange`.
* Useful when you want  **immediate validation, conditional UI, or form submission handling** .

**Example: Controlled Input**

```ts
import React, { useState } from "react";

function ControlledInput() {
  const [name, setName] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setName(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    alert(`Submitted name: ${name}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={name} onChange={handleChange} />
      <button type="submit">Submit</button>
    </form>
  );
}

```

✅ Behavior:

* `value={name}` ensures the input always shows the latest React state.
* Typing triggers `onChange` → updates React state → input updates.

**Advantages:**

* Easy validation, formatting, or conditional logic.
* React always “knows” the current value.

**Disadvantages:**

* Slightly more code.
* Re-renders on every keystroke (usually negligible).

---

**Uncontrolled Components**

An uncontrolled component is a form element whose  **value is managed by the DOM itself** , not by React state. React only reads the value **when needed** (e.g., on form submission).

**Key Points:**

* Uses **refs** (`useRef`) to access the DOM element’s current value.
* React does not control input updates; the DOM does.

**Example: Uncontrolled Input**

```ts
import React, { useRef } from "react";

function UncontrolledInput() {
  const inputRef = useRef<HTMLInputElement>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    alert(`Submitted name: ${inputRef.current?.value}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" ref={inputRef} />
      <button type="submit">Submit</button>
    </form>
  );
}

```

✅ Behavior:

* Input manages its own value internally.
* React only reads value via `ref` when needed.

**Advantages:**

* Less code for simple forms.
* No re-render on every keystroke.

**Disadvantages:**

* Harder to do  **validation or dynamic updates** .
* React “doesn’t know” the value until you query the ref.

---

**Key Differences**

| Aspect          | Controlled                 | Uncontrolled                               |
| --------------- | -------------------------- | ------------------------------------------ |
| State Ownership | React                      | DOM                                        |
| Value Prop      | `value`+`onChange`     | `defaultValue`or none                    |
| Access          | Always via state           | via `ref`when needed                     |
| Validation      | Easy, immediate            | Needs manual check                         |
| Re-render       | Every change updates React | Only updates DOM, React doesn’t re-render |

---

**When to Use Which**

* **Controlled** → forms that need: validation, formatting, conditional behavior, or dynamic UI.
* **Uncontrolled** → simple forms, quick demos, or when performance is critical and React state isn’t needed.

---

✅ **Notes:**

* **Controlled** = React controls everything.
* **Uncontrolled** = DOM controls the input; React just reads the value when needed.


# Keys in lists

**What are keys in React?**

In React, **keys** are special strings (or numbers) that you assign to elements in a list. They help React **identify which items have changed, been added, or removed** when rendering lists.

**Example:**

```ts
const users = ["Alice", "Bob", "Charlie"];

function UserList() {
  return (
    <ul>
      {users.map((user, index) => (
        <li key={index}>{user}</li>
      ))}
    </ul>
  );
}

```

Here, `key={index}` gives each `<li>` a unique identifier.

---

**Why React needs keys**

React uses a **Virtual DOM** to decide how to update the actual DOM efficiently. When a list changes:

1. React compares the **previous list** with the  **new list** .
2. Keys allow React to  **match elements between renders** .
3. Without keys (or with non-unique keys), React might:
   * Re-render the entire list unnecessarily
   * Lose the state of components (like input fields)

**Example problem without keys:**

```ts
const items = ["A", "B", "C"];
```

If we remove `"B"` and render `["A", "C"]`  **without keys** , React might:

* Remove `"A"` and `"B"` and create a new `"A"` and `"C"`, losing any internal state in those components.

---

**Rules for keys**

1. **Keys must be unique among siblings**
   * They don’t need to be globally unique.
2. **Avoid using array index as key** (unless list is static and won’t change order)
   * Using indexes can lead to bugs if the list is reordered or items are added/removed.
3. **Use a stable identifier if possible**
   * e.g., `user.id` instead of `index`.

**Better example:**

```ts
const users = [
  { id: 101, name: "Alice" },
  { id: 102, name: "Bob" },
  { id: 103, name: "Charlie" }
];

users.map(user => <li key={user.id}>{user.name}</li>);

```

---

**4️⃣** **Summary / Why it matters**

* **Keys tell React which items are which**
* **They help React update the DOM efficiently**
* **Using stable, unique keys avoids bugs with component state**
* Essential in **dynamic lists** (adding, removing, reordering)

---

💡 **Analogy:**

Think of keys like  **name tags at a party** . If someone leaves and a new person comes, the name tag lets the host know  **who’s who** , instead of guessing.


# Error Boundaries

**What is an Error Boundary?**

An **Error Boundary** is a  **React component that catches JavaScript errors anywhere in its child component tree** , logs those errors, and displays a fallback UI instead of crashing the entire app.

> Essentially, it’s React’s way of **gracefully handling runtime errors during rendering, lifecycle methods, and constructors** of child components.

---

**When to use Error Boundaries?**

Error Boundaries  **only catch errors in** :

* Render phase of child components
* Lifecycle methods of child components (e.g., `componentDidMount`, `componentDidUpdate`)
* Constructors of child components

They  **do not catch** :

* Errors inside event handlers
* Asynchronous code (e.g., `setTimeout`, `fetch`)
* Server-side rendering errors

---

**How to create an Error Boundary**

Error Boundaries are **class components** that implement  **two lifecycle methods** :

1. `static getDerivedStateFromError(error)` → updates state to render fallback UI
2. `componentDidCatch(error, info)` → logs error details

**Example:**

```ts
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render shows fallback UI
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    // You can log the error to an external service
    console.error("Error caught:", error, info);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}

```

**Usage:**

```ts
<ErrorBoundary>
  <MyComponent />
</ErrorBoundary>
```

* If `MyComponent` throws an error while rendering, the user sees **"Something went wrong."**
* The rest of the app continues to function normally.

---

**Why Error Boundaries matter**

1. **User experience:** Prevents the entire app from crashing
2. **Debugging:** Provides a place to log errors to monitoring tools (Sentry, LogRocket)
3. **Reliability:** Allows you to isolate problematic components

---

**Tips / Best Practices**

* Use Error Boundaries  **around sections of your UI** , not necessarily the whole app
* Combine with **fallback UI** that guides users to retry or navigate elsewhere
* You **cannot catch every error** — combine with proper unit/integration tests

---

💡 **Analogy:**

Think of an Error Boundary like a  **safety net under a tightrope walker** . If they slip (component crashes), the net catches them instead of letting them fall all the way down (crash the app).


# Important Additionals

## Unary plus operator

**What it is?**

* A **unary operator** means it works with  **only one operand** .
* The `+` operator converts its operand **into a number** (if it isn’t already).
* Syntax:

```ts
+operand
```

---

**Examples:**

**Strings to numbers**

```ts
const str = "42";
console.log(+str); // 42
console.log(typeof +str); // "number"

```

**Boolean to numbers**

```ts
console.log(+true);  // 1
console.log(+false); // 0
```

**Null and undefined**

```TS
console.log(+null);      // 0
console.log(+undefined); // NaN
```

**Already a number**

```TS
const num = 10;
console.log(+num); // 10 (no change)
```

**Non-numeric string**

```ts
console.log(+"hello"); // NaN
```

---

**Why use it**

* Fastest way to **convert a value to a number** in JavaScript.
* Commonly used in React when reading  **numeric input values** , because HTML inputs always return strings:

```
<input type="number" onChange={(e) => setCount(+e.target.value)} />
```

---

**Comparison to other methods**

| Method         | Example                | Result        |
| -------------- | ---------------------- | ------------- |
| Unary `+`    | `+ "42"`             | 42 (number)   |
| `Number()`   | `Number("42")`       | 42 (number)   |
| `parseInt`   | `parseInt("42")`     | 42 (number)   |
| `parseFloat` | `parseFloat("42.5")` | 42.5 (number) |

✅ `+` is short and clean, especially for inline conversions like in `onChange`.

---

**Quick tip**

* Use unary `+` for simple conversions.
* Use `Number()` if you want **explicit readability** in code.
* Avoid `parseInt` unless you specifically need integer parsing.

```ts
onChange={(e) => setNumber(+e.target.value)}
```

* `e.target.value` → always a  **string** , because HTML input elements always return values as strings.

  * Example: typing `5` in a number input gives `"5"`, not `5`.
* `+e.target.value` → **unary plus operator** converts the string into a number.

**Example:**

```ts
const value = "42";
console.log(typeof value); // "string"

const numberValue = +value;
console.log(numberValue); // 42
console.log(typeof numberValue); // "number"
```

**Example (Input):**

```ts
<input type="number" value={number} onChange={(e) => setNumber(+e.target.value)} />
```
