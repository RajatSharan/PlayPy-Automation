file = open('test.txt')

# print(file.read())
#
# print(file.readline())      # Read the first line
#
# file.close()
#
# #Print line by line using readline mehtod
# file = open('test.txt')
# line = file.readline()
# while line!= "":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)




