# ⚡ ThunderJS Runtime

ThunderJS is a lightweight JavaScript runtime built using Python and QuickJS.  
It executes JavaScript code inside a sandboxed environment and captures console output.

---

## 🚀 Features

- JavaScript execution using QuickJS
- console.log support
- JSON-safe output handling
- multiprocessing sandbox
- timeout protection
- CLI-based execution

---

## 🏗️ Architecture

JavaScript Code  
→ QuickJS Engine  
→ console.log override  
→ Python callback  
→ Output buffer  
→ Final runtime report

---

## ▶️ How to Run

### Run JS file:

```bash
python -m thunder.main run examples/demo.js