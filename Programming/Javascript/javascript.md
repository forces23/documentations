# oJavascript

## Arrays and Strings

Strings are considered Arrays but Arrays are not Strings

you cant revise a string by directly editing the character  like this

```javascript
let myString = "HelloWorld!";
myString[0] = "h"; // this is incorrect and will not do anything
```

you would have to use this :

```javascript
myString.replace("H", "h"); // the outcome of this will be a completely new string, 
```

you would need to store in another variable or overwrite the original to get the outcome of above

```javascript
mystring.replace("H", "h");
```

Accessing Elements

```javascript
const people = ["John", "Billy", "Caroline"];
console.log(people[2]); // output: Caroline
```

### **Concatentaion**

#### **Arrays**

you can use either the **spread operator** or the **concat()**  or **join()** function for arrays

##### spread operator ( ... )

    -- When using the spread operator for concatenation (`...myList`), the elements of `myList` are expanded into individual elements and combined with additional elements `[6, 7, 8]`.

    - more on spread operators go to spread operators section...

##### concat()

    -- adds what ever you put within the params to the list and returns a new list

##### join()

    -- used on string arrays to create asort of sentence with the strings within the array

```javascript
const myList = [1, 2, 3, 4, 5];

// using the spread operator
const newListSO = [...myList, 6, 7, 8]; // output: [1, 2, 3, 4, 5, 6, 7, 8];

// using the concat function
cosnt newListCon = myList.concat([6, 7, 8]); // output: [1, 2, 3, 4, 5, 6, 7, 8];

// using the join() method
let strings = ["Hello", "World!", "JavaScript", "Arrays!"];
let result = strings.join(" "); // this join adds a space in between each index joined but it can be anything i.e. +, --, etc
console.log(result);  // Output: "Hello World! JavaScript Arrays!"

```

#### **Strings**

you can use `+` operator or template literals for strings

```javascript
const myString = "Hello";

// using the '+' operator
const newStringPlus = myString + "World!"; // output: Hello World!

// using the template literals 
// !! must be enclosed by back ticks (`) !!
const newStingTL = `${myString} Bobby`; // output: Hello Bobby
```

### Methods:

#### Strings

##### replace()

-- is used to replace a character within a string...

```javascript
const string = string.replace(a,b);
```

a = character to find within the array

b = character to swap the original character with once found

##### toLowerCase()

-- transforms all character to the lowercase form

```
string.toLowerCase()
```

example:

```javascript
let string = "BILLY";

let lowerString = string.toLowerCase();

console.log(lowerString); // output: billy 
```

##### toUpperCase()

-- transforms all characters to the Uppercase form

```
string.toUpperCase()
```

example:

```javascript
let string = "billy";

let upperString = string.toUpperCase();

console.log(UpperString); // output: BILLY
```

##### trim()

-- removes all leading and trailing whitespaces

```javascript
string.trim()
```

example:

```javascript
const string = "   hello there     "; // notice all the extra whitespaces

console.log(string.trim()); // output: hello there (no extra white spaces)
```

##### substring()

```javascript
string.subsring(a,b)
```

a = index of where you want to start the slice

    - inclusive, meaning the index is included in the output string

b = index of where you want to stop the slice

    - exclusive, meaning the index you stop at is not included in the output

    - so where ever you want to stop you need to go up one index

example:

```javascript
const myString = "hello";
 
console.log( myString.substring(1,3) ); // output: el 
/* 
   Notice that it looks like it would be 'ell' since index 1 is 'e' and index 3 is 'l' 
   but the second param is exclusive so it is not included in the output which 
   results in only 'el' being the output.
*/


```

##### split()

**Purpose:** Splits a **string** into an **array of substrings** based on a separator.
**Returns:** An **array** (not the original string).
**Does not modify** the original string (strings are immutable in JavaScript).

```javascript
str.split(separator, limit)
```

* `separator` (optional): The character/string where splits occur (e.g., `" "`, `","`). If omitted, returns an array with the entire string.
* `limit` (optional): Maximum number of splits.

Example:

```javascript
const str = "Hello,World,JavaScript";

console.log(str.split(","));      // ["Hello", "World", "JavaScript"]
console.log(str.split(",", 2));   // ["Hello", "World"] (limited to 2 splits)
console.log(str.split(""));       // ["H", "e", "l", "l", "o", ",", ...] (split into chars)
```

##### .charAt()

-- returns the character at the specified `index` as a string.

-- mainly used for suppporting older browsers (pre 2011 versions)

-- in modern browser this identical to just doing `[i]` on a string

```
string.charAt(i)
```

-- `i` being the index af the character you want to grab

Example:

```javascript
let str = "hello";
let letter = str.charAt(1); // returns "e" 
```

---

---

#### Arrays/List

##### push()

-- Adds a new element to the end of the list

```javascript
list.push(a);
```

a = element added to the end of the list

##### join()

converts an **array into a string** by concatenating all its elements with a specified separator.

* **Applies to:** Arrays (not strings or other data types).
* **Does not modify** the original array (creates a new string).
* **Default separator:** `,` (comma) if no argument is provided.

```javascript
array.join(separator);
```

`separator` (optional): A string used to separate each element. If omitted, defaults to `","`.

Examples:

```javascript
const fruits = ["Apple", "Banana", "Cherry"];

console.log(fruits.join());      // "Apple,Banana,Cherry" (default comma)
console.log(fruits.join(" - ")); // "Apple - Banana - Cherry"
console.log(fruits.join(""));    // "AppleBananaCherry" (no separator)

// Converts Array → String
[1, 2, 3].join(); // output: "1,2,3"  

// Handles Different Data Types
[true, null, 5, { name: "John" }].join(" | ");  // output:  "true | null | 5 | [object Object]"

// ignores empty slots
["a", , "c"].join("-"); // "a--c" (empty slot becomes empty string)

// Works with Nested Arrays (Flattens One Level)
[1, [2, 3], 4].join(); // "1,2,3,4"  
```

##### reverse()

used to  **reverse the order of elements in an array**

* **Applies to:** Arrays (not strings, though you can convert a string to an array to use it).
* **Modifies the original array** (mutates it).
* **Returns:** The reversed array (same reference as the original, now reversed).

```javascript
array.reverse();
```

Examples:

```javascript
const arr = [1, 2, 3, 4];
arr.reverse();
console.log(arr); // [4, 3, 2, 1] (original array is modified)

// Mutates the original array 
const fruits = ["🍎", "🍌", "🍊"];
fruits.reverse();
console.log(fruits); // ["🍊", "🍌", "🍎"] (original is changed)

// returns reversed array but also changes the original array
const numbers = [10, 20, 30];
const reversed = numbers.reverse();
console.log(reversed); // [30, 20, 10]
console.log(numbers);  // [30, 20, 10] (original is also reversed)
```

Notes:

* best to create a copy then reverse that to avoid mutating the original array.
* does not work on strings. to make work on strings you will need to do this flow split >> reverse >> join

##### slice()

```javascript
string.slice(a,b)
```

a = index of where you want to start the slice

    - inclusive, meaning the index is included in the output array

b = index of where you want to stop the slice

    - exclusive, meaning the index you stop at is not included in the output

    - so where ever you want to stop you need to go up one index

example:

```javascript
const myList = [1, 2, 3, 4, 5];
 
console.log( myList.slice(2, 4) ); // output: [3, 4]
/* 
   Notice that it looks like it would be [3,4,5] since index 2 is 3 and index 4 is 5 
   but the second param is exclusive so it is not included in the output which 
   results in only [3, 4] being the output.
*/


```

##### splice()

-- allows one to insert a element at a specific index

-- allows one to remove a specific element

```javascript
const list = ["abc", "xyz", "mno"]
list.splice(a,b,c);
```

a = The start index where elements will be added or removed.

b = The number of elements to remove from the start index.

c = The elements to add at the start index.

Examples :

```javascript
const fruits = ["apple", "banana", "cherry"];

fruits.splice(fruits.indexOf("banana"), 1);
```

* `fruits.indexOf("banana")` returns the index of the element `"banana"`, which is `2` in this case.
* The first parameter `2` specifies the start index for removal.
* The second parameter `1` indicates that we want to remove one element starting from index `2`.

```javascript
// A packing list for a journey using JavaScript arrays
let travelItems = ["passport", "camera", "sunscreen", "hat"];

travelItems.splice(2,0,"sunglasses");

console.log("Updated travel items:", travelItems); 
// output: Updated travel items: [ 'passport', 'camera', 'sunglasses', 'sunscreen', 'hat' ]
```

##### indexOf()

-- returns the index of the specified element

-- does a search of the value in the array and returns the index of where that value is located within the array

```javascript
list.indexOf(a)
```

a = value of the element that is in the array that you would like to get the index of

example:

```javascript
const myList = [1, 2, 3, 4, 5];
const myString = "Hello";
 
const indexList = myList.indexOf(3); // output: 2 (Index of element '3')
const indexString = myString.indexOf('e'); // output: 1 (Index of character 'e')
```

##### includes()

-- does a search on the array it is applied to and returns true of it is in found and false if not

```javascript
array.includes(a)
```

a = value you are searching for

example:

```javascript
let word = "FRUIT Salad";
let vowels = ['a', 'e', 'i', 'o', 'u'];

console.log(word.includes('T')); // output: true
console.log(word.includes('t')); // output: flase
console.log(word.includes('lad')); // output: true

console.log(vowel.includes('a')); // output:true
console.log(vowel.includes('A')); // output: false
```

##### length

-- returns the how many indexes are in the array or if used on a string returns how many characters are in the string.

```javascript
string.length

list.length
```

example:

```javascript
const message = "helloWorld!"
console.log(message.length) // output: 11

const fruits = ["apple", "banana", "cherry"];
console.log(fruits.length) // output: 3

// to get the last index do use .length - 1
console.log(message.length - 1) // output: !
console.log(fruits.length - 1) // output: cherry

```

##### sort()

```javascript
array.sort([compareFunction])
```

**`compareFunction` (optional):**

A function that defines the sort order.

* **If omitted** , the array is sorted **lexicographically** (alphabetically, like strings).
* **If provided** , it should return:
* A **negative** number if `a` should come **before** `b`.
* A **positive** number if `b` should come **before** `a`.
* **Zero (0)** if `a` and `b` are equal (order remains unchanged).

**Examples:**

**1. Default (Lexicographical also Alphabetical Order) Sort (Bad for Numbers!)**

```javascript
// with number[]
const numbers = [10, 2, 1, 20, 5];
numbers.sort(); // No compare function → treats numbers as strings!
console.log(numbers); // Output: [1, 10, 2, 20, 5] (Not numerically sorted!)

// with string[]
const fruits = ["Banana", "Apple", "Mango", "Cherry"];
fruits.sort(); // No compare function → sorts alphabetically
console.log(fruits); // Output: ["Apple", "Banana", "Cherry", "Mango"]

```

**2. Numeric Ascending Sort**

```javascript
const numbers = [10, 2, 1, 20, 5];
numbers.sort((a, b) => a - b); // a - b → negative if a < b → a comes first
console.log(numbers); // Output: [1, 2, 5, 10, 20]
```

**3. Numeric Descending Sort**

```javascript
const numbers = [10, 2, 1, 20, 5];
numbers.sort((a, b) => b - a); // b - a → positive if b > a → b comes first
console.log(numbers); // Output: [20, 10, 5, 2, 1]
```

**Using Mutation instead of editing the original array**

```javascript
// with string[]
const fruits = ["Banana", "Apple", "Mango", "Cherry"];
const sortedFrits = [...fruits].sort(); 
console.log(sortedFrits ); // Output: ["Apple", "Banana", "Cherry", "Mango"]
```

**Key Notes:**

✅  **For numbers** , always use a **compare function** (`(a, b) => a - b` for ascending, `(a, b) => b - a` for descending).
❌  **Without a compare function** , numbers are sorted **as strings** (e.g., `"10"` comes before `"2"`).
🔄 **`sort()` modifies the original array** (use `[...array].sort()` to avoid mutation).

##### map()

    -- an**array method** that creates a new array by applying a function to every element of the original array.

    -- It does**not** change the original array.

    -- The function you pass to`map()` receives each element, its index, and the whole array.

Common Uses

* Transforming data (e.g., numbers to strings, objects to values)
* Creating new arrays without mutating the original

```javascript
array.map((element, index, array) => {
  // return new value
});
```

Examples:

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);
// doubled: [2, 4, 6, 8]

const words = ['hello', 'world'];
const upper = words.map(word => word.toUpperCase());
// upper: ['HELLO', 'WORLD']
```

---

---

## Sets

A `Set` is a built-in JavaScript object that stores  **unique values** —no duplicates allowed. It’s great for tracking things you’ve already seen, like visited indices.

Why Use a Set?

* **Fast lookups:** `.has()` is much faster than `.includes()` on arrays, especially for large data.
* **No duplicates:** Automatically prevents repeated values.
* **Great for tracking:** Useful for “have I seen this before?” logic, like in your array hopping problem.

Basic Usage

**Creating a Set:**

```javascript
let mySet = new Set();
```

**Adding values:**

```javascript
mySet.add(3);
mySet.add('hello');
mySet.add(3); // Duplicate, will not be added again
```

**Checking if a value exists:**

```javascript
mySet.has(3); // true
mySet.has(5); // false
```

**Removing a value:**

```javascript
mySet.delete(3);
```

**Getting the size:**

```javascript
mySet.size; // Number of unique elements
```

**Iterating through a Set:**

```javascript
for (let value of mySet) {
  console.log(value);
}
```

---

---

## Loops

Loops enable us to execute repetitive sequences automatically and efficiently.

### For Loops

The `for` loop is a control flow statement that allows code to be executed repeatedly.

The structure of a `for` loop is typically `for (initialization; condition; iteration) { loop body }`, where the `loop body` gets executed for as long as the `condition` evaluates to true. After each loop, the `iteration` is executed, which generally updates the value of the loop control variable. Here is how it generally works:

1. **Initialization** : This is where you set up the loop variable. It's executed once when the loop begins.
2. **Condition** : This Boolean expression determines if the loop will continue or stop. If it's true, the loop continues; if it's false, the loop ends, and the flow jumps to the next statement after the loop block.
3. **Iteration** : This is where you update the loop variable. This statement executes after the loop body and right before the next condition check.
4. **Loop Body** : The block of code to be executed in each loop.

```javascript
let friends = ["Alice", "Bob", "Charlie", "Daniel"];

for (let i = 0; i < friends.length; i++) {
    // `i` is the index that changes with each iteration
    // For each friend, print the greeting
    console.log("Hello, " + friends[i] + "! Nice to meet you.");
}

// Output:
// Hello, Alice! Nice to meet you.
// Hello, Bob! Nice to meet you.
// Hello, Charlie! Nice to meet you.
// Hello, Daniel! Nice to meet you.
```

### Enhanced For Loop

also know as the for...of loop

is used to traverse any sequence-like structure , such as strings and arrays, more simply and safely since it eliminates the need to manually control the loop variable.

```javascript
let fruits = ["apple", "banana", "cherry"];

// fruit stands for each fruit in the fruits array
for (let fruit of fruits) {
console.log(fruit);
}

// Output:
// apple
// banana
// cherry
```

```javascript
let word = "hello";
// `ch` is each individual character in `word`
for (let ch of word) {
    console.log(ch);
}

// Output:
// h
// e
// l
// l
// o
```

### While Loops

`While loops` in JavaScript continuously execute their content until a particular condition becomes false.

```javascript
let num = 0;
// The loop keeps running until `num` is no longer less than 5
while (num < 5) {
    console.log(num);
    // Increase `num` by 1 at the end of each iteration
    num++;
}

// Output:
// 0
// 1
// 2
// 3
// 4
```

---

---

## Conditional Statements

### if

the `if` statement triggers actions in our code based on a specific condition. Consider this straightforward example, where the `if` statement determines which message to print based on the value of `temperature`:

```javascript
let temperature = 15;

if (temperature > 30) {
    console.log("It's hot outside!"); // This will print if the temperature is over 30.
} else if (temperature > 20) {
    console.log("The weather is nice."); // This will print if the temperature is between 21 and 30.
} else {
    console.log("It might be cold outside."); // This will print if the temperature is 20 or below.
}
// Output: It might be cold outside.
```

### break

We use the `break` statement whenever we want to exit a loop prematurely once a condition is met:

```javascript
const numbers = [1, 3, 7, 9, 12, 15];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
        console.log("The first even number is: " + numbers[i]); // This prints the first even number.
        break; // This stops the loop after printing the first even number.
    }
    console.log("Number: " + numbers[i]);
}

// Output:
// Number: 1
// Number: 3
// Number: 7
// Number: 9
// The first even number is: 12
```

### continue

The `continue` statement bypasses the rest of the loop code for the current iteration only:

```javascript
for (let i = 0; i < 6; i++) {
    if (i === 3) {
        continue; // This skips the print command for '3'.
    }
    console.log(i); // This prints the numbers from 0 to 5, except 3.
}
// Output:
// 0
// 1
// 2
// 4
// 5
```

---

---

## String Manipulation

### Working with ASCII Codes in Characters

Characters in JavaScript can be manipulated using their **ASCII** values. **ASCII** (American Standard Code for Information Interchange) is a character encoding standard used to represent text in computers and other devices that use text. Every character has a unique ASCII value.

visit this site to view the full ASCII code table [ASCII Code Table](https://www.ascii-code.com/)

You don’t need to memorize ASCII codes, but it helps to know a few basics:

* `'a'` is `97`, `'z'` is `122`
* `'A'` is `65`, `'Z'` is `90`

You can always look up/print the numbers if you forget using `.charCodeAt()`

example of looking up the character codes programatically

```javascript
"A".charCodeAt(0); // output: 65
"Z".charCodeAt(0); // output: 90
"a".charCodeAt(0); // output: 97
"z".charCodeAt(0); // output: 122
```

You can convert a character into its ASCII value using the `charCodeAt()` method:

```javascript
let c = 'A';
let asciiVal = c.charCodeAt(0); // Retrieves the ASCII value of the character at index 0 of the string c, which is 'A', and assigns it to the variable asciiVal.
console.log(`The ASCII value of ${c} is: ${asciiVal}`);
// Prints: The ASCII value of A is: 65
```

Similarly, you can convert an ASCII value back to its corresponding character using `String.fromCharCode()`:

```javascript
let asciiVal = 65;
let c = String.fromCharCode(asciiVal);
console.log(`The character of ASCII value ${asciiVal} is: ${c}`);
// Prints: The character of ASCII value 65 is: A
```

Manipulating the ASCII value of characters can be quite useful in certain situations. For example, to convert a lowercase letter to uppercase (or vice versa), you could subtract (or add) 32 to the character's ASCII value.

### String Indexing Reminder

JavaScript strings work with a zero-based indexing system. This means that you can access specific characters in a string by using their position.

**Please note:** If you try to access an index that does not exist in your string, JavaScript will return `undefined`. Hence, it is always recommended to check the string length before accessing any index.

Here's an example:

```javascript
let text = "Hello, JavaScript!";
let index = 9; // The index we want to access

if (index < text.length) {
    let charAtIndex = text.charAt(index);
    console.log(`The character at index ${index} is: ${charAtIndex}`);
} else {
    console.log(`The index ${index} is out of bounds for the string!`);
}

// Prints: The character at index 9 is: v
```

### Character Operations

Let's now explore character operations in JavaScript. String methods such as `toUpperCase()` and `toLowerCase()` are used to change the case of a character. Additionally, we can create custom functions to check whether a character is lowercase or uppercase.

* Using `toUpperCase()` and `toLowerCase()` to change the case of characters:

```javascript
let s = "mark";
let result = '';
for (let i = 0; i < s.length; i++) {
    result += s.charAt(i).toUpperCase();
    // You can also use s[i] instead of s.charAt(i)
}
console.log(result);  // Prints: 'MARK'

s = "Mark";
result = '';
for (let i = 0; i < s.length; i++) {
    result += s.charAt(i).toLowerCase();
}
console.log(result);  // Prints: 'mark'
```

* Implementing custom functions to check the case of characters:

```javascript
function isLowerCase(char) {
    return char === char.toLowerCase() && char !== char.toUpperCase();
}

function isUpperCase(char) {
    return char === char.toUpperCase() && char !== char.toLowerCase();
}

console.log("Is 'a' lowercase? " + isLowerCase('a'));  // Prints: true
console.log("Is 'B' lowercase? " + isLowerCase('B'));  // Prints: false

console.log("Is 'a' uppercase? " + isUpperCase('a'));  // Prints: false
console.log("Is 'B' uppercase? " + isUpperCase('B'));  // Prints: true
```

In both functions, the `&&` operator (logical AND) ensures that both conditions must be true for the function to return `true`. For example, in the `isLowerCase` function, it checks that the character equals its lowercase version (`char === char.toLowerCase()`) and that it does not equal its uppercase version (`char !== char.toUpperCase()`). Without the second condition, non-alphabetic characters would also be considered lowercase letters. Both conditions must be satisfied to confirm that the character is indeed lowercase.

* Checking whether a character is a letter, digit, or alphanumeric using regular expressions:

```javascript
function isLetter(char) {
    return /^[a-zA-Z]$/.test(char);
}

function isDigit(char) {
    return /^[0-9]$/.test(char);
}

function isLetterOrDigit(char) {
    return /^[a-zA-Z0-9]$/.test(char);
}

console.log(isLetter('C'));  // Prints: true
console.log(isLetter('+'));  // Prints: false

console.log(isDigit('9'));  // Prints: true
console.log(isDigit('D'));  // Prints: false

console.log(isLetterOrDigit('6'));  // Prints: true
console.log(isLetterOrDigit('k'));  // Prints: true
console.log(isLetterOrDigit('?'));  // Prints: false
```

### Regular Expressions

* Regular expressions, often abbreviated as regex, are sequences of characters that form a search pattern. They are mainly used for pattern matching with strings.
* In this context, the regex `/^[a-zA-Z]$/` checks if a single character string is either a lowercase (`a-z`) or uppercase (`A-Z`) English letter. The `^` and `$` symbols are anchors that ensure the match is done on the entire string, meaning it should be exactly one letter.

### Tokenization

we can use the `split` method from the `String` class to tokenize a string, essentially splitting it into smaller parts or 'tokens'.

```javascript
let sentence = "JavaScript is an amazing language!";
let tokens = sentence.split(" ");

tokens.forEach(token => console.log(token));

// Output:
// JavaScript
// is
// an
// amazing
// language!
```

### Type Conversions

We can convert strings to numbers using methods like `parseInt` (string to integer) and `parseFloat` (string to float), and other data types to strings using `String`:

```javascript
let numStr = "123";
let num = parseInt(numStr);
console.log(num);  // Output: 123

let floatStr = "3.14";
let pi = parseFloat(floatStr);
console.log(pi);  // Output: 3.14

let age = 20;
let ageStr = String(age);
console.log("I am " + ageStr + " years old."); // Output: I am 20 years old.
```

---

---

## Numbers

### Methods

toFixed()

    -- formats a number using fixed-point notation.

    -- It returns a string representing the number with exactly`d` digits after the decimal point.

    -- The result is always a string, not a number.

    -- If you want to use it as a number again, you can convert it back with`parseFloat()`

```javascript
let x = 2.3456;

console.log(x.toFixed(2)); // output: 2.35  (rounded to 2 decimal places and is a string)
```

---

---

## Math Operations

### sqrt()

-- returns the square root of what you put inside the params

```javascript
Math.sqrt(x);
```

### round()

-- returns the given param to the nearest integer

```javascript
Math.round(X);
```

example:

```javascript
let x = 0.83484237

// rounds number to 2 decimal places
const twoDecimals = Math.round(x * 100) / 100 // output: 0.83
```

### floor()

 -- Function that rounds a number **down** to the nearest integer.

-- For negative numbers, it goes to the next lowest integer: `Math.floor(-2.3)` returns `-3`.

```javascript
Math.floor(x);
```

Example:

```javascript
let number = 7.8;
let roundedDown = Math.floor(number);
console.log(roundedDown); // Output: 7
```

### ceil()

-- Function that rounds the given number in the param number **up** to the nearest integer.

-- Even if the number is already an integer, it stays the same: `Math.ceil(5)` returns `5`.

-- It’s useful when you want to make sure you never round down.

```javascript
Math.ceil(X)
```

Example:

```javascript
let number = 4.2;
let roundedUp = Math.ceil(number);
console.log(roundedUp); // Output: 5
```

---

---

## Operators

### Modulos (%)

* The modulo operator returns the **remainder** after dividing one number by another.
* In JavaScript: `a % b` gives you the remainder when `a` is divided by `b`.

Examples:

* `7 % 3` is `1` (since 7 divided by 3 is 2 with a remainder of 1)
* `10 % 2` is `0` (since 10 divides evenly by 2)
* `5 % 4` is `1` (since 5 divided by 4 is 1 with a remainder of 1)

Why is Modulo Useful?

* **Wrapping Around:** When you want to cycle through a fixed set of positions (like array indices), modulo helps you "wrap around" to the start.
* **Even/Odd Check:** `n % 2` is `0` for even numbers, `1` for odd numbers.

Suppose you have a string of length `n`, and you want to jump forward by `step` each time.
If you reach the end, you want to start back at the beginning.

* Using `(currentIndex + step) % n` ensures you always stay within the bounds `0` to `n-1`.

Example:

For `inputString = "abcdefg"` (`n = 7`), `step = 3`:

* Start at index `0` (`'a'`)
* Next: `(0 + 3) % 7 = 3` (`'d'`)
* Next: `(3 + 3) % 7 = 6` (`'g'`)
* Next: `(6 + 3) % 7 = 2` (`'c'`)
* Next: `(2 + 3) % 7 = 5` (`'f'`)
* Next: `(5 + 3) % 7 = 1` (`'b'`)
* Next: `(1 + 3) % 7 = 4` (`'e'`)

---

---

## Spread Operators

### **1. Shallow Copy (Default Behavior)**

The spread operator **only does a shallow copy** (copies top-level elements, but nested objects/arrays are still referenced).

#### **Example with Arrays:**

```javascript
const original = [1, 2, { name: "Alice" }];
const copy = [...original]; // Shallow copy

copy[0] = 100; // Does NOT affect original
copy[2].name = "Bob"; // Affects original because it's a reference!

console.log(original); 
// Output: [1, 2, { name: "Bob" }] (nested object changed)
```

#### **Example with Objects:**

```javascript
const original = { a: 1, b: { name: "Alice" } };
const copy = { ...original }; // Shallow copy

copy.a = 100; // Does NOT affect original
copy.b.name = "Bob"; // Affects original!

console.log(original); 
// Output: { a: 1, b: { name: "Bob" } } (nested object changed)
```

### **2. Deep Copy (Requires Extra Work)**

To fully clone nested structures, you need additional methods since `...` alone  **does not deep copy** .

#### **Methods for Deep Copy:**

1. **`JSON.parse(JSON.stringify(obj))`** (Simple, but loses functions/`undefined`/special objects)

   ```javascript
   const original = { a: 1, b: { name: "Alice" } };
   const deepCopy = JSON.parse(JSON.stringify(original));
   ```

   * ✅ Works for plain objects/arrays.
   * ❌ Fails with `Date`, `functions`, `undefined`, circular references.
2. **Libraries like Lodash (`_.cloneDeep`)** (Robust solution)

   ```javascript
   const deepCopy = _.cloneDeep(original);
   ```
3. **`structuredClone()`** (Modern JS, handles most cases)

   ```javascript
   const deepCopy = structuredClone(original);
   ```

   * ✅ Built into browsers/Node.js.
   * ❌ Still doesn’t copy functions.

### **3. Semi-Deep Copy (Manual Nested Spread)**

You can manually spread nested levels, but it’s tedious:

```javascript
const original = { a: 1, b: { name: "Alice" } };
const semiDeepCopy = { 
  ...original, 
  b: { ...original.b } // Manually spread nested objects
};
```

### **Scenario: Updating a Nested Object in State**

You have a React component with a state that includes a nested object (e.g., a user profile).
You want to update **only one nested property** without accidentally mutating the original state.

#### **Initial State:**

```
const [user, setUser] = useState({
  name: "Alice",
  details: {
    age: 25,
    hobbies: ["coding", "gaming"]
  }
});
```

### ❌ **Problem: Shallow Copy Fails (Accidental Mutation)**

```javascript
const updateAge = () => {
  // ⚠️ Shallow copy (nested 'details' is still referenced!)
  const newUser = { ...user };
  newUser.details.age = 30; // Mutates the original state!
  setUser(newUser);
};
```

**What happens?**

* Both `user` and `newUser` **share the same `details` object** in memory.
* Directly changing `newUser.details.age` **also changes the original state** (bug!).

### ✅ **Solution 1: Manual Deep Copy with Spread**

```javascript
const updateAge = () => {
  // Deep copy for 'details' (spread nested objects/arrays)
  const newUser = {
    ...user,
    details: {
      ...user.details,       // Copy nested object
      age: 30                // Update only this property
    }
  };
  setUser(newUser);
};
```

**Why it works:**

* Creates a  **new `details` object** , breaking the reference to the original.

### ✅ **Solution 2: `structuredClone` (Modern JS)**

```javascript
const updateAge = () => {
  // Deep clone the entire state
  const newUser = structuredClone(user);
  newUser.details.age = 30; // Safe mutation
  setUser(newUser);
};
```

**Pros:**

* No manual spreading needed.
* Handles nested objects/arrays.

**Cons:**

* Doesn’t copy functions or special objects (e.g., `Date`).

### ✅ **Solution 3: Libraries (Lodash)**

```javascript
import _ from "lodash";

const updateAge = () => {
  const newUser = _.cloneDeep(user); // Full deep copy
  newUser.details.age = 30;
  setUser(newUser);
};
```

**When to use:**

* Complex objects with mixed data types.

### **Key Lesson:**

* **Shallow copy (`...`)** → Safe for top-level updates.
* **Deep copy (`structuredClone`/`_.cloneDeep`)** → Required for nested updates in state.
* **React’s golden rule:** Never mutate state directly. Always create new copies!

### **Real-World Impact:**

1. **UI Bugs:** Shallow copies cause components to re-render incorrectly.
2. **Data Corruption:** Original state gets modified unintentionally.
3. **Hard-to-Find Bugs:** Mutations might not crash your app but lead to weird behavior.

**Fix:** Always ask: *"Is my state nested? If yes, deep copy!"*

---

---

## CODE EXAMPLES

### reverse character casing program

```javascript
const text = "JavaScript is awesome!";
let cleanedText = '';
let lcCount = 0

for (let i = 0; i < text.length; i++) {
    let c = text[i];
    if (c === c.toLowerCase() && c !== c.toUpperCase()) {
        lcCount++;
        cleanedText += c.toUpperCase();
    } else if (c === c.toUpperCase() && c !== c.toLowerCase()) {
        cleanedText += c.toLowerCase();
    } else {  // Keep non-alphabetical characters unchanged
        cleanedText += c;
    }
}


console.log(cleanedText);  // outputs: "jAVAsCRIPT IS AWESOME!"
console.log(lcCount); // output: 17 (number of lowercase letters prior to transformation)
```

### Encrpypting A String

```javascript
function encryptString(text) {
    let encrypted = '';
  
    for (let i = 0; i < text.length; i++) {
        let c = text.charAt(i);
        // TODO: Check if `c` is a letter and it is not the letter 'z' or 'Z'.
  
        if (/^[a-yA-Y]$/.test(c)) {
            // If it is a letter other than 'z' or 'Z', shift its value by 1 in the ASCII table.
            let cAsciiCode = c.charCodeAt(0);
            encrypted += String.fromCharCode(cAsciiCode + 1); 
        } else if (/^[zZ]$/.test(c)) {
            // If the letter is 'z', change it to 'a'. If it is 'Z', change it to 'A'.
            if (c === 'Z') encrypted += 'A';
            if (c === 'z') encrypted += 'a';
        } else {
            // If `c` is not a letter, append it unchanged to the encrypted string.
            encrypted += c;
        }
    }
    return encrypted;
}

console.log("The encrypted text is: " + encryptString("Hello, Java!")); // Should print out "Ifmmp, Kbwb!"
```

### Ceaser Cipher Encryption

```javascript
// Simple text encryption using Caesar Cipher technique
// The Caesar Cipher for `shift = 3` cyclically shifts every letter of the word by 3 positions:
// a -> d, b -> e, c -> f, ..., x -> a, y -> b, z -> c

// Implement the encryption logic by shifting each alphabet character
function encryptText(text) {
    let encrypted = '';
    for (let i = 0; i < text.length; i++) {
        let c = text[i];
        if (/[a-zA-Z]/.test(c)) {  // check if the character is a letter
            let shift = 3;
            // TODO: Use correct calculations to shift the character within the alphabet
            // Hint: 'A' = 65, 'a' = 97
            // Hint 2: You can use the modulo (%) operator to wrap around the alphabet
            let cAsciiCode = c.charCodeAt(0);

            if (/^[a-z]$/.test(c)) {
                encrypted += String.fromCharCode((((cAsciiCode - 97) + shift) % 26) + 97);
            } else if (/^[A-Z]$/.test(c)) {
                encrypted += String.fromCharCode((((cAsciiCode - 65) + shift) % 26) + 65);
            }
        } else {
            encrypted += c;  // keep non-letter characters unchanged
        }
    }
    return encrypted;
}

// Example text to encrypt
let originalText = "Hello, JavaScript! ZZ";
// The encryptText function call and console.log statement should remain the same as the solution
let encryptedText = encryptText(originalText);
console.log(encryptedText);  // Correct output after TODO should be 'Khoor, MdydVfulsw!'
```

### Extracting and Processing Each Digit

(without converting to a string)

```javascript
function solution(n) {
    let digit_sum = 0;
    while (n > 0) {
        let digit = n % 10;
        if (digit % 2 === 0) {  // Check if the digit is even.
            digit_sum += digit;
        }
        n = Math.floor(n / 10);  // Remove the last digit.
    }
    return digit_sum;
}

console.log(solution(4625));  // Output should be 12
```

### Center-Outward Array Traversal

```javascript
/*
task is to produce a new array, given an array of integers, that starts from the center of the original array and alternates direction towards both ends. That is, the first element of our new array will be the middle element of the original one.

After defining the starting point, we will alternate between elements to the left and to the right of this center until all elements have been included. If the length of the initial array is even, we first take the element to the left of the center, then the one to the right of the center, and then do the alternation as described above.

For example, for numbers = [1, 2, 3, 4, 5], the output would be [3, 2, 4, 1, 5].

We will break down this seemingly complex task into manageable pieces to progressively build our JavaScript solution. Keep in mind an additional condition: the length of the array — represented as n — can range from 1 to 100,000, inclusive.
*/

function iterateMiddleToEnd(numbers) {
    let mid = Math.floor(numbers.length / 2); // index of the middle element
    let left, right;
    let newOrder = [];  // Array to store new order

    if (numbers.length % 2 === 1) {
        left = mid - 1; // Pointing to the left of the middle element
        right = mid + 1; // Pointing to the right of the middle element
        newOrder.push(numbers[mid]); // Adding the middle element to the resulting array
    } else {
        left = mid - 1; // Pointing to the left of the middle element
        right = mid; // Pointing to the middle element
    }

    while (left >= 0 && right < numbers.length) {
        newOrder.push(numbers[left--]);
        newOrder.push(numbers[right++]);
    }

    return newOrder;
}

const numbers = [1, 2, 3, 4, 5];
const result = iterateMiddleToEnd(numbers);
console.log(result);  // Output should be [3, 2, 4, 1, 5]
```

### Identifying Consecutive Character Groups

```javascript
/*
write a JavaScript function that accepts a string as input and identifies all consecutive groups of identical characters within it. A group is defined as a segment of the text wherein the same character is repeated consecutively.

Your function should return an array of strings. Each string will consist of the repeating character and the length of its repetition, joined by a colon (:). For example, if the input string is "aaabbcccaae", your function should output: ["a:3", "b:2", "c:3", "a:2", "e:1"].

Bear in mind that, while processing the input string, we are interested only in alphanumeric characters (i.e., alphabets and digits). Other characters present will not factor into the formation of these groups.
*/

function findGroups(s) {
    let groups = []; // Array to store the groups of characters
    let currentGroupChar = ''; // Variable to hold the current character group
    let currentGroupLength = 0; // Variable to hold the length of the current character group
  
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        if (/[a-zA-Z0-9]/.test(c)) { // Check if the character is alphanumeric
            if (c === currentGroupChar) { // If the character is part of the current group
                currentGroupLength += 1; // Increment the length of the current group
            } else { // If the character starts a new group
                if (currentGroupChar !== '') { // Add the previous group to groups if it exists
                    groups.push(currentGroupChar + ":" + currentGroupLength);
                }
                currentGroupChar = c; // Update the current character to the new group
                currentGroupLength = 1; // Reset the length for the new group
            }
        }
    }
    if (currentGroupChar !== '') { // Add the last group if it exists
        groups.push(currentGroupChar + ":" + currentGroupLength);
    }
    return groups; // Return the array of groups
}

// Example usage
let input = "aaabbcccaae";
let result = findGroups(input);
for (let group of result) {
    console.log(group);
}
// Output:
// "a:3"
// "b:2"
// "c:3"
// "a:2"
// "e:1"
```

### Parsing and Multiplying Numbers

```javascript
/*
Our task for the day involves creating a JavaScript function called parseAndMultiplyNumbers(). This function is designed to accept a string as input. However, it's not just any string — the input we'll consider is a playful mix of numbers and words.

The purpose of this function is to analyze the input string, extract all the numbers, convert these numbers (currently string types) into integer data types, and then multiply all these numbers together. The final output? It's the product of all those numbers!

Here's an illustration for clarification. Given the input string "I have 2 apples and 5 oranges," our function should return the product of 2 and 5, which is 10.
*/

function parseAndMultiplyNumbers(inputString) {
    let num = "";
    let numbers = [];

    for (let ch of inputString) {
        if (!isNaN(ch) && ch !== ' ') { // Check if character is a digit
            num += ch;
        } else if (num !== "") {
            numbers.push(parseInt(num)); // Convert num to integer and add it to numbers array
            num = "";
        }
    }
    if (num !== "") {
        numbers.push(parseInt(num));
    }

    let result = 1;
    for (let number of numbers) {
        result *= number;
    }
    return result;
}

// Call the function
console.log(parseAndMultiplyNumbers("I have 2 apples and 5 oranges"));
```

### Time Parsing and Manipulation

```javascript
/*
Imagine this: You receive a time formatted as a string in HH:MM:SS, where HH, MM, and SS denote the hour, minute, and second, respectively. You are also given an integer representing a certain number of seconds. Your task is to calculate the new time after adding the provided seconds, then output the result in the HH:MM:SS format.

For example, if the input time is 05:10:30 and the number of seconds to add is 123, the output should be 05:12:33 since 123 seconds translate to 2 minutes and 3 seconds.

Please note these points when resolving this task:

The input time is always a valid time string in the HH:MM:SS format, with HH ranging from 00 to 23 and MM and SS ranging from 00 to 59.
The output should be a time in the same format.
*/

function addSeconds(time, secondsToAdd) {
    let timeParts = time.split(":");
    let hours = parseInt(timeParts[0]);
    let minutes = parseInt(timeParts[1]);
    let seconds = parseInt(timeParts[2]);

    let secondsSinceStart = hours * 3600 + minutes * 60 + seconds;
    let totalSeconds = (secondsSinceStart + secondsToAdd) % (24 * 3600);

    let newHours = Math.floor(totalSeconds / 3600);
    totalSeconds %= 3600;
    let newMinutes = Math.floor(totalSeconds / 60);
    let newSeconds = totalSeconds % 60;

    return `${String(newHours).padStart(2, '0')}:${String(newMinutes).padStart(2, '0')}:${String(newSeconds).padStart(2, '0')}`;
}

// Call the function
console.log(addSeconds("05:10:30", 123));
// Output: 05:12:33
```

---

---
