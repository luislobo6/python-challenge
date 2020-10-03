import os
import csv

# Define the Path of the file to read
file_path = os.path.join("Resources","election_data.csv")

#Create and init variables
candidates = {}
total_votes = 0

# Read/Open the file to work with
with open(file_path, "r") as cvs_file:
    csv_reader = csv.reader(cvs_file, delimiter=",")
    
    # skip the header and save it
    csv_header = next(csv_reader)

    # Get the first row to start populate the candidates dictionary
    first_row = next(csv_reader)
    candidates = {first_row[2]:1}

    # As we got the first_row at the beginning we need to add 1 to the total_votes value
    total_votes += 1


    #iterate for each row
    for row in csv_reader:
        total_votes += 1

        actual_key = row[2]
        # If the key is present in the dictionary, then we add 1 to the vote
        if actual_key in candidates.keys():
            candidates[actual_key] += 1
        #else we add the key to the dictionary and the value of 1
        else:
            candidates[actual_key] = 1


# print(candidates)


str_candidates = ""
str_winner = ""
votes_winner = 0

# Iterate the dictionary to get all the candidates, percentage and total of votes
for candidate in candidates.items():
    # Append all the results to a string
    str_candidates = str_candidates + f"{candidate[0]}: {'{:.3f}'.format( (candidate[1]/total_votes)*100)}% ({candidate[1]})\n"
    # check who won the election
    if (candidate[1] >= votes_winner) :
        str_winner = candidate[0]
        votes_winner = candidate[1]



str_final = str(f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{str_candidates}-------------------------
Winner: {str_winner}
-------------------------""")

# Create and open TXT file
output_file = "results.txt"
file1 = open(output_file, "w")
file1.write(str_final) # write the results in the file

print(str_final)