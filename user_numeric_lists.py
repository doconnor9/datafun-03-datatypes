"""
Diandra O'Connor  1/26/23
Module 3, Task 3 - Numeric Lists

Domain: gymnastics

"""

import math
import statistics


# scores from OU vs. Utah on 1/22/23
OU_scores_list = [9.95, 9.85, 9.925, 9.95, 9.975, 9.775,
 9.9, 9.875, 9.875, 9.875, 9.7, 9.9, 9.725, 9.9, 9.875, 9.225, 9.95, 
 9.9, 9.925, 9.85, 9.675, 9.9, 9.875, 9.95]

Utah_scores_list = [9.875, 9.825, 9.9, 9.975, 9.95, 9.8, 
9.85, 9.875, 9.75, 9.825, 9.85, 9.675, 9.9, 9.85,9.775,9.9, 9.975, 
9.075, 9.675, 9.85, 9.925, 9.825, 9.725, 9.875]

x_time_after_doors_open = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # time in minutes
y_num_spectators = [88, 175, 211, 250, 430, 697, 799, 950, 1104, 1397] # made up numbers


print()
print("Welcome to the gymnastics recap")
print("On 1-22-23 the OU Sooners took on the Utah Utes at home in Norman, Oklahoma.")
print("OU outperformed Utah for the win, but lets take a closer looks at some scores")
print()
print(f"The Sooners scored the following across all events: {OU_scores_list}")
print()
print(f"The Utes managed to stack up the following scores: {Utah_scores_list}")
print()
print()
print()


# -------------------------------------------------------------------------------
# List 1. List Statistics
print ("--------List 1. List Statistics--------")

# Calculate mean, median and mode
mean_OU = statistics.mean(OU_scores_list)
median_OU = statistics.median(OU_scores_list)
mode_OU = statistics.mode(OU_scores_list)

mean_Utah = statistics.mean(Utah_scores_list)
median_Utah = statistics.median(Utah_scores_list)
mode_Utah = statistics.mode(Utah_scores_list)

print()
print("Lets compare the two teams by looking at the mean, median and mode of their scores")
print()
print(f"Following are the results for OU:")
print(f"     mean score:   {mean_OU:.3f}")
print(f"   median score:   {median_OU}")
print(f"           mode:   {mode_OU}")
print()
print("Now lets look at the same for Utah:")
print(f"     mean score:   {mean_Utah:.3f}")
print(f"   median score:   {median_Utah}")
print(f"           mode:   {mode_Utah}")
print()



# Calculate standard deviation and variance
var_OU = statistics.pvariance(OU_scores_list) # population because have all score from the meet
stdev_OU = statistics.pstdev(OU_scores_list)

var_Utah = statistics.pvariance(Utah_scores_list)
stdev_Utah = statistics.pstdev(Utah_scores_list)

print()
print("Next we will look at standard deviation and variance")
print()
print(f"The variance in OU scores is: {var_OU:.2f}")
print(f"The standard deviation is: {stdev_OU:.2f}")
print()
print(f"For the Utes, the variance of their scores is: {var_Utah:.2f}")
print(f"The standard deviation is: {stdev_Utah:.2f}")
print()
print()
print()


# -------------------------------------------------------------------------------
# List 2. Lists - Correlation and Prediction
print("-----List 2. Lists - Correlation and Prediction-----")


# Calculate correlation between x and y
if len(x_time_after_doors_open) != len(y_num_spectators):
    print("ERROR: The related sets are not the same size.")
    print(f"      {len(x_time_after_doors_open)}!={len(y_num_spectators)}")
    quit()

try:
   
    xy_corr = statistics.correlation(x_time_after_doors_open, y_num_spectators)

except Exception as e:
    print(f"ERROR:    {e}")
    print("Please fix error and try again.")
    quit()


# Calculate slope and intercept of best fit line
slope, intercept = statistics.linear_regression(x_time_after_doors_open, y_num_spectators)

future_x = 15

future_y = (slope * future_x + intercept)  # predicted y value when x = 15

print()
print("We will use some example data on time and number of spectators")
print("  to explore the topic of corelation and prediction")
print()
print("For our x values, lets use time in minutes since the doors opened")
print("For our y data we will use number of spectators in the venue")
print()
print("Here is our data:")
print(f"x(time values) = {x_time_after_doors_open}")
print(f"y(number of spectators) = {y_num_spectators}")
print()
print(f"The correlation of x and y is: {xy_corr:.2f}")
print()
print("Since the correlation is close to 1, lets predict a future y value")
print()
print("When the doors have been open for 15 minutes,")
print(f"  the predicted number of spectators in the venue will be: {future_y:.0f}")
print()
print()
print()


# --------------------------------------------------------------------------------
# List 3. List - Using Python Built-in Functions
# min(), max(), len(), sum(), average(), set(), sorted(), sorted() using reverse = True
print("-----List 3. List - Using Python Built-in Functions-----")

low_score_OU = min(OU_scores_list)
low_score_Utah = min(Utah_scores_list)

high_score_OU = max(OU_scores_list)
high_score_Utah = max(Utah_scores_list)

number_of_scores_OU = len(OU_scores_list)
number_of_scores_Utah = len(Utah_scores_list)

total_OU = math.fsum(OU_scores_list)
total_Utah = math.fsum(Utah_scores_list)

average_score_OU = total_OU / number_of_scores_OU
average_score_Utah = total_Utah / number_of_scores_Utah

score_set_OU = set(OU_scores_list)
score_set_Utah = set(Utah_scores_list)

asc_scores_OU = sorted(OU_scores_list)
asc_scores_Utah = sorted(Utah_scores_list)

desc_scores_OU = sorted(OU_scores_list, reverse=True)
desc_scores_Utah = sorted(Utah_scores_list, reverse=True)

print()
print("Next, we will use built-in Python function to compare the scores of the two teams")
print("We will use min, max, len, sum, average, set, and sorted to explore the data")
print()
print("The lowest score for each team was:")
print(f"     OU: {low_score_OU}")
print(f"   Utah: {low_score_Utah}")
print()
print("The highest score for each team was:")
print(f"     OU: {high_score_OU}")
print(f"   Utah: {high_score_Utah}")
print()
print("The total number of scores was the same for both teams.")
print(f"OU competed {number_of_scores_OU} routines and Utah competed {number_of_scores_Utah} routines")
print()
print("The total score for all the routines competed by each team is:")
print(f"     OU: {total_OU}")
print(f"   Utah: {total_Utah}")
print()
print("The average score for each team is:")
print(f"     OU: {average_score_OU:.3f}")
print(f"   Utah: {average_score_Utah:.3f}")
print()
print("The score set for each team is:")
print(f"     OU: {score_set_OU}")
print(f"   Utah: {score_set_Utah}")
print()
print("Following is a list of all scores from low to high for each team:")
print(f"     OU: {asc_scores_OU}")
print()
print(f"   Utah: {asc_scores_Utah}")
print()
print()
print("Now lets looks at the scores in opposite order, from high to low:")
print(f"     OU: {desc_scores_OU}")
print()
print(f"   Utah: {desc_scores_Utah}")
print()
print()
print()


# ----------------------------------------------------------------------------------
# List 4. List Methonds
print("-----List 4. List Methods-----")


print()
print("Now lets focus on the Sooners and make some changes to their score list using Methods")
print()

# append a single value to the list
OU_scores_list.append(9.5)

print("Let's add another score to their list, we will use 9.5")
print()
print("Now the OU list of scores has 9.5 as it's last value")
print(OU_scores_list)
print()
print()


# extend list with new list
OU_scores_list.extend([10.0, 9.9, 9.875])

print("Now lets extend their list by adding the following 3 scores: 10.0, 9.9, 9.875")
print(OU_scores_list)
print()
print()


# insert() at an index, insert a value
OU_scores_list.insert(5, 2)
OU_scores_list.insert(9, 5)

print("Next, we will insert 2 scores in the list")
print("We will make a score of 2 as the 6th score and a score of 5 as the 10th score")
print()
print(OU_scores_list)
print()
print()


# remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
if (5) in OU_scores_list: OU_scores_list.remove(5)

print("Now we will remove 5 from the OU scores:")
print(OU_scores_list)
print()
print()


# count(2) count how many times 2 appears in your list 
# (if it doesn't, change  2 to a value in your list)
ct_of_2 = OU_scores_list.count(2)
ct_of_9_95 = OU_scores_list.count(9.95)

print("Next, we will count how many times 2 appears in the score list")
print(f"The score 2 appears {ct_of_2} time in the list")
print()
print("This will be more fun, lets see how many times 9.95 appears in the list")
print(f"The Sooners had {ct_of_9_95} routines that scored 9.95! ")
print()
print()


# sort()
asc_OU_scores_list = OU_scores_list.sort()

print("The modified score list in order from lowest to highest is:")
print(OU_scores_list)
print()
print()


# sort(), with reverse=True to get them in descending order
desc_OU_scores_list = OU_scores_list.sort(reverse=True)

print("The modified score list in order from highes to lowest is:")
print(OU_scores_list)
print()
print()


# copy()
new_OU_scores_list = OU_scores_list.copy()

print("Now we will make a copy of the modified score list:")
print(new_OU_scores_list)
print()
print()


# pop() the first item off the top of the list/stack
first_pop = new_OU_scores_list.pop(0)

print("Next, we will remove/pop the first score from the list leaving the following:")
print(new_OU_scores_list)
print()
print()

# pop() the last time off the bottom of the list/stack
last_pop = new_OU_scores_list.pop(-1)

print("Now we will remove/pop the last value in the list leaving:")
print(new_OU_scores_list)
print()
print()
print()


# ---------------------------------------------------------------------------------
# List 5. List Transformations - Using filter() and map()
print("-----List 5. List Transformations - Using filter() and map()-----")


# use built in filter() function to keep all score above a 9.85
def above_9_85(score):
    """Returns True if score is above 9.85"""
    return score > 9.85

OU_above_9_85 = list(filter(above_9_85, OU_scores_list))

print()
print("Lets filter the OU score list to include only the score above 9.85")
print()
print("Wow! OU has a great team because that's still a lot of scores above 9.85!")
print(OU_above_9_85)
print()
print()


# use built in map() function to map each score to cuberoot of score (rounded to 4 decimal places)
cbrt_OU_scores = list(map(lambda score: round(math.cbrt(score), 4), OU_scores_list))

print("Now lets map each score to its cube root. We will round to 4 decimal places")
print(f"The results are: {cbrt_OU_scores}")
print()
print()


# use built in map() function to calculate volume of a cube with a side equal to 10.0
cube_10 = list(map(lambda score: score ** 3, filter(lambda score: score == 10.0, OU_scores_list)))

print("Next, we use map to calculate the volume of a cube with a side equal to one of the scores")
print("For easy math, I will choose the score 10.0.")
print(f"The volume for a cube with a side equal to 10 is: {cube_10}")
print("Since there is only one score of 10.0 in our list, we get a list with only one value, 1000")
print()
print()
print()


# -----------------------------------------------------------------------------------
# List 6. List Transformations - Using List Comprehension
print("-----List 6. List Transformations - Using List Comprehension-----")


# use list comprehension to filter to get scores above 9.9
OU_above_9_9 = [score for score in OU_scores_list if score > 9.9]

print()
print("Now we will find the scores above 9.9 using list comprehension")
print(f"The following is a list showing the Sooners scores above 9.9: {OU_above_9_9}")
print()


# use list comprehension to triple each value in the OU score list
OU_scores_triple = [round(score * 3, 2) for score in OU_scores_list]

print("Next, we will triple each score in the Sooners score list and round to 2 decimal places")
print(f"The new tripled scores are: {OU_scores_triple}")
print()


# Use list comprehension of my choice
# add 0.05 to every score under 9.8
OU_scores_add_on = [round(score + 0.05, 3) if score < 9.8 else score for score in OU_scores_list]

print("Now, for every score less than 9.8 we will add 0.05, the rest of the scores stay the same")
print(f"The score list now looks like this: {OU_scores_add_on}")
print()


# using lists in my domain to find the team score
Utah_vault = [9.875, 9.825, 9.9, 9.975, 9.95, 9.8]
Utah_bars = [9.85, 9.875, 9.75, 9.825, 9.85, 9.675]
Utah_beam = [9.9, 9.85, 9.775, 9.9, 9.975, 9.075]
Utah_floor = [9.675, 9.85, 9.925, 9.825, 9.725, 9.875]

 
def team_event_score(scorelist):
    """Returns sum of score list minus the lowest score"""   # top 5 out of 6 scores
    scorelist.remove(min(scorelist))   # if more than one score has value of min, only one removed
    return math.fsum(scorelist)                          

Utah_vault_total = team_event_score(Utah_vault)
Utah_bars_total = team_event_score(Utah_bars)
Utah_beam_total = team_event_score(Utah_beam)
Utah_floor_total = team_event_score(Utah_floor)
Utah_team_score = (Utah_vault_total + Utah_bars_total + Utah_beam_total + Utah_floor_total)


print()
print("Now we will jump back to the Utes and calculate their final score")
print()
print("Since the rules for college gymnastics allow you to drop the lowest score on each event,")
print("we will use a function to filter out the lowest score")
print("and add the remaining scores together to get each event total.")
print("Then, we will add all the events together to get the final score for the Utes")
print()
print("The event scores for Utah are:")
print(f"    Vault: {Utah_vault_total}")
print(f"     Bars: {Utah_bars_total}")
print(f"     Beam: {Utah_beam_total}")
print(f"    Floor: {Utah_floor_total}")
print()
print(f"The final score for the Utes is: {Utah_team_score:.3f} ")
print()
print(f"While {Utah_team_score:.3f} is a great score, it wasn't enough to beat the Sooners")
print("who scored 197.925!!  Boomer!")
print()



