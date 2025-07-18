#!/usr/bin/env python3
# Student ID: MGStephenson

def function1():
    global schoolName
    schoolName = 'SICT'  # local variable
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # use global variable
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'  # global variable
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
