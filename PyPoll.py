# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each canddiate won
#5. The winner of the election based on the popular vote

# Path = C:\Users\Junlee\Desktop\DataClass\Election_Analysis\Resources\election_results.csv

# Import the datetime class from the datetime module.
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

# Print the present time.
present_time = f'The time right now is {now}'
print(present_time)

#Add out dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')


# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Format for opening a file is file_variable = open (filename, mode)
# file_variable = name of the variable that will reference the file
# file_name = name of the file
# mode = what to do with file [ r - read, w - write, x - open for exclusive creation, a - append to existing file, + - open for reading/writing]

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    # write some data to the file.
    # deleted: txt_file.write("Hello World")

    # write three counties to the file.
    txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")

# (1)Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare empty dictionary.
candidate_votes = {}

# Determine the winning candidate
# Initialize the candidate tracker
winning_candidate = ""

# Initialize winning_count tracker
winning_count = 0

# Initialize winning_percentage tracker
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and Print the header row.
    headers = next(file_reader)
    print(headers)

    # print each row in the CSV file.
    for row in file_reader:
        # deleted: print(row)
        # (2)Add to the total vote count.
            #The standard Python format to increment a variable is number = number + 1, which can be augmented to number += 1
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
           
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate list.
# deleted: print(candidate_options)
# (3)Print the total votes
#deleted: print(total_votes)
#Print the candidates vote dictionary
print(candidate_votes)

#Close the file.
#election_data.close()

# Determine the percentage of votes for each candidate by looping through the counts.
# (1) Iterate through the candidate list
for candidate_name in candidate_votes:

    # (2) Retreive vote count of a candidate
    votes = candidate_votes[candidate_name]

    # (3) Calculate the percentage of votes.
    vote_percentage = float(votes)/float(total_votes) * 100

    # (4) Print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    # (1) Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

    # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage

        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name





winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.


