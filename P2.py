# Scenario: You are creating a program to determine the category of a movie based on its rating and genre. The categories are:
#
# Blockbuster: Rating 8 or above, and genre is Action or Adventure
# Art Film: Rating 7 or above, and genre is Drama or Comedy
# Average: Other movies

# Task: Write a Python program that takes the movie rating and genre as input and prints the movie category.

rating = float(input("Enter the movie rating: "))
genre = input("Enter the genre for the movie: ").lower()


if rating>=8 and (genre == "action" or genre == "adventure"):
    category = "blockbuster"

elif rating>=7 and (genre == "drama" or genre == "comedy"):
    category = "art film"

else:
    category = "average"

print("the category of the movie is : ", category)
