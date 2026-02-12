# =======================
# Icon Renderer
# =======================

from PIL import Image, ImageDraw, ImageFont

class IconRenderer:
    """Single responsibility: render text icon"""

    def __init__(self, size=32, font_size=22):
        self.size = size
        self.font = self._load_font(font_size)

    def _load_font(self, font_size):
        try:
            return ImageFont.truetype("seguisb.ttf", font_size)
        except:
            return ImageFont.load_default()

    def render(self, text: str, color: str) -> Image.Image:
        img = Image.new("RGBA", (self.size, self.size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text(
            (self.size // 2, self.size // 2),
            text,
            fill=color,
            font=self.font,
            anchor="mm"
        )
        return img
