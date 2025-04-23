import json
from persistence_preserving import DataPreserver
class StudentManager(DataPreserver):
    def __init__(self,name=' ',chinese=0,math=0,english=0):
        super().__init__(name,chinese,math,english)
        self.lot_dicts=[]
    def load_data(self):
        file_name='students_profile.json'
        with open(file_name) as f:
            self.lot_dicts=json.load(f)
    def print_mark(self,origin_texts):
        for a_dict in origin_texts:
            print(f'In the test,{a_dict.name} got {a_dict.chinese}\tin Chinese,{a_dict.math}\tin math,{a_dict.english}\tin English')
    def log_in_mark(self,subject):
        while True:
            ori_mark=input(f'what is his/her {subject} mark: ')
            try:
                fin_mark=int(ori_mark)
            except ValueError:
                print('Please enter a right number!')
            else:
                if  not 0<=fin_mark<=100 :
                    print('Please enter the right range!')
                    continue
                else:
                    return fin_mark
    def add_student(self):
        new_student=StudentManager()
        print("Now please add a new student's information:")
        student_name=input('what is his/her name: ')
        new_student.name=student_name.title()
        new_student.chinese=self.log_in_mark('Chinese')
        new_student.math=self.log_in_mark('math')
        new_student.english=self.log_in_mark('English')
        #print(new_student)
        return new_student
    def ranking(self,subject,origin_texts):
    def commit_data(self,to_restore):
        file_name= 'students_profile.json'
        with open(file_name, 'w') as f:
            json.dump(to_restore, f)






