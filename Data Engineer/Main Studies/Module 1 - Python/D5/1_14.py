#! Python3
p_list = list()
f = open(f"Data Engineer\\Main Studies\\Module 1 - Python\\D5\\phonelist.txt", "r")
content = f.read()
f.close()


# Handle file content
content = content[1:]
content = content[:-1]

if ", " in content:
    split_content = content.split(", ")

    for item in split_content:
        p_list.append(item)


class Person:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def __repr__(self):
        return f"Name:\t{self.__name}\tPhone:\t{self.__phone}\n"


print(p_list)


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

        f.write(str(p_list))
        f.close()
