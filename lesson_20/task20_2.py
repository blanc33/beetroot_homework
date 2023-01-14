import json
import unittest

def new_entries(person_data):
    with open('phonebook.json') as frombook:
        data = json.load(frombook)
        data.append(person_data)
        with open('phonebook.json', 'w') as inbook:
            json.dump(data, inbook, indent=2)
    return 'The person\'s data is added'

def search_by_fname(search):
    result = []
    with open('phonebook.json') as frombook:
        data = json.load(frombook)
    for l in data:
        if l[0] == search:
            result.append(l)
    if result != []:
        res = ""
        for c in result:
            for cc in c:
                res = res + cc + " "

        return res
    else:
        return 'there is no such data'

def search_by_lname(search):
    result = []
    with open('phonebook.json') as frombook:
        data = json.load(frombook)
    for l in data:
        if l[1] == search:
            result.append(l)
    if result != []:
        res = ""
        for c in result:
            for cc in c:
                res = res + cc + " "
        return res
    else:
        return 'there is no such data'

def search_by_full(search):
    result = []
    with open('phonebook.json') as frombook:
        data = json.load(frombook)
    for l in data:
        if l[0] == search[0] and l[1] == search[1]:
            result.append(l)
    if result != []:
        res = ""
        for c in result:
            for cc in c:
                res = res + cc + " "
        return res
    else:
        return 'there is no such data'

def search_by_number(search):
    result = []
    with open('phonebook.json') as frombook:
        data = json.load(frombook)
    for l in data:
        if l[2] == search:

            result.append(l)
    if result != []:
        res = ""
        for c in result:
            for cc in c:
                res = res + cc + " "
        return res
    else:
        return 'there is no such data'

def search_by_city(search):
    result = []
    with open('phonebook.json') as frombook:
        data = json.load(frombook)
    for l in data:
        if l[3] == search:
            result.append(l)
    if result != []:
        res = ""
        for c in result:
            for cc in c:
                res = res + cc + " "
        return res
    else:
        return 'there is no such data'

def delete_record(search):
    flag = 'There is no such data'
    with open('phonebook.json') as frombook:
        data = json.load(frombook)
    for l in data:
        if l[2] == search:
            data.remove(l)
            with open('phonebook.json', 'w') as inbook:
                json.dump(data, inbook, indent=2)
            flag = 'The person\'s data is deleted'
    return flag

def update_record(search, new_data):
    with open('phonebook.json') as frombook:
        data = json.load(frombook)
    for l in data:
        if l[2] == search:
            data.remove(l)
            data.append(new_data)
            with open('phonebook.json', 'w') as inbook:
                json.dump(data, inbook, indent=2)
    return 'The person\'s data is updated'

while True:
    wish = input('\n\nEnter a number depended on what do you want:'
                 '\n1 - add new antries,'
                 '\n2 - search by first name,'
                 '\n3 - search by last name,'
                 '\n4 - search by full name,'
                 '\n5 - search by telephone number,'
                 '\n6 - search by city or state,'
                 '\n7 - delete a record for a given telephone number,'
                 '\n8 - update a record for a given telephone number,'
                 '\n9 - exit the program     \n')

    if wish == '1':
        person_data = input('Enter your first name, last name, telephone number and city with space between them:  ').split()
        print(new_entries(person_data))

    elif wish == '2':
        search = input('For search enter a first name:  ')
        print(search_by_fname(search))

    elif wish == '3':
        search = input('For search enter a surname:  ')
        print(search_by_lname(search))

    elif wish == '4':
        search = input('For search enter a full name:  ').split()
        print(search_by_full(search))

    elif wish == '5':
        search = input('For search enter a telephone number:  ')
        print(search_by_number(search))

    elif wish == '6':
        search = input('For search enter a city or a state:  ')
        print(search_by_city(search))

    elif wish == '7':
        search = input('Enter a telephone number for deleting its record:  ')
        print(delete_record(search))

    elif wish == '8':
        search = input('Enter a telephone number for updating its record:  ')
        new_data = input('Enter your first name, last name, telephone number and city with space between them:  ').split()
        print(update_record(search, new_data))

    else:
        break


class PhonebookTest(unittest.TestCase):

    def test_new_entry(self):
        data = 'Name3 Surname3 33333 City3'
        self.assertEqual(new_entries(data), 'The person\'s data is added')

    def test_search_by_name(self):
        self.assertEqual(search_by_fname("name4"), 'name4 surname4 1235 lima4 ')

    def test_search_by_number(self):
        self.assertEqual(search_by_number("1235"), 'name4 surname4 1235 lima4 name5 surname5 1235 lima5 ')