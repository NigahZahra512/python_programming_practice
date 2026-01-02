#print length of list(if list is the parameter)
list=[1,23,4,5,5]
hereos=["quaid","iqbal"]
def fun_list(list):
    print(len(list))
fun_list(list)
fun_list(hereos)



#print element of list in a single line(if list is the parameter)

hereos=["quaid","iqbal" ,"muhammad"]
# print(hereos[0],end=" ")
# print(hereos[1],end=" ")
# print(hereos[2],end="\n")

def print_list(list):
    for item in list :
        print(item,end=" ")
print_list(hereos)
   


