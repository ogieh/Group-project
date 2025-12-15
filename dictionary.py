otuo_dict = {
    "Afternoon" : "Avan",
    "Bird" : "Ahiame",
    "Dog" : "Awa",
    "Earth" : "Oto",
    "Evening" : "Emhuan",
    "Father" : "Erha",
    "Fear" : "Ofen",
    "Fish" : "Ehen",
    "Fire" : "Erhen",
    "House" : "Owa",
    "King" : "Oba",
    "Leopard" : "Ekpen", 
    "Man" : "Arhie",
    "Money" : "Igho",
    "Moon" : "Uki",
    "Morning" : "Ewewie",
    "Night" : "Ason",
    "Pepper" : "Ehien",
    "Sun": "Uvo",
    "Water": "Ame", 
}

def Gabriel_dict():
    print("------------ Welcome to the Otuo Dictionary! -----------------------------")
    print("------------ Avaliable english words to translate to Otuo-----------------")
    
    for word in sorted(otuo_dict.keys()):
        print(f"- {word}")
    print("-" * 30)

    user_input = input("From the list of word above, what word do u need the meaning of? ").capitalize().strip()
    
    translate = otuo_dict.get(user_input)

    if translate:
        print(f"\nSuccess: The Otuo translation for the word '{user_input}' is '{translate}'.")
    else:
        print(f"\nError: The word '{user_input}' is not available in the Otuo dictionary.")

#--------------------------------------------------

#                Main Selector For Dictionaries

#--------------------------------------------------

def main():
    print("Select a dictionary to use:")
    print("1. Otuo Dictionary")
    print("2. [Other Dictionary Option]")  # Placeholder for additional dictionaries
    print("3. [Other Dictionary Option]")  # Placeholder for additional dictionaries
    print("4. [Other Dictionary Option]")  # Placeholder for additional dictionaries
    print("5. [Other Dictionary Option]")  # Placeholder for additional dictionaries
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        Gabriel_dict()
    elif choice == '2':
        print("Other Dictionary Option selected. (Functionality not implemented yet.)")
    elif choice == '3':
        print("Other Dictionary Option selected. (Functionality not implemented yet.)")
    elif choice == '4':
        print("Other Dictionary Option selected. (Functionality not implemented yet.)")
    elif choice == '5':
        print("Other Dictionary Option selected. (Functionality not implemented yet.)") 
    else:
        print("Invalid choice. Please select a valid dictionary.")
main()