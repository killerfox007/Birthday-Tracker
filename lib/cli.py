# lib/cli.py
from models.people import People
from helpers import (
    exit_program,
    helper_1,
    list_people,
    delete_person,
    find_by_name
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
            find_by_name()
        elif choice =="5":
            delete_person()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. List All People")
    print("3. Find By Name")
    print("5. Delete Person")


if __name__ == "__main__":
    main()
