
# =======================
# Speed Formatter
# =======================

class SpeedFormatter:
    """Single responsibility: format speed into display parts"""

    def format(self, kb: float):
        if kb >= 1024:
            mb = kb / 1024
            val = f"{mb:.1f}" if mb < 10 else f"{int(mb)}"
            color = "#ffaf40" if mb < 5 else "#ff4d4d"
            return val, "M", color

        val = f"{kb:.1f}" if kb < 10 else f"{int(kb)}"
        return val, "K", "white"

