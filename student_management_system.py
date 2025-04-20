students=[{'name':'Curry',
           'Chinese':100,
           'math':100,
           'English':100
}]

#实现欢迎功能，并且提示用户选择什么操作
def greet():
    print('------------------------------------------')
    print('Welcome to the students management system!')
    print('choose the function you want to achieve: ')
    choice = input('1.print the marks\n'
                   '2.add student\n'
                   '3.delete student\n'
                   '4.search student\n'
                   '9.exit\n'
                   'which one do you want to choose: ')
    return int(choice)

#打印每个学生的成绩
def print_mark(origin_texts):
    for origin_text in origin_texts:
        print(origin_text)

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
while True:
   choice=greet()
   if choice==1:
       print_mark(students)
   elif choice==2:
       private_name=input('Please enter his/her name: ')
       private_Chinese=int(input('Please enter his/her Chinese marks: '))
       private_math=int(input('Please enter his/her math marks: '))
       private_English=int(input('Please enter his/her English marks: '))
       privacy={}
       privacy['name']=private_name.title()
       privacy['Chinese']=private_Chinese
       privacy['math']=private_math
       privacy['English']=private_English
       add_student(students,privacy)
   elif choice==3:
       delete_one=input('Please enter the name of the student you want to delete: ')
       delete_student(students,delete_one)
   elif choice==4:
       search_student(students)
   elif choice==9:
       break
