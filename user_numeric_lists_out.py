"""Diandra O'Connor 1/27/23
Module 3 Project, Task 3: Numeric Lists

Domain: gymnastics

Output from a run of user_numeric_lists.py

"""



"""

Welcome to the gymnastics recap
On 1-22-23 the OU Sooners took on the Utah Utes at home in Norman, Oklahoma.
OU outperformed Utah for the win, but lets take a closer looks at some scores

The Sooners scored the following across all events: [9.95, 9.85, 9.925, 9.95, 9.975, 9.775, 9.9, 9.875, 9.875, 9.875, 9.7, 9.9, 9.725, 9.9, 9.875, 9.225, 9.95, 9.9, 9.925, 9.85, 9.675, 9.9, 9.875, 9.95]

The Utes managed to stack up the following scores: [9.875, 9.825, 9.9, 9.975, 9.95, 9.8, 9.85, 9.875, 9.75, 9.825, 9.85, 9.675, 9.9, 9.85, 9.775, 9.9, 9.975, 9.075, 9.675, 9.85, 9.925, 9.825, 9.725, 9.875]



--------List 1. List Statistics--------

Lets compare the two teams by looking at the mean, median and mode of their scores

Following are the results for OU:
     mean score:   9.846
   median score:   9.8875
           mode:   9.9

Now lets look at the same for Utah:
     mean score:   9.812
   median score:   9.85
           mode:   9.85


Next we will look at standard deviation and variance

The variance in OU scores is: 0.02
The standard deviation is: 0.15

For the Utes, the variance of their scores is: 0.03
The standard deviation is: 0.17



-----List 2. Lists - Correlation and Prediction-----

We will use some example data on time and number of spectators
  to explore the topic of corelation and prediction

For our x values, lets use time in minutes since the doors opened
For our y data we will use number of spectators in the venue

Here is our data:
x(time values) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y(number of spectators) = [88, 175, 211, 250, 430, 697, 799, 950, 1104, 1397]

The correlation of x and y is: 0.98

Since the correlation is close to 1, lets predict a future y value

When the doors have been open for 15 minutes,
  the predicted number of spectators in the venue will be: 1986



-----List 3. List - Using Python Built-in Functions-----

Next, we will use built-in Python function to compare the scores of the two teams
We will use min, max, len, sum, average, set, and sorted to explore the data

The lowest score for each team was:
     OU: 9.225
   Utah: 9.075

The highest score for each team was:
     OU: 9.975
   Utah: 9.975

The total number of scores was the same for both teams.
OU competed 24 routines and Utah competed 24 routines

The total score for all the routines competed by each team is:
     OU: 236.3
   Utah: 235.5

The average score for each team is:
     OU: 9.846
   Utah: 9.812

The score set for each team is:
     OU: {9.95, 9.775, 9.975, 9.85, 9.925, 9.9, 9.875, 9.7, 9.725, 9.225, 9.675}
   Utah: {9.875, 9.975, 9.9, 9.825, 9.95, 9.8, 9.85, 9.75, 9.675, 9.775, 9.075, 9.925, 9.725}

Following is a list of all scores from low to high for each team:
     OU: [9.225, 9.675, 9.7, 9.725, 9.775, 9.85, 9.85, 9.875, 9.875, 9.875, 9.875, 9.875, 9.9, 9.9, 9.9, 9.9, 9.9, 9.925, 9.925, 9.95, 9.95, 9.95, 9.95, 9.975]

   Utah: [9.075, 9.675, 9.675, 9.725, 9.75, 9.775, 9.8, 9.825, 9.825, 9.825, 9.85, 9.85, 9.85, 9.85, 9.875, 9.875, 9.875, 9.9, 9.9, 9.9, 9.925, 9.95, 9.975, 9.975]


Now lets looks at the scores in opposite order, from high to low:
     OU: [9.975, 9.95, 9.95, 9.95, 9.95, 9.925, 9.925, 9.9, 9.9, 9.9, 9.9, 9.9, 9.875, 9.875, 9.875, 9.875, 9.875, 9.85, 9.85, 9.775, 9.725, 9.7, 9.675, 9.225]

   Utah: [9.975, 9.975, 9.95, 9.925, 9.9, 9.9, 9.9, 9.875, 9.875, 9.875, 9.85, 9.85, 9.85, 9.85, 9.825, 9.825, 9.825, 9.8, 9.775, 9.75, 9.725, 9.675, 9.675, 9.075]



-----List 4. List Methods-----

Now lets focus on the Sooners and make some changes to their score list using Methods

Let's add another score to their list, we will use 9.5

Now the OU list of scores has 9.5 as it's last value
[9.95, 9.85, 9.925, 9.95, 9.975, 9.775, 9.9, 9.875, 9.875, 9.875, 9.7, 9.9, 9.725, 9.9, 9.875, 9.225, 9.95, 9.9, 9.925, 9.85, 9.675, 9.9, 9.875, 9.95, 9.5]


Now lets extend their list by adding the following 3 scores: 10.0, 9.9, 9.875
[9.95, 9.85, 9.925, 9.95, 9.975, 9.775, 9.9, 9.875, 9.875, 9.875, 9.7, 9.9, 9.725, 9.9, 9.875, 9.225, 9.95, 9.9, 9.925, 9.85, 9.675, 9.9, 9.875, 9.95, 9.5, 10.0, 9.9, 9.875]


Next, we will insert 2 scores in the list
We will make a score of 2 as the 6th score and a score of 5 as the 10th score

[9.95, 9.85, 9.925, 9.95, 9.975, 2, 9.775, 9.9, 9.875, 5, 9.875, 9.875, 9.7, 9.9, 9.725, 9.9, 9.875, 9.225, 9.95, 9.9, 9.925, 9.85, 9.675, 9.9, 9.875, 9.95, 9.5, 10.0, 9.9, 9.875]


Now we will remove 5 from the OU scores:
[9.95, 9.85, 9.925, 9.95, 9.975, 2, 9.775, 9.9, 9.875, 9.875, 9.875, 9.7, 9.9, 9.725, 9.9, 9.875, 9.225, 9.95, 9.9, 9.925, 9.85, 9.675, 9.9, 9.875, 9.95, 9.5, 10.0, 9.9, 9.875]


Next, we will count how many times 2 appears in the score list
The score 2 appears 1 time in the list

This will be more fun, lets see how many times 9.95 appears in the list
The Sooners had 4 routines that scored 9.95! 


The modified score list in order from lowest to highest is:
[2, 9.225, 9.5, 9.675, 9.7, 9.725, 9.775, 9.85, 9.85, 9.875, 9.875, 9.875, 9.875, 9.875, 9.875, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.925, 9.925, 9.95, 9.95, 9.95, 9.95, 9.975, 10.0]


The modified score list in order from highes to lowest is:
[10.0, 9.975, 9.95, 9.95, 9.95, 9.95, 9.925, 9.925, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.875, 9.875, 9.875, 9.875, 9.875, 9.875, 9.85, 9.85, 9.775, 9.725, 9.7, 9.675, 9.5, 9.225, 2]


Now we will make a copy of the modified score list:
[10.0, 9.975, 9.95, 9.95, 9.95, 9.95, 9.925, 9.925, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.875, 9.875, 9.875, 9.875, 9.875, 9.875, 9.85, 9.85, 9.775, 9.725, 9.7, 9.675, 9.5, 9.225, 2]


Next, we will remove/pop the first score from the list leaving the following:
[9.975, 9.95, 9.95, 9.95, 9.95, 9.925, 9.925, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.875, 9.875, 9.875, 9.875, 9.875, 9.875, 9.85, 9.85, 9.775, 9.725, 9.7, 9.675, 9.5, 9.225, 2]


Now we will remove/pop the last value in the list leaving:
[9.975, 9.95, 9.95, 9.95, 9.95, 9.925, 9.925, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.875, 9.875, 9.875, 9.875, 9.875, 9.875, 9.85, 9.85, 9.775, 9.725, 9.7, 9.675, 9.5, 9.225]



-----List 5. List Transformations - Using filter() and map()-----

Lets filter the OU score list to include only the score above 9.85

Wow! OU has a great team because that's still a lot of scores above 9.85!
[10.0, 9.975, 9.95, 9.95, 9.95, 9.95, 9.925, 9.925, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.875, 9.875, 9.875, 9.875, 9.875, 9.875]


Now lets map each score to its cube root. We will round to 4 decimal places
The results are: [2.1544, 2.1526, 2.1508, 2.1508, 2.1508, 2.1508, 2.149, 2.149, 2.1472, 2.1472, 2.1472, 2.1472, 2.1472, 2.1472, 2.1454, 2.1454, 2.1454, 2.1454, 2.1454, 2.1454, 2.1436, 2.1436, 2.1382, 2.1345, 2.1327, 2.1308, 2.1179, 2.0973, 1.2599]


Next, we use map to calculate the volume of a cube with a side equal to one of the scores
For easy math, I will choose the score 10.0.
The volume for a cube with a side equal to 10 is: [1000.0]
Since there is only one score of 10.0 in our list, we get a list with only one value, 1000



-----List 6. List Transformations - Using List Comprehension-----

Now we will find the scores above 9.9 using list comprehension
The following is a list showing the Sooners scores above 9.9: [10.0, 9.975, 9.95, 9.95, 9.95, 9.95, 9.925, 9.925]

Next, we will triple each score in the Sooners score list and round to 2 decimal places
The new tripled scores are: [30.0, 29.92, 29.85, 29.85, 29.85, 29.85, 29.78, 29.78, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.62, 29.62, 29.62, 29.62, 29.62, 29.62, 29.55, 29.55, 29.33, 29.17, 29.1, 29.03, 28.5, 27.67, 6]

Now, for every score less than 9.8 we will add 0.05, the rest of the scores stay the same
The score list now looks like this: [10.0, 9.975, 9.95, 9.95, 9.95, 9.95, 9.925, 9.925, 9.9, 9.9, 9.9, 9.9, 9.9, 9.9, 9.875, 9.875, 9.875, 9.875, 9.875, 9.875, 9.85, 9.85, 9.825, 9.775, 9.75, 9.725, 9.55, 9.275, 2.05]


Now we will jump back to the Utes and calculate their final score

Since the rules for college gymnastics allow you to drop the lowest score on each event,
we will use a function to filter out the lowest score
and add the remaining scores together to get each event total.
Then, we will add all the events together to get the final score for the Utes

The event scores for Utah are:
    Vault: 49.525
     Bars: 49.15
     Beam: 49.4
    Floor: 49.2

The final score for the Utes is: 197.275 

While 197.275 is a great score, it wasn't enough to beat the Sooners
who scored 197.925!!  Boomer!






 """