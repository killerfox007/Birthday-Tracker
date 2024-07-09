# lib/cli.py
from models.people import People
from helpers import (
    exit_program,
    helper_1,
    list_people,
    delete_person,
    find_by_name,
    list_birthday,
    create_person,
    create_birthday
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice =="2":
            list_people()
        elif choice == "3":
            list_birthday()
        elif choice == "4":
            find_by_name()
        elif choice == "5":
            create_person()
        elif choice == "6":
            create_birthday()
        elif choice =="8":
            delete_person()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. List All People")
    print("3. List All Birthdays")
    print("4. Find By Name")
    print("5. Create a Person")
    print("6. Create a Birthday")
    print("8. Delete Person")


if __name__ == "__main__":
    main()
