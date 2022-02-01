from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
class Runner(BoxLayout):
    value=NumericProperty(0)
    finish=BooleanProperty(False)
    def __init__(self, total=30, steptime=1.5,
                 autorepeat=True, bcolor=(0.2, 1, 0, 1),
                 btext="Приседание", **kw):
        super().__init__(**kw)
        self.total=total
        self.autorepeat=autorepeat
        self.btext=btext
        self.animation=Animation(pos_hint={"top": 0.1}, duration=steptime/2)+Animation(pos_hint={"top": 1.0}, duration=steptime/2)
        self.animation.on_progress=self.next
        self.btn=Button(size_hint=(1, 0.1), pos_hint={"top":1.0}, background_color=bcolor)
        self.add_widget(self.btn)
    def start(self):
        self.value=0
        self.finish=False
        self.btn.text=self.btext
        if self.autorepeat:
            self.animation.repeat=True
        self.animation.start(self.btn)
    def next(self, widget, step):
        if step==1:
            self.value+=1
            if self.total<=self.value:
                self.animation.repeat=False
                self.finish = True
