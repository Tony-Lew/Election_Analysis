# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options
candidiate_options = []
# Declare the empty dictionary
canidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidiate_name = row[2]

        # If the candidiate does not match any existing candidate...
        if candidiate_name not in candidiate_options:
            #add it to the list of candidates.
            candidiate_options.append(candidiate_name)

            # Begin tracking that candidate's vote count.
            canidate_votes[candidiate_name]=0

        # Add a vote to the candidate's count
        canidate_votes[candidiate_name] +=1

# Print the candidate list.
print(canidate_votes)