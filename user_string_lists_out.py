"""
Diandra O'Connor  1/28/23
Module 3 Project, Task 4: String Lists

Domain: gymnastics

Output from user_string_lists.py


----------------------------------------------------------

We have created 5 lists related to gymnastics

The lists are as follows:

gymnast names: ['Abby', 'Jillian', 'Lucy', 'Jordan', 'Katherine', 'Danielle']
college teams: ['Oklahoma', 'Florida', 'Michigan', 'Utah', 'Auburn', 'LSU']
skills: ['kip', 'handstand', 'double layout', 'yurchenko', 'wolf jump', 'handstand']
equipment: ['a springboard', 'grips', 'tape', 'a sting mat', 'chalk']
events: ['vault', 'bars', 'beam', 'floor']


-----String List 1. Using Python Built-in Functions-----


Let's see what the length of our lists are:
  gymnast names: 6
  college teams: 6
         skills: 6
      equipment: 5
         events: 4


To find the unique values in the skills list we can make it a set.
The set of skills is: {'double layout', 'yurchenko', 'handstand', 'wolf jump', 'kip'}


We can merge two lists to form a list of tuples.
For example, we can merge the names list with the teams list and get:

[('Abby', 'Oklahoma'), ('Jillian', 'Florida'), ('Lucy', 'Michigan'), ('Jordan', 'Utah'), ('Katherine', 'Auburn'), ('Danielle', 'LSU')]


In this next example we merge the names list with the events list to form:

[('Abby', 'vault'), ('Jillian', 'bars'), ('Lucy', 'beam'), ('Jordan', 'floor')]
Notice we only have 4 tuples because the events list only has 4 elements


We can also combine more than two lists.
Below we combine the 3 lists - teams, names and equipment:

[('Oklahoma', 'Abby', 'a springboard'), ('Florida', 'Jillian', 'grips'), ('Michigan', 'Lucy', 'tape'), ('Utah', 'Jordan', 'a sting mat'), ('Auburn', 'Katherine', 'chalk')]



-----String Lists 2. Random Choice-----


We will decide which event to start practice on today by selecting a random value from the list
Looks like we are starting on floor today!

We can make a fun sentence by using random selection
Random words were chosen from the lists above to make the sentence:

Abby from LSU did a perfect double layout despite not having tape


-----String List 3. Get Unique Words-----

We used the text of zen of python to get a list of the unique words.

Lets sort the list to be in alphabetical order
In order to do this we must first change all the letters to be either upper or lowercase
In addition, we need to remove the symbols * and - to clean up our words

Our alphabetical list of unique words with the unwanted characters removed is: 
['a', 'although', 'ambiguity,', 'and', 'are', "aren't", 'at', 'bad', 'be', 'beats', 'beautiful', 'better', 'break', 'cases', 'complex', 'complex.', 'complicated.', 'counts.', 'dense.', 'do', 'dutch.', 'easy', 'enough', 'errors', 'explain,', 'explicit', 'explicitly', 'face', 'first', 'flat', 'good', 'great', 'guess.', 'hard', 'honking', 'idea', 'idea.', 'if', 'implementation', 'implicit.', 'in', 'is', 'it', "it's", 'it.', "let's", 'may', 'more', 'namespaces', 'nested.', 'never', 'never.', 'not', 'now', 'now.', 'obvious', 'obvious', 'of', 'often', 'one', 'one', 'only', 'pass', 'practicality', 'preferably', 'purity.', 'readability', 'refuse', 'right', 'rules.', 'should', 'silenced.', 'silently.', 'simple', 'sparse', 'special', 'special', 'temptation', 'than', 'that', 'the', 'there', 'those!', 'to', 'ugly.', 'unless', 'unless', 'way', "you're"]

Our list has 89 unique words!




"""