# fd.py family dinner table and work assignments
#1/19/2020
#kenzie compsci
#done with my mom and jess and will



import random

# from stackoverflow...
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#declare list vars
kitchen = []
waiter = []
student = []
left_over = []

#read student file, stripping existing work/table assignment and build student name list
try:
    with open('Dinner Seating - Student List 2018-19 4.csv') as student_file:
        for line in student_file:
            #find second ',' and store the first and last names only in student list
            npos = find_nth(line,',',2)
            if npos > 0:
                name = line[:npos]
                #print(name)
                student.append(name)


    num_student = len(student)
    print ('number of students = '+ str(num_student))
    #randomly pick 7 kitchen students and 31 waiter students
    #random.sample randomly select # of unique items without repetition
    waiter = random.sample(student,31)
    print('number of waiters = ' + str(len(waiter)))
    
    #left_over = list(set(student) - set(waiter)) (same behavior as difference)
    left_over = list(set(student).difference(set(waiter)))

#debugging/verify
    x = set(student).intersection(set(waiter))
    print(x)
    print('count of x(intersection of students with waiters) = '+ str(len(x)))
    
    num_left_over = len(left_over)
    print('number of students less waiters = '+str(num_left_over))
    kitchen = random.sample(left_over,7)
    print(kitchen)

#debugging/verify
    x = set(student).intersection(set(kitchen))
    print(x)
    print('count of x(intersection of students with waiters) = '+ str(len(x)))

    #at_table = list(set(left_over) - set(kitchen)) (same behavior as difference)
    
    at_table = list(set(left_over).difference(set(kitchen)))
    num_at_table = len(at_table)
    print('num at tables = ' + str(num_at_table))

#open output csv file
    try:
        with open('Work and Seat Assignment.csv','w') as output_file:
            counter = 1
            max_table = 31
            for each_student in kitchen:
                print(each_student + ',Kitchen',file=output_file)
            for each_student in waiter:
                scounter = str(counter)
                print(each_student + ',' + 'W' + scounter.zfill(2),file=output_file)
                counter = counter + 1
                if counter > max_table:
                    counter = 1
            for each_student in at_table:
                print(each_student + ',' + str(counter),file=output_file)
                counter = counter + 1
                if counter > max_table:
                    counter = 1
    except IOError as err:
        print('IO Error writing seat assignment file')
    finally:
        output_file.close()
        
except IOError as err:
    print('IO Error reading student file: '+str(err))
finally:
    student_file.close()
    

    
        
    
