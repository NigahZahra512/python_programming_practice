#find factorial of a function(n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print(fact)
(cal_fact(5))
  


#convert USD to INR
def cal_INR(n):
    USD = 83
    INR = n*USD
    print( n, "USD" , "=" ,INR,"INR")
cal_INR(2)


# program for odd or even number using function
n=int(input("enter number:"))
def cal_Num(n):
    if(n%2 == 0):
        print("it is even Number")
    else:
        print("it is ODD  Number")
cal_Num(n)


