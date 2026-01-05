dict = {
    "name": "Nigah",
    "age": 23,
    "Subjects": {
       "DSA" : 92,
       "Math" : 88,
       "Algorithms" : 80
         
        
        }
    }

print(dict.keys())  
print(list(dict.keys()))      #Converting to list(type casting)

print(list(dict.values())) 
print(dict.items())  
print(len(dict)) 

print(dict["name"])     #Accessing value using key .error if key not found
print(dict.get("name"))  #Accessing value using get() method .none if key not found but no error printed

print(dict.update(name = "NIGAH ALI ZAHRA"))   
print(dict)

new_dict = {"country": "Pakistan", "isStudent": True}
dict.update(new_dict)
print(dict)