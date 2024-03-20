import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    name = input("Name: ")
    address = input("Address: ")
    phone = int(input("Phone: "))
    
    birth = input("Birth [DD/MM/YYYY]: ")
    birth_obj = datetime.strptime(birth, "%d/%m/%Y")
    actual_date = datetime.now()
    age = actual_date.year - birth_obj.year
    
    if actual_date.month < birth_obj.month or (actual_date.month == birth_obj.month and actual_date.day < birth_obj.day):
        age -= 1

    if age < 18:
        print("You need to be 18+ years old to register.")
        break
    else:
        gender = input("Gender [M/F]: ")
        while gender.upper() not in ('M', 'F'):
            print("Invalid character")
            gender = input("Gender [M/F]: ")

    clear_screen()

    question = input("Do you want to continue? [Y/N]: ").upper()
    while question != "Y" and question != "N":
        print("Invalid character")
        question = input("Do you want to continue? [Y/N]: ").upper()

    if question == "N":
        print("Registration complete. Thank you!")       
        print("Name: {} \nAddress: {} \nPhone: {} \nAge: {} \nGender: {} ".format(name, address, phone, age, gender))
        break
    else:
        clear_screen()
        print("Continuing...")