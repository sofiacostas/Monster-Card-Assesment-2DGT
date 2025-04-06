catalogue = {"Stoneling":
            {"Strength": 7,
            "Speed": 1,
            "Stealth": 25,
            "Cunning": 15,},

        "Vexscream":
        {"Strength": 1,
        "Speed": 6,
        "Stealth": 21,
        "Cunning": 19,},

        "Dawnmirage":
        {"Strength": 5,
        "Speed": 15,
        "Stealth": 18,
        "Cunning": 22,},   

        "Blazegolem":
        {"Strength": 15,
        "Speed": 20,
        "Stealth": 23,
        "Cunning": 6,},
        
        "Websnake":
        {"Strength": 7,
        "Speed": 15,
        "Stealth": 10,
        "Cunning": 5,},
              
        "Moldvine":
        {"Strength": 21,
        "Speed": 18,
        "Stealth": 14,
        "Cunning": 5,},
              
        "Vortexwing":
        {"Strength": 19,
        "Speed": 13,
        "Stealth": 19,
        "Cunning": 2,},
        
        "Rotthing":
        {"Strength": 16,
        "Speed": 7,
        "Stealth": 4,
        "Cunning": 12,},
              
        "Froststep":
        {"Strength": 14,
        "Speed": 14,
        "Stealth": 17,
        "Cunning": 4,},
              
        "Wispghoul":
        {"Strength": 17,
        "Speed": 19,
        "Stealth": 3,
        "Cunning": 2,},
        }

def show_card(): #Shows the card and their values (stats/power)
    print("\n---CARDS---")
    for key, value in catalogue.items():
        print(f"\n--{key}--")
        for stat, power in value.items():
            print(f"{stat}: {power}")


def add_card(): #Able to add a new card
    card_name = input("Enter name of new card: ")
    card_name = card_name.capitalize()
    catalogue[card_name] = {}
    stats = ["Strength", "Speed", "Stealth", "Cunning"]

    for stat in stats:
        while True:
            try:
                power = int(input(f"Enter a numerical value from 1-25 for {card_name}'s {stat}: "))
                if power > 25: #If power input more than 25 it says invalid and loops back to power input
                    print("Invalid input! Please input a number between 1-25")
                elif power < 1: #If power input less than 1 it says invalid and loops back to power input
                    print("Invalid input! Please input a number between 1-25")
                else:   
                    break
            except ValueError: #If a non number is put it says invalid and loops back to power input
                print("Invalid input! Please input a number")
        catalogue[card_name][stat] = power


def search_card(): #Search for a specific card and show its values
    print("\n---CURRENT CARDS---")
    for key, value in catalogue.items():
        print(key)
    card_name = input("Search for card: ")
    card_name = card_name.capitalize()
    if card_name in catalogue:
        print(f"\n--{card_name}--")
        for stat, power in catalogue[card_name].items():
            print(f"{stat}: {power}")

    else:
        print("Card not found")


def delete_card(): #Delete a chosen card
    print("\n---CURRENT CARDS---")
    for key, value in catalogue.items():
        print(key)
    card_name = input("Enter the card you want to delete: ")
    card_name = card_name.capitalize()
    if card_name in catalogue:
        print(f"{card_name} card has been deleted")
    else:
        print("Please input a valid card")

    del catalogue[card_name]


while True: 
    print("\n---MONSTER CARDS---")
    print("-Please type in a number between 1-5 to navigate-")
    print("1 Show Card(s)" "\n2 Add Card" "\n3 Search Card" "\n4 Delete Card" "\n5 Quit")
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("\nInvalid input! Please input a number between 1-5")
            print("1 Show Card(s)" "\n2 Add Card" "\n3 Search Card" "\n4 Delete Card" "\n5 Quit")

    if number == 1: #When user inputs 1 it runs the function 'show_card'
        show_card()

    elif number == 2: #When user inputs 2 it runs the function 'add_card'
        add_card()

    elif number == 3: #When user inputs 3 it runs the function 'search_card'
        search_card()

    elif number == 4: #When user inputs 4 it runs the function 'delete_card'
        delete_card()

    elif number == 5: #Quit/ends the code
        print("Thank you for using MONSTER CARDS")
        break