# lib/cli.py
from models.people import People
from helpers import (
    exit_program,
    list_people,
    delete_person,
    find_by_name,
    list_birthday,
    create_person,
    create_birthday,
    delete_birthday
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice =="1":
            list_people()
        elif choice == "2":
            list_birthday()
        elif choice == "3":
            find_by_name()
        elif choice == "4":
            create_person()
        elif choice == "5":
            create_birthday()
        elif choice == "6":
            delete_birthday()
        elif choice =="7":
            delete_person()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List All People")
    print("2. List All Birthdays")
    print("3. Find By Name")
    print("4. Create a Person")
    print("5. Create a Birthday")
    print("6. Delete a Birthday")
    print("7. Delete Person")


if __name__ == "__main__":
    main()
