"""
Diandra O'Connor   1/28/23
Module 3 Project, Optional Bonus

Find the number of words greater than 10 letters in the
text of Hamlet and Julius Caesar

>>> len(longwordset1)
415

>>> len(longwordset2)
197 

>>> len(longwords)
13
"""

import doctest

# read from Hamlet and get a list of words

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  # split on whitespace

# read from Julius Caesar and get a list of words

with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  # split on whitespace



# Remove duplicates by creating two sorted sets
wordset1 = set(sorted(wordlist1))  
wordset2 = set(sorted(wordlist2)) 


# initialize a variable maxlen = 10
maxlen = 10 


# use a list comprension to get a list of words longer than 10
longwordset1 = set(list(word for word in wordset1 if len(word) > maxlen))  # TODO: fix this line
longwordset2 = set([word for word in wordset2 if len(word) > maxlen])  # TODO: fix this line


# find the intersection of the two sets
longwords = longwordset1 & longwordset2


# print the length of the sets and the list
print()
print(f"The number of unique words in Hamlet with more than 10 letters is: {len(longwordset1)}")
print()
print(f"The number of unique words in Julius Caesar with more than 10 letters is: {len(longwordset2)}")
print()
print(f"The number of unique words with more than 10 letters that are in both")
print(f"Hamlet and Julius Caesar is: {len(longwords)} and are displayed below:")
print()
print(f"{sorted(longwords)}")
print()



# check your work
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")
