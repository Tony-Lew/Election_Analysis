# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of canidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# open the election results and read the file.
with open (file_to_load) as election_data:

    #to do: perform analysis.
    print(election_data)

#Close the file.
election_data.close()

import csv
import os
#Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources","election_results.csv")
#open the election results and read the file.
with open(file_to_load)as election_data:

    #print the file object.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("r","analysis", "election_analysis.txt")
file_to_save = "analysis/election_analysis.txt"
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct of indirect path to the file
file_to_save=os.path.join("analysis","election_anaylysis.text")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
outfile.close()

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)