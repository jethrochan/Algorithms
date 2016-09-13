#README
#Author: Jethro Chan

#The attached code starts out with comments on what the code should do, specified during the interview
#The following lines reads in the raw input as a string, passed into the function parseCourseInfo(string)

'''
On our site, students can enter the course information of the courses they are taking
in the format of:

Department + course number and semester + year

department and semester are always alphabetic
course number and year are always numeric

Valid forms of Department+Course Number are:
CS111
CS 111
CS:111
CS-111

And valid forms of Semester+Year are:
Fall 2014
fall 14
2014 Fall
F2014

Semesters are Fall (F), Winter (W), Spring (S), Summer (Su).

For example, all of the above combinations would give you:
Department: CS
Course Number: 111
Year: 2014
Semester: Fall

More examples:
"CS111 2016 Fall"
"CS-111 Fall 2016"
"MATH 123 2015 Spring"
'''