#python is used to perform operations on a file(read,write)
#we have to open file before reading and writing.
 
f = open("demo.txt","rt")
data = f.read()
#data = f.read(5) . Also used this as a parameter only read these idxs
# f.readline() .read line by line.

print(data)
print(type(data))

f.close()
