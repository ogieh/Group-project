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
    "Hello": "Sannu",
    "Good morning": "Ina kwana",
    "Good afternoon": "Ina wuni",
    "Good evening": "Ina yini",
    "Fine": "Lafiya",
    "Thank you": "Nagode",
    "Please": "Don Allah",
    "Yes": "Eh",
    "No": "A'a",
    "Water": "Ruwa",
    "Food": "Abinci",
    "House": "Gida",
    "Person": "Mutum",
    "Boy": "Yaro",
    "Girl": "Yarinya",
    "Car": "Mota",
    "Money": "Kudi",
    "Market": "Kasuwa",
    "School": "Makaranta",
    "Job": "Aiki",
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


#-----------------Kelechi's Dictionary-----------------------
print('<<<<< WELCOME TO MY IGBO LANGUAGE DICTIONARY >>>>>')
print("You can translate from English to Igbo or Igbo to English")

# Dictionary with 20 Igbo words and their English meanings
igbo_to_english_dict = {
    "bia": "come",
    "do nana": "sit down",
    "kedu": "how are you",
    "ụtụtụ ọma": "good morning",
    "daalụ": "thank you",
    "ka ọ dị": "goodbye",
    "nnọọ": "welcome",
    "kedu aha gị": "what is your name",
    "aha m bụ": "my name is",
    "mmiri": "water",
    "nri": "food",
    "nwa": "child",
    "nne": "mother",
    "nna": "father",
    "ụlọ": "house",
    "ego": "money",
    "ahịa": "market",
    "biko": "please",
    "ndo": "sorry",
    "ka anyị laa": "let's go"
}

# Create the reverse dictionary for English to Igbo
def kelechi_dict():
    kelechi_dict = {v: k for k, v in igbo_to_english_dict.items()}

    print(f"\n📚 Dictionary contains {len(igbo_to_english_dict)} words/phrases")
    print("-" * 50)

    while True:
        print("\n" + "=" * 50)
        print("TRANSLATION OPTIONS:")
        print("1. English → Igbo")
        print("2. Igbo → English")
        print("3. Show all words")
        print("4. Quit")
        print("=" * 50)

        choice = input("\nChoose option (1-4): ").strip()

        # QUIT
        if choice == '4':
            print("\nDaalụ! (Thank you!) Ka ọ dị! (Goodbye!)")
            break

        # SHOW ALL WORDS
        elif choice == '3':
            print("\n" + "=" * 50)
            print("ALL WORDS IN DICTIONARY:")
            print("=" * 50)
            print("\nENGLISH → IGBO:")
            print("-" * 30)
            for i, (eng, igbo) in enumerate(sorted(kelechi_dict.items()), 1):
                print(f"{i:2}. {eng:20} → {igbo}")

            print("\nIGBO → ENGLISH:")
            print("-" * 30)
            for i, (igbo, eng) in enumerate(sorted(igbo_to_english_dict.items()), 1):
                print(f"{i:2}. {igbo:20} → {eng}")
            continue

        # ENGLISH TO IGBO
        elif choice == '1':
            word = input("\nEnter English word/phrase: ").strip().lower()
            if word in kelechi_dict:
                print(f"\n✓ Translation: '{word}' → '{kelechi_dict[word]}'")
            else:
                print(f"\n✗ '{word}' not found in dictionary")
                # Show similar words
                suggestions = [w for w in kelechi_dict.keys() if word in w or w.startswith(word[:2])]
                if suggestions:
                    print(f"   Did you mean: {', '.join(suggestions[:3])}?")

        # IGBO TO ENGLISH
        elif choice == '2':
            word = input("\nEnter Igbo word/phrase: ").strip().lower()
            if word in igbo_to_english_dict:
                print(f"\n✓ Translation: '{word}' → '{igbo_to_english_dict[word]}'")
            else:
                print(f"\n✗ '{word}' not found in dictionary")
                # Show similar words
                suggestions = [w for w in igbo_to_english_dict.keys() if word in w or w.startswith(word[:2])]
                if suggestions:
                    print(f"   Did you mean: {', '.join(suggestions[:3])}?")

        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

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
    print("5. Igbo Dictionary")  # Placeholder for additional dictionaries
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
       kelechi_dict()
    else:
        print("Invalid choice. Please select a valid dictionary.")
main()






