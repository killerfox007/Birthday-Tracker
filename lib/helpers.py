# lib/helpers.py
from models.people import People
from models.birthday import Birthday
def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
def list_birthday():
    birthday = Birthday.list_all_birthdays()
    for birthday in birthdays:
        print(birthday)
def list_people():
    peoples = People.all_people()
    for people in peoples:
        print(people)

def delete_person():
    name = input("Enter Persons Name: ")
    if person := People.find_by_name(name):
        person.delete()
        print(f'{name} is Deleted')
    else:
        print(f'{name} is not found')
#todo Print out bday and id with this function
def find_by_name():
    name = input("Enter Persons Name: ")
    if person := People.find_by_name(name):
        print(f'{name} Is in database')
    else:
        print(f'{name} Isnt in the database')
def create_person():
    name = input("Enter Persons name: ")
    if name:
        person = People.create(name)
        print(f'Added {name}')
    else:
        print("Input a name")
#todo i need the persons name from id to print correct info
def create_birthday():
    date = input("Enter Persons Date of birth. (Example 00/00/0000) Enter: ")
    person = input("Enter Persons Id: ")
    if date and person:
        bday = Birthday.create(date,person)
        print(f'Added {date}')