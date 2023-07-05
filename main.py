from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from plyer import gps
from plyer import sms
from kivymd.uix.dialog import MDDialog
#from android.permissions import Permission, request_permissions
import os.path
from service import Service
from jnius import autoclass, cast



class TheLayout(Widget):
    def submit_press(self):
        filename = "number.txt"
        check_if_exists = os.path.isfile(filename)
        open_file = open("number.txt", "r")
        if_empty = open_file.read()
        if check_if_exists == False or if_empty == '':
            number = self.ids.number.text
            print(number)
            number_txt = open(filename, "w")
            number_txt.write(number)
            number_txt.close()

            open_file = open("number.txt", "r")
            if_empty = open_file.read()
            if if_empty != '':
                number = open("number.txt", "r")
                read_number = number.read()
                number_str = str(read_number)
                self.ids.submit.text = "Кнопка отключена"
                self.ids.number.text = "Добавленный номер: "+number_str
                self.ids.label.text = "Успешно!"
                self.ids.submit.disabled = True
                self.ids.number.disabled = True

        
        elif check_if_exists == True and if_empty != '':
            number = open("number.txt", "r")
            read_number = number.read()
            number_str = str(read_number)
            self.ids.number.text = "Рабочий номер: "+number_str
            self.ids.submit.text = "Кнопка отключена"
            self.ids.label.text = "Разрешается добавить только 1 номер!"
            self.ids.submit.disabled = True
            self.ids.number.disabled = True

    
                    

class Main(App):
    def build(self):
        return TheLayout()
    def on_start(self):
        Service().run()
         
    
if __name__ == '__main__':
    Main().run()
