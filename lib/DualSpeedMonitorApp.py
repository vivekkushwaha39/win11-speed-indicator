import threading
import time
import sys
from abc import ABC, abstractmethod
import pystray

from .NetworkSpeedProvider import NetworkSpeedProvider
from  .SpeedFormatter import SpeedFormatter
from .IconRenderer import IconRenderer
from  .TrayIcon import TrayIcon


class DualSpeedMonitorApp:
    """Coordinates everything (no business logic inside)"""

    def __init__(self):
        self.running = True

        self.speed_provider = NetworkSpeedProvider()
        self.formatter = SpeedFormatter()
        self.renderer = IconRenderer()

        self.value_icon = TrayIcon("SpeedValue", self.renderer, "0")
        self.unit_icon = TrayIcon("SpeedUnit", self.renderer, "K")

        menu = pystray.Menu(pystray.MenuItem("Exit", self._on_exit))
        self.value_icon.set_menu(menu)
        self.unit_icon.set_menu(menu)

    def _update_loop(self):
        while self.running:
            kb = self.speed_provider.get_download_kb()
            val, unit, color = self.formatter.format(kb)

            tooltip = f"Download: {kb:.1f} KB/s"

            self.value_icon.update(val, color, tooltip)
            self.unit_icon.update(unit, color, tooltip)

            time.sleep(1)

    def _on_exit(self, icon, item):
        self.running = False
        self.value_icon.stop()
        self.unit_icon.stop()
        sys.exit()

    def run(self):
        threading.Thread(target=self._update_loop, daemon=True).start()
        self.value_icon.run(detached=True)
        self.unit_icon.run()

