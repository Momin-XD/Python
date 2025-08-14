
# Module_3

This module provides a comprehensive introduction to Python's core data structures: **Lists**, **Tuples & Sets**, and **Dictionaries**. Each file demonstrates creation, manipulation, and common operations for its respective data structure.

## Contents

- `list.py`: Examples and operations for Python lists.
- `Tuples&Set.py`: Examples and operations for tuples and sets.
- `dictionaries.py`: Examples and operations for dictionaries.

## Differentiation Table: List vs Tuple vs Set vs Dictionary

| Feature         | List                | Tuple               | Set                 | Dictionary                |
|----------------|---------------------|---------------------|---------------------|---------------------------|
| Ordered        | Yes                 | Yes                 | No                  | Yes                       |
| Mutable        | Yes                 | No                  | Yes                 | Yes (values only)         |
| Duplicates     | Allowed             | Allowed             | Not allowed         | Keys not allowed          |
| Indexing       | Yes                 | Yes                 | No                  | Keys (not index)          |
| Syntax         | [ ]                 | ( )                 | { }                 | {key: value}              |
| Use Case       | Collections         | Fixed collections   | Unique items        | Key-value pairs           |

## Usage

### Lists (`list.py`)
- Create, access, modify, and remove elements.
- Add elements with `append`, `extend`, `insert`.
- Concatenate, repeat, and slice lists.
- Use built-in methods: `sort`, `reverse`, `index`, `count`, `copy`.
- Work with nested lists and perform numerical operations.

### Tuples & Sets (`Tuples&Set.py`)
- Tuples: Immutable, ordered collections. Supports indexing, slicing, unpacking, and methods like `count` and `index`.
- Sets: Unordered, mutable collections of unique items. Supports add, remove, union, intersection, difference, and conversion from lists. Includes `frozenset` (immutable set).

### Dictionaries (`dictionaries.py`)
- Store key-value pairs.
- Access, add, update, and remove items.
- Use methods like `get`, `update`, `pop`, `keys`, `values`, `items`.
- Support for nested dictionaries and various key types (tuple, int, float, string, bool).
