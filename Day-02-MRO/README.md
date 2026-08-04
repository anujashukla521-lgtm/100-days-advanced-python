# Day 2 – Method Resolution Order (MRO)

## 📚 Topics Covered
- Method Resolution Order (MRO)
- Single Inheritance
- Multiple Inheritance
- Diamond Problem
- C3 Linearization
- `super()`
- `mro()`
- `__mro__`
- Constructor MRO
- Cooperative Multiple Inheritance
- Mixins

## 💻 Practice Files
- Single Inheritance MRO
- Multiple Inheritance MRO
- Diamond Problem
- `super()` with MRO
- `mro()` vs `__mro__`
- Changing Inheritance Order
- Complex MRO
- Constructor MRO
- Logger System (Real-world Example)
- Shape System using Mixins

## 🎯 Key Learnings
- Python follows C3 Linearization to resolve methods.
- `super()` calls the next class in the MRO, not necessarily the parent.
- Every class must call `super()` to maintain the cooperative method chain.
- Mixins provide reusable behavior using multiple inheritance.
- `mro()` and `__mro__` reveal the exact order Python follows for method lookup.

## 🚀 Status
✅ Completed Day 2 successfully.