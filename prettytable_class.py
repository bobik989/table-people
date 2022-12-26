from prettytable import PrettyTable

class People():
    
    def __init__(self, name, country, work):
        self.name = name
        self.country = country
        self.work = work

    def info_people(self):
        print(self.name, self.country, self.work)

number_workes = int(input("How many workes you want add (no more 5): "))

table = PrettyTable()
table.field_names = ["Name","Country","Work"]

if number_workes > 5:
    print("You wanted add MORE 5 workes!")

elif number_workes <= 5:

    for i in range(0, number_workes):

        name = input("Entry you name: ")
        country = input("Entry you country: ")
        work = input("Entry you work: ")
    
        print("----------OK----------")
        people = People(name, country, work)
        table.add_row([name, country, work])
            
    print("-"*50)
    print(table)