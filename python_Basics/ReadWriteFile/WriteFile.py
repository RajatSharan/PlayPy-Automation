# file = open('test.txt')
#
# file.close()

#read the file and store all the line in a list
# reverse the list
# write the list back to the file

with open('test.txt','r') as reader:
    content = reader.readlines()        #read the file and store all the line in a list
    reversed(content)                   # reverse the list
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)         # write the list back to the file






