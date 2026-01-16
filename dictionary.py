import streamlit as st

st.set_page_config(page_title="Nigerian Language Dictionary", layout="centered")

st.title(" Nigerian Language Dictionary")
st.write("Select a language and translate English words.")

choice = st.selectbox(
    "Select a language", ("Otuo", "Tiv", "Yoruba", "Hausa", "Igbo")
)

# ---------------- Dictionaries ----------------

Gabriel_dict = {
    "Otuo": {
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
}

Kamsi_dict = {
    "Tiv": {
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
}

Hadassah_dict = {
    "Yoruba": {
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
}

Ella_dict = {
    "Hausa": {
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
}

Kelechi_dict = {
    "Igbo": {
    "Come": "bia",
    "Sit down": "do nana",
    "How are you?": "kedu?",
    "Good morning": "ụtụtụ ọma",
    "Thank you": "daalụ",
    "Goodbye": "ka ọ dị",
    "Welcome": "nnọọ",
    "What is your name?": "kedu aha gị?",
    "My name is": "aha m bụ",
    "Water": "mmiri",
    "Food": "nri",
    "Child": "nwa",
    "Mother": "nne",
    "Father": "nna",
    "House": "ụlọ",
    "Money": "ego",
    "Market": "ahịa",
    "Please": "biko",
    "Sorry": "ndo",
    "Let's go": "ka anyị laa"
    }
}

# ---------------- UI ----------------
words = st.text_input('Enter an English word')

if st.button("Translate"):
    # Get the selected dictionary
    if choice == "Hausa":
        dictionary = Ella_dict["Hausa"]
    elif choice == "Igbo":
        dictionary = Kelechi_dict["Igbo"]
    elif choice == "Otuo":
        dictionary = Gabriel_dict["Otuo"]
    elif choice == "Tiv":
        dictionary = Kamsi_dict["Tiv"]
    elif choice == "Yoruba":
        dictionary = Hadassah_dict["Yoruba"]
    else:
        dictionary = {}
        st.error("Language not supported.")
    
    # Check if word was entered
    if not words:
        st.warning("Please enter a word to translate.")
    else:
        # Capitalize and strip the word for matching
        word_clean = words.capitalize().strip()
        
        # Look up the word in the dictionary
        if word_clean in dictionary:
            st.success(f' Translation ({choice}): **{dictionary[word_clean]}**')
        else:
            st.error(f' Sorry, "{word_clean}" is not in the {choice} dictionary.')
            
        # Show available words
        with st.expander("View available words in this dictionary"):
            for word in sorted(dictionary.keys()):
                st.write(f"- {word}")