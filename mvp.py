from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput  import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from instructions import*
from scrollLabel import ScrollLabel
from ryphe import test
from seconds import Seconds
from seats import Seats
from runner import Runner
from l import Colored_layout
name=""
age=0
p1=0
p2=0
p3=0
Window.clearcolor=(0.5, 0.5, 0.5, 1)
def check_int(num):
    try:
        return int(num)
    except:
        return False
def get_result():
    res=test(p1,p2,p3,age)
    return name+"\n"+res[0]+"\n"+res[1]
class Instr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr=ScrollLabel(txt_instruction)
        lb1=Label(text="Имя:", halign="right")
        self.in_name=TextInput(multiline=False)
        lb2 = Label(text="Возраст:", halign="right")
        self.in_age = TextInput(multiline=False)
        self.btn=Button(text="Начать", size_hint=(0.3, 0.2), pos_hint={"center_x" : 0.5})
        self.btn.background_color=self.btn.color
        self.btn.on_press=self.next
        line1=BoxLayout(size_hint=(0.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line1.add_widget(lb1)
        line1.add_widget(self.in_name)
        line1.add_widget(lb2)
        line1.add_widget(self.in_age)
        outer=BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global age, name
        name=self.in_name.text
        age=check_int(self.in_age.text)
        if age<7 or age==False:
            age=7
            self.in_age.text=str(age)
            popup=Popup(title="Ошибка", content=Label(text="Возраст должен быть  от 7 лет"),
                        size_hint=(None, None), size=(600,400), pos_hint={"center_x":0.5,
                                                                           "center_y":0.5})
            popup.open()
        else:
            self.manager.current="pulse1"

class PulseScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        instr = ScrollLabel(txt_test1)
        lbl1 = ScrollLabel("Считайте пульс")
        self.lbl_sec=Seconds(15)
        self.next_screen=False
        self.lbl_sec.bind(done=self.seconds_finish)

        line=Colored_layout(l_color=(0.5, 0.7, 0.5, 1))
        vlayout=Colored_layout(l_color=(0.5, 0.5, 0.5, 1), orientation="vertical")
        vlayout.add_widget(lbl1)
        vlayout.add_widget(self.lbl_sec)
        line.add_widget(instr)
        line.add_widget(vlayout)

        line2=BoxLayout(size_hint=(0.8, None), height="30sp")
        lb_result=Label(text="Введите результат", halign="right")
        self.in_result = TextInput(multiline=False, text="0")
        self.in_result.set_disabled(True)

        line2.add_widget(lb_result)
        line2.add_widget(self.in_result)


        self.btn=Button(text="Начать", pos_hint={"center_x":0.5})
        self.btn.on_press=self.next
        self.line3=BoxLayout(size_hint=(0.6, None), height="80sp", pos_hint={"center_x":0.5})
        self.line3.add_widget(self.btn)
        main_layout=BoxLayout(orientation="vertical", padding=8, spacing=8)
        main_layout.add_widget(line)
        main_layout.add_widget(line2)
        main_layout.add_widget(self.line3)
        self.add_widget(main_layout)

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1=check_int(self.in_result.text)
            if p1<0 or p1==False:
                p=0
                self.in_result.text=str(p1)
                popup = Popup(title="Ошибка", content=Label(text="Введите верное значение"),
                              size_hint=(None, None), size=(600, 400), pos_hint={"center_x": 0.5,
                                                                                 "center_y": 0.5})
                popup.open()
            else:
                self.manager.current="sits"
    def seconds_finish(self, *args):
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text="Дальше"
        self.next_screen=True
        self.line3.remove_widget(self.btn)
        self.btn_back=Button(text="Назад")
        self.line3.add_widget(self.btn_back)
        self.line3.add_widget(self.btn)
        self.btn_back.on_press=self.back
    def back(self):
        self.manager.current = self.manager.previous()
class Checksits(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        instr = ScrollLabel(txt_sits)
        lbl=ScrollLabel("Сделайте 30 приседаний")
        self.lbl_seats=Seats(30)
        self.run=Runner()
        self.run.bind(finish=self.run_finished)

        line = Colored_layout(l_color=(0.5, 0.7, 0.5, 1))
        vlayout = BoxLayout(orientation="vertical")
        vlayout.add_widget(lbl)
        vlayout.add_widget(self.lbl_seats)
        line.add_widget(instr)
        line.add_widget(vlayout)
        line.add_widget(self.run)

        self.next_screen=False
        self.btn = Button(text="Дальше", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.on_press = self.next
        main_layout = BoxLayout(orientation="vertical", padding=8, spacing=8)
        main_layout.add_widget(line)
        main_layout.add_widget(self.btn)
        self.add_widget(main_layout)
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_seats.next)
        else:
            self.manager.current = "pulse2"
    def run_finished(self, instance, value):
        self.btn.set_disabled(False)
        self.btn.text="Продолжить"
        self.next_screen=True
class PulseScreen2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.next_screen=False
        self.stage=0
        self.lbl1 = ScrollLabel("Считайте пульс")
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finish)
        instr = ScrollLabel(txt_test3)
        line0=Colored_layout(l_color=(0.5, 0.7, 0.5, 1))
        vl=Colored_layout(l_color=(0.5, 0.7, 0.5, 1), orientation="vertical")
        vl.add_widget(self.lbl1)
        vl.add_widget(self.lbl_sec)
        line0.add_widget(instr)
        line0.add_widget(vl)
        line=BoxLayout(size_hint=(0.8, None), height="30sp")
        lb_result=Label(text="Введите результат", halign="right")
        self.in_result = TextInput(multiline=False, text="0")
        line.add_widget(lb_result)
        line.add_widget(self.in_result)

        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        lb_result2 = Label(text="Введите результат", halign="right")
        self.in_result2 = TextInput(multiline=False, text="0")
        line2.add_widget(lb_result2)
        line2.add_widget(self.in_result2)

        self.btn=Button(text="Закончить", size_hint=(0.3, 0.2), pos_hint={"center_x":0.5})
        self.btn.on_press=self.next
        main_layout=BoxLayout(orientation="vertical", padding=8, spacing=8)
        main_layout.add_widget(line0)
        main_layout.add_widget(line)
        main_layout.add_widget(line2)
        main_layout.add_widget(self.btn)
        self.add_widget(main_layout)
    def sec_finish(self, instance, value):
        if value:
            if self.stage==0:
                self.stage=1
                self.lbl1.set_text("Отдыхайте")
                self.lbl_sec.restart(30)
                self.in_result.set_disabled(False)
            elif self.stage==1:
                self.stage=2
                self.lbl1.set_text("Измерить пульс")
                self.lbl_sec.restart(15)
            elif self.stage==2:
                self.stage=3
                self.lbl1.set_text("Вы закончили")
                self.btn.set_disabled(False)
                self.in_result2.set_disabled(False)
                self.btn.text="Результат"
                self.next_screen=True


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()

        else:
            global p2, p3
            p2=check_int(self.in_result.text)
            p3 = check_int(self.in_result.text)
            if p2==False and p3==False:
                p2=0
                p3=0
                self.in_result2.text=str(p2)
                self.in_result.text = str(p3)
                popup = Popup(title="Ошибка", content=Label(text="Введите верное значение"),
                              size_hint=(None, None), size=(600, 400), pos_hint={"center_x": 0.5,
                                                                                 "center_y": 0.5})
                popup.open()
            elif p2==False:
                p2 = 0
                self.in_result.text = str(p2)
            elif p3==False:
                p3 = 0
                self.in_result.text = str(p3)
            else:
                self.in_result2.text = str(0)
                self.in_result.text = str(0)
                self.manager.current="result"

class Result(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.instr = ScrollLabel("")
        self.main_layout=BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.main_layout.add_widget(self.instr)
        self.add_widget(self.main_layout)
        self.on_enter=self.before
    def before(self):
        self.instr.set_text(get_result())

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Instr(name="main"))
        sm.add_widget(PulseScreen(name="pulse1"))
        sm.add_widget(Checksits(name="sits"))
        sm.add_widget(PulseScreen2(name="pulse2"))
        sm.add_widget(Result(name="result"))
        return sm

app = MyApp()
app.run()