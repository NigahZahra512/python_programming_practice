"""Store key-value pairs.
They are unordered, changeable, and do not allow duplicate keys."""

dict = {
    "name" : "Nigah",
    "age" : 23,
    "city" : "MZD",
    "isStudent" : True,
    "skills" : ["Python", "ML", "AI"],
    "Topics" : ("Dictionary", "set")
}
print(dict)
print(dict["name"])
print(dict["skills"])
print(dict["skills"][1])

dict["name"] = "NIGAH ALI ZAHRA"
dict["skills"][1] = "Data Science"
print(dict)


dict["country"] = "Pakistan"
print(dict)

null_value_dict = {}
null_value_dict["Name"] = "Hassan"
null_value_dict["AGE"] = 23
print(null_value_dict)