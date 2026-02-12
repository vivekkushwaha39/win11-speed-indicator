

import threading
import time
import sys

from lib import DualSpeedMonitorApp
from lib import SingleInstance

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    SingleInstance.SingleInstance("Global\\DualSpeedMonitorTrayApp")
    DualSpeedMonitorApp.DualSpeedMonitorApp().run()
