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

def range_stats(card_name,catalogue): #Asks the user the power they want to input for each of the 4 stats
    stats = ["Strength", "Speed", "Stealth", "Cunning"] #The 4 stats
    for stat in stats:
        while True:
            try:
                power = int(input(f"Enter a numerical value from 1-25 for {card_name}'s {stat}: "))
                if 1 <= power <= 25: #Sees if power value is between 1-25
                    break
                else:
                    print("Invalid input! Please input a number between 1-25")
            except ValueError: #If a non number is put it says invalid and loops back to power input
                print("Invalid input! Please input a number between 1-25")
        catalogue[card_name][stat] = power


def show_card(): #Shows the card and their values (stats/power)
    print("\n---CARDS---")
    for key, value in catalogue.items():
        print(f"\n--{key}--")  #Prints the name of the card eg. 'Wispghoul'
        for stat, power in value.items(): 
            print(f"{stat}: {power}")  #Prints the values of the card 


def add_card(): #Able to add a new card
    card_name = input("Enter name of new card: ")
    card_name = card_name.capitalize()
    catalogue[card_name] = {}
    range_stats(card_name, catalogue) #Calls function which asks for the values and checks if the values are between 1-25
    print(f"Added {card_name} to catalogue!")


def search_card(): #Search for a specific card and show its values
    print("\n---CURRENT CARDS---")
    for key, value in catalogue.items():
        print(key)
    card_name = input("Search for card: ")
    card_name = card_name.capitalize()
    if card_name in catalogue:
        print(f"\n--{card_name}--") #Shows card's name
        for stat, power in catalogue[card_name].items():
            print(f"{stat}: {power}") #Shows card's values (stats/power)

    else: #If a card not in the catalogue is inputted it loops here until a valid card is inputted
        while card_name not in catalogue: 
            print("Please input a valid card")
            card_name = input("Enter the card you want to search: ")
            card_name = card_name.capitalize()  
            message = (f"--{card_name}--\n") 
        for stat, power in catalogue[card_name].items(): 
            message += (f"{stat}: {power}\n")
        print(message)

    change = input(f"Would you like to change {card_name}'s values? Y/N: ") #To see if they want to change the card they searched values
    change = change.capitalize()
    if change == "Y": 
       range_stats(card_name, catalogue) #Calls function which asks for the values and checks if the values are between 1-25
    elif change == "N":
        breakpoint


def delete_card(): #Delete a chosen card
    print("\n---CURRENT CARDS---")
    for key, value in catalogue.items():
        print(key)
    card_name = input("Enter the card you want to delete: ")
    card_name = card_name.capitalize()
    if card_name in catalogue:
        print(f"{card_name} card has been deleted")

    else: #If a card not in the catalogue is inputted it loops here until a valid card is inputted
        while card_name not in catalogue:
            print("Please input a valid card")
            card_name = input("Enter the card you want to delete: ")
            card_name = card_name.capitalize()
        print(f"{card_name} card has been deleted")
    del catalogue[card_name] #Deletes the card from the catalogue


print("---WELCOME TO MONSTER CARDS---")
while True: 
    print("\n-Please type in a number between 1-5 to navigate-")
    print("1 Show Card(s)" "\n2 Add Card" "\n3 Search Card" "\n4 Delete Card" "\n5 Quit")
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError: #If non integer is inputted it loops until a number is inputted
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