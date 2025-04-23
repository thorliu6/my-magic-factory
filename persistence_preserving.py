import json

from student_data import Student
class DataPreserver(Student):
    def __init__(self, name=' ', chinese=0,math=0,english=0):
        super().__init__(name,chinese,math,english)
        self.lot_dicts=[]
        self.record_init_data=[]
        self.record_final_data=[]
    def switch_dict_data(self,to_switch):
        for a_dict in to_switch:
            new_student=DataPreserver()
            new_student.name=a_dict['name']
            new_student.chinese=int(a_dict['Chinese'])
            new_student.math=int(a_dict['math'])
            new_student.english=int(a_dict['English'])
            self.record_init_data.append(new_student)
    def switch_data_dict(self):
        new_student={}
        for a_dict in self.record_init_data:
            new_student['name']=a_dict.name.title()
            new_student['Chinese']=str(a_dict.chinese)
            new_student['math']=str(a_dict.math)
            new_student['English']=str(a_dict.english)
            self.record_final_data.append(new_student)

