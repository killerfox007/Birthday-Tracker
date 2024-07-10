# lib/helpers.py
from models.people import People
from models.birthday import Birthday


def exit_program():
    print("Goodbye!")
    exit()
def list_birthday():
    birthdays = Birthday.list_all_birthdays()
    peoples = People.all_people()
    if birthdays:
        for birthday in birthdays:
            person = People.find_by_id(birthday.person_id)
            print(f'Person ID:{person.id} Person name:{person.name} Date Of Birth:{birthday.date}')
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
    person_id = input("Enter Persons ID: ")
    if person := People.find_by_id(person_id):
        if birthday := Birthday.find_by_id(person.id):
            birthday.delete()
            person.delete()
            print(f'Person Name:{person.name} was deleted and birthdays were deleted')
        else:
            person.delete()
            print(f'{person.name} is Deleted')
    else:
        print(f'ID:{person_id} is not found')

def find_by_id():
    person_id = input("Enter Persons ID: ")
    if person := People.find_by_id(person_id):
        bday = Birthday.find_by_id(person.id)
        if bday:
            print(f'{person.name}s birthday is {bday.date}')
        else:
            print(f'{person.name} is created but birthday is not set yet')
    else:
        print(f'{person_id} Isnt in the database')
def create_person():
    name = input("Enter Persons name: ")
    if len(name) >= 2:
        person = People.create(name)
        print(f'Added {name}')
    else:
        print("Input a name longer then 2 characters")

# def create_birthday():
#     date = input("Enter Persons Date of birth. (Example 00/00/0000) Enter: ")
#     person = input("Enter Persons Id: ")
#     name = People.find_by_id(person)
#     birthday_checker = Birthday.find_by_id(person)
#     if birthday_checker:
#         print("Person Already has a birthday set, Delete birthday first then set")
#     else:
#         if name:
#             if len(date) == 10 and person:
#                 bday = Birthday.create(date,person)
#                 print(f'Added {name.name}s birthday and the birthday is {date}')
#         else:
#             print("Date format is strict 00/00/0000")
    

def delete_birthday():
    person_id = input("Enter Persons ID: ")
    name = People.find_by_id(person_id)
    if birthday := Birthday.find_by_id(person_id):
        birthday.delete()
        print(f'{name.name}s Birthday(s) was deleted')
    else:
        print("not found")

def create_multi_birthdays():
    date = input("Enter Persons Date of birth. (Example 00/00/0000) Enter: ")
    person = input("Enter Persons Id: ")
    name = People.find_by_id(person)
    if name:
        if len(date) == 10 and person:
            bday = Birthday.create(date,person)
            print(f'Added {name.name}s birthday and the birthday is {date}')
    else:
        print("Date format is strict 00/00/0000")