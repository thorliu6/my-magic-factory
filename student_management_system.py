import json
import matplotlib.pyplot as plt
import persistence_method as method
students=method.students_init()
#实现欢迎功能，并且提示用户选择什么操作
def greet():
    print('------------------------------------------')
    print('Welcome to the students management system!')
    print('choose the function you want to achieve: ')
    while True:
        origin_choice = input('1.print the marks\n'
                              '2.add student\n'
                              '3.delete student\n'
                              '4.search student\n'
                              '5.a chart to oversee the marks\n'
                              '9.exit\n'
                              'which one do you want to choose: ')
        try:
           choice=int(origin_choice)
        except ValueError:
            print('Please enter a reasonable order!')
        else:
            break
    return choice

#打印每个学生的成绩
def print_mark(origin_texts):
    for origin_text in origin_texts:
        print(origin_text)

#录入每一个加入学生的成绩信息
def log_in(mark):
    while True:
        if mark<=100 and mark>=0:
            break
        else :
            mark_again=input('Sorry,you may log in wrongly,please enter it again: ')
            mark=int(mark_again)
    return mark

#加入学生的成绩
def add_student(origin_texts,informations):
    origin_texts.append(informations)

#删除某个学生
def delete_student(origin_texts,who_to_delete):
    flag=1
    for origin_text in origin_texts:
        if origin_text['name']==who_to_delete.title():
            origin_texts.remove(origin_text)
            flag -=1
    if flag:
        print('There seems no students that you want to delete')
#寻找某一个学生
def search_student(origin_texts):
    flag=1
    search_name=input('which student do you want search: ')
    for origin_text in origin_texts:
        if origin_text['name']==search_name.title():
            print('Successfully find him/her!')
            print(origin_text)
            flag -=1
    if flag:
        print('There seems no students that you want to search')
#做一个可视化的图表
def make_mark_visible(subject,origin_texts):
    marks=[]
    names=[]
    for origin_text in origin_texts:
        names.append(origin_text['name'])
        marks.append(origin_text[subject])
    plt.scatter(names,marks,s=40)
    plt.title(f"The whole class's marks of {subject}",fontsize=24)
    plt.xlabel('names')
    plt.ylabel('marks')
    plt.savefig('student_marks.png',bbox_inches='tight')
    plt.show()

while True:
   choice=greet()
   if choice==1:
       print_mark(students)
   elif choice==2:
       privacy = {}
       private_name=input('Please enter his/her name: ')
       privacy['name'] = private_name.title()
       tip1=int(input("Please enter his/her Chinese mark: "))
       privacy['Chinese'] = log_in(tip1)
       tip2=int(input("Please enter his/her math mark: "))
       privacy['math'] = log_in(tip2)
       tip3=int(input("Please enter his/her English mark: "))
       privacy['English'] = log_in(tip3)
       add_student(students,privacy)
   elif choice==3:
       delete_one=input('Please enter the name of the student you want to delete: ')
       delete_student(students,delete_one)
   elif choice==4:
       search_student(students)
   elif choice==5:
       subject=['Chinese','math','English']
       while True:
           selected_subject=input('Which subject do you want to see: ')
           if selected_subject in subject:
              make_mark_visible(selected_subject,students)
              break
           else:
               print('You enter a wrong subject!')
   elif choice==9:
      method.marks_record(students)
      break
   else:
       print('Please enter the right order!')
       continue
