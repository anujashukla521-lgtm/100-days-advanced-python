# Day 5 — Magic (Dunder) Methods

## 📚 Topic

Magic (Dunder) Methods in Python

## 🎯 Objective

Understand how Python's special methods allow custom objects to interact with built-in functions, operators, and Python syntax.

## 🧠 Concepts Covered

* What are magic/dunder methods?
* `__init__()` — object initialization
* `__str__()` — user-friendly object representation
* `__repr__()` — developer-friendly representation
* `__add__()` — operator overloading with `+`
* `__eq__()` — equality comparison
* `__gt__()` / `__lt__()` — comparison operators
* `__len__()` — making objects work with `len()`
* `__getitem__()` — making objects subscriptable
* `__contains__()` — customizing the `in` operator
* `__call__()` — making objects callable
* Understanding that redefining the same method replaces the previous definition

## 💻 Practice

Completed 8 practice problems covering:

1. Student representation using `__str__()` and `__repr__()`
2. Money addition using `__add__()`
3. Student comparison using comparison dunder methods
4. Playlist length using `__len__()`
5. Custom list indexing using `__getitem__()`
6. Course membership using `__contains__()`
7. Callable Calculator using `__call__()`
8. BankAccount mini-project combining multiple dunder methods

## 🔑 Key Takeaway

Dunder methods allow custom Python objects to behave naturally with Python's built-in syntax and operations.

For example:

```text
print(obj)       → obj.__str__()
obj1 + obj2      → obj1.__add__(obj2)
obj1 == obj2     → obj1.__eq__(obj2)
obj1 > obj2      → obj1.__gt__(obj2)
len(obj)         → obj.__len__()
obj[index]       → obj.__getitem__(index)
item in obj      → obj.__contains__(item)
obj()            → obj.__call__()
```

## ✅ Status

Day 5 completed successfully.

**Progress: 5/100 Days**
