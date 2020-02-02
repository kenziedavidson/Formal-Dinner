# non-repeat-fd.py family dinner table and work assignments, WITH non repeat addition
#1/28/2020
#kenzie compsci
#done with my mom, worked a bit with jess 



import random


#declare list vars
kitchen = []
waiter = []
waiter_option = []
to_be_seated_option = []
kitchen_option = []
to_be_seated = []


#read student file, Splitting on comma into a list and then slicing the list to retain the first three columns-- because we need the old assignment to make sure no repeats
#now we know previous assignments
try:
    with open('Dinner Seating - Student List 2018-19 4.csv') as student_file:
        for line in student_file:
            alist = line.split(',')
            #print(alist)
            x = slice(3)
            a = alist[x]
            #print(a)
            if a[2][:1] == 'W':
                kitchen_option.append(a)
                to_be_seated_option.append(a)               
            elif a[2] == 'Kitchen':
                waiter_option.append(a)
                to_be_seated_option.append(a)
            else:
                waiter_option.append(a)
                kitchen_option.append(a)
                to_be_seated_option.append(a)

#waiterOption needs to contain student minus last week's waiters
    
    num_student = len(to_be_seated_option)
    print ('number of students = '+ str(num_student))
    #print(student)
    #print('waiter option')
    #print(waiter_option)
    #print('kitchen option..')
    #print(kitchen_option)
    
    #randomly pick 7 kitchen students and 31 waiter students
    #random.sample randomly select # of unique items without repetition
    waiter = random.sample(waiter_option,31)
    print('number of waiters = ' + str(len(waiter)))
    print(waiter)

#got an occasional value error because it is not necessarily true that new waiters were in the kitchen option so we had to confirm that it was in the list before we removed
    
    for each in waiter:
        if each in kitchen_option:
            kitchen_option.remove(each)


    #making new kitchen assignments using kitchen option list so that new staff is made of students who didn't work last week
    kitchen = random.sample(kitchen_option,7)
    print(kitchen)

    #de-insect-ing
    print('to be seated count= '+str(len(to_be_seated_option)))



    for each in waiter:
        to_be_seated_option.remove(each)
        
    for each in kitchen:
        to_be_seated_option.remove(each)

    #de-insect-ing
    print('to be seated count= '+str(len(to_be_seated_option)))

    #sorting the to be seated by their previous assignment (the second element in the array); sorting by going consecutively through the tables so no table number sits with that same table number
    #lambda defines the function that we are sorting by, which is the third element in the array (2nd subscript)

    sort_to_be_seated  = sorted(to_be_seated_option,key=lambda x: x[2])
    #quit()     
#open output csv file
    try:
        with open('Work and Seat Assignment.csv','w') as output_file:
            counter = 1
            max_table = 31
            for each_student in kitchen:
                #print(each_student + ',Kitchen',file=output_file)
                print(each_student[0] + ',' + each_student[1] + ',Kitchen',file=output_file)
            for each_student in waiter:
                scounter = str(counter)
                #print(each_student + ',' + 'W' + scounter.zfill(2),file=output_file)
                print(each_student[0] + ',' + each_student[1] + ',W' + scounter.zfill(2),file=output_file)
                counter = counter + 1
                if counter > max_table:
                    counter = 1 
            for each_student in sort_to_be_seated:
                #print(each_student + ',' + str(counter),file=output_file)
                print(each_student[0] + ',' + each_student[1] + ',' + str(counter),file=output_file)
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
    

    
        
    
