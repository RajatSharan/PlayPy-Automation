values = [1, 2, "rajat", 4, 5]
#List is a collection of values which can be of any type

print(values[0])

print(values[3])

print(values[-1])
print(values[1:3])

values.insert(3, "sharan")
print(values)

values[2]="Rajat"
print(values)

del values[0]
print(values)


#Tuple is a collection of values which can be of any type

values = (1, 2, "rajat", 4, 5)
print(values[0])


#Dictionary is a collection of key value pairs

values = {"rajat": "sharan", "rajat1": "sharan1"}
print(values["rajat"])

#Dictornary at run time
dic = {}
dic["rajat"] = "sharan"
dic["rajat1"] = "sharan1"
print(values)