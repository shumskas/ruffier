from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput  import TextInput
from kivy.uix.scrollview import ScrollView
class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen=screen
        self.direction=direction
        self.goal=goal
    def on_press(self):
        self.screen.manager.transition.direction=self.direction
        self.screen.manager.current=self.goal

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl=BoxLayout(orientation="vertical", padding=8, spacing=80)
        hl=BoxLayout()
        txt=Label(text="Выбери экран")
        vl.add_widget(ScrButton(self,direction="left", goal="first", text="1"))
        vl.add_widget(ScrButton(self, direction="right", goal="second", text="2"))
        vl.add_widget(ScrButton(self, direction="up", goal="third", text="3"))
        vl.add_widget(ScrButton(self, direction="down", goal="fourth", text="4"))
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)
class FirstScr(Screen):
    def __init__(self,**kwargs ):
        super().__init__(**kwargs)  # имя экрана должно передаваться конструктору класса Screen
        vl=BoxLayout(orientation="vertical", padding=8, spacing=8)
        btn_back=ScrButton(self, direction="right", goal="main", text="Назад")
        vl.add_widget(btn_back)
        self.add_widget(vl)

class SecondScr(Screen):
    def __init__(self,**kwargs ):
        super().__init__(**kwargs)  # имя экрана должно передаваться конструктору класса Screen
        vl=BoxLayout(orientation="vertical", padding=8, spacing=8)
        h1_0=BoxLayout(size_hint=(0.8,None), height='30sp')
        h1_0.add_widget(Label(text="password:", halign='right'))
        self.input=TextInput(multiline=False)
        h1_0.add_widget(self.input)
        vl.add_widget(h1_0)
        h1 = BoxLayout()
        self.txt=Label(text="Choice: 2")
        btn_false=Button(text="OK!")
        btn_back=ScrButton(self, direction="left", goal="main", text="Назад")
        vl.add_widget(self.txt)
        h1.add_widget(btn_false)
        h1.add_widget(btn_back)
        vl.add_widget(h1)
        self.add_widget(vl)
        btn_false.on_press=self.change_text
    def change_text(self):
        self.txt.text=self.input.text+"? not working..."
class ThirdScr(Screen):
    def __init__(self,**kwargs ):
        super().__init__(**kwargs)  # имя экрана должно передаваться конструктору класса Screen
        vl=BoxLayout(orientation="vertical", padding=8, spacing=8)
        btn_back=ScrButton(self, direction="down", goal="main", text="Назад")


        a="Screen:3"*200
        self.label=Label(text=a, size_hint_y=None, font_size="24sp",halign="left", valign="top")
        self.label.bind(size=self.resize)
        self.scroll=ScrollView(size_hint=(1,1))
        self.scroll.add_widget(self.label)
        vl.add_widget(btn_back)
        vl.add_widget(self.scroll)
        self.add_widget(vl)
    def resize(self, *args):
        self.label.text_size=(self.label.width, None)
        self.label.texture_update()
        self.label.height=self.label.texture_size[1]
class FourthScr(Screen):
    def __init__(self,**kwargs ):
        super().__init__(**kwargs)  # имя экрана должно передаваться конструктору класса Screen
        vl=BoxLayout(orientation="vertical", padding=8, spacing=8)
        btn_back=ScrButton(self, direction="right", goal="main", text="Назад")
        vl.add_widget(btn_back)
        self.add_widget(vl)
        h1_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        h1_0.add_widget(Label(text="password:", halign='right'))
        self.input = TextInput(multiline=False)
        h1_0.add_widget(self.input)
        vl.add_widget(h1_0)

c