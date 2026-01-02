#recursive fun to cal sum of first n natural number
def cal_sum(n):
    if(n == 0):
        return 0
    
    return cal_sum(n-1)+n
print(cal_sum(5))

#recursive function to print all elements in a list(use list and index as parameter)
def print_list(list,i=0):
    if(i == len(list)):
        return 
    print(list[i])
    print_list(list,i+1)

lst =[1,2,3,5,8]
lst2 =["ALI" ,"AHMED"]
print_list(lst)
print_list(lst2)