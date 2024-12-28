f = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()


line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()