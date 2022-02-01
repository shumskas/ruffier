from scrollLabel import ScrollLabel
class Seats(ScrollLabel):
    def __init__(self, total, **kw):
        self.current = 0
        self.total = total
        text = "Приседаний осталось: " + str(self.total)
        super().__init__(text, **kw)

    def next(self, *args):
        self.current +=1
        left=max(self.total-self.current,0)
        text = "Приседаний осталось: " + str(left)
        super().set_text(text)
