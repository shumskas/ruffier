from scrollLabel import ScrollLabel
from kivy.clock import Clock
from kivy.properties import BooleanProperty

class Seconds(ScrollLabel):
    done=BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.done=False
        self.current=0
        self.total=total
        text="Прошло секунд: "+str(self.current)
        super().__init__(text, **kwargs)
    def restart(self, total, **kwargs ):
        self.done=False
        self.current = 0
        self.total = total
        self.set_text("Прошло секунд: "+str(self.current))
        self.start()
    def start(self):
        Clock.schedule_interval(self.change,1)
    def change(self, dt):
        self.current += 1
        self.set_text("Прошло секунд: " + str(self.current))
        if self.current >= self.total:
            self.done=True
            return False
