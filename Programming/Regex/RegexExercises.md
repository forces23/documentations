# Regex Exercises for Practice

This document contains exercises to help you practice and master regular expressions. Each exercise includes a problem statement, example inputs/outputs, and a hint. Solutions are provided at the end.

## Beginner Exercises

### Exercise 1: Match All Digits
**Problem**: Write a regex pattern that matches all digits in a string.

**Example**:
- Input: "I have 2 apples and 15 oranges."
- Expected matches: "2", "1", "5"

**Hint**: Use the digit character class.

### Exercise 2: Match Valid Usernames
**Problem**: Write a regex pattern that matches usernames that:
- Start with a letter
- Contain only letters, numbers, and underscores
- Are between 3-16 characters long

**Example**:
- Valid: "user_123", "john_doe", "a_b_c"
- Invalid: "123user", "user-name", "toolongusernamehere12345"

**Hint**: Use anchors, character classes, and quantifiers.

### Exercise 3: Extract Email Domains
**Problem**: Write a regex pattern that extracts the domain part of an email address.

**Example**:
- Input: "Contact us at support@example.com"
- Expected match: "example.com"

**Hint**: Use capturing groups and the @ symbol as a reference point.

### Exercise 4: Match HTML Tags
**Problem**: Write a regex pattern that matches simple HTML tags.

**Example**:
- Input: "<p>This is a paragraph.</p> <div>This is a div.</div>"
- Expected matches: "<p>", "</p>", "<div>", "</div>"

**Hint**: Use character classes and escape special characters.

### Exercise 5: Validate Phone Numbers
**Problem**: Write a regex pattern that matches phone numbers in these formats:
- (123) 456-7890
- 123-456-7890

**Example**:
- Valid: "(555) 123-4567", "555-123-4567"
- Invalid: "5551234567", "555 123 4567"

**Hint**: Use alternation (|) and escape special characters.

## Intermediate Exercises

### Exercise 6: Match Dates
**Problem**: Write a regex pattern that matches dates in MM/DD/YYYY format.

**Example**:
- Valid: "12/31/2022", "01/01/2000"
- Invalid: "13/01/2022", "01/32/2022", "1/1/2022"

**Hint**: Use character classes with ranges and anchors.

### Exercise 7: Extract URLs
**Problem**: Write a regex pattern that extracts URLs from text.

**Example**:
- Input: "Visit https://example.com or http://test.org for more info."
- Expected matches: "https://example.com", "http://test.org"

**Hint**: Use alternation for http/https and character classes for domain parts.

### Exercise 8: Password Validation
**Problem**: Write a regex pattern that validates passwords with these rules:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (!@#$%^&*)

**Example**:
- Valid: "Password1!", "Secure@123"
- Invalid: "password", "PASSWORD", "12345678", "Pass word"

**Hint**: Use positive lookaheads for each requirement.

### Exercise 9: Remove Extra Whitespace
**Problem**: Write a regex pattern to replace multiple spaces with a single space.

**Example**:
- Input: "This   has    too    many    spaces."
- Expected output: "This has too many spaces."

**Hint**: Use the whitespace character class with a quantifier.

### Exercise 10: Match IP Addresses
**Problem**: Write a regex pattern that matches IPv4 addresses.

**Example**:
- Valid: "192.168.1.1", "10.0.0.255"
- Invalid: "256.0.0.1", "192.168.1", "192.168.1.1.1"

**Hint**: Use character classes with ranges and anchors.

## Advanced Exercises

### Exercise 11: Match Balanced Parentheses
**Problem**: Write a regex pattern that matches text within balanced parentheses.

**Example**:
- Input: "This (is a test) with (multiple) parentheses."
- Expected matches: "(is a test)", "(multiple)"

**Hint**: Use non-greedy quantifiers.

### Exercise 12: Extract CSS Color Codes
**Problem**: Write a regex pattern that matches CSS hex color codes.

**Example**:
- Input: "The colors are #FFF, #123456, and #A1B2C3."
- Expected matches: "#FFF", "#123456", "#A1B2C3"

**Hint**: Use character classes with hexadecimal digits and alternation for different formats.

### Exercise 13: Match Valid JSON Keys
**Problem**: Write a regex pattern that matches valid JSON property keys (with their quotes).

**Example**:
- Input: '{"name": "John", "age": 30, "city": "New York"}'
- Expected matches: '"name"', '"age"', '"city"'

**Hint**: Use character classes and escape special characters.

### Exercise 14: Extract Markdown Links
**Problem**: Write a regex pattern that extracts links from Markdown text.

**Example**:
- Input: "Check out [Google](https://www.google.com) or [GitHub](https://github.com)."
- Expected matches: "[Google](https://www.google.com)", "[GitHub](https://github.com)"

**Hint**: Use capturing groups and non-greedy quantifiers.

### Exercise 15: Validate Semantic Versioning
**Problem**: Write a regex pattern that validates semantic version numbers (MAJOR.MINOR.PATCH).

**Example**:
- Valid: "1.0.0", "2.10.5", "0.0.1"
- Invalid: "1.0", "1.0.0.0", "01.1.1"

**Hint**: Use anchors and character classes with quantifiers.

## Solutions

<details>
<summary>Click to reveal solutions</summary>

### Exercise 1: Match All Digits
```javascript
const pattern = /\d/g;
```

### Exercise 2: Match Valid Usernames
```javascript
const pattern = /^[a-zA-Z][a-zA-Z0-9_]{2,15}$/;
```

### Exercise 3: Extract Email Domains
```javascript
const pattern = /@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$/;
// Use match[1] to get the captured group
```

### Exercise 4: Match HTML Tags
```javascript
const pattern = /<\/?[a-zA-Z][a-zA-Z0-9]*>/g;
```

### Exercise 5: Validate Phone Numbers
```javascript
const pattern = /^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$/;
```

### Exercise 6: Match Dates
```javascript
const pattern = /^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{4}$/;
```

### Exercise 7: Extract URLs
```javascript
const pattern = /https?:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;
```

### Exercise 8: Password Validation
```javascript
const pattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$/;
```

### Exercise 9: Remove Extra Whitespace
```javascript
const pattern = /\s+/g;
// Use with: text.replace(pattern, ' ');
```

### Exercise 10: Match IP Addresses
```javascript
const pattern = /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
```

### Exercise 11: Match Balanced Parentheses
```javascript
const pattern = /\([^()]*\)/g;
// Note: This only works for non-nested parentheses
```

### Exercise 12: Extract CSS Color Codes
```javascript
const pattern = /#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})/g;
```

### Exercise 13: Match Valid JSON Keys
```javascript
const pattern = /"[^"\\]*(?:\\.[^"\\]*)*"/g;
```

### Exercise 14: Extract Markdown Links
```javascript
const pattern = /\[([^\]]+)\]\(([^)]+)\)/g;
```

### Exercise 15: Validate Semantic Versioning
```javascript
const pattern = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/;
```
</details>

## Next Steps

After completing these exercises, try:

1. Creating your own regex patterns for specific use cases
2. Refactoring existing code to use regex for validation or extraction
3. Exploring more advanced regex features like lookaheads and lookbehinds
4. Practicing with real-world data validation scenarios

Remember that regular expressions are powerful but can become complex. Always test your patterns thoroughly with various inputs!