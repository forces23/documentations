![1756231471226](image/basics/1756231471226.png)

# variables

variables in python are very simple there is no need to declare the type when initalizing it.

* type annotations are available but they are optional.
* type annotations do not actually do anything to the code at compilation they will just give you warnings when writing the code

it is smart enough to know what the data type is when you set a value to it.

```python
# python knows that the data type is a string due to the value given 
name = "Bobby"
```

## Constants

declared by making the variable name all caps

* you can also use type annotation my importing this

```python
from typing import Final

VERSION: Final[str] = '1.0.12'
```

# Data Types

## Basic DataTypes

* `int` -> integer numbers
* `float` -> floating-point decimal numbers
* `complex` -> complex numbers (e.g., 3+4j)
* `str` -> string text
* `bool` -> boolean (True/False)

## Collection Data Types (Data Structures)

* `list` -> ordered, mutable sequences
  * Can contain duplicates
  * Items can be changed after creation
* `tuple` -> ordered, immutable sequences
  * Like list but cannot be changed after creation
  * Often used for coordinates, database records
* `set` -> unordered collection of unique elements
  * No duplicates allowed
  * Useful for removing duplicates or membership testing
* `dict` -> key-value pairs (dictionaries)
  * Like objects in JavaScript
  * Keys must be unique and immutable

## Additional Built-in Types

* `bytes` -> immutable byte sequences
* `bytearray` -> mutable byte sequences
* `range` -> sequence of numbers
* `frozenset` -> immutable version of set
* `NoneType` -> represents None/null values

## Examples:

```python
# Basic types
number: int = 10
decimal: float = 1.1
complex_num: complex = 3 + 4j
text: str = "Hello"
activated: bool = True  # Note: True/False are capitalized in Python

# Collection types
names: list = ["bobby", "Caroline", "Lawson"]
coordinates: tuple = (1.2, 2.5)
unique: set = {1, 4, 5, 9}
data: dict = {'name': 'bob', 'age': 30}

# Additional types
byte_data: bytes = b"Hello"
number_range: range = range(1, 10)
nothing: None = None
```

# Functions

in python the key word `def` to declare a function

```python
# the "-> float" is just stating that the return type should be a float. 
# the return type is optional
def add(a:float, b:float) -> float:
    return a + b

def greet(name: str):
    print(f'hello, {name}!')
```

## OOP Core

OOP organizes code into reusable, maintainable, and logical structures that model real-world relationships.

---

### Encapcilation

Encapcilation keeps our attributes safe and allows controlled ways to access and modify them.

### Inheritance

Inheritance is when one class(child/subclass) inherits properties and methods from another class (parent/superclass).

* creates an "is-a" relationship

```python
# Parent class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name
  
    def speak(self):
        pass

# Child class (subclass) inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
```

### Polymorphism

polymorphism means `Many-Forms`. It allows Objects of different Types to be treated as the same type, but behave differently.

```python
# Different classes with same method name
class Circle:
    def __init__(self, radius):
        self.radius = radius
  
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
  
    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")  # Same method call, different behavior
```

![1756211245186](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/Bobby/Desktop/Projects/documentations/Programming/Java/Fundamentals/image/basics/1756211245186.png)

### Abstraction

Abstraction is hiding complex implementation details and showing only essential features to the user

**Real-world example:**

* **Car** - You know how to drive (gas pedal, brake, steering wheel)
* **Hidden complexity** - Engine mechanics, fuel injection, transmission details
* **You interact with** - Simple interface (pedals, wheel)

in Python, abstraction is achieved through:

1. Abstract Classes (using ABC module)

   ```python
   from abc import ABC, abstractmethod

   class Shape(ABC):
       @abstractmethod
       def area(self):
           pass

       @abstractmethod
       def perimeter(self):
           pass

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14159 * self.radius ** 2

       def perimeter(self):
           return 2 * 3.14159 * self.radius
   ```
2. Protocols (Python 3.8+) - Similar to interfaces

   ```python
   from typing import Protocol

   class Drawable(Protocol):
       def draw(self) -> None:
           ...

   class Button:
       def draw(self) -> None:
           print("Drawing button")

   # Button implicitly implements Drawable protocol
   ```

### Class

a class in Python is a blueprint or template for creation of objects

it defines :

* Attributes (fields/variables)
  * what data the object stores
* Methods (functions)
  * what actions the object can perform
* Constructor (`__init__` method)
  * how to create/initialize the object

```python
class Person:
    # Class attribute (shared by all instances)
    species = "Homo sapiens"
  
    # Constructor method
    def __init__(self, name, age):
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age
  
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
  
    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}"
```

To create objects from the class, you simply call the class name :

```python
# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Using methods
print(person1.introduce())  # Hi, I'm Alice and I'm 25 years old
print(person2.have_birthday())  # Happy birthday! Bob is now 31

# Accessing attributes
print(person1.name)  # Alice
print(Person.species)  # Homo sapiens
```

## Dunder Methods (Magic Methods)

Dunder methods are special methods in Python that start and end with double underscores (`__`). They allow you to define how objects behave with built-in operations.

### Common Dunder Methods:

* `__init__()` - Constructor (object initialization)
* `__str__()` - String representation for users
* `__repr__()` - String representation for developers
* `__len__()` - Length of object (used by len())
* `__eq__()` - Equality comparison (==)
* `__lt__()` - Less than comparison (<)
* `__add__()` - Addition operator (+)
* `__sub__()` - Subtraction operator (-)
* `__mul__()` - Multiplication operator (*)
* `__getitem__()` - Index access (obj[key])
* `__setitem__()` - Index assignment (obj[key] = value)
* `__call__()` - Makes object callable like a function

### Example:

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
  
    def __str__(self):
        return f"{self.title} ({self.pages} pages)"
  
    def __len__(self):
        return self.pages
  
    def __eq__(self, other):
        return self.pages == other.pages
  
    def __add__(self, other):
        return self.pages + other.pages

# Usage
book1 = Book("Python Guide", 300)
book2 = Book("Web Dev", 250)

print(book1)           # Python Guide (300 pages)
print(len(book1))      # 300
print(book1 == book2)  # False
print(book1 + book2)   # 550
```
