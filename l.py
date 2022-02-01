from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color,Rectangle
class Colored_layout(BoxLayout):
    def __init__(self, l_color=(0.7, 0, 0, 1), **kw):
        super().__init__(**kw)
        self.padding="10dp"
        with self.canvas.before:
            Color(*l_color)
            self.rect=Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, instance, value):
        self.rect.pos=instance.pos
        self.rect.size=instance.size
