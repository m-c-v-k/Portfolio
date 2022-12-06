#! python3

# Importing necessary libraries
from person import Person


def person_information():
    person_list = []

    while True:
        choice = input(
            "Do you wish to ENTER data, PRINT out information or QUIT? ").strip().upper()

        if choice == 'ENTER':
            first_name = input("Please enter the first name: ")
            last_name = input("Please enter the last name: ")
            title = input("Please enter the title: ")

            person_list.append(Person(first_name, last_name, title))

        elif choice == 'PRINT':
            if len(person_list) == 0:
                print("No person created.")
            else:
                for person in person_list:
                    print(person)
        elif choice == 'QUIT':
            print("Thank you for today, good bye.")
            quit()


if __name__ == "__main__":
    person_information()
