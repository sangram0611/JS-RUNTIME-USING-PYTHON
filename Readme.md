⚡ ThunderJS Runtime

A JavaScript Runtime Engine built in Python using QuickJS that executes JavaScript code, simulates console output, and demonstrates real-world interpreter + sandbox architecture design.

🚀 Overview

ThunderJS Runtime is a lightweight JavaScript execution engine written in Python.
It executes JavaScript code inside a controlled environment using the QuickJS engine and simulates how real-world runtimes like Node.js work internally.

This project focuses on:

JavaScript execution model
Runtime architecture design
Sandbox execution system
Output interception and formatting
Interpreter-level thinking
Hackathon Objective

Build a system that:

Accepts JavaScript code as input
Executes it using a non-JavaScript language (Python)
Produces correct output
Supports core JavaScript concepts
Handles execution safely using sandboxing
⚙️ Tech Stack
Python 3
QuickJS (JavaScript Engine)
multiprocessing (Sandbox system)
Custom runtime layer
🧠 System Architecture
JavaScript Code Input
        ↓
Python Runtime (ThunderJS Engine)
        ↓
QuickJS Execution Engine
        ↓
console.log Override (JS Layer)
        ↓
Python Callback (_print function)
        ↓
Output Buffer (Python List)
        ↓
Formatted Output + Execution Report
🔥 Core Features

✔ JavaScript execution in Python
✔ console.log simulation
✔ Variables (let/const) support
✔ Functions & arrow functions
✔ Loops (for/while)
✔ Arrays & objects handling
✔ String & number operations
✔ Boolean & undefined handling
✔ Type coercion support
✔ Sandbox execution using multiprocessing
✔ Timeout protection
✔ Execution reporting system
✔ Multi-test runner support

🧪 Supported JavaScript Concepts
Variables (let, const)
Functions & arrow functions
Loops (for, while)
Arrays & array methods
Objects
Strings methods
Math operations
Boolean logic
Undefined / null handling
console.log simulation
Type coercion
⚙️ How It Works (Internal Flow)
JavaScript code is passed to QuickJS engine
console.log is overridden with Python callback
Output is captured in Python memory
Data types are normalized:
arrays → JSON.stringify
objects → safe string conversion
undefined → "undefined"
boolean → true/false strings
Final output is collected
Execution report is generated
🧪 Example Execution
Input JavaScript
let arr = [1,2,3];
console.log(arr);
console.log("ThunderJS");
Output
[1,2,3]
ThunderJS
📊 Execution Report
------------------------
ThunderJS Runtime Report
------------------------
Status: SUCCESS
Time: 10.25 ms
File: example.js
------------------------
🛡 Sandbox System

ThunderJS uses Python multiprocessing to:

Isolate execution
Prevent infinite loops
Enforce timeout limits
Avoid system crash from unsafe JS

🚀 How to Run
Install dependencies
pip install quickjs
Run JavaScript file
python -m thunder.main run examples/master_test.js
Run tests (if available)
python test_runner.py
🧠 Design Inspiration

This project is inspired by:

Node.js runtime architecture
V8 JavaScript engine concepts
Python interpreter design
Real-world sandbox execution systems

It demonstrates how programming languages are executed internally.
