#Assigning a default value to parameter , which is used when no argument is passed.
def cal_prod(a=1,b=2):
    mul=a*b
    return(mul)
print(cal_prod())


def cal_sum(a,b=5):
    sum=a+b
    return(sum)
print(cal_sum(3))