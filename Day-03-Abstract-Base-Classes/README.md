# Day 3 – Abstract Base Classes (ABC)

## 📚 Topics Covered

* Introduction to Abstract Base Classes (ABC)
* `abc` module
* `ABC` class
* `@abstractmethod` decorator
* Creating abstract classes
* Creating concrete (child) classes
* Method overriding
* Using `super()`
* Constructors in abstract classes
* Abstract classes with normal methods
* Real-world implementation of abstraction

## 💻 Practice Completed

### ✅ Question 1

* Basic Abstract Class
* Implemented `Animal`, `Dog`, and `Cat`

### ✅ Question 2

* Multiple Abstract Methods
* Created abstract methods and implemented them in child classes

### ✅ Question 3

* Abstract Class with Constructor
* Used `super().__init__()` to initialize parent attributes

### ✅ Question 4

* Abstract Class with Normal Method
* Combined abstract and concrete methods in the same class

### ✅ Question 5

* Bank Management System (Mini Project)
* Designed a `BankAccount` abstract class
* Implemented `SavingsAccount` and `CurrentAccount`
* Added deposit and withdrawal functionality
* Implemented overdraft logic for current accounts
* Eliminated duplicate code by moving common `deposit()` logic to the parent class
* Used inheritance, abstraction, method overriding, and constructors effectively

## 🎯 Key Learnings

* Abstract classes define a common contract for subclasses.
* Objects of abstract classes cannot be created.
* Every subclass must implement all abstract methods.
* Shared functionality should be implemented in the parent class to avoid code duplication.
* Different business rules should be implemented through method overriding.
* `super()` helps reuse parent class functionality cleanly.

## 🚀 Outcome

Today strengthened my understanding of abstraction and object-oriented design by building practical examples and a mini project using Abstract Base Classes.
