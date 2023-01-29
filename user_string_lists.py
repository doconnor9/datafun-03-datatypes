"""
Diandra O'Connor 1/27/23
Module 3 Project, Task 4 String Lists

Domain: gymnastics

"""

import random

# define five lists of strings

# define list of names
list_names = ["Abby", "Jillian", "Lucy", "Jordan", "Katherine", "Danielle"]

# define list of teams
list_teams = ["Oklahoma", "Florida", "Michigan", "Utah", "Auburn", "LSU"]

# define list of skills
list_skills = ["kip", "handstand", "double layout", "yurchenko", "wolf jump", "handstand"]

# define list of equipment
list_equipment = ["a springboard", "grips", "tape", "a sting mat", "chalk"]

# define list of events
list_events = ["vault", "bars", "beam", "floor"]

print()
print("We have created 5 lists related to gymnastics")
print()
print("The lists are as follows:")
print()
print(f"gymnast names: {list_names}")
print(f"college teams: {list_teams}")
print(f"skills: {list_skills}")
print(f"equipment: {list_equipment}")
print(f"events: {list_events}")
print()
print()


# -------------------------------------------------------------------------------------------
# String List 1. Using Python Built-in Functions
print("-----String List 1. Using Python Built-in Functions-----")

# use built in functions len(), set(), zip()


# len()
print()
print()
print("Let's see what the length of our lists are:")
print(f"  gymnast names: {len(list_names)}")
print(f"  college teams: {len(list_teams)}")
print(f"         skills: {len(list_skills)}")
print(f"      equipment: {len(list_equipment)}")
print(f"         events: {len(list_events)}")
print()


# set()
print()
print("To find the unique values in the skills list we can make it a set.")
print(f"The set of skills is: {set(list_skills)}")
print()


def merge (list1, list2):
    """Returns a list of tuples from merging two string lists."""
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

print()
print("We can merge two lists to form a list of tuples.")
print("For example, we can merge the names list with the teams list and get:")
print()
print(merge (list_names, list_teams))
print()
print()


# zip()
print("In this next example we merge the names list with the events list to form:")
print()
print(list(zip(list_names, list_events)))
print("Notice we only have 4 tuples because the events list only has 4 elements")
print()
print()

print("We can also combine more than two lists.")
print("Below we combine the 3 lists - teams, names and equipment:")
print()
print(list(zip(list_teams, list_names, list_equipment)))
print()
print()
print()


# ---------------------------------------------------------------------------------------
# String Lists 2. Random Choice
print("-----String Lists 2. Random Choice-----")


# select a random value from a list using random.choice()
def random_selection(list):
    """Return random value from list."""
    return random.choice(list)


print()
print()
print("We will decide which event to start practice on today by selecting a random value from the list")
print(f"Looks like we are starting on {random_selection(list_events)} today!")
print()

# use sentence generator to create a random sentence
sentence = (f"{random.choice(list_names)} from {random.choice(list_teams)} did a perfect "
f"{random.choice(list_skills)} despite not having {random.choice(list_equipment)}.")

print("We can make a fun sentence by using random selection")
print("Random words were chosen from the lists above to make the sentence:")
print()
print(sentence)
print()
print()


# ----------------------------------------------------------------------------------------
# String List 3. Get Unique Words
print("-----String List 3. Get Unique Words-----")

# read in zen of python to get a list of words
with open("text_zen_of_python.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()  # split on whitespace
    unique_words = set(list_words)  # remove duplicates


print()
print("We used the text of zen of python to get a list of the unique words.")
print()
print("Lets sort the list to be in alphabetical order")
print("In order to do this we must first change all the letters to be either upper or lowercase")
print("In addition, we need to remove the symbols * and - to clean up our words")

unique_words_lower = [x.lower() for x in unique_words] # change to lowercase

unique_words_lower_mod = [str.replace("-", "") for str in unique_words_lower] # remove -
unique_words_lower_mod2 = [str.replace("*", "") for str in unique_words_lower_mod] # remove *
unique_words_lower_mod2.remove("") # remove now empty space

alphabetical_list = sorted(unique_words_lower_mod2)

unique_word_ct = len(unique_words_lower_mod2)

print()
print("Our alphabetical list of unique words with the unwanted characters removed is: ")
print(alphabetical_list)
print()
print(f"Our list has {unique_word_ct} unique words!")
print()




