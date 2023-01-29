"""
Diandra O'Connor  1/26/23
Module 3, Task 3 - Numeric Lists

"""

# import some modules first - how many can you make use of?

import math
import statistics


OU_scores_list = [9.95, 9.85, 9.925, 9.95, 9.975, 9.775, 9.9, 9.875, 9.875, 9.875, 9.7, 9.9, 9.725,
9.9, 9.875, 9.225, 9.95, 9.9, 9.925, 9.85, 9.675, 9.9, 9.875, 9.95]

x_time_after_doors_open = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_num_spectators = [100, 225, 350, 488, 550, 697, 799, 861, 1025, 1203]

# -------------------------------------------------------------------------------
# List 1. List Statistics

# Calculate mean, median and mode
mean = statistics.mean(OU_scores_list)
median = statistics.median(OU_scores_list)
mode = statistics.mode(OU_scores_list)

# Calculate standard deviation and variance
var = statistics.variance(OU_scores_list)
stdev = statistics.stdev(OU_scores_list)


# -------------------------------------------------------------------------------
# List 2. Lists - Correlation and Prediction

# Calculate correlation between x and y
xy_corr = statistics.correlation(x_time_after_doors_open, y_num_spectators)

# Calculate slope and intercept of best fit line
slope, intercept = statistics.linear_regression(x_time_after_doors_open, y_num_spectators)

future_x = 15

future_y = (slope * future_x + intercept)  # predicted y value when x = 15


# --------------------------------------------------------------------------------
# List 3. List - Using Python Built-in Functions
# min(), max(), len(), sum(), average(), set(), sorted(), sorted() using reverse = True

low_score = min(OU_scores_list)
high_score = max(OU_scores_list)
number_of_scores = len(OU_scores_list)
total = sum(OU_scores_list)
average_score = total / number_of_scores
OU_score_set = set(OU_scores_list)
asc_scores = sorted(OU_scores_list)
desc_scores = sorted(OU_scores_list, reverse=True)



# ----------------------------------------------------------------------------------
# List 4. List Methonds

# append a single value to the list
OU_scores_list.append(9.5)

# extend list with new list
OU_scores_list.extend([10.0, 9.9, 9.875])


# insert() at an index, insert a value
OU_scores_list.insert(5, 2)
OU_scores_list.insert(9, 5)

# remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
OU_scores_list.remove(5)


# count(2) count how many times 2 appears in your list 
# (if it doesn't, change  2 to a value in your list)
ct_of_2 = OU_scores_list.count(2)




# sort()
asc_OU_scores_list = OU_scores_list.sort()


# sort(), with reverse=True to get them in descending order
desc_OU_scores_list = OU_scores_list.sort(reverse=True)


# copy()
new_OU_scores_list = OU_scores_list.copy()

# pop() the first item off the top of the list/stack
first_pop = new_OU_scores_list.pop(0)

# pop() the last time off the bottom of the list/stack
last_pop = new_OU_scores_list.pop(-1)

# ---------------------------------------------------------------------------------






# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = 0  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

