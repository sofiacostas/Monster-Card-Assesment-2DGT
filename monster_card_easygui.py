import easygui as eg

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
                power = eg.integerbox(f"Enter a numerical value from 1-25 for {card_name}'s {stat}: ", "Values")
                if power is None: #If user clicks cancel it goes back to navigation screen
                    return 
                elif 1 <= power <= 25: #Sees if power value is between 1-25
                    break
                else:
                    eg.msgbox("Invalid input! Please input a number between 1-25")
            except ValueError: #If a non number is put it says invalid and loops back to power input
                eg.msgbox("Invalid input! Please input a number between 1-25")
        catalogue[card_name][stat] = power


def show_card(): #Shows the card and their values (stats/power)
    message = ""
    for card, values in catalogue.items():
        message += f"\n--{card}--\n"  
        for stat, power in values.items(): 
            message += f"{stat}: {power}\n"  #Is the values of the cards
    eg.codebox("All Current Cards and its Stats", "Show Card(s)", message) #Shows the values of the cards


def add_card(): #Able to add a new card
    card_name = eg.enterbox("Enter name of new card: ", "Add Card")
    if card_name is None: #If user clicks cancel it goes back to navigation screen
        return
        del catalogue[card_name]
    card_name = card_name.capitalize()
    catalogue[card_name] = {}
    range_stats(card_name, catalogue) #Calls function which asks for the values and checks if the values are between 1-25
    eg.msgbox(f"Added {card_name} to catalogue!", "Add Card")


def search_card(): #Search for a specific card and show its values
    card_name = eg.enterbox("Search for card: ", "Search Card")
    if card_name is None:
        return
    card_name = card_name.capitalize()
    if card_name in catalogue:
        card_data = catalogue[card_name]
        message = ""
        for stat, power in card_data.items():
            message += (f"{stat}: {power}\n") #Is the card's values (stats/power)
        eg.msgbox(message, "Card Values")

    else: #If a card not in the catalogue is inputted it loops here until a valid card is inputted
        while card_name not in catalogue: 
            eg.msgbox("Please input a valid card", "Invalid Input")
            card_name = eg.enterbox("Enter the card you want to search: ", "Change")
            if card_name is None:
                return
            card_name = card_name.capitalize()  
            message = (f"--{card_name}--\n") 
        for stat, power in catalogue[card_name].items(): 
            message += (f"{stat}: {power}\n")
        eg.msgbox(message, "Card Values")

    change = eg.enterbox(f"Would you like to change {card_name}'s values? Y/N: ", "Change Value") #To see if they want to change the card they searched values
    if change is None:
        return
    change = change.capitalize()
    if change == "Y": 
       range_stats(card_name, catalogue) #Calls function which asks for the values and checks if the values are between 1-25
    elif change == "N":
        breakpoint


def delete_card(): #Delete a chosen card
    card_name = eg.enterbox("Enter the card you want to delete: ", "Delete Card")
    if card_name is None:
        return
    card_name = card_name.capitalize()
    if card_name in catalogue:
        eg.msgbox(f"{card_name} card has been deleted", "Delete Card")

    else: #If a card not in the catalogue is inputted it loops here until a valid card is inputted
        while card_name not in catalogue:
            eg.msgbox("Please input a valid card")
            card_name = eg.enterbox("Enter the card you want to delete: ", "Delete Card")
            if card_name is None:
                return
            card_name = card_name.capitalize()
        eg.msgbox(f"{card_name} card has been deleted", "Delete Card")
    del catalogue[card_name] #Deletes the card from the catalogue


eg.msgbox("Welcome to MONSTER CARDS","Title Screen")
while True:
    choice = eg.buttonbox("Click on one of the buttons to navigate","Navigation Screen", choices = ["Show Card(s)", "Add Card", "Search Card", "Delete Card", "Quit"]) #Shows the choices as buttons which will lead to the function

    if choice == "Show Card(s)": #When user clicks "Show Card(s)" it runs the function 'show_card'
        show_card()

    elif choice == "Add Card": #When user clicks "Add Card" it runs the function 'add_card'
        add_card()

    elif choice == "Search Card": #When user clicks "Search Card" it runs the function 'search_card'
        search_card()

    elif choice == "Delete Card": #When user clicks "Delete Card" it runs the function 'delete_card'
        delete_card()

    elif choice == "Quit": #Quit/ends the code
        eg.msgbox("Thank you for using MONSTER CARDS", "Quit")
        break