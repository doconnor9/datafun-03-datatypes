"""
Diandra O'Connor  1/28/23
Module 3, Project: Task 5

Domain: gymnastics

Output from user_tuples_etc.py


------------------------------------

=======Tuples=======


The following tuples were created and contain the vault scores for Utah and Oklahoma
at their dual meet

vault_Utah = (9.875, 9.825, 9.9, 9.975, 9.95, 9.8)
vault_OU = (9.95, 9.85, 9.925, 9.95, 9.975, 9.775)


The following tuples were created and contain gymnast name, team and a list of scores
on each of the 4 events

gym1 = ('Amanda', 'Michigan', [9.85, 9.925, 9.775, 9.9])
gym2 = ('Bailey', 'Boise State', [9.775, 9.875, 9.8, 9.85])
gym3 = ('Sarah', 'Iowa', [9.875, 9.875, 9.75, 9.85])
gym4 = ('Laura', 'LSU', [9.9, 9.85, 9.925, 9.95])


We will combine the OU and Utah tuples using concatenation
to show all the vault scores for the meet:

(9.875, 9.825, 9.9, 9.975, 9.95, 9.8, 9.95, 9.85, 9.925, 9.95, 9.975, 9.775)



Tuples can also be repeated. We show the OU vault tuple repeated times 3

(9.95, 9.85, 9.925, 9.95, 9.975, 9.775, 9.95, 9.85, 9.925, 9.95, 9.975, 9.775, 9.95, 9.85, 9.925, 9.95, 9.975, 9.775)



We can use membership testing to determine if a value is in the tuple

Let's see if 9.85 was scored on vault at the competition
9.85 was scored on vault: True

How about a perfect 10.0?
10.0 was scored on vault: False
No, nobody got a 10.0 on vault this time!


There was a petition on Amanda's beam score and it was raised from 9.775 to 9.825
We can modify the score list in the gym1 tuple to reflect this change

The new tuple is ('Amanda', 'Michigan', [9.85, 9.925, 9.825, 9.9])


==========Sets==========

The following sets of beam and floor score were created:
    beam scores: {9.9, 9.85, 9.775, 9.975, 9.075, 9.725, 9.875, 9.225, 9.95}
    floor scores: {9.725, 9.875, 9.825, 9.925, 9.9, 9.85, 9.675}

The union of the two set results in:
{9.9, 9.85, 9.775, 9.975, 9.075, 9.725, 9.875, 9.225, 9.95, 9.825, 9.925, 9.675}

The intersection of the two sets will result in the scores that were scored
on both beam and floor.
Those scores are: {9.725, 9.85, 9.9, 9.875}


========Dictionaries========

We created a dictionary of word : count for each word in the woodchuck text

{'how': 1, 'much': 3, 'wood': 4, 'would': 4, 'a': 4, 'woodchuck': 4, 'chuck': 5, 'if': 2, 'could': 3, 'he': 3, 'as': 4, 'and': 1}







"""