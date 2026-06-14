import sys
from thunder.sandbox import run_with_timeout


def banner():
    print("""
========================
⚡ ThunderJS Runtime ⚡
A JavaScript Engine in Python
========================
""")


def run_file(file_path):
    banner()

    with open(file_path, "r", encoding="utf-8") as f:
        js_code = f.read()

    result = run_with_timeout(js_code, timeout=1)

    # 🔥 PRINT JS OUTPUT FIRST
    if isinstance(result, dict):
        print("\nOUTPUT:")
        print(result.get("output", ""))

    # 🔥 REPORT SECTION
    print("\n------------------------")
    print("ThunderJS Runtime Report")
    print("------------------------")

    if isinstance(result, dict):
        print("Status:", result.get("status"))

        if result.get("status") == "ERROR":
            print("Error:", result.get("error"))

        print("Time:", result.get("time_ms"), "ms")

    print("File:", file_path)
    print("------------------------")


def main():
    args = sys.argv

    if len(args) < 3:
        print("Usage: python main.py run <file.js>")
        return

    command = args[1]
    file_path = args[2]

    if command == "run":
        run_file(file_path)
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()