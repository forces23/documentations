# Unit Testing in JS/TS

---

## what is Unit testing?

Form of automated testing where we write code to check if our code works as expected.

## what are the benefits of untit testing?

helps fix bugs early in the development process, since we can test everything after making a change.

* Detects Bugs Early
* Facilitates Refactoring
* Improves Code Quality
* Documentation

## Types of Test

### Unit Tests

verify the correctness of individual units or components of an application in issloation.

* These units could be :
  * functions
  * classes
  * small modules

Unit Test help catch bugs early in the development process

### Integration Tests

Focus on verifing how different units or components of your application work together as a whole

* help identify issues that might arise when combining different units such as:
  * data flow problems
  * communication between modules
  * compatibility issues between components and

### End-to-End Tests

the broadest type, focusing on testing the entire application as a whole by simulating real user interactions with the entire system from the user interface  to the backend services.

## Testing Frameworks

* Jest
  * most widely adopted
  * Experimental support for ECMAScript Modules
* Mocha
* Jasmin
* Vitest
  * used for modern JS
  * Supports ESM, Typescript, and JSX
* Cypress
* Playwright

## Test Patterns

### AAA

* Arrange
  * set up test env including any necsessay data or configurations
* Act
  * perform the action we want to test
* Assert
  * check the outcome to make sure that it matches expectations

Example :

Testing if a tv will turn off

    Arrange: turn on the tv
	Act: Press the power button
	Assert: verify if TV is off

```javascript
//intro.js
export function max(a, b) {
  if (a > b) return a;
  else if (b > a) return b;
  return a;
}


//intro.test.js
describe("max", ()=>{
    it("should return the first arg if it is greater", () =>{
        // --- AAA pattern ---
        // Arrange
        const a = 2;
        const b = 1;

        // Act
        const result = max(a,b);
  
        // Assert
        expect(result).toBe(2);
    })
})

// Can be simplified to 
describe("max", ()=>{
    it("should return the first arg if it is greater", () =>{
        expect(max(2,1)).toBe(2);
    })
})
```

## Two Ways to Write Test

* Code First
  * write the code then cover it with test
* Test First
  * create the test first then write the code
  * also known as TDD(Test-driven Development)

## Test-driven Development (TDD)

* start by writing a failing test
* Write just enough code to make the test pass
* Refactor if necessary

Benefits:

1. Functions are fully covered by test
2. If implementation is not complete we can add other test cases to drive development
3. prevents from over engineering  because focus is on writing the simplest logic to pass the test cases

Cons:

1. can be difficult especially for new learners

## Vitest

to get vitest installed into your project run this sript in the terminal :

```bash
npm i -D vitest
```

after the installtion is finished you need to go to `package.json` and add a test script in the scripts section

```json
{
  "name": "javascript-testing",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "test" : "vitest", // here is what should be added
    "test:ui" : "vitest --ui" // (optional) here is what should be added
    // vitest --ui give you a very nice web based visual for your testing which is easier to look at then the terminal based vitest
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "vitest": "^3.1.4"
  },
  "dependencies": {
    "delay": "^6.0.0"
  }
}
```

## Helpful Extenions

1. Vitest Snippets -- Dein Software
   * allows you to quickly import most used lines of code when dealing with vitest testing
2. Testing Library Snippets
   * VS Code Testing Library snippets for JS and TS
3. React Testing Library - Quick Debug
   * Makes debugging in react testing library a cinch!

## Start Writing Test

create a folder in the root folder of where src is located

within that folder create a file in this naming convention

```bash
file-name.test.js
```

Note: notice the `.test.js` the file must end with this syntax for vitest to recognize that it is a test file

## Functions Used From Vitest

### describe()

Vitest's `describe()` is a powerful function for **organizing your tests** into logical groups. It helps structure your test suite, making it more readable and maintainable.

#### **What is `describe()`?**

* A **grouping function** that bundles related test cases (`test()` or `it()` blocks).
* Helps **categorize tests** (e.g., by feature, component, or scenario).
* Supports **nested `describe()` blocks** for hierarchical structuring.

#### **Basic Syntax**

```javascript
import { describe, test, expect } from 'vitest';

describe('Test Group Name', () => {
  test('Test Case 1', () => {
    expect(1 + 1).toBe(2);
  });

  test('Test Case 2', () => {
    expect('hello').toMatch('hello');
  });
});
```

#### **Key Features**

##### **✅ Nested `describe()` for Hierarchical Tests**

```javascript
describe('User Authentication', () => {
  describe('Login', () => {
    test('should return a token on success', () => { /* ... */ });
    test('should reject invalid credentials', () => { /* ... */ });
  });

  describe('Logout', () => {
    test('should clear the session', () => { /* ... */ });
  });
});
```

##### **✅ `describe.skip()` – Skip a Test Group**

```javascript
describe.skip('Legacy Feature (Deprecated)', () => {
  test('old test', () => { /* Won't run */ });
});
```

##### **✅ `describe.only()` – Run Only This Group**

```javascript
describe.only('Critical Feature', () => {
  test('must pass', () => { /* Only this runs */ });
});
```

##### **✅ `describe.concurrent()` – Parallel Execution**

```javascript
describe.concurrent('API Tests (Parallel)', () => {
  test('fetch user', async () => { /* ... */ });
  test('fetch posts', async () => { /* ... */ });
});
```

#### **Best Practices**

1. **Group by Feature/Component**

   ```javascript
   describe('ShoppingCart', () => { ... });
   describe('UserProfile', () => { ... });
   ```
2. **Use Clear, Descriptive Names**
   ❌ `describe('Test 1', ...)`
   ✅ `describe('User Login Validation', ...)`
3. **Avoid Deep Nesting (Max 2-3 levels)**

   ```javascript
   describe('User', () => {
     describe('Authentication', () => {
       describe('Login', () => { /* ... */ }); // ❌ Too deep!
     });
   });
   ```
4. **Combine with `beforeEach`/`afterEach` for Setup**

   ```javascript
   describe('Database', () => {
     beforeEach(() => setupDB());
     afterEach(() => clearDB());

     test('insert record', () => { ... });
   });
   ```

#### Real-World Example

```javascript
import { describe, test, expect } from 'vitest';

describe('Math Utilities', () => {
  describe('add()', () => {
    test('should add two numbers', () => {
      expect(add(2, 3)).toBe(5);
    });

    test('should handle negative numbers', () => {
      expect(add(-1, 5)).toBe(4);
    });
  });

  describe('subtract()', () => {
    test('should subtract two numbers', () => {
      expect(subtract(5, 2)).toBe(3);
    });
  });
});
```

---

### test()

Vitest's `test()` function (also available as `it()`) is the **core building block** for writing individual test cases. It lets you define what behavior you're testing and how to verify it.

#### **What is `test()`?**

* Defines a  **single test case** .
* Accepts:
  * A **description** (string explaining the test).
  * A **function** containing the test logic.
* Works with **assertions** (`expect`) to verify outcomes.

#### **Basic Syntax**

```javascript
import { test, expect } from 'vitest';

test('should add two numbers', () => {
  expect(1 + 1).toBe(2);
});
```

*(Equivalent to `it()` – both work the same way.)*

#### **Key Features**

##### **✅ Basic Test**

```javascript
test('returns true when input is valid', () => {
  const result = validateInput('hello');
  expect(result).toBe(true);
});
```

##### **✅ Async/Await Support**

```javascript
test('fetches user data', async () => {
  const user = await fetchUser(1);
  expect(user).toHaveProperty('name');
});
```

##### **✅ Test Lifecycle (Hooks)**

```javascript
beforeEach(() => setupTestDatabase()); // Runs before each test
afterEach(() => clearTestDatabase());  // Runs after each test

test('database inserts a record', () => {
  insertRecord({ id: 1 });
  expect(getRecord(1)).toBeDefined();
});
```

##### **✅ `test.skip()` – Skip a Test**

```javascript
test.skip('legacy feature (deprecated)', () => {
  // Won't run
});
```

##### **✅ `test.only()` – Run Only This Test**

```javascript
test.only('critical fix verification', () => {
  // Only this test runs
});
```

##### **✅ `test.concurrent()` – Parallel Execution**

```javascript
test.concurrent('API call 1', async () => { /* ... */ });
test.concurrent('API call 2', async () => { /* ... */ });
```

##### **✅ `test.todo()` – Mark a Test for Later**

```javascript
test.todo('implement error handling');
```

#### **Best Practices**

1. **Descriptive Test Names**
   ❌ `test('works', ...)`
   ✅ `test('returns HTTP 404 if user does not exist', ...)`
2. **One Assertion Per Test (When Possible)**

   ```javascript
   // ❌ Avoid
   test('validates user', () => {
     expect(validate('alice')).toBe(true);
     expect(validate('')).toBe(false);
   });

   // ✅ Better (split into two tests)
   test('accepts valid username', () => {
     expect(validate('alice')).toBe(true);
   });

   test('rejects empty username', () => {
     expect(validate('')).toBe(false);
   });
   ```
3. **Use `expect` for Assertions**

   ```javascript
   test('sums numbers', () => {
     expect(add(2, 3)).toBe(5);       // Exact value
     expect([1, 2]).toContain(2);    // Array check
     expect({ a: 1 }).toEqual({ a: 1 }); // Deep equality
   });
   ```
4. **Keep Tests Isolated**

   * Avoid sharing state between tests.
   * Use `beforeEach`/`afterEach` for cleanup.

#### **Real-World Example**

```javascript
import { test, expect } from 'vitest';

function divide(a, b) {
  if (b === 0) throw new Error('Cannot divide by zero');
  return a / b;
}

describe('divide()', () => {
  test('divides two numbers', () => {
    expect(divide(10, 2)).toBe(5);
  });

  test('throws error when dividing by zero', () => {
    expect(() => divide(10, 0)).toThrow('Cannot divide by zero');
  });
});
```

### it()

`it()` is simply an alias for `test()` in Vitest (and other testing frameworks like Jest). It follows the **Behavior-Driven Development (BDD)** style, making tests read like natural language specifications.

#### **What is `it()`?**

* **Same as `test()`** - Just a different name
* Makes tests read like English:
  `"it should do something..."`
  (More expressive than `"test that..."`)
* Uses the exact same features as `test()`

#### **Basic Syntax**

```javascript
import { it, expect } from 'vitest';

it('should add two numbers', () => {
  expect(1 + 1).toBe(2);
});
```

#### **Key Features (Same as `test()`)**

##### **✅ Basic Test**

```javascript
it('returns true for valid input', () => {
  expect(validate('hello')).toBe(true);
});
```

##### **✅ Async Tests**

```javascript
it('fetches user data', async () => {
  const user = await fetchUser(1);
  expect(user).toHaveProperty('name');
});
```

##### **✅ Lifecycle Hooks**

```javascript
beforeEach(() => setupTest());
afterEach(() => cleanupTest());

it('works with fresh state', () => {
  expect(getState()).toBe('clean');
});
```

##### **✅ Skipping/Isolating Tests**

```javascript
it.skip('legacy test', () => { /* skipped */ });
it.only('critical test', () => { /* only this runs */ });
it.todo('needs implementation');
```

##### **✅ Concurrent Tests**

```javascri[t
it.concurrent('handles API call 1', async () => { /* ... */ });
it.concurrent('handles API call 2', async () => { /* ... */ });
```

#### **`it()` vs `test()`**

| Feature                 | `it()`           | `test()`          |
| ----------------------- | ------------------ | ------------------- |
| **Alias**         | Yes                | Original name       |
| **BDD Style**     | `"it should..."` | `"test that..."`  |
| **Functionality** | Identical          | Identical           |
| **Preference**    | Teams using BDD    | Traditional testing |

#### **Best Practices**

1. **Use Descriptive Names**

   ```javascript
   // ❌ Bad
   it('works', () => { ... });

   // ✅ Good (reads like a spec)
   it('should return 404 if user not found', () => { ... });
   ```
2. **Follow BDD Style**
   Start descriptions with:

   * `"should..."`
   * `"must..."`
   * `"will..."`
3. **Keep Tests Focused**

   ```javascript
   // ❌ Tests too much
   it('handles user login', () => {
     expect(validate('user')).toBe(true);
     expect(login('user')).toBeTruthy();
     expect(getSession()).toBeActive();
   });

   // ✅ Better (split into multiple tests)
   it('should validate username format', () => { ... });
   it('should log in with valid credentials', () => { ... });
   it('should create a session on login', () => { ... });
   ```

#### **Real-World Example**

```javascript
import { it, expect } from 'vitest';

function isEven(num) {
  return num % 2 === 0;
}

describe('isEven()', () => {
  it('should return true for even numbers', () => {
    expect(isEven(2)).toBe(true);
  });

  it('should return false for odd numbers', () => {
    expect(isEven(3)).toBe(false);
  });

  it.todo('should handle edge cases');
});
```

### expect()

`expect()` is Vitest's assertion library for verifying test outcomes. It provides a rich set of matchers to validate different types of values and behaviors.

#### **1. Basic Structure**

```javascript
expect(actualValue).matcher(expectedValue)
```

#### **2. Common Matchers**

##### **Equality Checks**

```javascript
expect(2 + 2).toBe(4) // Strict equality (===)
expect({a: 1}).toEqual({a: 1}) // Deep equality
expect([]).not.toBe([]) // Different references
```

##### **Truthiness**

```javascript
expect('').toBeFalsy()
expect(1).toBeTruthy()
expect(null).toBeNull()
expect(undefined).toBeUndefined()
expect(value).toBeDefined()
```

##### **Numbers**

```javascript
expect(10).toBeGreaterThan(5)
expect(10).toBeGreaterThanOrEqual(10)
expect(5).toBeLessThan(10)
expect(3.14159).toBeCloseTo(3.14, 2) // 2 decimal places
```

##### **Strings**

```javascript
expect('hello').toMatch(/^hel/)
expect('hello').toContain('ell')
expect('HELLO').toEqual(expect.stringContaining('ell'))
```

##### **Arrays & Objects**

```javascripts
expect([1, 2, 3]).toContain(2)
expect([1, 2, 3]).toHaveLength(3)
expect({a: 1, b: 2}).toHaveProperty('a')
expect({a: 1, b: 2}).toMatchObject({a: 1})
```

##### **Exceptions**

```javascript
expect(() => throwError()).toThrow()
expect(() => throwError()).toThrow('Specific message')
expect(() => throwError()).toThrow(ErrorType)
```

##### **Async/Promises**

```javascript
await expect(Promise.resolve(1)).resolves.toBe(1)
await expect(Promise.reject('error')).rejects.toMatch('error')
```

##### **Mock Functions**

```javascript
const mockFn = vi.fn()
mockFn('arg')
expect(mockFn).toHaveBeenCalled()
expect(mockFn).toHaveBeenCalledWith('arg')
expect(mockFn).toHaveBeenCalledTimes(1)
```

#### **Custom Matchers**

```javascript
expect.extend({
  toBeWithinRange(received, floor, ceiling) {
    const pass = received >= floor && received <= ceiling
    return {
      message: () => `expected ${received}${pass ? 'not ' : ''}to be within ${floor}-${ceiling}`,
      pass
    }
  }
})

expect(10).toBeWithinRange(5, 15)
```

#### **Best Practices**

1. **One assertion per test** (when practical)
2. **Use the most specific matcher** available
3. **Prefer `.toEqual()` over `.toBe()`** for objects/arrays
4. **Use `.not` judiciously** - positive assertions are clearer

#### **Real-World Example**

```javascript
describe('UserService', () => {
  it('should create user with valid data', async () => {
    const user = await UserService.create({
      name: 'John',
      email: 'john@example.com'
    })
  
    expect(user).toMatchObject({
      id: expect.any(String),
      name: 'John',
      email: 'john@example.com'
    })
    expect(user.createdAt).toBeInstanceOf(Date)
  })
  
  it('should reject invalid email', async () => {
    await expect(
      UserService.create({name: 'John', email: 'invalid'})
    ).rejects.toThrow('Invalid email')
  })
})
```

#### **Common Pitfalls**

* Using `.toBe()` when you need `.toEqual()`
* Forgetting `await` with promise matchers
* Overusing `.not` making tests harder to understand
* Not cleaning up mocks between tests

#### **Advanced Features**

* **Snapshot testing** : `expect(value).toMatchSnapshot()`
* **Asymmetric matchers** : `expect.any(String)`, `expect.stringContaining()`
* **Custom error messages** : `expect(value, 'custom message').toBe()`

---

---

# Testing In React

---

Writing Test Cases specific to React require these libraries

* [React Testing Library](https://www.npmjs.com/package/@testing-library/react)
  * RTL GitHub
* [jsdom](https://www.npmjs.com/package/jsdom)
  * (alternative) [happy-dom](https://www.npmjs.com/package/happy-dom)
    * happy-dom GitHub
  * jsdom GitHub
* [jest-dom](https://www.npmjs.com/package/@testing-library/jest-dom)
  * gives matchers for writing assertions against the Dom
    * examples: is an element in the dom if it has the right content etc.
  * [jest-dom GitHub](https://github.com/testing-library/jest-dom)

go here to view the queries you can use for assertions

* [testing-library](https://testing-library.com/docs/queries/about/)

**Install process of the above libraries:**

1. React Testing Library `@testing-library/react`

```bash
npm i -D @testing-library/react@latest
```

2. jsdom `jsdom`

```bash
npm i -D jsdom
```

after install make sure to go to the root of the project and create a file called `vitest.config.ts`

inside this file you need to declare the test environment to be jsdom

```ts
import { defineConfig} from "vitest/config";

export default defineConfig({
    test:{
        environment: 'jsdom'
    }
});
```

    3. jest-dom`@testing-library/jest-dom`

```bash
npm i -D @testing-library/jest-dom@latest
```

## Testing Components

### What to test?

#### How they render

* verfiy coponents reender under various conditions
* if the component has props, pass props and verify if the component renders correctly

#### How they respond to user actions

* if the componet handles user actions such as :
  * clicks
  * keyboard inputs
  * etc
    we should simulate those actions to make sure they react the way we expect

##### Testing User Interactions

to test user interactions you need to install a special library called `user-event` from `@testing-library`

to install paste the following command into the termainal:

```
npm install --save-dev @testing-library/user-event
```
