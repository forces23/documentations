# Regular Expressions (Regex) Cheatsheet for Beginners

Regular expressions are powerful patterns used to match character combinations in strings. This cheatsheet will help you understand and use regex effectively.

## Basic Patterns

### Literal Characters
Match exactly what you type:

```
hello
```

Matches: "hello" in "hello world"

Visual:
```
Text:    hello world
Pattern: hello
Match:   █████
```

### Character Classes
Match any one character from a set:

```
[aeiou]
```

Matches: any vowel

Visual:
```
Text:    hello
Pattern: [aeiou]
Match:    █   █
```

### Negated Character Classes
Match any character NOT in the set:

```
[^aeiou]
```

Matches: any consonant or non-letter

Visual:
```
Text:    hello
Pattern: [^aeiou]
Match:   █ █ 
```

### Character Ranges
Match any character in a range:

```
[a-z]     # Lowercase letters
[A-Z]     # Uppercase letters
[0-9]     # Digits
[a-zA-Z]  # Any letter
```

Visual:
```
Text:    Hello123
Pattern: [a-z]
Match:    ████
```

## Quantifiers

### Zero or More (*)
Match 0 or more of the preceding character:

```
a*
```

Visual:
```
Text:    baaa
Pattern: a*
Match:    ███
```

### One or More (+)
Match 1 or more of the preceding character:

```
a+
```

Visual:
```
Text:    baaa
Pattern: a+
Match:    ███
```

### Zero or One (?)
Match 0 or 1 of the preceding character:

```
colou?r
```

Matches: "color" or "colour"

Visual:
```
Text:    color colour
Pattern: colou?r
Match:   █████ ██████
```

### Exact Count {n}
Match exactly n occurrences:

```
a{3}
```

Visual:
```
Text:    baaaa
Pattern: a{3}
Match:    ███
```

### Range Count {n,m}
Match between n and m occurrences:

```
a{2,4}
```

Visual:
```
Text:    baaaaa
Pattern: a{2,4}
Match:    ████
```

## Special Characters

### Any Character (.)
Match any single character except newline:

```
.
```

Visual:
```
Text:    abc
Pattern: .
Match:   █
```

### Escape Character (\\)
Use to match special characters literally:

```
\.
```

Matches: a period character

Visual:
```
Text:    example.com
Pattern: \.
Match:          █
```

### Start of String (^)
Match pattern at the beginning of a string:

```
^hello
```

Visual:
```
Text:    hello world
Pattern: ^hello
Match:   █████
```

### End of String ($)
Match pattern at the end of a string:

```
world$
```

Visual:
```
Text:    hello world
Pattern: world$
Match:         █████
```

## Common Predefined Character Classes

### Digit (\\d)
Equivalent to [0-9]:

```
\d
```

Visual:
```
Text:    abc123
Pattern: \d
Match:      ███
```

### Non-digit (\\D)
Equivalent to [^0-9]:

```
\D
```

Visual:
```
Text:    abc123
Pattern: \D
Match:   ███
```

### Word Character (\\w)
Equivalent to [a-zA-Z0-9_]:

```
\w
```

Visual:
```
Text:    hello_123
Pattern: \w
Match:   █████████
```

### Non-word Character (\\W)
Equivalent to [^a-zA-Z0-9_]:

```
\W
```

Visual:
```
Text:    hello world!
Pattern: \W
Match:         █   █
```

### Whitespace (\\s)
Match any whitespace character (space, tab, newline):

```
\s
```

Visual:
```
Text:    hello world
Pattern: \s
Match:        █
```

### Non-whitespace (\\S)
Match any non-whitespace character:

```
\S
```

Visual:
```
Text:    hello world
Pattern: \S
Match:   █████ █████
```

## Grouping and Alternation

### Grouping ()
Group patterns together:

```
(ab)+
```

Matches: "ab", "abab", "ababab", etc.

Visual:
```
Text:    abababc
Pattern: (ab)+
Match:   ██████
```

### Alternation (|)
Match either pattern:

```
cat|dog
```

Matches: "cat" or "dog"

Visual:
```
Text:    I have a cat and a dog
Pattern: cat|dog
Match:          ███     ███
```

## Common JavaScript Regex Methods

### test()
Returns true if pattern matches, false otherwise:

```javascript
/pattern/.test(string)
```

Example:
```javascript
const isEmail = /^\w+@\w+\.\w+$/.test("user@example.com");  // true
```

### match()
Returns an array of matches:

```javascript
string.match(/pattern/)
```

Example:
```javascript
const matches = "hello world".match(/\w+/g);  // ["hello", "world"]
```

### replace()
Replace matches with a new string:

```javascript
string.replace(/pattern/, replacement)
```

Example:
```javascript
const censored = "bad word".replace(/bad/, "****");  // "**** word"
```

## Regex Flags

Add after the closing slash to modify behavior:

```
/pattern/flags
```

### Common Flags:

- `g` - Global: Find all matches, not just the first
- `i` - Case-insensitive: Ignore case
- `m` - Multiline: ^ and $ match start/end of each line
- `s` - Dotall: . matches newlines too

Example:
```javascript
const globalMatch = "hello hello".match(/hello/g);  // ["hello", "hello"]
const caseInsensitive = "Hello".match(/hello/i);    // ["Hello"]
```

## Common Regex Patterns

### Email
```
/^[\w.-]+@[\w.-]+\.\w+$/
```

### URL
```
/https?:\/\/[\w\-\.]+\.\w{2,}/
```

### Phone Number (US)
```
/\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}/
```

### Date (MM/DD/YYYY)
```
/^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{4}$/
```

## Practice Examples

### Example 1: Extract all numbers from text
```javascript
const text = "I have 2 apples and 3 oranges";
const numbers = text.match(/\d+/g);  // ["2", "3"]
```

### Example 2: Validate a username (letters, numbers, underscore, 3-16 chars)
```javascript
const isValidUsername = /^[a-zA-Z0-9_]{3,16}$/.test("user_123");  // true
```

### Example 3: Replace multiple spaces with a single space
```javascript
const formatted = "too    many    spaces".replace(/\s+/g, " ");  // "too many spaces"
```

### Example 4: Extract domain from email
```javascript
const email = "user@example.com";
const domain = email.match(/@([\w.-]+)/)[1];  // "example.com"
```

## Online Tools for Learning and Testing Regex

1. **Regex101**: https://regex101.com/
   - Interactive regex tester with explanation and highlighting

2. **RegExr**: https://regexr.com/
   - Visual regex tester with reference guide

3. **Regexper**: https://regexper.com/
   - Visualizes regex patterns as railroad diagrams

## Tips for Beginners

1. **Start simple**: Begin with basic patterns and gradually add complexity
2. **Test incrementally**: Add one feature at a time and test
3. **Use online tools**: Visualize and test your patterns
4. **Read the documentation**: Different languages have slight variations in regex syntax
5. **Practice regularly**: Regex becomes easier with practice

Remember: Regular expressions are powerful but can become complex quickly. When in doubt, break down the problem into smaller parts!