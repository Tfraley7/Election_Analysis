import os
import csv
from smtpd import DebuggingServer
from unittest.util import _count_diff_all_purpose


print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
my_list = []
counties
counties[0]

print(counties[2])

len(counties)

# Append and remove Arapahoe and El Paso. Also, place Denver in position two on list.
counties.append("El Paso")
counties.remove("El Paso")
counties[2] = "Denver"
counties.append("Arapahoe")
counties.remove("Arapahoe")
counties


# Apply tuple to counties
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
counties_tuple[1]

# Apply dictionaries
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)

counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})

counties.append("El Paso")
counties_dict["El Paso"] = 461149
voting_data.append({"county": "El Paso", "registered_voters": 461149})
voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county"[4]: "Denvery", "registered_voters": 422829})
voting_data.append({"county": "Aarapahoe", "registered_voters": 422829})


# Fstrings
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

counties_tuple = ("Arapahoe", "Denver", "Jefferson")
for county in counties_tuple:
    print(county)

# Loops on county voters data based on F-strings with dictionaries

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Get the Key-Value Pairs of a Dictionary
for county, voters in counties_dict.items():
    print(county, voters)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print("Arapahoe county has 422829 registered voters.", "Denver county has 463353 registered voters.",
          "Jefferson county has 432438 registered voters.")

# Get Each Dictionary in a List of Dictionaries
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:

    print(county_dict['registered_voters'])

# Print only the number of registered voters in the counties
for county_dict in voting_data:
    print(county_dict['registered_voters'])

# F-strings: Formatted String Literals

candidate_votes = int(
    input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")

print(f"{county} county has {voters} registered voters.")

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
