file1 = open("learning_python.txt", 'r')
file2 = open("learning_python_copied.txt", 'w')

for x in file1.readlines() :
    x = x.replace("python", 'C')
    file2.write(x)

file1.close()
file2.close()