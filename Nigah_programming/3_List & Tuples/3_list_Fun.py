list = [1,6,5,3,2,1]
print(list.sort())
print(list)

list.append(1000)
print(list)

list.sort(reverse=True)
print(list)

list.remove(1000)  #remove first occurenceof element
print(list)

list.pop(0)    #removes at index 
print(list)

print(list.count(1))
print(list.index(5))

list.reverse()
print(list)

list.insert(2, "hello")
print(list)