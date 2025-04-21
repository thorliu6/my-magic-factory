import json


def students_init():
    file_name='students_profile.json'
    with open(file_name) as pf:
        origin_texts=json.load(pf)
    return origin_texts
def marks_record(origin_texts):
    file_name='students_profile.json'
    with open(file_name,'w') as f:
        json.dump(origin_texts, f)print('来自feature分支的修改')
