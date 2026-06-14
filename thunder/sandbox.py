import multiprocessing
from thunder.engine import JSEngine


def _run_js(code, output_queue):
    try:
        engine = JSEngine()
        result = engine.run(code)
        output_queue.put(result)
    except Exception as e:
        output_queue.put({
            "status": "ERROR",
            "output": "",
            "error": str(e),
            "time_ms": 0
        })


def run_with_timeout(code, timeout=1):
    queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=_run_js,
        args=(code, queue)
    )

    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        return {
            "status": "TIMEOUT",
            "output": "",
            "time_ms": timeout * 1000
        }

    # 🔥 SAFE FETCH (IMPORTANT FIX)
    if queue.empty():
        return {
            "status": "ERROR",
            "output": "",
            "error": "No output from engine",
            "time_ms": 0
        }

    return queue.get()