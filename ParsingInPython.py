#Please view Readme.txt for explanation of the program
#Author: Jethro Chan


def parseCourseInfo(info):    
    
    department = None
    coursenumber = None
    year = None
    semester = None
    
    departmentList = []
    coursenumberList = []
    yearList = []
    semesterList = []
    
    for i in info:
        if not department: #department string is None
            if not i.isalpha():
				department = ''.join(departmentList)
            else:
				departmentList.append(i)
             
        if not coursenumber: #coursenumber string is None
            if i.isdigit():
                coursenumberList.append(i)               	
            else:
            	if i != ":" and i != "-":                           
					coursenumber = ''.join(coursenumberList)
        
        if department and coursenumber:#the other string not department is the semester
            if i.isalpha(): 
				semesterList.append(i)
				semester = ''.join(semesterList)
            else:
				if i.isdigit():
				    yearList.append(i)
				    year = ''.join(yearList)
                    
    if year:
       if len(year) == 2: #standardize the year format
           year = '20' + year
    
    if semester: #standardize the semester format
    	if semester == 'F' or semester == 'f' or semester == 'fall':
            semester = "Fall"
        elif semester == 'W' or semester == 'w' or semester == 'winter':
            semester = "Winter"
        elif semester == 'S' or semester == 's' or semester == 'spring':
            semester = "Spring"
        elif semester == 'Su' or semester == 'su'or semester == 'summer':
            semester = "Summer"
            
    print('Department: %s' %department)    
    print('Course Number: %s' %coursenumber)	
    print('Semester: %s' %semester)
    print('Year: %s' %year)

#test cases
parseCourseInfo("CS111 2016 Fall")
parseCourseInfo("CS111 f2016")
parseCourseInfo("CS:111 2016 Fall")
parseCourseInfo("MATH 123 2015 Spring")