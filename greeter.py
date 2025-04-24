from student_manager import StudentManager
from persistence_preserving import DataPreserver
class Greeter:
    def __init__(self, origin_choice):
        self.origin_choice = origin_choice
    def  greet(self):
        print('------------------------------------------')
        print('Welcome to the students management system!')
        print('choose the function you want to achieve: ')
        print('1.print the marks')
        print('2.add student')
        print('3.rank this test')
        print('4.search student')
        print('5.a chart to oversee the marks')
        print('9.exit')
        print('which one do you want to choose:')
    def choose(self):
        while True:
            choice = input()
            try:
                self.origin_choice = int(choice)
            except ValueError:
                print('Please enter a reasonable order!')
            else:
                break
def main():
    while True:
    #包括欢迎和提示选择
        greeter=Greeter(1)
        greeter.greet()
        greeter.choose()
        #导入所有的学生数据
        secretary = StudentManager()
        transformer=DataPreserver()
        secretary.load_data()
    #将数据转换
        students=transformer.switch_dict_data(secretary.lot_dicts)
        if greeter.origin_choice==1:
            secretary.print_mark(students)
        elif greeter.origin_choice==2:
            a_new_student=secretary.add_student()
            students.append(a_new_student)
            #print(students)
            #print(f'this is{transformer.record_init_data},hhhhhh{students}')
            change_students=transformer.switch_data_dict(students)
            #print(change_students)
            secretary.commit_data(change_students)
            path=secretary.commit_data_csv(change_students)
            print(path)
        elif greeter.origin_choice==3:
            received_word=input('which subject do you want to search to have a birdview: ')
            secretary.ranking(received_word,transformer.record_init_data)
        elif greeter.origin_choice==9:
            break
        else:
            print('Please enter a right order!')
main()
