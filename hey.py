from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Rectangle

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
# egg
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 540)
Config.set('graphics', 'height', 800)


class CalculatorApp(App):
    def set_background(self, *args):
        self.root_window.bind(size=self.do_resize)
        with self.root_window.canvas.before:
            self.bg = Rectangle(source='catscalc.jpg', pos=(0, 0), size=(self.root_window.size))

    def do_resize(self, *args):
        self.bg.size = self.root_window.size

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if self.formula[-1] in ['*', '/', '+', '-', 'в степ.', 'корень из ']:
            self.formula = self.formula[:-1]
        if str(instance.text) == 'x':
            self.formula += '*'
        else:
            self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        if 'в степ.' in self.formula:
            self.formula = self.formula.replace('в степ.', '**')
        elif 'корень из ' in self.formula:
            self.formula = self.formula.replace('корень из ', '')
            self.formula += '**(0.5)'
        self.formula = str(eval(self.formula))
        if '.' in self.formula:
            self.test_float = (self.formula).split('.')[1]
            if self.test_float == '0':
                self.formula = str(((self.formula).split('.'))[0])
        self.update_label()

    def del_text(self, instance):
        self.formula = '0'
        self.update_label()

    def add_float(self, instance):
        if self.formula[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            self.formula += '.'
            self.update_label()

    def x2_but(self, instance):
        self.formula += 'в степ.'
        self.update_label()

    def sqrt_but(self, instance):
        self.formula = 'корень из '
        self.update_label()

    def back_but(self, instance):
        self.formula = self.formula[:-1]
        self.update_label()

    def build(self):
        Clock.schedule_once(self.set_background, 0)
        self.formula = '0'
        b1 = BoxLayout(orientation='vertical', padding=15)
        g1 = GridLayout(cols=4, spacing=1, size_hint=(1, .6))

        self.lbl = Label(text='0', font_size=50, halign='right', valign='top', size_hint=(1, .8),
                         text_size=(540 - 30, 1000 * .4 - 30))

        b1.add_widget(self.lbl)

        btn1 = (Button(text='C', font_size=40, background_color=[1, 0, 1, .25], on_press=self.del_text))
        btn2 = (Button(text='x2', font_size=40, background_color=[1, 0, 1, .25], on_press=self.x2_but))
        btn3 = (Button(text='sqrt', font_size=40, background_color=[1, 0, 1, .25], on_press=self.sqrt_but))
        btn4 = (Button(text='/', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_operation))

        btn5 = (Button(text='7', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn6 = (Button(text='8', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn7 = (Button(text='9', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn8 = (Button(text='x', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_operation))

        btn9 = (Button(text='4', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn10 = (Button(text='5', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn11 = (Button(text='6', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn12 = (Button(text='-', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_operation))

        btn13 = (Button(text='1', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn14 = (Button(text='2', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn15 = (Button(text='3', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn16 = (Button(text='+', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_operation))

        btn17 = (Button(text='<', font_size=40, background_color=[.9, .9, .9, .2], on_press=self.back_but))
        btn18 = (Button(text='0', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_number))
        btn19 = (Button(text=',', font_size=40, background_color=[1, 0, 1, .25], on_press=self.add_float))
        btn20 = (Button(text='=', font_size=40, background_color=[1, 0, 0, .3], on_press=self.calc_result))

        g1.add_widget(btn1)
        g1.add_widget(btn2)
        g1.add_widget(btn3)
        g1.add_widget(btn4)
        g1.add_widget(btn5)
        g1.add_widget(btn6)
        g1.add_widget(btn7)
        g1.add_widget(btn8)
        g1.add_widget(btn9)
        g1.add_widget(btn10)
        g1.add_widget(btn11)
        g1.add_widget(btn12)
        g1.add_widget(btn13)
        g1.add_widget(btn14)
        g1.add_widget(btn15)
        g1.add_widget(btn16)
        g1.add_widget(btn17)
        g1.add_widget(btn18)
        g1.add_widget(btn19)
        g1.add_widget(btn20)

        b1.add_widget(g1)

        return b1


if __name__ == "__main__":
    CalculatorApp().run()
