# lib/helpers.py
from models.people import People

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

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