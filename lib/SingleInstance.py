import sys
import ctypes

class SingleInstance:
    def __init__(self, name: str):
        self.mutex = ctypes.windll.kernel32.CreateMutexW(
            None,
            False,
            name
        )

        ERROR_ALREADY_EXISTS = 183
        if ctypes.windll.kernel32.GetLastError() == ERROR_ALREADY_EXISTS:
            print("App already running")
            sys.exit(0)
