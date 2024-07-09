# lib/helpers.py
from models.people import People
from models.birthday import Birthday

def exit_program():
    print("Goodbye!")
    exit()
def list_birthday():
    birthdays = Birthday.list_all_birthdays()
    if birthdays:
        for birthday in birthdays:
            print(f'Person ID:{birthday.person_id} Date Of Birth:{birthday.date}')
    else:
        print('No Birthdays added yet, Use 5 to create a birthday')
def list_people():
    peoples = People.all_people()
    if peoples:
        for people in peoples:
            print(f'Name:{people.name} ID:{people.id}')
    else:
        print("No people have been added yet, Use 4 to create a person")

def delete_person():
    name = input("Enter Persons Name: ")
    if person := People.find_by_name(name):
        if birthday := Birthday.find_by_id(person.id):
            print(birthday)
            birthday.delete()
            person.delete()
            print(f'{name} is Deleted and Birthday {birthday.date} was deleted')
        else:
            person.delete()
            print(f'{name} is Deleted')
    else:
        print(f'{name} is not found')

def find_by_name():
    name = input("Enter Persons Name: ")
    if person := People.find_by_name(name):
        bday = Birthday.find_by_id(person.id)
        if bday:
            print(f'{person.name}s birthday is {bday.date}')
        else:
            print(f'{person.name} is created but birthday is not set yet')
    else:
        print(f'{name} Isnt in the database')
def create_person():
    name = input("Enter Persons name: ")
    if name:
        person = People.create(name)
        print(f'Added {name}')
    else:
        print("Input a name")
#todo check input 
#before sending to birthday.create so no error, 
#if wrong loop create_birthday()  
def create_birthday():
    date = input("Enter Persons Date of birth. (Example 00/00/0000) Enter: ")
    person = input("Enter Persons Id: ")
    name = People.find_by_id(person)
    if len(date) == 10 and person:
        bday = Birthday.create(date,person)
        print(f'Added {name.name}s birthady and the birthday is {date}')
    else:
        print("Date format is strict 00/00/0000")

def delete_birthday():
    person_id = input("Enter Persons ID: ")
    name = People.find_by_id(person_id)
    if birthday := Birthday.find_by_id(person_id):
        birthday.delete()
        print(f'{name.name}s Birthday was deleted')
    else:
        print("not found")