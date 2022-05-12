from sqlite3 import dbapi2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import listItemButton

class StudentListButton(listItemButton):
    pass

class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()
    
    def submit_students(self):
        pass
    
    def delete_student(self):
        pass
    
    def replace_student(self):
        pass

class StudentDBApp(App):
    def build(self):
        return StudentDB()
    
dbApp = StudentDBApp()
dbApp.run()