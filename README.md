# find-text.py

Find-text is a Kicad utility that search text elements in kicad_sch files.

## Usage
python3 find-text.py [-h] [-p0-2]

- -h help
- -p0 - no path
- -p1 - path inline - (default) 
- -p2 - path once

# KiCad Turtle Graphics

This repository contains turtle graphics implementations for KiCad PCB design.

## Python Implementation (kicad_turtle.py)

A Python turtle graphics library for creating PCB traces programmatically.

See `turtle-example1.py`, `turtle-example2.py`, `turtle-example3.py`, and `turtle-example4.py` for usage examples.

## C++ Base Class (kicad_turtle_base.h)

An abstract C++ base class for implementing turtle graphics in KiCad plugins.

### Building the Example

```bash
g++ -std=c++11 -o turtle_example turtle_example.cpp
./turtle_example
```

The base class provides:
- Forward/backward movement
- Left/right turning
- Pen up/down control
- Line width control
- Position and heading getters

Derived classes must implement the `gotoReal()` method to perform actual drawing operations.
