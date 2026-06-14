import time
import quickjs


class JSEngine:
    def __init__(self):
        self.output = []
        self.ctx = quickjs.Context()
        self.ctx.add_callable("_print", self._print)

        # Serialize everything in JS — avoids opaque quickjs Python objects entirely
        self.ctx.eval("""
            var console = {
                log: function() {
                    var parts = [];
                    for (var i = 0; i < arguments.length; i++) {
                        var v = arguments[i];
                        if (v === undefined)       parts.push('undefined');
                        else if (v === null)        parts.push('null');
                        else if (typeof v === 'object') parts.push(JSON.stringify(v));
                        else                        parts.push(String(v));
                    }
                    _print(parts.join(' '));
                }
            };
        """)

    def _print(self, msg):
        # msg is always a string now — quickjs passes None only for JS undefined
        self.output.append("undefined" if msg is None else str(msg))

    def run(self, code: str):
        self.output = []
        start = time.time()
        try:
            self.ctx.eval(code)
            return {
                "status": "SUCCESS",
                "output": "\n".join(self.output),
                "time_ms": round((time.time() - start) * 1000, 2)
            }
        except Exception as e:
            return {
                "status": "ERROR",
                "output": "\n".join(self.output),
                "error": str(e),
                "time_ms": round((time.time() - start) * 1000, 2)
            }