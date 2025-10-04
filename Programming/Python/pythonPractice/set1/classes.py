'''
    🔹 Question 5 — Classes

    Define a class BankAccount with:

    attributes: owner, balance

    methods: deposit(amount), withdraw(amount) (don’t allow overdrafts), __str__() to show balance.

    Example:

    acct = BankAccount("Alice", 100)
    acct.deposit(50)      
    acct.withdraw(30)     
    print(acct)  # -> "Alice's balance: 120"
'''

# i dont remeber anything on classes and how to build them

''' 
🔹 Practice Question

Question — Classes

Define a class Dog with:

attributes: name, age

methods:

bark() → prints "Woof! My name is <name>!"

have_birthday() → increases the dog’s age by 1

__str__() → returns a string like: "<name> is <age> years old"

Example:
fido = Dog("Fido", 3)
fido.bark()               # Woof! My name is Fido!
fido.have_birthday()
print(fido)               # Fido is 4 years old
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"Woof! My name is {self.name}!")
    
    def have_birthday(self):
        self.age += 1

    def __str__(self):
        return f"{self.name} is {self.age} {'years' if self.age > 1 else 'year'} old"

fido = Dog("Fido", 1)
fido.bark()
print(fido)
fido.have_birthday()
print(fido)
