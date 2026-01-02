my_list=["ali" ,2 ,3.5 ,True ,"hello",5]
print(my_list[1:4])  #slicing from index 1 to index 3
print(my_list[:3])   #slicing from start to index 2
my_list.append(786)
print(my_list)
my_list.insert(2,"new_item")
print(my_list)

#negative indexing
print(my_list[-1])  #last item