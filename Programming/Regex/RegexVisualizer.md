# Regex Pattern Visualizer

This document provides visual representations of common regex patterns to help you understand how they work.

## Basic Pattern Matching

### Simple Character Matching

```
Pattern: cat
```

```
Text:  The cat sat on the mat.
Match:     ███
```

### Character Classes

```
Pattern: [cm]at
```

```
Text:  The cat sat on the mat.
Match:     ███            ███
```

### Negated Character Classes

```
Pattern: [^cm]at
```

```
Text:  The cat sat on the mat rat.
Match:             ███
                           ███
```

## Quantifiers

### Zero or More (*)

```
Pattern: ca*t
```

```
Text:  ct cat caat caaat
Match:  ██ ███ ████ █████
```

### One or More (+)

```
Pattern: ca+t
```

```
Text:  ct cat caat caaat
Match:     ███ ████ █████
```

### Zero or One (?)

```
Pattern: colou?r
```

```
Text:  color colour
Match:  █████ ██████
```

### Exact Count {n}

```
Pattern: a{3}
```

```
Text:  a aa aaa aaaa
Match:        ███ ███
```

## Anchors

### Start of String (^)

```
Pattern: ^The
```

```
Text:  The cat is here. The dog is there.
Match:  ███
```

### End of String ($)

```
Pattern: end$
```

```
Text:  This is the end
Match:             ███
```

## Word Boundaries

### Word Boundary (\b)

```
Pattern: \bcat\b
```

```
Text:  The cat concatenated with cats.
Match:     ███
```

## Character Shortcuts

### Digit (\d)

```
Pattern: \d+
```

```
Text:  There are 123 apples and 456 oranges.
Match:           ███           ███
```

### Word Character (\w)

```
Pattern: \w+
```

```
Text:  Hello, world! 123_test
Match:  █████  █████  ████████
```

### Whitespace (\s)

```
Pattern: \s+
```

```
Text:  Hello   world!
Match:      ███
```

## Grouping and Capturing

### Basic Grouping

```
Pattern: (ab)+
```

```
Text:  ab abab ababab c
Match:  ██ ████ ██████
```

### Alternation

```
Pattern: cat|dog
```

```
Text:  I have a cat and a dog.
Match:          ███       ███
```

## Common Use Cases

### Email Validation

```
Pattern: ^[\w.-]+@[\w.-]+\.\w{2,}$
```

```
Text:  user@example.com
Match:  ████████████████
```

### URL Matching

```
Pattern: https?:\/\/[\w-\.]+\.\w{2,}
```

```
Text:  Visit https://example.com for more info.
Match:       ████████████████
```

### Phone Number Format

```
Pattern: \d{3}-\d{3}-\d{4}
```

```
Text:  Call me at 555-123-4567 anytime.
Match:            ████████████
```

## Lookahead and Lookbehind

### Positive Lookahead

```
Pattern: \w+(?=ing)
```

```
Text:  I am walking and talking.
Match:      ████      ████
```

### Negative Lookahead

```
Pattern: \w+(?!ing)
```

```
Text:  I am walking and talk now.
Match:  █  ██               ████
```

## Interactive Learning

For a more interactive experience with regex patterns, try these online tools:

1. **Regex101**: https://regex101.com/
   - Provides real-time highlighting and explanation

2. **RegExr**: https://regexr.com/
   - Visual testing with reference guide

3. **Regexper**: https://regexper.com/
   - Creates railroad diagrams of your patterns

Remember that visualization is key to understanding regex patterns. Practice by breaking down complex patterns into smaller parts and understanding how each part works.