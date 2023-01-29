"""
Diandra O'Connor  1/28/23
Module 3, Project, Task 5

Domain: gymnastics

Using tuples, dictionaries and sets

"""
print()
print("=======Tuples=======")

# Create some tuples
gym1 = ("Amanda", "Michigan", [9.85, 9.925, 9.775, 9.9])
gym2 = ("Bailey", "Boise State", [9.775, 9.875, 9.8, 9.85])
gym3 = ("Sarah", "Iowa", [9.875, 9.875, 9.75, 9.85])
gym4 = ("Laura", "LSU", [9.9, 9.85, 9.925, 9.95])

vault_Utah = (9.875, 9.825, 9.9, 9.975, 9.95, 9.8)
vault_OU = (9.95, 9.85, 9.925, 9.95, 9.975, 9.775)

print()
print()
print("The following tuples were created and contain the vault scores for Utah and Oklahoma")
print("at their dual meet")
print()
print(f"{vault_Utah = }")
print(f"{vault_OU = }")

print()
print()
print("The following tuples were created and contain gymnast name, team and a list of scores")
print("on each of the 4 events")
print()
print(f"{gym1 = }")
print(f"{gym2 = }")
print(f"{gym3 = }")
print(f"{gym4 = }")
print()

# tuple concatenation
vault_meet = vault_Utah + vault_OU

print()
print("We will combine the OU and Utah tuples using concatenation")
print("to show all the vault scores for the meet:")
print()
print(vault_meet)
print()

# tuple repetition
vault3_OU = vault_OU * 3

print()
print()
print("Tuples can also be repeated. We show the OU vault tuple repeated times 3")
print()
print(vault3_OU)
print()
print()
print()


# tuple membership testing
vault9_85 = 9.85 in vault_meet  
vault10_0 = 10.0 in vault_meet


print("We can use membership testing to determine if a value is in the tuple")
print()
print("Let's see if 9.85 was scored on vault at the competition")
print(f"9.85 was scored on vault: {vault9_85}")
print()
print("How about a perfect 10.0?")
print(f"10.0 was scored on vault: {vault10_0}")
print("No, nobody got a 10.0 on vault this time!")
print()


# modifying a list within a tuple
gym1[2][2] = 9.825

print()
print("There was a petition on Amanda's beam score and it was raised from 9.775 to 9.825")
print("We can modify the score list in the gym1 tuple to reflect this change")
print()
print(f"The new tuple is {gym1}")
print()
print()


print("==========Sets==========")
# =============================================================================================
# Sets


# create two sets
beam_scores = {9.9, 9.85, 9.775, 9.975, 9.075, 9.725, 9.875, 9.225, 9.95}
floor_scores = {9.925, 9.85, 9.675, 9.9, 9.875, 9.9, 9.825, 9.725}

# set union
beam_floor = beam_scores | floor_scores

# set intersection
beam_floor_both = beam_scores & floor_scores


print()
print("The following sets of beam and floor score were created:")
print(f"    beam scores: {beam_scores}")
print(f"    floor scores: {floor_scores}")
print()
print("The union of the two set results in:")
print(f"{beam_floor}")
print()
print("The intersection of the two sets will result in the scores that were scored")
print("on both beam and floor.")
print(f"Those scores are: {beam_floor_both}")
print()
print()



print("========Dictionaries========")
# ==============================================================================
# Dictionaries


with open("text_woodchuck.txt") as file_object:
    word_list = file_object.read().split()

word_list_lower = [x.lower() for x in word_list] # change to lowercase
word_list_mod = [str.replace(",", "") for str in word_list_lower] # remove ,
word_list_mod2 = [str.replace("?", "") for str in word_list_mod] # remove ?
word_list_mod3 = [str.replace(".", "") for str in word_list_mod2] # remove .

word_counts_dict = {word: word_list_mod3.count(word) for word in word_list_mod3}

print()
print("We created a dictionary of word : count for each word in the woodchuck text")
print()
print(word_counts_dict)
print()

