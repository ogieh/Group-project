#-----------------Kamsi Dictionary--------------------
tiv_english_dict = {
    "Hello": "Môr",
    "Goodbye": "Hangegh",
    "Thank you": "Ker",
    "Yes": "ey",
    "No": "Yam",
    "How are you?": "Ter ka v???",
    "I am fine": "Me laa sha",
    "What is your name?": "Ter ka tsough?",
    "My name is...": "Ter ne me shi...",
    "I don't know": "I never know",
    "Please": "Yôô",
    "Water": "Mai",
    "Food": "Kwagh",
    "Man": "Or",
    "Woman": "Or kwase",
    "Child": "Iyou",
    "Sun": "Iyu",
    "Moon": "Tanger",
    "Big": "Ter",
    "Small": "Môm",
}

def kamsi_dict():
    print("----------------Hello, welcome to the tiv language dictionary---------------------")  # Output: Môr
    print("----------------Avaliable english word to translate to Tiv------------------------")  # Output: Ker
    for word in sorted(tiv_english_dict.keys()):
        print(f"- {word}")
    print(f"- " * 30)

    user_input = input("from list of words above, Choose one to translate? ").capitalize().strip()

    translate = tiv_english_dict.get(user_input)

    if translate:
        print(f"\nSuccess: The Tiv translation for the word '{user_input}' is '{translate}'")  
    else:
        print(f"\nError: The word '{user_input}' is not found in this dictionary")

#-----------------Hadassah Dictionary--------------------
Yoruba_dict = {
"Good-morning": "Ekaro",
"How are you?": "Ba wo ni?",
"Good-evening" : "Ekale",
    "Woman" : " Obirin",
   "Mother" : "Iya",
   "Father" : "Baba",
   "School" : "Alakoiwe",
   "House"  : "ile",
   "Food"   : "Onje",
   "Book"   : "Iwe",
   "Shoe"   : "Bata",
   "Cloth"  : "Aso",
   "Hair"   : "Irun",
   "SackBag": "Saka",
   "Snake"    : "Ejo",
   "Light"  : "Ina",
   "Boy"    : "Omo-okunrin",
   "Girl"   : "Omo-obirin",
   "Beans"  : "Ewa",
   "please" : "Ejor",
}

def Hadassah_dict():
    print("------------ Welcome to the Yoruba Dictionary! -----------------------------")
    print("------------ Avaliable english words to translate to Yoruba-----------------")
    
    for word in sorted(Yoruba_dict.keys()):
        print(f"- {word}")
    print("-" * 30)

    user_input = input("From the list of word above, what word do u need the meaning of? ").capitalize().strip()
    
    translate = Yoruba_dict.get(user_input)

    if translate:
        print(f"\nSuccess: The Yoruba translation for the word '{user_input}' is '{translate}'.")
    else:
        print(f"\nError: The word '{user_input}' is not available in the Yoruba dictionary.")


#-----------------Ella Dictionary-----------------------
Hausa_dict = {
    "Sannu" : "Hello",
    "Ina kwana" : "Good morning",
    "Ina wuni" : "Good afternoon",
    "Ina yini" : "Good evening",
    "Lafiya" : "Fine",
    "Nagode" : "Thank you",
    "Don Allah" : "Please",
    "Eh" : "Yes",
    "A'a" : "No",
    "Ruwa" : "Water",
    "Abinci" : "Food",
    "Gida" : "House",
    "Mutum" : "Person",
    "Yaro" : "Boy",
    "Yarinya" : "Girl",
    "Mota" : "Car",
    "Kudi" : "Money",
    "Kasuwa" : "Market",
    "Makaranta" : "School",
    "Aiki" : "Job",
}

def Ella_dict():
    print("------------ Welcome to the Hausa Dictionary! -----------------------------")
    print("------------ Avaliable english words to translate to Hausa-----------------")
    
    for word in sorted(Hausa_dict.keys()):
        print(f"- {word}")
    print("-" * 30)

    user_input = input("From the list of word above, what word do u need the meaning of? ").capitalize().strip()
    
    translate = Hausa_dict.get(user_input)

    if translate:
        print(f"\nSuccess: The Hausa translation for the word '{user_input}' is '{translate}'.")
    else:
        print(f"\nError: The word '{user_input}' is not available in the Hausa dictionary.")

#-----------------Gabriel Dictionary--------------------
otuo_dict = {
    "Afternoon" : "Oronta",
    "Bird" : "Ghafe",
    "Dog" : "Ghawa",
    "Earth" : "Oto",
    "Evening" : "Ohodere",
    "Father" : "Erah",
    "Fear" : "Ohi",
    "Fish" : "Eshe",
    "Fire" : "Ghera",
    "House" : "Afeh",
    "King" : "Oba",
    "Leopard" : "Ekpe", 
    "Man" : "Omohi",
    "Money" : "Egho",
    "Moon" : "Uki",
    "Morning" : "Ugbere",
    "Night" : "Onighao",
    "Pepper" : "Ashe",
    "Sun": "Ovoh",
    "Water": "Ameh", 
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
    print("2. Tiv Dictionary")  # Placeholder for additional dictionaries
    print("3. Yoruba Dictionary")  # Placeholder for additional dictionaries
    print("4. Hausa Dictionary")  # Placeholder for additional dictionaries
    print("5. [Other Dictionary Option]")  # Placeholder for additional dictionaries
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        Gabriel_dict()
    elif choice == '2':
        kamsi_dict()
    elif choice == '3':
        Hadassah_dict()
    elif choice == '4':
        Ella_dict()
    elif choice == '5':
        print("Other Dictionary Option selected. (Functionality not implemented yet.)") 
    else:
        print("Invalid choice. Please select a valid dictionary.")
main()





