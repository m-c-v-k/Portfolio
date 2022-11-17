#! Python3

f = open("Data Engineer\\Main Studies\\Module 1 - Python\\D4\\test.txt")
lines = f.readlines()
f.close()


lines = "kinke, lane, koff"
f = open("Data Engineer\\Main Studies\\Module 1 - Python\\D4\\test.txt", "w")
f.write(lines)
f.close()
print(lines)
