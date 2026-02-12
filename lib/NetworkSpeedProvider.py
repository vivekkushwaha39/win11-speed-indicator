import psutil
# =======================
# Speed Provider
# =======================

class NetworkSpeedProvider:
    """Single responsibility: measure network speed"""
    def __init__(self):
        self._last_recv = psutil.net_io_counters().bytes_recv

    def get_download_kb(self) -> float:
        current = psutil.net_io_counters().bytes_recv
        diff = (current - self._last_recv) / 1024
        self._last_recv = current
        return diff

