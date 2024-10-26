# Practice questions for Object-Oriented Programming (OOP) in Python

# Basic Concepts
# Classes and Objects

# Define a class called Dog that has attributes for name and age. Create an object of this class and print its attributes.
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Create an object of the Dog class
#     def __str__(self):
#             return f"Name: {self.name}, Age: {self.age}"

# dog = Dog("Buddy", 3)
# print(dog)  # Output: Name: Buddy, Age: 3




# Encapsulation

# Create a class BankAccount with a private attribute balance. Include methods to deposit and withdraw, ensuring that withdrawals do not exceed the balance.

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         # Private attribute
#         self.__balance = initial_balance

#     def deposit(self, amount):
#         """Deposit money into the account."""
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: ${amount}. New balance: ${self.__balance}.")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         """Withdraw money from the account if sufficient balance exists."""
#         if amount > 0:
#             if amount <= self.__balance:
#                 self.__balance -= amount
#                 print(f"Withdrew: ${amount}. New balance: ${self.__balance}.")
#             else:
#                 print("Withdrawal amount exceeds balance.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def get_balance(self):
#         """Return the current balance."""
#         return self.__balance

# # Example usage:
# if __name__ == "__main__":
#     account = BankAccount(100)  # Create an account with an initial balance of $100
#     account.deposit(50)          # Deposit $50
#     account.withdraw(30)         # Withdraw $30
#     account.withdraw(150)        # Attempt to withdraw $150
#     print(f"Current balance: ${account.get_balance()}")  # Check current balance



# Inheritance

# Create a base class Vehicle with attributes make and model. Derive a class Car that adds an attribute num_doors. Instantiate a Car object and print its attributes.

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def display_info(self):
#         """Display vehicle information."""
#         return f"Make: {self.make}, Model: {self.model}"

# class Car(Vehicle):
#     def __init__(self, make, model, num_doors):
#         super().__init__(make, model)  # Initialize attributes from the base class
#         self.num_doors = num_doors

#     def display_info(self):
#         """Display car information, including number of doors."""
#         base_info = super().display_info()
#         return f"{base_info}, Number of Doors: {self.num_doors}"

# # Example usage:
# if __name__ == "__main__":
#     my_car = Car("Toyota", "Corolla", 4)  # Create a Car object
#     print(my_car.display_info())           # Print the car's attributes






# Polymorphism

# Create a base class Shape with a method area(). Derive classes Circle and Rectangle, each implementing the area() method differently. Demonstrate polymorphism by creating a list of shapes and calculating their areas.

# import math

# class Shape:
#     def area(self):
#         """Method to calculate area, to be implemented by subclasses."""
#         raise NotImplementedError("This method should be overridden by subclasses")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         """Calculate the area of the circle."""
#         return math.pi * (self.radius ** 2)

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         """Calculate the area of the rectangle."""
#         return self.width * self.height

# # Example usage:
# if __name__ == "__main__":
#     shapes = [
#         Circle(5),           # Circle with radius 5
#         Rectangle(4, 6),     # Rectangle with width 4 and height 6
#         Circle(3),           # Circle with radius 3
#         Rectangle(2, 8)      # Rectangle with width 2 and height 8
#     ]

#     for shape in shapes:
#         print(f"Area: {shape.area():.2f}")  #


# Intermediate Concepts
# Class vs Instance Variables

# Define a class Employee with a class variable company_name and an instance variable name. Show the difference by creating multiple employee objects and changing the class variable.

# class Employee:
#     # Class variable
#     company_name = "Tech Corp"

#     def __init__(self, name):
#         # Instance variable
#         self.name = name

#     def display_info(self):
#         """Display employee information."""
#         return f"Employee Name: {self.name}, Company: {Employee.company_name}"

# # Example usage:
# if __name__ == "__main__":
#     # Create multiple Employee objects
#     emp1 = Employee("Alice")
#     emp2 = Employee("Bob")
    
#     # Display initial information
#     print(emp1.display_info())
#     print(emp2.display_info())
    
#     # Change the class variable
#     Employee.company_name = "New Tech Inc."

#     # Display information after changing the class variable
#     print("\nAfter changing the company name:")
#     print(emp1.display_info())
#     print(emp2.display_info())
    

# Magic Methods

# Implement a class Vector that supports addition and subtraction using magic methods (__add__ and __sub__). Create instances of Vector and demonstrate the operations.

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         """Add two vectors."""
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented

#     def __sub__(self, other):
#         """Subtract two vectors."""
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return NotImplemented

#     def __repr__(self):
#         """String representation of the vector."""
#         return f"Vector({self.x}, {self.y})"

# # Example usage:
# if __name__ == "__main__":
#     v1 = Vector(2, 3)
#     v2 = Vector(5, 7)

#     # Demonstrating addition
#     v3 = v1 + v2
#     print(f"Addition: {v1} + {v2} = {v3}")

#     # Demonstrating subtraction
#     v4 = v1 - v2
#     print(f"Subtraction: {v1} - {v2} = {v4}")



# Static and Class Methods

# Create a class MathOperations with a static method factorial(n) and a class method from_string(cls, string). The class method should create an instance of the class from a string representation of its attributes.

# class MathOperations:
#     def __init__(self, value):
#         self.value = value

#     @staticmethod
#     def factorial(n):
#         """Calculate the factorial of a non-negative integer n."""
#         if n < 0:
#             raise ValueError("Factorial is not defined for negative numbers.")
#         if n == 0 or n == 1:
#             return 1
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result

#     @classmethod
#     def from_string(cls, string):
#         """Create an instance of MathOperations from a string."""
#         value = int(string)
#         return cls(value)

#     def __repr__(self):
#         """String representation of the MathOperations instance."""
#         return f"MathOperations(value={self.value})"

# # Example usage:
# if __name__ == "__main__":
#     # Using the static method
#     num = 5
#     print(f"Factorial of {num} is {MathOperations.factorial(num)}")

#     # Using the class method to create an instance from a string
#     string_value = "10"
#     math_op = MathOperations.from_string(string_value)
#     print(math_op)  # Output: MathOperations(value=10)



# Advanced Concepts
# Composition vs Inheritance

# Define a class Engine and a class Car that uses Engine as a component (composition). Show how you can instantiate Car objects with different types of Engine.

# class Engine:
#     def __init__(self, engine_type, horsepower):
#         self.engine_type = engine_type
#         self.horsepower = horsepower

#     def __repr__(self):
#         return f"Engine(type={self.engine_type}, horsepower={self.horsepower})"

# class Car:
#     def __init__(self, make, model, engine: Engine):
#         self.make = make
#         self.model = model
#         self.engine = engine  # Composition: Car has an Engine component

#     def display_info(self):
#         """Display information about the car."""
#         return f"Car(make={self.make}, model={self.model}, engine={self.engine})"

# # Example usage:
# if __name__ == "__main__":
#     # Create different types of engines
#     petrol_engine = Engine("Petrol", 150)
#     diesel_engine = Engine("Diesel", 180)
#     electric_engine = Engine("Electric", 200)

#     # Create cars with different engines
#     car1 = Car("Toyota", "Camry", petrol_engine)
#     car2 = Car("Ford", "F-150", diesel_engine)
#     car3 = Car("Tesla", "Model 3", electric_engine)

#     # Display information about the cars
#     print(car1.display_info())
#     print(car2.display_info())
#     print(car3.display_info())



# Abstract Base Classes

# Create an abstract base class Animal with an abstract method sound(). Implement subclasses Dog and Cat that provide their own implementations of sound().

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         """Return the sound made by the animal."""
#         pass

# class Dog(Animal):
#     def sound(self):
#         """Return the sound made by a dog."""
#         return "Woof!"

# class Cat(Animal):
#     def sound(self):
#         """Return the sound made by a cat."""
#         return "Meow!"

# # Example usage:
# if __name__ == "__main__":
#     animals = [Dog(), Cat()]

#     for animal in animals:
#         print(f"A {animal.__class__.__name__} says: {animal.sound()}")




# Error Handling

# Modify the BankAccount class from earlier to raise exceptions for insufficient funds during a withdrawal. Write a test to handle this exception gracefully.

# class InsufficientFundsError(Exception):
#     """Custom exception for insufficient funds."""
#     pass

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.__balance = initial_balance

#     def deposit(self, amount):
#         """Deposit money into the account."""
#         if amount > 0:
#             self.__balance += amount
#         else:
#             raise ValueError("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         """Withdraw money from the account."""
#         if amount > self.__balance:
#             raise InsufficientFundsError("Withdrawal amount exceeds available balance.")
#         elif amount > 0:
#             self.__balance -= amount
#         else:
#             raise ValueError("Withdrawal amount must be positive.")

#     def get_balance(self):
#         """Get the current balance."""
#         return self.__balance

# # Example usage with error handling:
# if __name__ == "__main__":
#     account = BankAccount(100)

#     try:
#         account.withdraw(150)  # This should raise an exception
#     except InsufficientFundsError as e:
#         print(f"Error: {e}")

#     # Valid operations
#     account.deposit(50)
#     print(f"New balance after deposit: ${account.get_balance()}")  # Output: $50

#     try:
#         account.withdraw(30)  # This should succeed
#         print(f"Balance after withdrawal: ${account.get_balance()}")  # Output: $20
#     except InsufficientFundsError as e:
#         print(f"Error: {e}")





# Practical Applications
# Real-world Scenario

# Design a simple library management system with classes for Book, Member, and Library. Include methods for borrowing and returning books, ensuring that a member cannot borrow more than a specified number of books.

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False

#     def __repr__(self):
#         return f"'{self.title}' by {self.author}"


# class Member:
#     def __init__(self, name, max_books=3):
#         self.name = name
#         self.max_books = max_books
#         self.borrowed_books = []

#     def borrow_book(self, book):
#         """Borrow a book from the library."""
#         if len(self.borrowed_books) < self.max_books:
#             if not book.is_borrowed:
#                 self.borrowed_books.append(book)
#                 book.is_borrowed = True
#                 print(f"{self.name} borrowed {book}.")
#             else:
#                 print(f"Sorry, {book} is already borrowed.")
#         else:
#             print(f"{self.name} cannot borrow more than {self.max_books} books.")

#     def return_book(self, book):
#         """Return a borrowed book to the library."""
#         if book in self.borrowed_books:
#             self.borrowed_books.remove(book)
#             book.is_borrowed = False
#             print(f"{self.name} returned {book}.")
#         else:
#             print(f"{self.name} did not borrow {book}.")

#     def list_borrowed_books(self):
#         """List all books borrowed by the member."""
#         return self.borrowed_books


# class Library:
#     def __init__(self):
#         self.books = []
#         self.members = []

#     def add_book(self, book):
#         """Add a book to the library."""
#         self.books.append(book)
#         print(f"Added {book} to the library.")

#     def add_member(self, member):
#         """Add a member to the library."""
#         self.members.append(member)
#         print(f"Added member: {member.name}")

#     def list_books(self):
#         """List all available books in the library."""
#         available_books = [book for book in self.books if not book.is_borrowed]
#         return available_books


# # Example usage:
# if __name__ == "__main__":
#     # Create library
#     library = Library()

#     # Add books to the library
#     book1 = Book("1984", "George Orwell")
#     book2 = Book("To Kill a Mockingbird", "Harper Lee")
#     book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    
#     library.add_book(book1)
#     library.add_book(book2)
#     library.add_book(book3)

#     # Add members
#     member1 = Member("Alice")
#     member2 = Member("Bob", max_books=2)  # Bob can borrow a maximum of 2 books

#     library.add_member(member1)
#     library.add_member(member2)

#     # Members borrow books
#     member1.borrow_book(book1)
#     member1.borrow_book(book2)
#     member1.borrow_book(book3)  # This should fail

#     member2.borrow_book(book1)  # This should fail because book1 is already borrowed
#     member2.borrow_book(book2)

#     # List borrowed books
#     print(f"{member1.name}'s borrowed books: {member1.list_borrowed_books()}")
#     print(f"{member2.name}'s borrowed books: {member2.list_borrowed_books()}")

#     # Members return books
#     member1.return_book(book1)
#     member2.return_book(book2)

#     # Attempt to return a book not borrowed
#     member2.return_book(book1)  # This should fail

#     # List available books
#     print(f"Available books in the library: {library.list_books()}")






# Data Encapsulation with Properties

# Refactor the BankAccount class to use properties for balance instead of direct access. Ensure that balance can only be modified through deposit and withdrawal methods.

# class InsufficientFundsError(Exception):
#     """Custom exception for insufficient funds."""
#     pass

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance  # Using a single underscore for convention

#     @property
#     def balance(self):
#         """Property to get the current balance."""
#         return self._balance

#     def deposit(self, amount):
#         """Deposit money into the account."""
#         if amount > 0:
#             self._balance += amount
#         else:
#             raise ValueError("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         """Withdraw money from the account."""
#         if amount > self._balance:
#             raise InsufficientFundsError("Withdrawal amount exceeds available balance.")
#         elif amount > 0:
#             self._balance -= amount
#         else:
#             raise ValueError("Withdrawal amount must be positive.")

# # Example usage:
# if __name__ == "__main__":
#     account = BankAccount(100)

#     # Display initial balance
#     print(f"Initial balance: ${account.balance}")

#     try:
#         account.withdraw(150)  # This should raise an exception
#     except InsufficientFundsError as e:
#         print(f"Error: {e}")

#     # Valid operations
#     account.deposit(50)
#     print(f"New balance after deposit: ${account.balance}")  # Output: $150

#     try:
#         account.withdraw(30)  # This should succeed
#         print(f"Balance after withdrawal: ${account.balance}")  # Output: $120
#     except InsufficientFundsError as e:
#         print(f"Error: {e}")



# Testing and Validation
# Unit Testing

# Write unit tests for the BankAccount class to validate the functionality of deposit and withdrawal methods, including edge cases like overdrafts.

# class InsufficientFundsError(Exception):
#     """Custom exception for insufficient funds."""
#     pass

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance  # Using a single underscore for convention

#     @property
#     def balance(self):
#         """Property to get the current balance."""
#         return self._balance

#     def deposit(self, amount):
#         """Deposit money into the account."""
#         if amount > 0:
#             self._balance += amount
#         else:
#             raise ValueError("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         """Withdraw money from the account."""
#         if amount > self._balance:
#             raise InsufficientFundsError("Withdrawal amount exceeds available balance.")
#         elif amount > 0:
#             self._balance -= amount
#         else:
#             raise ValueError("Withdrawal amount must be positive.")

# # new file (test_bank_account.py)

# import unittest

# class TestBankAccount(unittest.TestCase):

#     def setUp(self):
#         """Set up a BankAccount instance for testing."""
#         self.account = BankAccount(100)  # Initial balance of $100

#     def test_initial_balance(self):
#         """Test the initial balance of the account."""
#         self.assertEqual(self.account.balance, 100)

#     def test_deposit(self):
#         """Test depositing money into the account."""
#         self.account.deposit(50)
#         self.assertEqual(self.account.balance, 150)

#     def test_deposit_negative_amount(self):
#         """Test depositing a negative amount raises an error."""
#         with self.assertRaises(ValueError):
#             self.account.deposit(-20)

#     def test_withdraw(self):
#         """Test withdrawing money from the account."""
#         self.account.withdraw(30)
#         self.assertEqual(self.account.balance, 70)

#     def test_withdraw_overdraft(self):
#         """Test withdrawing more than the balance raises an error."""
#         with self.assertRaises(InsufficientFundsError):
#             self.account.withdraw(150)

#     def test_withdraw_negative_amount(self):
#         """Test withdrawing a negative amount raises an error."""
#         with self.assertRaises(ValueError):
#             self.account.withdraw(-20)

#     def test_multiple_deposits_and_withdrawals(self):
#         """Test a series of deposits and withdrawals."""
#         self.account.deposit(200)  # Balance should be 300
#         self.account.withdraw(100)  # Balance should be 200
#         self.assertEqual(self.account.balance, 200)

#     def test_withdraw_all_balance(self):
#         """Test withdrawing the entire balance."""
#         self.account.withdraw(100)
#         self.assertEqual(self.account.balance, 0)

# if __name__ == "__main__":
#     unittest.main()

# # python test_bank_account.py  (run this command for testing)




# Documentation

# Document the Shape, Circle, and Rectangle classes using docstrings. Include descriptions of attributes, methods, and example usage.

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     """Abstract base class for all shapes.

#     This class defines the common interface for shapes, requiring 
#     implementations of methods to calculate area and perimeter.

#     Methods
#     -------
#     area() -> float:
#         Calculate the area of the shape.
    
#     perimeter() -> float:
#         Calculate the perimeter of the shape.
#     """

#     @abstractmethod
#     def area(self):
#         """Calculate the area of the shape."""
#         pass

#     @abstractmethod
#     def perimeter(self):
#         """Calculate the perimeter of the shape."""
#         pass


# class Circle(Shape):
#     """Class representing a circle.

#     Attributes
#     ----------
#     radius : float
#         The radius of the circle.

#     Methods
#     -------
#     area() -> float:
#         Calculate the area of the circle.
    
#     perimeter() -> float:
#         Calculate the circumference of the circle.
    
#     Example
#     -------
#     >>> circle = Circle(5)
#     >>> circle.area()
#     78.53981633974483
#     >>> circle.perimeter()
#     31.41592653589793
#     """

#     def __init__(self, radius):
#         """Initialize a Circle with a given radius.

#         Parameters
#         ----------
#         radius : float
#             The radius of the circle.
#         """
#         self.radius = radius

#     def area(self):
#         """Calculate the area of the circle.

#         Returns
#         -------
#         float
#             The area of the circle.
#         """
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         """Calculate the circumference of the circle.

#         Returns
#         -------
#         float
#             The circumference of the circle.
#         """
#         return 2 * math.pi * self.radius


# class Rectangle(Shape):
#     """Class representing a rectangle.

#     Attributes
#     ----------
#     width : float
#         The width of the rectangle.
#     height : float
#         The height of the rectangle.

#     Methods
#     -------
#     area() -> float:
#         Calculate the area of the rectangle.
    
#     perimeter() -> float:
#         Calculate the perimeter of the rectangle.
    
#     Example
#     -------
#     >>> rectangle = Rectangle(4, 6)
#     >>> rectangle.area()
#     24
#     >>> rectangle.perimeter()
#     20
#     """

#     def __init__(self, width, height):
#         """Initialize a Rectangle with a given width and height.

#         Parameters
#         ----------
#         width : float
#             The width of the rectangle.
#         height : float
#             The height of the rectangle.
#         """
#         self.width = width
#         self.height = height

#     def area(self):
#         """Calculate the area of the rectangle.

#         Returns
#         -------
#         float
#             The area of the rectangle.
#         """
#         return self.width * self.height

#     def perimeter(self):
#         """Calculate the perimeter of the rectangle.

#         Returns
#         -------
#         float
#             The perimeter of the rectangle.
#         """
#         return 2 * (self.width + self.height)


# # Example usage
# if __name__ == "__main__":
#     circle = Circle(5)
#     print(f"Circle Area: {circle.area()}")
#     print(f"Circle Perimeter: {circle.perimeter()}")

#     rectangle = Rectangle(4, 6)
#     print(f"Rectangle Area: {rectangle.area()}")
#     print(f"Rectangle Perimeter: {rectangle.perimeter()}")
