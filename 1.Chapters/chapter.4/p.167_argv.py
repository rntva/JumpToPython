import sys

args = sys.argv[1:]
for x in args :
    print(x, end=' ')
    print(x.upper(), end=' ')

file2 = open("argv.txt", 'w')
file2.write(str(args))

