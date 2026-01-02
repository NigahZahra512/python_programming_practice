#built in data type that lets us create immutable sequence of values
tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(tup[0])
print(tup[3])

print(tup[1:3])   #slicing in tuples
print(tup[-4:-1])
# tup[0]=6  not allowed
tup1=("hello")
print(type(tup1))


tup1=("hello",)
print(type(tup1))
