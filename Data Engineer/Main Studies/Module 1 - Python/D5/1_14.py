#! Python3
p_list = list()
f = open(f"Data Engineer\\Main Studies\\Module 1 - Python\\D5\\phonelist.txt", "r")
with open() as file:
    for line in file:
        p_list.append(line)
        print(line)
file.close()

print(p_list)


class Person:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def __repr__(self):
        return f"Name: {self.__name}\nPhone: {self.__phone}"


# print(file)


while True:
    command = input("Command: ").upper()

    if command == "QUIT":
        exit()
    elif command == "LIST":
        for p in p_list:
            print(p)
    elif command == "ADD":
        name = input("Please enter the name: ")
        phone = input("Please enter the phone number: ")
        p_list.append(Person(name, phone))
    elif command == "DELETE":
        delete = input(
            "Please enter the name for the contact to delete: ")
        for i in range(len(p_list)):
            print(i)
            if p_list[i][0] == delete:
                del p_list[i]
    elif command == "SAVE":
        f = open(
            "Data Engineer\\Main Studies\\Module 1 - Python\\D5\\phonelist.txt", "w+")
        print(str(p_list))
        f.write(str(p_list))
        f.close()
