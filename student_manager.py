import json
from persistence_preserving import DataPreserver
import csv
import os
from datetime import datetime
class StudentManager(DataPreserver):
    def __init__(self,name=' ',chinese=0,math=0,english=0):
        super().__init__(name,chinese,math,english)
        self.lot_dicts=[]
    def load_data(self):
        file_name='students_profile.json'
        with open(file_name) as f:
            self.lot_dicts=json.load(f)
    def import_csv(self):
        file_name='students_20250424_224031.csv'
        with open(file_name,newline='',encoding='utf-8') as f:
            reader=csv.DictReader(f)
           for row in reader:
               cleaned_row={k:v.strip() }
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
    #def ranking(self,subject,origin_texts):
    def commit_data(self,to_restore):
        file_name= 'students_profile.json'
        with open(file_name, 'w') as f:
            json.dump(to_restore, f)
    def commit_data_csv(self,to_store,folder:str="exports")->str :
        os.makedirs(folder,exist_ok=True)
        timestamp=datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name=f'students_{timestamp}.csv'
        full_path=os.path.join(folder,file_name)
        try:
            with open(full_path,'w',newline='',encoding='utf-8-sig') as f:
                fieldnames=['name','Chinese','math','English']
                writer=csv.DictWriter(f,fieldnames=fieldnames)
                writer.writeheader()
                for a_dict in to_store:
                    writer.writerow(a_dict)
        except PermissionError:
            raise RuntimeError('导出失败，文件被Excel/WPS等软件占用，请关闭后重试')
        except Exception as e:
            raise RuntimeError(f'导出发生意外错误：{str(e)}')
        return full_path





