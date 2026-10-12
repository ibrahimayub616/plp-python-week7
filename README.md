
# PLP Python Week 7: Shopping List Manager

This project demonstrates Python lists, list methods, loops, conditions, and membership checking.

## Project Files

- `list_warmup.py` - Demonstrates indexing, append(), remove(), and len().
- `shopping_list.py` - Allows users to add, remove, and display shopping items.
- `list_report.py` - Numbers items, counts names with more than four letters, and finds the longest item name.
- `screenshots/` - Contains screenshots of the three programs running.

## Why Check `in` Before Calling `.remove()`?

Checking whether an item exists before removing it makes the program safer. If an item is missing, the `remove()` method raises a `ValueError`. Using `in` allows the program to display a helpful message instead of raising that error.

## How to Run

Run these commands in the project directory:

- `py list_warmup.py`
- `py shopping_list.py`
- `py list_report.py`
