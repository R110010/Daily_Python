'''
Write a Python program that:

Takes input of 5 students’ names and their marks as a list of tuples.
Sorts the list of tuples based on marks in descending order.
Prints the top 3 students with the highest marks.
Calculates and prints the average marks of all students.

'''
my_list=[]
n=5
marks_sum =0
for _ in range(n):
    name,marks = input("enter name and mark seperated by coma :").split(",")
    my_list.append((name.strip(),int(marks.strip())))
print("Initail list",my_list)
sorted_list = sorted(my_list,key=lambda x:x[1],reverse=True )
print("Sorted list:",sorted_list)
print("Top three students with highest marks",sorted_list[:3])
for x in sorted_list:
    marks_sum += x[1]
average_marks = marks_sum/n
print("average marks of students is",average_marks)