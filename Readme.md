# ⚡ ThunderJS Runtime

A sandboxed JavaScript execution engine built in Python — runs JS code through QuickJS, intercepts output at the interpreter level, and reports execution results with full type normalization.

---

## What It Actually Does

Most people think "running JavaScript" means a browser or Node.js. ThunderJS proves otherwise.

It embeds a full JavaScript engine (QuickJS) inside Python, intercepts `console.log` at the C-binding layer, normalizes every JS type into human-readable output, and wraps the entire execution in an OS-level process sandbox with timeout enforcement.

No browser. No Node. Pure Python → JS execution pipeline.

---

## Architecture

```
JavaScript Source Code
        │
        ▼
┌─────────────────────────┐
│   Sandbox Layer         │  ← multiprocessing isolates execution
│   (Process Boundary)    │    enforces timeout, prevents crashes
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   ThunderJS Engine      │  ← Python runtime orchestrator
│   (JSEngine class)      │    owns QuickJS context lifecycle
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   QuickJS Context       │  ← embedded C-level JS engine
│   ctx.eval(code)        │    executes actual JavaScript
└────────────┬────────────┘
             │
        console.log called
             │
             ▼
┌─────────────────────────┐
│   JS-layer Override     │  ← console.log replaced at JS boot
│   arguments → string    │    handles variadic args, all types
└────────────┬────────────┘
             │
        _print() callback
             │
             ▼
┌─────────────────────────┐
│   Python Output Buffer  │  ← list collects each line
│   Type Normalization    │    array→JSON, bool→lowercase, etc.
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Execution Report      │  ← status, time_ms, output, errors
└─────────────────────────┘
```

---

## Why Each Layer Exists

**QuickJS over a Python JS parser** — QuickJS is a complete, spec-compliant JS engine in C. It handles closures, prototypes, coercion, and the full ES2020 spec correctly. Writing that from scratch would be months of work.

**console.log override in JS, not Python** — JS arrays and objects cross the Python boundary as opaque C pointers. Trying to serialize them in Python produces garbage (`<_quickjs.Object at 0x...>`). By running `JSON.stringify` inside JS before handing the string to Python, the boundary is clean.

**multiprocessing sandbox over threading** — `threading` shares memory; a runaway JS loop starves the whole process. `multiprocessing` gives a true OS process boundary — the sandbox dies, the host lives.

**Output buffer over stdout capture** — redirecting stdout is fragile and can break logging, error reporting, and test frameworks. A Python list as the buffer gives fine-grained control per execution.

---

## Type Normalization Table

| JS Value | Raw Python Receives | ThunderJS Outputs |
|---|---|---|
| `[1,2,3]` | opaque object | `[1,2,3]` |
| `{a:1}` | opaque object | `{"a":1}` |
| `true` / `false` | `True` / `False` | `true` / `false` |
| `undefined` | `None` | `undefined` |
| `null` | `None` | `null` |
| `NaN` | `nan` | `NaN` |
| `"hello"` | `"hello"` | `hello` |
| `42` | `42` | `42` |

---

## Supported JavaScript

| Category | Features |
|---|---|
| Declarations | `let`, `const`, `var` |
| Types | `number`, `string`, `boolean`, `null`, `undefined`, `object`, `array` |
| Operators | arithmetic, comparison, logical, assignment, ternary, spread `...` |
| Control flow | `if/else if/else`, `switch`, ternary |
| Loops | `for`, `while`, `do...while` |
| Functions | declarations, expressions, arrow functions, callbacks, rest params |
| Arrays | `push`, `pop`, `shift`, `unshift`, `slice`, `splice`, `concat`, `includes`, `indexOf`, `sort`, `reverse`, `map`, `filter`, `reduce`, `find`, `some`, `every` |
| Strings | `trim`, `toUpperCase`, `toLowerCase`, `replace`, `replaceAll`, `substring`, `slice`, `split`, `includes`, `startsWith`, `endsWith`, `indexOf` |
| Objects | literals, dot/bracket notation, `Object.keys`, spread, destructuring |
| Built-ins | `Math`, `Date`, `JSON`, `Array.isArray`, `Number.isNaN`, `parseInt`, `parseFloat` |
| Coercion | type casting, `==` vs `===`, implicit conversions |

---

## Installation

```bash
pip install quickjs
```

---

## Usage

**Run a JS file:**
```bash
python -m thunder.main run examples/script.js
```

**Example input** (`script.js`):
```javascript
let arr = [1, 2, 3];
console.log(arr);
console.log(arr.map(x => x * 2));
console.log("ThunderJS");
```

**Output:**
```
[1,2,3]
[2,4,6]
ThunderJS

──────────────────────────
 ThunderJS Execution Report
──────────────────────────
 Status  : SUCCESS
 Time    : 8.42 ms
 File    : script.js
──────────────────────────
```



---

## Tech Stack

| Component | Technology | Role |
|---|---|---|
| Host language | Python 3 | Orchestration, I/O, sandboxing |
| JS engine | QuickJS (via `quickjs` binding) | JavaScript execution |
| Sandbox | `multiprocessing` | Process isolation + timeout |
| Serialization | `json` + JS `JSON.stringify` | Cross-boundary type normalization |

---

## Design Inspiration

ThunderJS mirrors the internal architecture of production runtimes:

- **Node.js** — embeds V8 (C++ JS engine) inside a C++ host with JS API overrides
- **Deno** — embeds V8 inside Rust with sandboxed system calls
- **ThunderJS** — embeds QuickJS inside Python with sandboxed process execution

The core idea is identical: a host language wraps a JS engine, intercepts I/O at the boundary, and exposes controlled APIs. ThunderJS is that architecture in its simplest, most readable form.


<img width="2720" height="1360" alt="thunderjs_banner" src="https://github.com/user-attachments/assets/416bf9dd-dd32-496a-a113-98a534755e14" />

