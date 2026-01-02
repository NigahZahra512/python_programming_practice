#when a fuction call itself repeatedly it is recursion.it is same like loops
#print n to backward

def fun(n):
    print(n)
fun(5)
print("end")


# recursive function.
def show(n):
    if(n == 0):  #base case
        return
    print(n)
    show(n-1)
show(5)
print("END")



def show(n):
    if(n == 0):  
        return
    print(n)
    show(n-1)
    print("END")
show(3)