# =======================
# Tray Icon Wrapper
# =======================
import pystray
from .IconRenderer import IconRenderer 

class TrayIcon:
    """Single responsibility: manage a pystray icon"""

    def __init__(self, name: str, renderer: IconRenderer, initial_text: str):
        self.renderer = renderer
        self.icon = pystray.Icon(
            name,
            icon=self.renderer.render(initial_text, "white")
        )

    def update(self, text: str, color: str, tooltip: str):
        self.icon.icon = self.renderer.render(text, color)
        self.icon.title = tooltip

    def set_menu(self, menu):
        self.icon.menu = menu

    def run(self, detached=False):
        if detached:
            self.icon.run_detached()
        else:
            self.icon.run()

    def stop(self):
        self.icon.stop()
