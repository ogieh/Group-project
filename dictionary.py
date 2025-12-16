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

# Example usage:

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

kamsi_dict()


Yoruba_dict = {
 "Good-morning": "Ekaro"
"How are you?": "Ba wo ni?"
"Good-evening" : "Ekale"
    "Woman" : " Obirin"
   "Mother" : "Iya"
   "Father" : "Baba"
   "School" : "Alakoiwe"
   "House"  : "ile"
   "Food"   : "Onje"
   "Book"   : "Iwe"
   "Shoe"   : "Bata"
   "Cloth"  : "Aso"
   "Hair"   : "Irun"
   "SackBag": "Saka"
   "Snake"    : "Ejo"
   "Light"  : "Ina"
   "Boy"    : "Omo-okunrin"
   "Girl"   : "Omo-obirin"
   "Beans"  : "Ewa"
   "please" : "Ejor"
}
