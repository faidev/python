#!/usr/bin/env python3

name = input("name:")
# raw_input 2.x 同 input 3.x
# input 2.x 输入需要加""，否则认为是个变量
age = int(input("age:"))
print(type(age), type(str(age)))
job = input("job:")

print(name, age, job)


info = '''
-------- info of %s -----
name:%s
age:%d
job:%s
''' % (name, name, age, job)

print(info)


info1 = '''
-------- info1 of {_name} -----
name:{_name}
age:{_age}
job:{_job}
'''.format(_name=name, _age=age, _job=job)

print(info1)


info2 = '''
-------- info2 of {0} -----
name:{0}
age:{1}
job:{2}
'''.format(name, age, job)

print(info2)


info3 = '''
-------- info3 of ''' + name + '''-----
name:''' + name + '''
age:''' + str(age) + '''
job:''' + job

print(info3)
