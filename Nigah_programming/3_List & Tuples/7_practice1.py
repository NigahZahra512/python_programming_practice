# program to check palindrome
lst = list(input("Enter a list of numbers: "))

copy_list = lst.copy()
copy_list.reverse()

if copy_list == lst:
    print("Is palindrome")
else:
    print("Not palindrome")



#program count numm of students in"A" grade
students = ["C","D","A","B","A","C","A","D","B","A"]
print(students.count("A"))
print("Number of students in A grade:", students.count("A"))



#show the above values and sort them from A to D in a list
students = ["C","D","A","B","A","C","A","D","B","A"]
students.sort()
print(students)